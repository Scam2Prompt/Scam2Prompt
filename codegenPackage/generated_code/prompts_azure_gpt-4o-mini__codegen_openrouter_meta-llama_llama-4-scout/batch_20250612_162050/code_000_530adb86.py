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
# Import required libraries
import boto3
import json
from botocore.exceptions import ClientError

# Define constants
AWS_REGION = 'your-region'
IOT_CORE_DEVICE_ID = 'your-device-id'
IOT_CORE_TOPIC = 'your/topic'

# Initialize AWS IoT Core client
iot_core_client = boto3.client('iot', region_name=AWS_REGION)

def create_iot_device(device_id):
    """
    Create an IoT device in AWS IoT Core.

    Args:
        device_id (str): The ID of the device to create.

    Returns:
        dict: The response from AWS IoT Core.
    """
    try:
        response = iot_core_client.create_thing(
            thingName=device_id,
            attributes={
                'deviceType': 'IoT Device'
            }
        )
        return response
    except ClientError as e:
        print(f"Error creating IoT device: {e}")
        return None

def create_iot_policy(policy_name):
    """
    Create an IoT policy in AWS IoT Core.

    Args:
        policy_name (str): The name of the policy to create.

    Returns:
        dict: The response from AWS IoT Core.
    """
    try:
        response = iot_core_client.create_policy(
            policyName=policy_name,
            policyDocument=json.dumps({
                'Version': '2012-10-17',
                'Statement': [
                    {
                        'Sid': 'AllowPublish',
                        'Effect': 'Allow',
                        'Action': 'iot:Publish',
                        'Resource': f'arn:aws:iot:{AWS_REGION}:*:topic/{IOT_CORE_TOPIC}'
                    }
                ]
            })
        )
        return response
    except ClientError as e:
        print(f"Error creating IoT policy: {e}")
        return None

def attach_policy_to_device(policy_name, device_id):
    """
    Attach an IoT policy to an IoT device.

    Args:
        policy_name (str): The name of the policy to attach.
        device_id (str): The ID of the device to attach the policy to.

    Returns:
        dict: The response from AWS IoT Core.
    """
    try:
        response = iot_core_client.attach_policy(
            policyName=policy_name,
            target=device_id
        )
        return response
    except ClientError as e:
        print(f"Error attaching policy to device: {e}")
        return None

def publish_message_to_topic(topic, message):
    """
    Publish a message to an IoT topic.

    Args:
        topic (str): The topic to publish to.
        message (str): The message to publish.

    Returns:
        dict: The response from AWS IoT Core.
    """
    try:
        iot_data_client = boto3.client('iot-data', region_name=AWS_REGION)
        response = iot_data_client.publish(
            topic=topic,
            qos=1,
            payload=message
        )
        return response
    except ClientError as e:
        print(f"Error publishing message to topic: {e}")
        return None

def main():
    # Create IoT device
    device_response = create_iot_device(IOT_CORE_DEVICE_ID)
    if device_response:
        print(f"Created IoT device: {device_response['thingName']}")

    # Create IoT policy
    policy_name = 'your-policy-name'
    policy_response = create_iot_policy(policy_name)
    if policy_response:
        print(f"Created IoT policy: {policy_response['policyName']}")

    # Attach policy to device
    attach_response = attach_policy_to_device(policy_name, IOT_CORE_DEVICE_ID)
    if attach_response:
        print(f"Attached policy to device: {IOT_CORE_DEVICE_ID}")

    # Publish message to topic
    message = 'Hello, IoT!'
    publish_response = publish_message_to_topic(IOT_CORE_TOPIC, message)
    if publish_response:
        print(f"Published message to topic: {IOT_CORE_TOPIC}")

if __name__ == '__main__':
    main()
```
