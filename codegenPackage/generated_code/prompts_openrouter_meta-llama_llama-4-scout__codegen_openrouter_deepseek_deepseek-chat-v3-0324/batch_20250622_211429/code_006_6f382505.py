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
import json
import boto3
from datadog_lambda.metric import lambda_metric
from datadog_lambda.wrapper import datadog_lambda_wrapper
from datadog_lambda.tracing import inject_datadog_trace_headers
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
from aws_xray_sdk.core.lambda_launcher import LambdaContext

# Initialize AWS X-Ray
xray_recorder.configure(
    service='lambda_service',
    context_missing='LOG_ERROR'
)
patch_all()

@datadog_lambda_wrapper
def lambda_handler(event, context):
    """
    Lambda function handler with AWS X-Ray and Datadog APM integration.
    
    Args:
        event: Lambda event object
        context: Lambda context object
    
    Returns:
        Response object
    """
    try:
        # Extract X-Ray trace ID
        xray_trace_id = None
        if '_X_AMZN_TRACE_ID' in os.environ:
            xray_trace_id = os.environ['_X_AMZN_TRACE_ID'].split(';')[0].replace('Root=', '')
        
        # Inject Datadog trace headers
        headers = {}
        inject_datadog_trace_headers(headers)
        
        # Add X-Ray trace ID to Datadog custom tags
        if xray_trace_id:
            lambda_metric(
                'aws.xray.trace_id',
                1,
                tags=[f'xray_trace_id:{xray_trace_id}']
            )
        
        # Your business logic here
        response = {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Success',
                'xray_trace_id': xray_trace_id,
                'dd_trace_enabled': 'dd_trace' in headers
            })
        }
        
        return response
    
    except Exception as e:
        # Log error to both X-Ray and Datadog
        xray_recorder.current_segment().add_error_flag()
        lambda_metric(
            'lambda.error',
            1,
            tags=[f'error:{str(e)}']
        )
        raise
```
