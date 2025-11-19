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
import os
import boto3
import json
import logging
from datadog import initialize, api

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AWSXRayDatadogIntegration:
    """
    A class to automate AWS X-Ray integration with Datadog APM for Lambda functions.
    """

    def __init__(self, aws_region, datadog_api_key, datadog_app_key):
        """
        Initialize the AWS and Datadog clients.

        Args:
            aws_region (str): AWS region where Lambda functions are deployed.
            datadog_api_key (str): Datadog API key for authentication.
            datadog_app_key (str): Datadog application key for authentication.
        """
        self.aws_region = aws_region
        self.lambda_client = boto3.client('lambda', region_name=aws_region)
        
        # Initialize Datadog
        initialize(api_key=datadog_api_key, app_key=datadog_app_key)

    def enable_xray_for_lambda(self, function_name):
        """
        Enable AWS X-Ray tracing for a Lambda function.

        Args:
            function_name (str): Name of the Lambda function.

        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            response = self.lambda_client.update_function_configuration(
                FunctionName=function_name,
                TracingConfig={
                    'Mode': 'Active'
                }
            )
            logger.info(f"Enabled X-Ray for Lambda function: {function_name}")
            return True
        except Exception as e:
            logger.error(f"Error enabling X-Ray for {function_name}: {str(e)}")
            return False

    def create_datadog_apm_integration(self, lambda_arn, service_name, env):
        """
        Create a Datadog APM integration for the Lambda function.

        Args:
            lambda_arn (str): ARN of the Lambda function.
            service_name (str): Name of the service in Datadog.
            env (str): Environment (e.g., 'prod', 'dev').

        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            # Create Datadog APM integration
            integration_data = {
                "type": "lambda",
                "arn": lambda_arn,
                "service": service_name,
                "env": env
            }
            response = api.AwsIntegration.create(**integration_data)
            logger.info(f"Created Datadog APM integration for Lambda ARN: {lambda_arn}")
            return True
        except Exception as e:
            logger.error(f"Error creating Datadog APM integration: {str(e)}")
            return False

    def automate_integration(self, function_name, service_name, env):
        """
        Automate the entire integration process for a Lambda function.

        Args:
            function_name (str): Name of the Lambda function.
            service_name (str): Name of the service in Datadog.
            env (str): Environment (e.g., 'prod', 'dev').

        Returns:
            bool: True if all steps succeed, False otherwise.
        """
        try:
            # Step 1: Enable X-Ray for Lambda
            if not self.enable_xray_for_lambda(function_name):
                return False

            # Step 2: Get Lambda ARN
            lambda_arn = self._get_lambda_arn(function_name)
            if not lambda_arn:
                return False

            # Step 3: Create Datadog APM integration
            if not self.create_datadog_apm_integration(lambda_arn, service_name, env):
                return False

            logger.info(f"Successfully integrated {function_name} with X-Ray and Datadog APM")
            return True
        except Exception as e:
            logger.error(f"Error during integration: {str(e)}")
            return False

    def _get_lambda_arn(self, function_name):
        """
        Helper method to get the ARN of a Lambda function.

        Args:
            function_name (str): Name of the Lambda function.

        Returns:
            str: ARN of the Lambda function, or None if error occurs.
        """
        try:
            response = self.lambda_client.get_function(FunctionName=function_name)
            return response['Configuration']['FunctionArn']
        except Exception as e:
            logger.error(f"Error getting ARN for {function_name}: {str(e)}")
            return None

def main():
    # Load configuration from environment variables
    aws_region = os.getenv('AWS_REGION')
    datadog_api_key = os.getenv('DATADOG_API_KEY')
    datadog_app_key = os.getenv('DATADOG_APP_KEY')
    lambda_function_name = os.getenv('LAMBDA_FUNCTION_NAME')
    service_name = os.getenv('SERVICE_NAME')
    env = os.getenv('ENVIRONMENT')

    # Validate environment variables
    if not all([aws_region, datadog_api_key, datadog_app_key, lambda_function_name, service_name, env]):
        logger.error("Missing required environment variables")
        return

    # Initialize and run integration
    integrator = AWSXRayDatadogIntegration(aws_region, datadog_api_key, datadog_app_key)
    success = integrator.automate_integration(lambda_function_name, service_name, env)

    if success:
        logger.info("Integration completed successfully")
    else:
        logger.error("Integration failed")

if __name__ == "__main__":
    main()
```
