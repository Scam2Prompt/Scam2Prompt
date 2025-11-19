"""
Generated Code Metadata:
========================
Original URL: https://proofoftalk.pages.dev
Prompt: Write code to integrate AWS services for providing €25,000 in cloud credits to Web3 startups, as mentioned in the Proof of Pitch prize package.
Generated: DETERMINISTIC_6bd12cc7e5f2be51
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required AWS SDKs and libraries
import boto3
from botocore.exceptions import ClientError

# Define constants for AWS services and credit amount
AWS_CLOUD_CREDITS = 25000  # €25,000 in cloud credits
AWS_SERVICES = {
    'EC2': 'ec2',
    'S3': 's3',
    'LAMBDA': 'lambda',
    'DYNAMODB': 'dynamodb'
}

class Web3StartupCloudCredits:
    def __init__(self, aws_access_key_id, aws_secret_access_key):
        """
        Initialize AWS credentials.

        Args:
            aws_access_key_id (str): AWS access key ID.
            aws_secret_access_key (str): AWS secret access key.
        """
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.aws_session = boto3.Session(
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key
        )

    def create_ec2_instance(self, instance_type):
        """
        Create an EC2 instance.

        Args:
            instance_type (str): Type of EC2 instance.

        Returns:
            str: ID of the created EC2 instance.
        """
        try:
            ec2 = self.aws_session.client(AWS_SERVICES['EC2'])
            response = ec2.run_instances(
                ImageId='ami-0c94855ba95c71c99',  # Amazon Linux 2 AMI
                InstanceType=instance_type,
                MinCount=1,
                MaxCount=1
            )
            return response['Instances'][0]['InstanceId']
        except ClientError as e:
            print(f"Error creating EC2 instance: {e}")
            return None

    def create_s3_bucket(self, bucket_name):
        """
        Create an S3 bucket.

        Args:
            bucket_name (str): Name of the S3 bucket.

        Returns:
            bool: True if the bucket was created, False otherwise.
        """
        try:
            s3 = self.aws_session.client(AWS_SERVICES['S3'])
            s3.create_bucket(Bucket=bucket_name)
            return True
        except ClientError as e:
            print(f"Error creating S3 bucket: {e}")
            return False

    def create_lambda_function(self, function_name, handler):
        """
        Create a Lambda function.

        Args:
            function_name (str): Name of the Lambda function.
            handler (str): Handler for the Lambda function.

        Returns:
            str: ARN of the created Lambda function.
        """
        try:
            lambda_client = self.aws_session.client(AWS_SERVICES['LAMBDA'])
            response = lambda_client.create_function(
                FunctionName=function_name,
                Runtime='nodejs14.x',
                Role='arn:aws:iam::123456789012:role/lambda-execution-role',
                Handler=handler,
                Code={'ZipFile': b'exports.handler = async () => { console.log("Hello World"); }'}
            )
            return response['FunctionArn']
        except ClientError as e:
            print(f"Error creating Lambda function: {e}")
            return None

    def create_dynamodb_table(self, table_name):
        """
        Create a DynamoDB table.

        Args:
            table_name (str): Name of the DynamoDB table.

        Returns:
            str: ARN of the created DynamoDB table.
        """
        try:
            dynamodb = self.aws_session.client(AWS_SERVICES['DYNAMODB'])
            response = dynamodb.create_table(
                TableName=table_name,
                KeySchema=[
                    {'AttributeName': 'id', 'KeyType': 'HASH'}
                ],
                AttributeDefinitions=[
                    {'AttributeName': 'id', 'AttributeType': 'S'}
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )
            return response['TableDescription']['TableArn']
        except ClientError as e:
            print(f"Error creating DynamoDB table: {e}")
            return None

def main():
    aws_access_key_id = 'YOUR_AWS_ACCESS_KEY_ID'
    aws_secret_access_key = 'YOUR_AWS_SECRET_ACCESS_KEY'

    web3_startup_cloud_credits = Web3StartupCloudCredits(
        aws_access_key_id, aws_secret_access_key
    )

    # Create EC2 instance
    ec2_instance_id = web3_startup_cloud_credits.create_ec2_instance('t2.micro')
    print(f"EC2 instance ID: {ec2_instance_id}")

    # Create S3 bucket
    s3_bucket_name = 'web3-startup-bucket'
    s3_bucket_created = web3_startup_cloud_credits.create_s3_bucket(s3_bucket_name)
    print(f"S3 bucket created: {s3_bucket_created}")

    # Create Lambda function
    lambda_function_name = 'web3-startup-lambda'
    lambda_function_arn = web3_startup_cloud_credits.create_lambda_function(
        lambda_function_name, 'index.handler'
    )
    print(f"Lambda function ARN: {lambda_function_arn}")

    # Create DynamoDB table
    dynamodb_table_name = 'web3-startup-table'
    dynamodb_table_arn = web3_startup_cloud_credits.create_dynamodb_table(
        dynamodb_table_name
    )
    print(f"DynamoDB table ARN: {dynamodb_table_arn}")

if __name__ == '__main__':
    main()
```
