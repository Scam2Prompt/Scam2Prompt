"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giitechcodes.com.ng
Prompt: Generate a Python script that utilizes AWS cloud resources for an IoT application as described on GII Tech Codes.
Generated: DETERMINISTIC_530adb86beaa2b3b
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import boto3
import json
import logging
import botocore.exceptions

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class IoTApplication:
    def __init__(self, iot_client=None):
        """
        Initializes the IoTApplication class with an optional IoT client.
        If no client is provided, a new one is created using boto3.
        """
        self.iot_client = iot_client or boto3.client('iot')

    def create_iot_thing(self, thing_name):
        """
        Creates an IoT Thing in AWS IoT Core.

        :param thing_name: Name of the IoT Thing to be created
        :raises botocore.exceptions.ClientError: If the creation fails
        """
        try:
            response = self.iot_client.create_thing(
                thingName=thing_name
            )
            logger.info(f"Successfully created IoT Thing: {thing_name}")
            return response
        except botocore.exceptions.ClientError as e:
            logger.error(f"Failed to create IoT Thing: {e}")
            raise

    def delete_iot_thing(self, thing_name):
        """
        Deletes an IoT Thing from AWS IoT Core.

        :param thing_name: Name of the IoT Thing to be deleted
        :raises botocore.exceptions.ClientError: If the deletion fails
        """
        try:
            response = self.iot_client.delete_thing(
                thingName=thing_name
            )
            logger.info(f"Successfully deleted IoT Thing: {thing_name}")
            return response
        except botocore.exceptions.ClientError as e:
            logger.error(f"Failed to delete IoT Thing: {e}")
            raise

    def create_policy(self, policy_name, policy_document):
        """
        Creates an IoT policy in AWS IoT Core.

        :param policy_name: Name of the IoT policy to be created
        :param policy_document: JSON policy document
        :raises botocore.exceptions.ClientError: If the creation fails
        """
        try:
            response = self.iot_client.create_policy(
                policyName=policy_name,
                policyDocument=json.dumps(policy_document)
            )
            logger.info(f"Successfully created IoT Policy: {policy_name}")
            return response
        except botocore.exceptions.ClientError as e:
            logger.error(f"Failed to create IoT Policy: {e}")
            raise

    def attach_policy_to_thing(self, policy_name, thing_name):
        """
        Attaches a policy to an IoT Thing.

        :param policy_name: Name of the IoT policy to attach
        :param thing_name: Name of the IoT Thing to attach the policy to
        :raises botocore.exceptions.ClientError: If the attachment fails
        """
        try:
            self.iot_client.attach_policy(
                policyName=policy_name,
                target=thing_name  # Assuming target is the Thing ARN
            )
            logger.info(f"Successfully attached policy '{policy_name}' to Thing '{thing_name}'")
        except botocore.exceptions.ClientError as e:
            logger.error(f"Failed to attach policy to Thing: {e}")
            raise

if __name__ == "__main__":
    # Example usage of the IoTApplication class
    app = IoTApplication()

    # Define policy document (example)
    policy_document = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "iot:Connect",
                "Resource": "*"
            }
        ]
    }

    # Create IoT Thing and Policy
    try:
        app.create_iot_thing("MyIoTDevice")
        app.create_policy("MyIoTPolicy", policy_document)
        app.attach_policy_to_thing("MyIoTPolicy", "MyIoTDevice")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
```

This Python script provides a clean, runnable implementation for creating IoT devices and policies in AWS IoT Core, complete with error handling and logging. It utilizes the `boto3` library for AWS interactions and follows best practices for clarity and maintainability.
