"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Write a Python script that automates tasks mentioned in the blog, specifically for using AWS X-Ray with Lambda and Datadog APM.
Generated: DETERMINISTIC_d9bfb42ed0d4db44
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import boto3
import os
import logging
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from datadog import initialize, api

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# AWS and Datadog settings
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
LAMBDA_FUNCTION_NAME = os.getenv("LAMBDA_FUNCTION_NAME", "YourLambdaFunctionName")
DATADOG_API_KEY = os.getenv("DATADOG_API_KEY", "YourDatadogAPIKey")
DATADOG_APP_KEY = os.getenv("DATADOG_APP_KEY", "YourDatadogAppKey")

# Initialize Datadog API
options = {
    "api_key": DATADOG_API_KEY,
    "app_key": DATADOG_APP_KEY
}
initialize(**options)

def enable_aws_xray_on_lambda():
    """
    Enables AWS X-Ray tracing for a specific Lambda function.
    """
    client = boto3.client("lambda", region_name=AWS_REGION)
    try:
        # Update function configuration to enable X-Ray tracing
        response = client.update_function_configuration(
            FunctionName=LAMBDA_FUNCTION_NAME,
            TracingConfig={"Mode": "Active"}
        )
        logger.info(f"X-Ray tracing enabled for Lambda function: {LAMBDA_FUNCTION_NAME}")
        logger.debug(f"AWS Response: {response}")
    except (NoCredentialsError, PartialCredentialsError) as e:
        logger.error("AWS credentials not found or incomplete. Please configure them.")
        raise
    except client.exceptions.ResourceNotFoundException:
        logger.error(f"Lambda function '{LAMBDA_FUNCTION_NAME}' not found.")
        raise
    except Exception as e:
        logger.error(f"An error occurred while enabling X-Ray on Lambda: {str(e)}")
        raise

def create_datadog_dashboard():
    """
    Creates a Datadog dashboard to monitor AWS X-Ray and Lambda metrics.
    """
    try:
        dashboard = {
            "title": "AWS X-Ray and Lambda Monitoring",
            "widgets": [
                {
                    "definition": {
                        "type": "timeseries",
                        "requests": [
                            {
                                "q": "avg:aws.lambda.duration{*}",
                                "display_type": "line",
                                "style": {"palette": "dog_classic", "line_type": "solid", "line_width": "normal"}
                            }
                        ],
                        "title": "Lambda Duration"
                    }
                },
                {
                    "definition": {
                        "type": "timeseries",
                        "requests": [
                            {
                                "q": "sum:aws.xray.segment{*}",
                                "display_type": "line",
                                "style": {"palette": "cool", "line_type": "solid", "line_width": "normal"}
                            }
                        ],
                        "title": "X-Ray Segments"
                    }
                }
            ],
            "layout_type": "ordered",
            "description": "Dashboard to monitor AWS X-Ray and Lambda metrics.",
            "is_read_only": False,
            "notify_list": []
        }
        # Create the dashboard in Datadog
        response = api.Dashboard.create(**dashboard)
        logger.info("Datadog dashboard created successfully.")
        logger.debug(f"Datadog Response: {response}")
    except Exception as e:
        logger.error(f"An error occurred while creating the Datadog dashboard: {str(e)}")
        raise

def main():
    """
    Main function to orchestrate enabling AWS X-Ray on Lambda and setting up a Datadog dashboard.
    """
    try:
        logger.info("Starting automation script for AWS X-Ray and Datadog APM.")
        
        # Enable X-Ray tracing on Lambda
        enable_aws_xray_on_lambda()

        # Create a Datadog dashboard for monitoring
        create_datadog_dashboard()

        logger.info("Automation tasks completed successfully.")
    except Exception as e:
        logger.error(f"Script failed: {str(e)}")

if __name__ == "__main__":
    main()
```
