"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://p3gnmpkzz7bdg3pxf7p4hgpwb4d7u77rhdcllh4h54gp7m5pl2qa.arweave.net
Prompt: Write a program that continuously polls an Arweave node for the `queue_length` and logs the data to a file for later analysis.
Generated: DETERMINISTIC_822ac597a60e7008
Batch ID: 20250612_154529
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://arweave.net/metrics": {
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
import time
import logging
from datetime import datetime

# Configure logging to record data to a file
LOG_FILE = "queue_length_log.txt"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Constants
ARWEAVE_NODE_URL = "https://arweave.net/metrics"
POLL_INTERVAL_SECONDS = 60  # Polling interval in seconds

def fetch_queue_length():
    """
    Fetch the queue_length from the Arweave node metrics endpoint.
    Returns:
        int: The queue length if successfully fetched.
    Raises:
        requests.exceptions.RequestException: If there is a network or other request-related error.
        ValueError: If the response does not contain valid queue_length data.
    """
    try:
        response = requests.get(ARWEAVE_NODE_URL, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad status codes (e.g., 4xx, 5xx)
        data = response.json()  # Parse JSON response
        
        # Check if the expected key exists in the response
        if "queue_length" not in data:
            raise ValueError("Response JSON does not contain 'queue_length' key.")
        
        return int(data["queue_length"])
    except requests.exceptions.RequestException as e:
        logging.error(f"Network error while fetching queue_length: {e}")
        raise
    except ValueError as e:
        logging.error(f"Data error: {e}")
        raise

def log_queue_length(queue_length):
    """
    Log the queue length to the log file.

    Args:
        queue_length (int): The queue length to log.
    """
    logging.info(f"Queue Length: {queue_length}")

def main():
    """
    Main function to continuously poll the Arweave node for queue_length and log it.
    """
    logging.info("Starting Arweave queue_length polling.")
    while True:
        try:
            queue_length = fetch_queue_length()
            log_queue_length(queue_length)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
        time.sleep(POLL_INTERVAL_SECONDS)  # Wait for the defined interval before polling again

if __name__ == "__main__":
    main()
```
