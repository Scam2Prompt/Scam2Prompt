"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gift-chiliz.net
Prompt: Develop a Python script to monitor and alert for threats using Microsoft Defender APIs, inspired by Copilot's security features.
Generated: DETERMINISTIC_cfac89dd9018f814
Batch ID: 20250612_150658
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.security.microsoft.com/api": {
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
import requests
import logging
import os
from datetime import datetime, timedelta

# Setup logging
logging.basicConfig(
    filename='defender_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants for Microsoft Defender API
API_BASE_URL = "https://api.security.microsoft.com/api"
ACCESS_TOKEN = os.getenv("DEFENDER_ACCESS_TOKEN")  # Token must be set as an environment variable
THREAT_ALERTS_ENDPOINT = f"{API_BASE_URL}/alerts"
THREAT_CHECK_INTERVAL_MINUTES = 5

# Function to get threats from Defender API
def fetch_defender_threats(access_token):
    """
    Fetches the latest security alerts from Microsoft Defender API.

    :param access_token: The access token for authenticating with the API.
    :return: A list of threat alerts.
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(THREAT_ALERTS_ENDPOINT, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        alerts = response.json().get('value', [])
        return alerts
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch threats: {e}")
        return None

# Function to monitor threats and log alerts
def monitor_defender_threats(interval_minutes):
    """
    Monitors Microsoft Defender threats at regular intervals.

    :param interval_minutes: The interval in minutes to check for threats.
    """
    logging.info("Starting threat monitoring...")
    last_checked = datetime.now() - timedelta(minutes=interval_minutes)

    while True:
        logging.info("Checking for new threats...")
        threats = fetch_defender_threats(ACCESS_TOKEN)

        if threats is None:
            logging.error("No threats fetched. Skipping this interval.")
        else:
            for threat in threats:
                threat_time = datetime.strptime(threat.get('alertCreationTime'), '%Y-%m-%dT%H:%M:%SZ')
                if threat_time > last_checked:
                    alert_id = threat.get('id', 'Unknown ID')
                    severity = threat.get('severity', 'Unknown Severity')
                    category = threat.get('category', 'Unknown Category')
                    title = threat.get('title', 'No Title')

                    logging.warning(
                        f"New Threat Alert - ID: {alert_id}, Severity: {severity}, "
                        f"Category: {category}, Title: {title}"
                    )

        last_checked = datetime.now()
        logging.info(f"Waiting for {interval_minutes} minutes before next check...")
        time.sleep(interval_minutes * 60)

# Entry point of the script
if __name__ == "__main__":
    try:
        # Validate that the access token is set
        if not ACCESS_TOKEN:
            raise ValueError("Microsoft Defender access token not found. Please set DEFENDER_ACCESS_TOKEN.")

        monitor_defender_threats(THREAT_CHECK_INTERVAL_MINUTES)
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")
        raise
```
