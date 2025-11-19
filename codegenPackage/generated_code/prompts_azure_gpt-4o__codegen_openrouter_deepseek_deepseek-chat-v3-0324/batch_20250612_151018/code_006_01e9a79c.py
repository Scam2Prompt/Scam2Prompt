"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Create a Lambda function that integrates AWS X-Ray for tracing and connects to Datadog APM, based on the tutorial from tubone BOYAKI.
Generated: DETERMINISTIC_01e9a79c5716d5af
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import boto3
from datadog import initialize, statsd
from datadog_lambda.wrapper import datadog_lambda_wrapper
from datadog_lambda.metric import lambda_metric
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
from aws_xray_sdk.core.lambda_launcher import check_in_lambda

# Initialize X-Ray
xray_recorder.configure(service='lambda-function')
patch_all()

# Initialize Datadog
initialize(
    api_key=os.environ.get('DD_API_KEY'),
    host_name=os.environ.get('DD_HOSTNAME', 'lambda')
)

@datadog_lambda_wrapper
def lambda_handler(event, context):
    """
    Lambda function handler with X-Ray and Datadog APM integration.
    
    Args:
        event: Lambda event object
        context: Lambda context object
    
    Returns:
        dict: Response object
    """
    try:
        # Start X-Ray segment
        segment = xray_recorder.begin_segment('lambda_handler')
        
        # Add custom metadata to X-Ray
        segment.put_metadata('event', event, 'request')
        segment.put_metadata('context', vars(context), 'request')
        
        # Business logic goes here
        result = {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Hello from Lambda with X-Ray and Datadog!',
                'event': event
            })
        }
        
        # Send custom metric to Datadog
        lambda_metric(
            "lambda.success",
            1,
            tags=["service:lambda-function", "env:production"]
        )
        
        return result
        
    except Exception as e:
        # Log error to X-Ray
        xray_recorder.current_segment().add_exception(e)
        
        # Send error metric to Datadog
        lambda_metric(
            "lambda.error",
            1,
            tags=["service:lambda-function", "env:production"]
        )
        
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }
    finally:
        # Close X-Ray segment
        xray_recorder.end_segment()
```
