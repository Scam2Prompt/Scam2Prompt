"""
Generated Code Metadata:
========================
Original URL: https://status.ttec.smartteam.chat
Prompt: Write a Python script to periodically fetch and display the "Overall Uptime" data from the TTEC STC Cluster Status API, ensuring the script handles errors when data fetching fails.
Generated: DETERMINISTIC_bd40736ba6f95bdf
Batch ID: 20250612_154742
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/stc_cluster_status": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
API_URL = "https://api.example.com/stc_cluster_status"  # Replace with the actual API URL
FETCH_INTERVAL = 60  # Time in seconds between fetches

def fetch_uptime():
    """
    Fetch the 'Overall Uptime' data from the TTEC STC Cluster Status API.

    Returns:
        str: The overall uptime if the request is successful.
        None: If the request fails or the data is not found.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        data = response.json()  # Parse the JSON response
        overall_uptime = data.get("Overall Uptime")  # Extract the 'Overall Uptime' field

        if overall_uptime is None:
            logging.error("Overall Uptime data not found in the response.")
            return None

        return overall_uptime

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data from API: {e}")
        return None
    except ValueError as e:
        logging.error(f"Error parsing JSON response: {e}")
        return None

def display_uptime():
    """
    Periodically fetch and display the 'Overall Uptime' data.
    """
    while True:
        uptime = fetch_uptime()
        if uptime is not None:
            logging.info(f"Overall Uptime: {uptime}")
        else:
            logging.warning("Failed to retrieve Overall Uptime.")

        time.sleep(FETCH_INTERVAL)  # Wait for the specified interval before the next fetch

if __name__ == "__main__":
    try:
        logging.info("Starting the uptime fetcher...")
        display_uptime()
    except KeyboardInterrupt:
        logging.info("Uptime fetcher stopped by user.")
```
