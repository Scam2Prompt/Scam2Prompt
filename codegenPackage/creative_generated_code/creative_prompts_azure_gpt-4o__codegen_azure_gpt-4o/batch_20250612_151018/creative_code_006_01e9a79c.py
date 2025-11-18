"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Create a Lambda function that integrates AWS X-Ray for tracing and connects to Datadog APM, based on the tutorial from tubone BOYAKI.
Generated: DETERMINISTIC_01e9a79c5716d5af
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import boto3
import logging
from aws_xray_sdk.core import patch_all, xray_recorder
from datadog_lambda.metric import lambda_metric
from datadog_lambda.tracing import create_dd_trace_context

# Patch all supported libraries for AWS X-Ray tracing
patch_all()

# Initialize Logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Environment variables for Datadog
DATADOG_API_KEY = os.getenv("DD_API_KEY")
DATADOG_SITE = os.getenv("DD_SITE", "datadoghq.com")

# Initialize AWS clients
s3_client = boto3.client('s3')

# Lambda handler function
def lambda_handler(event, context):
    """
    Main Lambda function handler.

    :param event: The event payload passed to the Lambda function
    :param context: AWS Lambda context object
    :return: Response dict
    """
    # Create Datadog APM trace context
    create_dd_trace_context(event, context)
    
    try:
        # Log the event payload
        logger.info("Received event: %s", json.dumps(event))
        
        # Example X-Ray segment creation
        with xray_recorder.in_segment("ProcessingSegment") as segment:
            segment.put_annotation("LambdaFunction", context.function_name)
            segment.put_annotation("AWSRequestId", context.aws_request_id)

            # Example interaction with S3
            bucket_name = "example-bucket"
            key = "example-key"
            try:
                response = s3_client.get_object(Bucket=bucket_name, Key=key)
                logger.info("Fetched object from S3: %s", response)
            except Exception as s3_error:
                logger.error("Error fetching object from S3: %s", str(s3_error))
                segment.put_metadata("S3Error", str(s3_error))
                raise s3_error
            
            # Record a custom Datadog metric
            lambda_metric(
                "custom.metric_name",
                1,
                tags=["environment:production", "function_name:" + context.function_name]
            )
        
        # Return successful response
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Lambda executed successfully!"}),
        }
    
    except Exception as e:
        # Log and propagate the exception
        logger.error("An error occurred: %s", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal server error"}),
        }
```

**Note:** Ensure that the Datadog Python Lambda Layer is added to your Lambda function and the required environment variables (`DD_API_KEY`, `DD_SITE`) are set properly during deployment.
