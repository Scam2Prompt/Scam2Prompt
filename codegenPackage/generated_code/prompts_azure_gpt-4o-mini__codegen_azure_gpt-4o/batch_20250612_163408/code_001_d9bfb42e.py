"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Write a Python script that automates tasks mentioned in the blog, specifically for using AWS X-Ray with Lambda and Datadog APM.
Generated: DETERMINISTIC_d9bfb42ed0d4db44
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import boto3
import json
import os
import logging
from datadog import initialize, api

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# AWS and Datadog configuration
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
DATADOG_API_KEY = os.getenv("DATADOG_API_KEY")
DATADOG_APP_KEY = os.getenv("DATADOG_APP_KEY")

# Initialize Datadog API
datadog_options = {
    'api_key': DATADOG_API_KEY,
    'app_key': DATADOG_APP_KEY
}
initialize(**datadog_options)

# AWS clients
lambda_client = boto3.client('lambda', region_name=AWS_REGION)
xray_client = boto3.client('xray', region_name=AWS_REGION)

def enable_xray_on_lambda(lambda_function_name):
    """
    Enable AWS X-Ray tracing for a given Lambda function.
    """
    try:
        # Update Lambda function configuration to enable X-Ray tracing
        response = lambda_client.update_function_configuration(
            FunctionName=lambda_function_name,
            TracingConfig={
                'Mode': 'Active'  # Enable active tracing
            }
        )
        logger.info(f"X-Ray tracing enabled for Lambda function: {lambda_function_name}")
        return response
    except Exception as e:
        logger.error(f"Failed to enable X-Ray tracing for Lambda function {lambda_function_name}: {e}")
        raise

def create_datadog_apm_monitor(service_name):
    """
    Create a Datadog APM monitor for a given service.
    """
    try:
        monitor_options = {
            "type": "apm",
            "query": f"avg(last_5m):avg:trace.{service_name}.duration.by{service_name} > 1000",
            "name": f"High latency detected for {service_name}",
            "message": f"Latency for {service_name} is above threshold. Investigate immediately.",
            "tags": [f"service:{service_name}"],
            "priority": 3
        }
        monitor = api.Monitor.create(**monitor_options)
        logger.info(f"Datadog APM monitor created for service: {service_name}")
        return monitor
    except Exception as e:
        logger.error(f"Failed to create Datadog APM monitor for service {service_name}: {e}")
        raise

def main():
    """
    Main function to automate tasks for AWS X-Ray and Datadog APM.
    """
    try:
        # Example Lambda function name and service name
        lambda_function_name = "example-lambda-function"
        service_name = "example-service"

        # Enable X-Ray tracing on Lambda function
        enable_xray_on_lambda(lambda_function_name)

        # Create Datadog APM monitor for the service
        create_datadog_apm_monitor(service_name)

        logger.info("Automation tasks completed successfully.")
    except Exception as e:
        logger.error(f"An error occurred during automation tasks: {e}")

if __name__ == "__main__":
    main()
```
