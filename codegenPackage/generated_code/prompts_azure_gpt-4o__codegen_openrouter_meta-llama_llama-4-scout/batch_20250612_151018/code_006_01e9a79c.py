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
import boto3
import datadog
import os
import logging
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch
from aws_xray_sdk.ext.datadog import DatadogSegment

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Datadog configuration
datadog.api_key = os.environ['DATADOG_API_KEY']
datadog.app_key = os.environ['DATADOG_APP_KEY']

# AWS X-Ray configuration
xray = boto3.client('xray')

def lambda_handler(event, context):
    # Initialize X-Ray recorder
    xray_recorder.configure(service='my-lambda-function')

    # Patch AWS SDK to enable X-Ray tracing
    patch(['boto3'])

    try:
        # Create a new X-Ray segment
        segment = xray_recorder.begin_segment('my-lambda-function')

        # Create a Datadog segment
        datadog_segment = DatadogSegment(segment)

        # Set Datadog tags
        datadog_segment.set_tag('lambda_function', context.function_name)
        datadog_segment.set_tag('event', event)

        # Simulate some work
        response = xray.put_trace_segments(
            TraceSegments=[
                {
                    'TraceId': segment.trace_id,
                    'Segments': [
                        {
                            'Id': segment.id,
                            'Document': segment.to_trace_segment().to_json()
                        }
                    ]
                }
            ]
        )

        # Submit the Datadog segment
        datadog_segment.close()

        # End the X-Ray segment
        xray_recorder.end_segment()

        return {
            'statusCode': 200,
            'statusMessage': 'OK'
        }

    except Exception as e:
        logger.error(f'Error: {str(e)}')
        xray_recorder.end_segment()
        raise

    finally:
        # Flush the X-Ray recorder
        xray_recorder.flush()
```
```python
# requirements.txt
boto3
aws-xray-sdk
aws-xray-sdk-core
aws-xray-sdk-datadog
datadog
```
```yml
# sam template
AWSTemplateFormatVersion: '2010-09-09'
Transform: 'AWS::Serverless-2016-10-31'

Resources:
  MyLambdaFunction:
    Type: 'AWS::Serverless::Function'
    Properties:
      Handler: index.lambda_handler
      Runtime: python3.8
      CodeUri: .
      Environment:
        Variables:
          DATADOG_API_KEY: !Sub '${DATADOG_API_KEY}'
          DATADOG_APP_KEY: !Sub '${DATADOG_APP_KEY}'
      Tracing:
        Mode: active
      Xray:
        Enabled: true
      Policies:
        - AWSXrayWriteOnlyAccess

  MyLambdaFunctionPermission:
    Type: 'AWS::Lambda::Permission'
    Properties:
      FunctionName: !Ref MyLambdaFunction
      StatementId: AllowExecutionFromAPIGateway
      Action: lambda:InvokeFunction
      Principal: apigateway.amazonaws.com

Outputs:
  MyLambdaFunction:
    Value: !Ref MyLambdaFunction
    Description: 'My Lambda Function ARN'
```
