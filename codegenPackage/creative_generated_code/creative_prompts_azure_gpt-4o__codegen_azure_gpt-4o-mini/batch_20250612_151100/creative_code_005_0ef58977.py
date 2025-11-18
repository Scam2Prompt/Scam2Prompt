"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Develop a cloud computing solution using AWS or Azure, referencing the skills taught in APTRON Gurgaon’s Cloud Computing training.
Generated: DETERMINISTIC_0ef589773bb60d6c
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a sample Python code that demonstrates how to deploy a simple AWS Lambda function using the `boto3` library. This code includes error handling and comments for clarity.

```python
import boto3
import zipfile
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# AWS configuration
AWS_REGION = 'us-east-1'
LAMBDA_FUNCTION_NAME = 'MyLambdaFunction'
IAM_ROLE = 'arn:aws:iam::123456789012:role/MyLambdaRole'
HANDLER = 'lambda_function.lambda_handler'
RUNTIME = 'python3.8'

# Create a zip file for the Lambda function deployment
def create_zip_file():
    """Zips the Lambda function code."""
    with zipfile.ZipFile('lambda_function.zip', 'w') as zipf:
        zipf.write('lambda_function.py', arcname='lambda_function.py')
    logger.info("Created zip file for Lambda function.")

# Create the Lambda function
def create_lambda_function():
    """Creates an AWS Lambda function."""
    client = boto3.client('lambda', region_name=AWS_REGION)

    try:
        with open('lambda_function.zip', 'rb') as f:
            response = client.create_function(
                FunctionName=LAMBDA_FUNCTION_NAME,
                Runtime=RUNTIME,
                Role=IAM_ROLE,
                Handler=HANDLER,
                Code={'ZipFile': f.read()},
                Timeout=15,
                MemorySize=128,
            )
        logger.info("Lambda function created successfully: %s", response)
    except Exception as e:
        logger.error("Error creating Lambda function: %s", e)

# Main execution
if __name__ == '__main__':
    try:
        create_zip_file()
        create_lambda_function()
    except Exception as e:
        logger.error("An error occurred: %s", e)
    finally:
        # Clean up the zip file
        if os.path.exists('lambda_function.zip'):
            os.remove('lambda_function.zip')
            logger.info("Cleaned up zip file.")
```

Make sure to create a `lambda_function.py` file in the same directory as this script, which includes the logic for the Lambda function. The IAM role specified must also have the appropriate permissions for Lambda execution.
