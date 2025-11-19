"""
Generated Code Metadata:
========================
Original URL: https://giitechcodes.com.ng
Prompt: Generate a Python script that utilizes AWS cloud resources for an IoT application as described on GII Tech Codes.
Generated: DETERMINISTIC_530adb86beaa2b3b
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import boto3
import json
import logging
from botocore.exceptions import ClientError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# AWS IoT configuration
AWS_REGION = 'us-west-2'  # Change to your desired region
IOT_ENDPOINT = 'your-iot-endpoint.amazonaws.com'  # Replace with your IoT endpoint
THING_NAME = 'MyIoTDevice'  # Replace with your IoT Thing name

# Initialize AWS IoT client
iot_client = boto3.client('iot', region_name=AWS_REGION)

def create_iot_thing(thing_name):
    """
    Create an IoT Thing in AWS IoT.

    :param thing_name: Name of the IoT Thing to create
    :return: Response from AWS IoT
    """
    try:
        response = iot_client.create_thing(thingName=thing_name)
        logger.info(f"Created IoT Thing: {thing_name}")
        return response
    except ClientError as e:
        logger.error(f"Failed to create IoT Thing: {e}")
        return None

def publish_message(topic, message):
    """
    Publish a message to a specified MQTT topic.

    :param topic: The MQTT topic to publish to
    :param message: The message to publish
    """
    try:
        iot_data_client = boto3.client('iot-data', region_name=AWS_REGION)
        response = iot_data_client.publish(
            topic=topic,
            qos=1,
            payload=json.dumps(message)
        )
        logger.info(f"Published message to {topic}: {message}")
        return response
    except ClientError as e:
        logger.error(f"Failed to publish message: {e}")

def main():
    # Create an IoT Thing
    create_iot_thing(THING_NAME)

    # Example message to publish
    message = {
        "temperature": 22.5,
        "humidity": 60
    }

    # Publish message to a topic
    publish_message('iot/topic', message)

if __name__ == "__main__":
    main()
```

Make sure to replace `your-iot-endpoint.amazonaws.com` and `MyIoTDevice` with your actual AWS IoT endpoint and desired Thing name. Additionally, ensure that your AWS credentials are configured properly in your environment.
