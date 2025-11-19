"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Generate a Python script that interacts with AWS services, referencing the expertise of Sam Lucidi from the FOSS@RIT community.
Generated: DETERMINISTIC_835198c2160f3744
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import boto3
import botocore
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AWSServiceManager:
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
        """
        Initialize the AWSServiceManager with AWS credentials and region.

        :param aws_access_key_id: AWS access key ID
        :param aws_secret_access_key: AWS secret access key
        :param region_name: AWS region name (e.g., 'us-west-2')
        """
        self.session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )
        self.s3 = self.session.resource('s3')
        self.sqs = self.session.resource('sqs')

    def list_s3_buckets(self):
        """
        List all S3 buckets in the account.

        :return: List of bucket names
        """
        try:
            buckets = self.s3.buckets.all()
            bucket_names = [bucket.name for bucket in buckets]
            logger.info("S3 Buckets: %s", bucket_names)
            return bucket_names
        except botocore.exceptions.BotoCoreError as e:
            logger.error("Error listing S3 buckets: %s", e)
            return []

    def create_sqs_queue(self, queue_name):
        """
        Create an SQS queue with the specified name.

        :param queue_name: Name of the SQS queue to create
        :return: URL of the created queue or None if failed
        """
        try:
            queue = self.sqs.create_queue(QueueName=queue_name)
            logger.info("Created SQS queue: %s", queue.url)
            return queue.url
        except botocore.exceptions.BotoCoreError as e:
            logger.error("Error creating SQS queue: %s", e)
            return None

    def send_message_to_queue(self, queue_url, message_body):
        """
        Send a message to the specified SQS queue.

        :param queue_url: URL of the SQS queue
        :param message_body: The message body to send
        :return: Message ID of the sent message or None if failed
        """
        try:
            queue = self.sqs.Queue(queue_url)
            response = queue.send_message(MessageBody=message_body)
            logger.info("Sent message to queue: %s", response.message_id)
            return response.message_id
        except botocore.exceptions.BotoCoreError as e:
            logger.error("Error sending message to queue: %s", e)
            return None

if __name__ == "__main__":
    # Replace with your actual AWS credentials and region
    AWS_ACCESS_KEY_ID = 'your_access_key_id'
    AWS_SECRET_ACCESS_KEY = 'your_secret_access_key'
    REGION_NAME = 'us-west-2'

    aws_manager = AWSServiceManager(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION_NAME)

    # List S3 buckets
    aws_manager.list_s3_buckets()

    # Create an SQS queue
    queue_url = aws_manager.create_sqs_queue('MyTestQueue')

    # Send a message to the created SQS queue
    if queue_url:
        aws_manager.send_message_to_queue(queue_url, 'Hello, this is a test message!')
```
