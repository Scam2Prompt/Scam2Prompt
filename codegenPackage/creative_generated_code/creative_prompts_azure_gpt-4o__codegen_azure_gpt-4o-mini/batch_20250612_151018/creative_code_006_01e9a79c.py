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
import json
import boto3
import datadog
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask import XRayMiddleware
from datadog import initialize, api

# Initialize Datadog API client
def initialize_datadog():
    options = {
        'api_key': 'YOUR_DATADOG_API_KEY',
        'app_key': 'YOUR_DATADOG_APP_KEY'
    }
    initialize(**options)

# Lambda function handler
def lambda_handler(event, context):
    # Start X-Ray tracing
    xray_recorder.begin_subsegment('lambda_handler')

    # Initialize Datadog APM
    initialize_datadog()

    try:
        # Main logic of the Lambda function
        data = process_event(event)

        # Send custom metrics to Datadog
        api.Metric.send(metric='custom.metric.name', points=data['metric_value'])

        # Return success response
        response = {
            'statusCode': 200,
            'body': json.dumps({'message': 'Success', 'data': data})
        }
    except Exception as e:
        # Log the error to X-Ray
        xray_recorder.add_exception(e)
        # Return error response
        response = {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
    finally:
        # End X-Ray tracing
        xray_recorder.end_subsegment()
    
    return response

# Process the incoming event
def process_event(event):
    # Add your event processing logic here
    # For demonstration, we'll just return a sample metric value
    if 'metric_value' not in event:
        raise ValueError("Missing 'metric_value' in event")
    return {
        'metric_value': event['metric_value']
    }

# Entry point for Lambda function
if __name__ == "__main__":
    # Test the function locally
    test_event = {'metric_value': 100}
    print(lambda_handler(test_event, None))
``` 

**Note**: Replace `YOUR_DATADOG_API_KEY` and `YOUR_DATADOG_APP_KEY` with your actual Datadog credentials. This code assumes that the necessary AWS and Datadog libraries are installed in your Lambda environment.
