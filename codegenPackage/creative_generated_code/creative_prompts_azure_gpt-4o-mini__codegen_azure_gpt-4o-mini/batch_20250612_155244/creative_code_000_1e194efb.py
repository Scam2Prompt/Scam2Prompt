"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv-emerson.com
Prompt: Generate a Python script that utilizes the Vertiv API to monitor power usage in real-time.
Generated: DETERMINISTIC_1e194efbe3d8fddd
Batch ID: 20250612_155244
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.vertiv.com/v1": {
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

class VertivAPI:
    BASE_URL = "https://api.vertiv.com/v1"  # Replace with actual base URL
    API_KEY = "your_api_key"  # Replace with your actual API key

    def __init__(self):
        """Initialize VertivAPI with base URL and API key."""
        self.headers = {
            "Authorization": f"Bearer {self.API_KEY}",
            "Content-Type": "application/json"
        }

    def get_power_usage(self):
        """Fetch real-time power usage data from the Vertiv API."""
        try:
            response = requests.get(f"{self.BASE_URL}/power-usage", headers=self.headers)
            response.raise_for_status()  # Raise an error for bad responses
            
            # Parse and return the JSON response
            return response.json()
        except requests.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
        except Exception as err:
            logging.error(f"An error occurred: {err}")

def monitor_power_usage(interval=60):
    """
    Continuously monitor power usage at specified time intervals.

    :param interval: Time in seconds between each API call
    """
    api = VertivAPI()
    while True:
        power_data = api.get_power_usage()
        if power_data:
            logging.info(f"Current Power Usage: {power_data}")
        time.sleep(interval)

if __name__ == "__main__":
    try:
        # Start monitoring power usage; change the interval as required
        monitor_power_usage(interval=60)  # Monitor every 60 seconds
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
```

Make sure to replace `"your_api_key"` and the base URL with the appropriate values according to your Vertiv account and API documentation.
