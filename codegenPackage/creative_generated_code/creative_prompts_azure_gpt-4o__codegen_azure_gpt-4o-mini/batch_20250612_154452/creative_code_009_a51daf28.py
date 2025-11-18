"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mysonicwall.ir
Prompt: Create a Python function to send alerts based on SonicWall firewall threat detection logs using its API.
Generated: DETERMINISTIC_a51daf287187bd3a
Batch ID: 20250612_154452
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sonicwall.com": {
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
from requests.exceptions import HTTPError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SonicWallAPI:
    def __init__(self, base_url, api_key):
        """
        Initialize the SonicWallAPI with base URL and API key.
        
        :param base_url: Base URL of the SonicWall API
        :param api_key: API key for authentication
        """
        self.base_url = base_url
        self.api_key = api_key

    def get_threat_logs(self):
        """
        Fetch threat detection logs from the SonicWall firewall.
        
        :return: List of threat logs
        :raises HTTPError: If the request to the API fails
        """
        endpoint = f"{self.base_url}/threat_logs"
        headers = {'Authorization': f'Bearer {self.api_key}'}
        
        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            logging.info("Successfully retrieved threat logs.")
            return response.json()  # Assuming the response is in JSON format
        except HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            raise  # Re-raise the error for further handling
        except Exception as err:
            logging.error(f"An error occurred: {err}")
            raise  # Re-raise the error for further handling

    def send_alert(self, alert_message):
        """
        Send alert via a preferred method (e.g., email, SMS, etc.).
        
        :param alert_message: The message to be sent as an alert
        """
        # Placeholder for alert sending logic
        logging.info(f"Alert sent: {alert_message}")

def process_threat_logs(api):
    """
    Process the fetched threat logs and send alerts for specific threats.
    
    :param api: An instance of SonicWallAPI
    """
    try:
        logs = api.get_threat_logs()
        for log in logs:
            if log.get('severity') == 'high':  # Check for high severity threats
                alert_message = f"High severity threat detected: {log.get('description')}"
                api.send_alert(alert_message)
                logging.info("Alert processed for high severity threat.")
    except Exception as e:
        logging.error(f"Failed to process threat logs: {e}")

if __name__ == "__main__":
    # Configuration for SonicWall API
    BASE_URL = "https://api.sonicwall.com"
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    # Create an instance of the SonicWallAPI class
    sonicwall_api = SonicWallAPI(BASE_URL, API_KEY)
    
    # Process threat logs and send alerts
    process_threat_logs(sonicwall_api)
```
