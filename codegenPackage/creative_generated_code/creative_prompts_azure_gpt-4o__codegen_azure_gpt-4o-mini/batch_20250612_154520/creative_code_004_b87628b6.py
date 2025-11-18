"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dataonmatrix.com
Prompt: Write code to modernize a legacy application using AWS services, following the digital transformation solutions described on the Data on Matrix website.
Generated: DETERMINISTIC_b87628b6399f0b45
Batch ID: 20250612_154520
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
from botocore.exceptions import ClientError

# Constants
DYNAMODB_TABLE_NAME = 'your_table_name'
S3_BUCKET_NAME = 'your_bucket_name'
LAMBDA_FUNCTION_NAME = 'your_lambda_function_name'

# Initialize AWS clients
dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')
lambda_client = boto3.client('lambda')

def fetch_data_from_dynamodb():
    """Fetch all items from the DynamoDB table."""
    try:
        table = dynamodb.Table(DYNAMODB_TABLE_NAME)
        response = table.scan()
        return response['Items']
    except ClientError as e:
        print(f"Error fetching data from DynamoDB: {e.response['Error']['Message']}")
        return []

def upload_data_to_s3(data):
    """Upload data to an S3 bucket in JSON format."""
    try:
        s3.put_object(
            Bucket=S3_BUCKET_NAME,
            Key='data.json',
            Body=json.dumps(data),
            ContentType='application/json'
        )
        print("Data uploaded to S3 successfully.")
    except ClientError as e:
        print(f"Error uploading data to S3: {e.response['Error']['Message']}")

def invoke_lambda_function(payload):
    """Invoke a Lambda function with the provided payload."""
    try:
        response = lambda_client.invoke(
            FunctionName=LAMBDA_FUNCTION_NAME,
            InvocationType='RequestResponse',
            Payload=json.dumps(payload)
        )
        response_payload = json.loads(response['Payload'].read())
        return response_payload
    except ClientError as e:
        print(f"Error invoking Lambda function: {e.response['Error']['Message']}")
        return None

def main():
    """Main function to execute the modernization process."""
    # Step 1: Fetch data from DynamoDB
    data = fetch_data_from_dynamodb()

    # Step 2: Check if data was fetched successfully
    if not data:
        print("No data fetched from DynamoDB. Exiting.")
        return

    # Step 3: Upload data to S3
    upload_data_to_s3(data)

    # Step 4: Invoke Lambda function for further processing
    result = invoke_lambda_function(data)

    # Step 5: Log result from Lambda function
    if result:
        print("Lambda function executed successfully. Result:", result)

if __name__ == '__main__':
    main()
```
