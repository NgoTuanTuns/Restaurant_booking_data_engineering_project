from pyspark.sql.functions import *
from pyspark.sql.types import *

# Event Hubs configuration
EH_NAMESPACE                    = "your_eh_namespace"
EH_NAME                         = "your_topic"
EH_CONN_STR                     = "your_conn_str"
# Kafka Consumer configuration

KAFKA_OPTIONS = {
  "kafka.bootstrap.servers"  : f"{EH_NAMESPACE}.servicebus.windows.net:9093",
  "subscribe"                : EH_NAME,
  "kafka.sasl.mechanism"     : "PLAIN",
  "kafka.security.protocol"  : "SASL_SSL",
  "kafka.sasl.jaas.config"   : f"kafkashaded.org.apache.kafka.common.security.plain.PlainLoginModule required username=\"$ConnectionString\" password=\"{EH_CONN_STR}\";",
  "kafka.request.timeout.ms" : 10000,
  "kafka.session.timeout.ms" : 10000,
  "maxOffsetsPerTrigger"     : 10000,
  "failOnDataLoss"           : 'true',
  "startingOffsets"          : 'earliest'
}

#Read from Kafka
df = spark.readStream.format("kafka").options(**KAFKA_OPTIONS).load()

#Write data to bronze table
query = (df.writeStream
  .outputMode("append")
  .trigger(availableNow=True)
  .option("checkpointLocation", "your_volume")
  .toTable("restaurant_booking_project.bronze_layer.bronze_table")
)

query.awaitTermination()
