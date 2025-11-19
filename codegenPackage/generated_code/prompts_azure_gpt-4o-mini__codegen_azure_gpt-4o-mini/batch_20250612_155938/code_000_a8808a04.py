"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: Generate a Python script that integrates AWS cloud services for scalable business operations as described on IMTS's website.
Generated: DETERMINISTIC_a8808a04c4cb0fbb
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import boto3
import logging
from botocore.exceptions import ClientError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AWSIntegration:
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
        """
        Initialize the AWSIntegration class with AWS credentials and region.

        :param aws_access_key_id: AWS access key ID
        :param aws_secret_access_key: AWS secret access key
        :param region_name: AWS region name
        """
        self.session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )
        self.s3 = self.session.resource('s3')
        self.sqs = self.session.resource('sqs')
        self.dynamodb = self.session.resource('dynamodb')

    def create_s3_bucket(self, bucket_name):
        """
        Create an S3 bucket.

        :param bucket_name: Name of the bucket to create
        :raises ClientError: If the bucket cannot be created
        """
        try:
            self.s3.create_bucket(Bucket=bucket_name)
            logger.info(f'S3 bucket {bucket_name} created successfully.')
        except ClientError as e:
            logger.error(f'Error creating bucket {bucket_name}: {e}')
            raise

    def send_message_to_sqs(self, queue_name, message_body):
        """
        Send a message to an SQS queue.

        :param queue_name: Name of the SQS queue
        :param message_body: The message body to send
        :raises ClientError: If the message cannot be sent
        """
        try:
            queue = self.sqs.get_queue_by_name(QueueName=queue_name)
            response = queue.send_message(MessageBody=message_body)
            logger.info(f'Message sent to SQS queue {queue_name}: {response.get("MessageId")}')
        except ClientError as e:
            logger.error(f'Error sending message to SQS queue {queue_name}: {e}')
            raise

    def create_dynamodb_table(self, table_name, partition_key):
        """
        Create a DynamoDB table.

        :param table_name: Name of the table to create
        :param partition_key: Partition key for the table
        :raises ClientError: If the table cannot be created
        """
        try:
            table = self.dynamodb.create_table(
                TableName=table_name,
                KeySchema=[
                    {
                        'AttributeName': partition_key,
                        'KeyType': 'HASH'  # Partition key
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': partition_key,
                        'AttributeType': 'S'  # String type
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )
            table.wait_until_exists()
            logger.info(f'DynamoDB table {table_name} created successfully.')
        except ClientError as e:
            logger.error(f'Error creating DynamoDB table {table_name}: {e}')
            raise

if __name__ == "__main__":
    # Example usage
    aws_access_key_id = 'YOUR_AWS_ACCESS_KEY_ID'
    aws_secret_access_key = 'YOUR_AWS_SECRET_ACCESS_KEY'
    region_name = 'YOUR_AWS_REGION'

    aws_integration = AWSIntegration(aws_access_key_id, aws_secret_access_key, region_name)

    # Create an S3 bucket
    aws_integration.create_s3_bucket('my-unique-bucket-name')

    # Send a message to SQS
    aws_integration.send_message_to_sqs('my-queue-name', 'Hello, SQS!')

    # Create a DynamoDB table
    aws_integration.create_dynamodb_table('my-table-name', 'my-partition-key')
```
