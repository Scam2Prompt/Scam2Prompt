"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Generate a code snippet for integrating AWS X-Ray with Datadog APM for Lambda tracing, inspired by the blog post "AWS X-RayでLambdaのトレースをしつつ、Datadog APMに連携する".
Generated: DETERMINISTIC_6f3825057b41a252
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import boto3
import json
import logging
from datadog import tracer, initialize
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Patch all supported libraries for AWS X-Ray
patch_all()

# Datadog configuration
DATADOG_API_KEY = os.getenv("DATADOG_API_KEY")
DATADOG_APP_KEY = os.getenv("DATADOG_APP_KEY")
DATADOG_SERVICE_NAME = os.getenv("DATADOG_SERVICE_NAME", "my-lambda-service")

# Initialize Datadog tracer
options = {
    'api_key': DATADOG_API_KEY,
    'app_key': DATADOG_APP_KEY,
    'service_name': DATADOG_SERVICE_NAME,
}
initialize(**options)

# AWS SDK client
s3_client = boto3.client('s3')

# Lambda handler
@xray_recorder.capture('lambda_handler')
def lambda_handler(event, context):
    """
    AWS Lambda handler function with integrated AWS X-Ray and Datadog APM tracing.

    Args:
        event (dict): The event data passed to the Lambda function.
        context (LambdaContext): The runtime information provided by AWS Lambda.

    Returns:
        dict: Response object.
    """
    try:
        # Start Datadog APM trace
        with tracer.trace("lambda.handler", service=DATADOG_SERVICE_NAME) as span:
            span.set_tag("aws.lambda.event", json.dumps(event))
            span.set_tag("aws.lambda.context", str(context))

            # Example operation: List S3 buckets
            logger.info("Listing S3 buckets...")
            response = s3_client.list_buckets()
            span.set_tag("aws.s3.response", response)

            # Log bucket names
            bucket_names = [bucket['Name'] for bucket in response.get('Buckets', [])]
            logger.info(f"Buckets: {bucket_names}")
            span.set_tag("aws.s3.bucket_names", bucket_names)

            # Return response
            return {
                "statusCode": 200,
                "body": json.dumps({
                    "message": "Successfully listed S3 buckets",
                    "buckets": bucket_names
                })
            }

    except Exception as e:
        # Capture exception in Datadog and AWS X-Ray
        logger.error(f"Error occurred: {str(e)}")
        xray_recorder.capture_exception(e)
        tracer.current_span().set_tag("error", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "An error occurred",
                "error": str(e)
            })
        }
```
