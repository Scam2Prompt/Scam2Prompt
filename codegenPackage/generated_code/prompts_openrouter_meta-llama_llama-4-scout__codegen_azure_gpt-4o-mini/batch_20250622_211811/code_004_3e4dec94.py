"""
Generated Code Metadata:
========================
Original URL: https://daplatform.one
Prompt: "Design a basic architecture for a data platform that handles real-time data streams."
Generated: DETERMINISTIC_3e4dec94715d4217
Batch ID: 20250622_211811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from kafka import KafkaConsumer, KafkaProducer
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI application instance
app = FastAPI()

# Kafka configuration
KAFKA_BROKER = 'localhost:9092'
INPUT_TOPIC = 'input_data'
OUTPUT_TOPIC = 'output_data'

# Pydantic model for incoming data
class DataModel(BaseModel):
    id: int
    value: float

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Initialize Kafka consumer
consumer = KafkaConsumer(INPUT_TOPIC,
                         bootstrap_servers=KAFKA_BROKER,
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                         auto_offset_reset='earliest',
                         enable_auto_commit=True)

# Function to process incoming data
def process_data(data: DataModel):
    # Example processing logic
    logger.info(f"Processing data: {data}")
    # Here you can add your data processing logic
    # For demonstration, we will just send it to the output topic
    producer.send(OUTPUT_TOPIC, data.dict())
    producer.flush()

# Background task to consume data from Kafka
@app.on_event("startup")
async def startup_event():
    logger.info("Starting Kafka consumer...")
    for message in consumer:
        try:
            data = DataModel(**message.value)
            process_data(data)
        except Exception as e:
            logger.error(f"Error processing message: {e}")

# API endpoint to send data to Kafka
@app.post("/data/", response_model=DataModel)
async def send_data(data: DataModel):
    try:
        # Send data to Kafka
        producer.send(INPUT_TOPIC, data.dict())
        producer.flush()
        logger.info(f"Data sent to Kafka: {data}")
        return data
    except Exception as e:
        logger.error(f"Failed to send data: {e}")
        raise HTTPException(status_code=500, detail="Failed to send data")

# Shutdown event to clean up resources
@app.on_event("shutdown")
def shutdown_event():
    logger.info("Shutting down Kafka producer and consumer...")
    producer.close()
    consumer.close()
```
