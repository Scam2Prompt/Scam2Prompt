"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Write a script to use AWS X-Ray for tracing Lambda functions and integrate the results with Datadog APM, as outlined on the "tubone BOYAKI" blog.
Generated: DETERMINISTIC_85f93bf99f9358a1
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import os
import boto3
from aws_xray_sdk.core import patch_all, xray_recorder
from datadog import initialize, statsd

# Enable AWS X-Ray for tracing
patch_all()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Datadog configuration
DD_API_KEY = os.getenv("DD_API_KEY")
DD_APP_KEY = os.getenv("DD_APP_KEY")

if not DD_API_KEY or not DD_APP_KEY:
    raise EnvironmentError("Datadog API Key or APP Key is missing in environment variables")

datadog_options = {
    'api_key': DD_API_KEY,
    'app_key': DD_APP_KEY
}

initialize(**datadog_options)

# AWS Lambda handler
def lambda_handler(event, context):
    """
    AWS Lambda function handler for tracing execution using AWS X-Ray
    and sending metrics to Datadog APM
    """
    # Start an AWS X-Ray segment for tracing
    segment = xray_recorder.begin_segment('lambda_function_trace')

    try:
        logger.info("Starting Lambda function")
        
        # Example AWS operation: List S3 buckets
        s3_client = boto3.client('s3')
        buckets = s3_client.list_buckets()
        bucket_names = [bucket['Name'] for bucket in buckets.get('Buckets', [])]
        logger.info(f"S3 Buckets: {bucket_names}")

        # Send custom metrics to Datadog
        statsd.increment('lambda_function.invocations', tags=["function:lambda_function_trace"])
        statsd.gauge('lambda_function.s3_bucket_count', len(bucket_names), tags=["resource:s3"])

        # Log and complete tracing
        logger.info("Lambda function execution completed successfully")
        return {
            'statusCode': 200,
            'body': {
                'message': 'Function executed successfully',
                'buckets': bucket_names
            }
        }

    except Exception as e:
        # Capture exception in X-Ray and log error
        xray_recorder.capture_exception()
        logger.error(f"Error occurred: {e}")
        statsd.increment('lambda_function.errors', tags=["function:lambda_function_trace"])
        return {
            'statusCode': 500,
            'body': {
                'message': 'Internal server error occurred',
                'error': str(e)
            }
        }

    finally:
        # Close the X-Ray segment
        xray_recorder.end_segment()
```

**Note**: Ensure you have all necessary AWS IAM permissions for the Lambda function and set up environment variables (`DD_API_KEY`, `DD_APP_KEY`) for Datadog integration. This script assumes you have the AWS X-Ray SDK, Datadog Python client, and `boto3` installed.
