from azure.eventhub import EventData
from azure.eventhub import EventHubProducerClient
from GenerateData import generate_data
import json
import os
from dotenv import load_dotenv

load_dotenv()
CONNECTION_STRING = os.getenv('CONNECTION_STRING')
EVENT_HUB_NAME = os.getenv('EVENT_HUB_NAME')

def send_data(data = None):
    try:
        producer = EventHubProducerClient.from_connection_string(
        conn_str=CONNECTION_STRING, eventhub_name=EVENT_HUB_NAME
    )

        # Create a batch.
        event_data_batch = producer.create_batch()

        data_json = json.dumps(data, ensure_ascii=False)
        # Add events to the batch.
        event_data_batch.add(EventData(data_json))

        # Send the batch of events to the event hub.
        producer.send_batch(event_data_batch)

        producer.close()
    except Exception as e:
        print(f"Error sending data: \n {e}")
        return False
    