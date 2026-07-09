from pyspark.sql.functions import *
from pyspark.sql.types import *

#Identify the schema of the incoming data
booking_schema = StructType([
    StructField("Client_Name", StringType()),
    StructField("Table_Types", StringType()),
    StructField("Time", TimestampType()),
    StructField("Num_Of_Individuals", IntegerType()),
    StructField("Order", StringType()),
    StructField("Is_Birthdate", BooleanType())])

bronze_df = (spark.readStream.format("delta").table("restaurant_booking_project.bronze_layer.bronze_table"))
#Parsing the incoming data
silver_df_parsed = bronze_df.select(from_json(col("value").cast("string"), booking_schema).alias("data")).select("data.*")

#Transforming the data
silver_df_transformed = silver_df_parsed.filter(col("Client_Name").isNotNull())
silver_df_transformed = silver_df_transformed.filter(col("Time").isNotNull())
silver_df_transformed = silver_df_transformed.filter(col("Table_Types").isNotNull())
silver_df_transformed = silver_df_transformed.dropDuplicates(subset=["Client_Name", "Table_Types", "Time"])
silver_df_transformed = silver_df_transformed.withColumn("booking_id", expr("uuid()"))

#Write transformed data to silver table
query = (silver_df_transformed.writeStream
            .outputMode("append")
            .trigger(availableNow=True)
            .option("checkpointLocation", "your_volume")
            .toTable("restaurant_booking_project.silver_layer.silver_table")
)
query.awaitTermination()



