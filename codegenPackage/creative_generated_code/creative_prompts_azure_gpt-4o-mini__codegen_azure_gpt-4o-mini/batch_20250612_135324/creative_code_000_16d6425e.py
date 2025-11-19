"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starkware.in
Prompt: Generate a code snippet for a cloud service that scales rapidly and utilizes breakthrough technologies as described by Starkware.
Generated: DETERMINISTIC_16d6425ecfba886a
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import boto3
from botocore.exceptions import ClientError
import json
import os

# Initialize the AWS Lambda client and API Gateway client
lambda_client = boto3.client('lambda')
apigateway_client = boto3.client('apigateway')

# Constants
FUNCTION_NAME = os.environ.get('FUNCTION_NAME', 'MyLambdaFunction')
API_NAME = os.environ.get('API_NAME', 'MyAPI')

def create_lambda_function():
    """Creates a new AWS Lambda function."""
    try:
        response = lambda_client.create_function(
            FunctionName=FUNCTION_NAME,
            Runtime='python3.9',
            Role=os.environ['LAMBDA_EXECUTION_ROLE'],
            Handler='lambda_function.lambda_handler',
            Code={
                'ZipFile': open('lambda_function.zip', 'rb').read()
            },
            MemorySize=128,
            Timeout=10,
            Publish=True,
            Environment={
                'ENV_VAR': 'value'
            }
        )
        print(f"Lambda function created: {response['FunctionArn']}")
    except ClientError as e:
        print(f"Error creating Lambda function: {e.response['Error']['Message']}")

def create_api_gateway():
    """Creates a new API Gateway for the Lambda function."""
    try:
        response = apigateway_client.create_rest_api(
            name=API_NAME,
            description='API for Lambda function',
            failOnWarnings=True
        )
        api_id = response['id']
        print(f"API Gateway created: {api_id}")
        return api_id
    except ClientError as e:
        print(f"Error creating API Gateway: {e.response['Error']['Message']}")

def create_resource(api_id):
    """Creates a resource in the API Gateway."""
    try:
        response = apigateway_client.create_resource(
            restApiId=api_id,
            parentId=api_id,
            pathPart='myresource'
        )
        resource_id = response['id']
        print(f"Resource created: {resource_id}")
        return resource_id
    except ClientError as e:
        print(f"Error creating API resource: {e.response['Error']['Message']}")

def create_method(api_id, resource_id):
    """Creates a method for the resource in the API Gateway."""
    try:
        response = apigateway_client.put_method(
            restApiId=api_id,
            resourceId=resource_id,
            httpMethod='GET',
            authorizationType='NONE'
        )
        print(f"Method created for resource: {response}")
    except ClientError as e:
        print(f"Error creating method: {e.response['Error']['Message']}")

def create_integration(api_id, resource_id):
    """Creates an integration between API Gateway and Lambda function."""
    try:
        response = apigateway_client.put_integration(
            restApiId=api_id,
            resourceId=resource_id,
            httpMethod='GET',
            type='AWS_PROXY',
            integrationHttpMethod='POST',
            uri=f'arn:aws:lambda:{os.environ["AWS_REGION"]}:{os.environ["AWS_ACCOUNT_ID"]}:function:{FUNCTION_NAME}'
        )
        print(f"Integration created: {response}")
    except ClientError as e:
        print(f"Error creating integration: {e.response['Error']['Message']}")

def main():
    """Main function to set up the Lambda and API Gateway."""
    create_lambda_function()
    api_id = create_api_gateway()
    resource_id = create_resource(api_id)
    create_method(api_id, resource_id)
    create_integration(api_id, resource_id)

if __name__ == "__main__":
    main()
```
