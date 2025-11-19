"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Write a Python script that automates tasks mentioned in the blog, specifically for using AWS X-Ray with Lambda and Datadog APM.
Generated: DETERMINISTIC_d9bfb42ed0d4db44
Batch ID: 20250612_163408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.datadoghq.com/api/v1/series": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import boto3
import json
import os
import logging
import requests

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants for AWS and Datadog
AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
DATADOG_API_KEY = os.getenv('DATADOG_API_KEY')
DATADOG_APP_KEY = os.getenv('DATADOG_APP_KEY')
DATADOG_API_URL = 'https://api.datadoghq.com/api/v1/series'

# Initialize the AWS X-Ray client
xray_client = boto3.client('xray', region_name=AWS_REGION)

def get_trace_data(trace_id):
    """
    Retrieve trace data from AWS X-Ray given a trace ID.

    :param trace_id: ID of the trace to retrieve
    :return: Trace data as a dictionary
    """
    try:
        response = xray_client.get_trace(Id=trace_id)
        trace_data = response['Trace']
        logger.info(f"Successfully retrieved trace data for trace ID: {trace_id}")
        return trace_data
    except Exception as e:
        logger.error(f"Error retrieving trace data: {e}")
        raise

def send_trace_to_datadog(trace_data):
    """
    Send the trace data to Datadog APM.

    :param trace_data: Trace data to send
    """
    if not DATADOG_API_KEY or not DATADOG_APP_KEY:
        logger.error("Datadog API key or application key is missing.")
        return

    # Prepare payload for Datadog
    payload = {
        "series": [
            {
                "metric": "aws.xray.traces",
                "points": [[int(trace_data['StartTime'] * 1000), len(trace_data['Segments'])]],
                "tags": ["service:my_lambda_service", f"trace_id:{trace_data['Id']}"],
            }
        ]
    }

    try:
        response = requests.post(
            DATADOG_API_URL,
            headers={"Content-Type": "application/json",
                     "DD-API-KEY": DATADOG_API_KEY,
                     "DD-APPLICATION-KEY": DATADOG_APP_KEY},
            data=json.dumps(payload)
        )
        response.raise_for_status()
        logger.info("Successfully sent trace data to Datadog.")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred while sending to Datadog: {http_err}")
    except Exception as e:
        logger.error(f"Error occurred while sending trace data to Datadog: {e}")

def main(trace_id):
    """
    Main function to run the script.

    :param trace_id: ID of the trace to process
    """
    try:
        trace_data = get_trace_data(trace_id)
        send_trace_to_datadog(trace_data)
    except Exception as e:
        logger.error(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    # Example trace ID
    example_trace_id = "1-5c8c3d7c-0c84e9b5e6cbe101c93b1876"  # Replace with your actual trace ID
    main(example_trace_id)
```
