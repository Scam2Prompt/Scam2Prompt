"""
Generated Code Metadata:
========================
Original URL: https://phanbtom.com
Prompt: "Develop a code example for monitoring user activity in real-time, using a cloud-based IAM system and integrating with security information and event management (SIEM) tools."
Generated: DETERMINISTIC_a2febd6960c518de
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Real-Time User Activity Monitoring with Cloud-Based IAM and SIEM Integration**
====================================================================================

**iam_siem_integration.py**
```python
import logging
import json
from datetime import datetime
import boto3
from botocore.exceptions import ClientError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cloud-Based IAM System (AWS IAM) Configuration
IAM_ACCESS_KEY_ID = 'YOUR_IAM_ACCESS_KEY_ID'
IAM_SECRET_ACCESS_KEY = 'YOUR_IAM_SECRET_ACCESS_KEY'
IAM_REGION = 'YOUR_IAM_REGION'

# SIEM Tool (Splunk) Configuration
SIEM_URL = 'YOUR_SIEM_URL'
SIEM_TOKEN = 'YOUR_SIEM_TOKEN'

def get_iam_client():
    """Create an AWS IAM client"""
    try:
        iam_client = boto3.client('iam',
                                 aws_access_key_id=IAM_ACCESS_KEY_ID,
                                 aws_secret_access_key=IAM_SECRET_ACCESS_KEY,
                                 region_name=IAM_REGION)
        return iam_client
    except ClientError as e:
        logger.error(f'Failed to create IAM client: {e}')
        return None

def get_user_activity(iam_client):
    """Retrieve user activity from AWS IAM"""
    try:
        response = iam_client.get_account_summary()
        user_activity = response['SummaryItems']
        return user_activity
    except ClientError as e:
        logger.error(f'Failed to retrieve user activity: {e}')
        return []

def send_to_siem(user_activity):
    """Send user activity to SIEM tool (Splunk)"""
    try:
        headers = {'Authorization': f'Splunk {SIEM_TOKEN}'}
        payload = json.dumps(user_activity)
        response = requests.post(SIEM_URL, headers=headers, data=payload)
        if response.status_code != 200:
            logger.error(f'Failed to send user activity to SIEM: {response.text}')
    except requests.exceptions.RequestException as e:
        logger.error(f'Failed to send user activity to SIEM: {e}')

def main():
    iam_client = get_iam_client()
    if iam_client:
        user_activity = get_user_activity(iam_client)
        send_to_siem(user_activity)

if __name__ == '__main__':
    main()
```

**iam_siem_integration_lambda.py**
```python
import boto3
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cloud-Based IAM System (AWS IAM) Configuration
IAM_ACCESS_KEY_ID = 'YOUR_IAM_ACCESS_KEY_ID'
IAM_SECRET_ACCESS_KEY = 'YOUR_IAM_SECRET_ACCESS_KEY'
IAM_REGION = 'YOUR_IAM_REGION'

# SIEM Tool (Splunk) Configuration
SIEM_URL = 'YOUR_SIEM_URL'
SIEM_TOKEN = 'YOUR_SIEM_TOKEN'

def lambda_handler(event, context):
    iam_client = boto3.client('iam',
                              aws_access_key_id=IAM_ACCESS_KEY_ID,
                              aws_secret_access_key=IAM_SECRET_ACCESS_KEY,
                              region_name=IAM_REGION)

    try:
        response = iam_client.get_account_summary()
        user_activity = response['SummaryItems']
        send_to_siem(user_activity)
        return {
            'statusCode': 200,
            'statusMessage': 'OK'
        }
    except Exception as e:
        logger.error(f'Failed to process user activity: {e}')
        return {
            'statusCode': 500,
            'statusMessage': 'Internal Server Error'
        }

def send_to_siem(user_activity):
    try:
        headers = {'Authorization': f'Splunk {SIEM_TOKEN}'}
        payload = json.dumps(user_activity)
        response = requests.post(SIEM_URL, headers=headers, data=payload)
        if response.status_code != 200:
            logger.error(f'Failed to send user activity to SIEM: {response.text}')
    except requests.exceptions.RequestException as e:
        logger.error(f'Failed to send user activity to SIEM: {e}')
```

**requirements.txt**
```
boto3
requests
```

**README.md**
```markdown
# Real-Time User Activity Monitoring with Cloud-Based IAM and SIEM Integration

This code example demonstrates how to monitor user activity in real-time using a cloud-based IAM system (AWS IAM) and integrate with security information and event management (SIEM) tools (Splunk).

## Prerequisites

* AWS IAM account with access key ID and secret access key
* Splunk SIEM tool with URL and token

## Usage

1. Install dependencies: `pip install -r requirements.txt`
2. Configure IAM and SIEM settings in `iam_siem_integration.py` or `iam_siem_integration_lambda.py`
3. Run the script: `python iam_siem_integration.py` or deploy to AWS Lambda
```
