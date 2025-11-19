"""
Generated Code Metadata:
========================
Original URL: https://soneiumcount.vercel.app
Prompt: How would you implement a transaction count checker using a serverless architecture, inspired by the Soneium Transaction Count Checker tool?
Generated: DETERMINISTIC_2eb62d49140bc352
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of a transaction count checker using AWS Lambda and DynamoDB in Python. This code assumes you are using the AWS SDK (`boto3`) and have set up the necessary AWS resources.

```python
import json
import boto3
from botocore.exceptions import ClientError

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')

# Environment variable for the table name
TABLE_NAME = "TransactionCounts"  # Replace with your DynamoDB table name

def lambda_handler(event, context):
    """
    AWS Lambda function to check and update transaction counts.
    
    Args:
        event (dict): Input event containing 'user_id' and 'transaction_count'.
        context (object): Lambda context object (not used here).
    
    Returns:
        dict: Response containing status and message.
    """
    try:
        # Validate input
        if 'user_id' not in event or 'transaction_count' not in event:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Invalid input. 'user_id' and 'transaction_count' are required."})
            }
        
        user_id = event['user_id']
        transaction_count = event['transaction_count']
        
        # Ensure transaction_count is an integer
        if not isinstance(transaction_count, int):
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "'transaction_count' must be an integer."})
            }
        
        # Get reference to the DynamoDB table
        table = dynamodb.Table(TABLE_NAME)
        
        # Check if the user exists in the table
        response = table.get_item(Key={'user_id': user_id})
        if 'Item' in response:
            # User exists, update the transaction count
            current_count = response['Item']['transaction_count']
            new_count = current_count + transaction_count
            
            table.update_item(
                Key={'user_id': user_id},
                UpdateExpression="SET transaction_count = :new_count",
                ExpressionAttributeValues={':new_count': new_count}
            )
            
            return {
                "statusCode": 200,
                "body": json.dumps({"message": f"Transaction count updated to {new_count} for user {user_id}."})
            }
        else:
            # User does not exist, create a new record
            table.put_item(Item={
                'user_id': user_id,
                'transaction_count': transaction_count
            })
            
            return {
                "statusCode": 201,
                "body": json.dumps({"message": f"New user {user_id} created with transaction count {transaction_count}."})
            }
    
    except ClientError as e:
        # Handle AWS client errors
        return {
            "statusCode": 500,
            "body": json.dumps({"message": f"An error occurred: {e.response['Error']['Message']}"})
        }
    except Exception as e:
        # Handle general errors
        return {
            "statusCode": 500,
            "body": json.dumps({"message": f"An unexpected error occurred: {str(e)}"})
        }
```

### Notes:
1. Ensure the DynamoDB table has a primary key named `user_id`.
2. Deploy this Lambda function using AWS Lambda and configure the necessary IAM permissions to access DynamoDB.
3. Set the `TABLE_NAME` environment variable in the Lambda function configuration or replace it directly in the code.
