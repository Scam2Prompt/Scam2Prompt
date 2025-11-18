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
  "https://api.security.microsoft.com/api/": {
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
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for Microsoft Defender API
DEFENDER_API_URL = "https://api.security.microsoft.com/api/"
THREAT_ALERTS_ENDPOINT = "threatAlerts"
API_TOKEN = "YOUR_API_TOKEN"  # Replace with your Microsoft Defender API token

# Function to get threat alerts from Microsoft Defender API
def get_threat_alerts():
    """
    Fetches threat alerts from Microsoft Defender API.
    
    Returns:
        list: A list of threat alerts or an empty list if an error occurs.
    """
    try:
        headers = {
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json"
        }
        response = requests.get(DEFENDER_API_URL + THREAT_ALERTS_ENDPOINT, headers=headers)

        # Check if the request was successful
        response.raise_for_status()

        # Return the JSON response containing threat alerts
        return response.json().get('value', [])

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        logging.error(f"An error occurred: {err}")
    
    return []

# Function to alert the user about the threats
def alert_user(threat_alerts):
    """
    Alerts the user about the detected threats.
    
    Args:
        threat_alerts (list): A list of threat alerts.
    """
    for alert in threat_alerts:
        logging.warning(f"Threat Alert: {alert.get('title')}")
        logging.info(f"Severity: {alert.get('severity')}")
        logging.info(f"Description: {alert.get('description')}")
        # Here you could add integration with email/SMS services for real alerts

# Main function to monitor threats
def monitor_threats(interval=60):
    """
    Monitors for threats at a defined interval.
    
    Args:
        interval (int): Time in seconds to wait before checking for threats again.
    """
    logging.info("Starting threat monitoring...")
    
    while True:
        threat_alerts = get_threat_alerts()
        
        if threat_alerts:
            alert_user(threat_alerts)
        else:
            logging.info("No new threat alerts detected.")

        time.sleep(interval)  # Wait for the specified interval before checking again

if __name__ == "__main__":
    try:
        monitor_threats(interval=60)  # Monitor threats every 60 seconds
    except KeyboardInterrupt:
        logging.info("Threat monitoring stopped by user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```

**Note:** Replace `YOUR_API_TOKEN` with your actual Microsoft Defender API token before running the script.
