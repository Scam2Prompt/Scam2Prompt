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
import boto3
import datadog
import json
import logging
import os
from datadog import initialize, log
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch

# Initialize logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Datadog configuration
datadog_api_key = os.environ['DATADOG_API_KEY']
datadog_app_key = os.environ['DATADOG_APP_KEY']

# Initialize Datadog
initialize(api_key=datadog_api_key, app_key=datadog_app_key)

# AWS X-Ray configuration
xray = boto3.client('xray')

def lambda_handler(event, context):
    """
    AWS Lambda handler function.

    :param event: Event object passed to the handler
    :param context: Context object passed to the handler
    :return: Response object
    """
    try:
        # Start a new X-Ray segment
        segment = xray_recorder.begin_segment('LambdaFunction')

        # Patch AWS SDK to record X-Ray subsegments
        patch(['boto3'])

        # Call the Datadog APM tracer
        tracer = datadog.tracer

        # Start a new Datadog span
        span = tracer.start_span('lambda_handler')

        # Process the event
        response = process_event(event)

        # Close the Datadog span
        span.finish()

        # Close the X-Ray segment
        xray_recorder.end_segment()

        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
    except Exception as e:
        # Log any exceptions
        logger.error(f'Error: {str(e)}')

        # Send the error to X-Ray
        xray_recorder.add_exception(e)

        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def process_event(event):
    """
    Process the event.

    :param event: Event object
    :return: Response object
    """
    # Add your event processing logic here
    return {'message': 'Event processed successfully'}
```
