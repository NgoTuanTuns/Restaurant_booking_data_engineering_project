from pyspark.sql.functions import *
from pyspark.sql.types import *

silver_df = spark.read.table('restaurant_booking_project.silver_layer.silver_table')
dim_table_types = spark.read.table('restaurant_booking_project.gold_layer.dim_table_types')

#Load fact_booking table
fact_booking = silver_df.join(dim_table_types,
                              silver_df['Table_Types'] == dim_table_types['table_name'],
                              'left'
                              ).select(col('booking_id'),
                                    col('client_name'),
                                    col('table_id').alias('table_types_id'),
                                    col('time').alias('booking_time'),
                                    col('num_of_individuals'),
                                    col('is_birthdate')
                              )

fact_booking.createOrReplaceTempView("fact_booking")

#Using merge wiht when to avoid duplicates
spark.sql("""
    MERGE INTO restaurant_booking_project.gold_layer.fact_booking AS target
    USING fact_booking AS source
    ON target.booking_id = source.booking_id      
    WHEN NOT MATCHED THEN INSERT *                 
""")

#Load fact_order table
order_schema = MapType(StringType(), ArrayType(StringType()))

#Parse the data from order column and use explode to get the food_category_name and food_list
#Then explode the food_list to get the food_name
fact_order = (silver_df
             .select("booking_id", from_json(col("Order"), order_schema).alias("Order"))
             .select("booking_id", explode("Order").alias("food_category_name", "food_list"))
             .select("booking_id", "food_category_name", explode("food_list").alias("food_name")))

#Read data from gold layer
food_category_df = spark.read.table('restaurant_booking_project.gold_layer.dim_food_category')
food_df = spark.read.table('restaurant_booking_project.gold_layer.dim_food')

#Join two dim table to get the id of those table
fact_order = fact_order.join(food_category_df, fact_order['food_category_name'] == food_category_df['food_category_name'], 'left')
fact_order = fact_order.join(food_df, fact_order['food_name'] == food_df['food_name'], 'left')
fact_order = fact_order.select("booking_id", col("restaurant_booking_project.gold_layer.dim_food_category.food_category_id").alias("food_category_id"), "food_id")
fact_order.createOrReplaceTempView("fact_order_new")

spark.sql("""
          MERGE INTO restaurant_booking_project.gold_layer.fact_order AS target
          USING fact_order_new AS source
          ON target.booking_id = source.booking_id
          WHEN NOT MATCHED THEN INSERT *
""")


