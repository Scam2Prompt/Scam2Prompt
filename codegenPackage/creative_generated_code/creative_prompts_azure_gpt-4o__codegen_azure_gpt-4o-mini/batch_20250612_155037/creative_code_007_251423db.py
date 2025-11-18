"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperlane.cc
Prompt: Generate a Python script that interacts with Hyperlane's APIs to monitor cross-chain message status and log the results.
Generated: DETERMINISTIC_251423dbf7ec5155
Batch ID: 20250612_155037
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hyperlane.xyz/messages": {
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Hyperlane API Endpoint
HYPERLANE_API_URL = "https://api.hyperlane.xyz/messages"

# Function to check the status of a cross-chain message
def check_message_status(message_id, retries=3, delay=5):
    """
    Check the status of a message on Hyperlane's API.

    :param message_id: The unique identifier of the message to check.
    :param retries: Number of times to retry the API call in case of failure.
    :param delay: Delay (in seconds) between retries.
    :return: Status of the message if successful, None otherwise.
    """
    for attempt in range(retries):
        try:
            response = requests.get(f"{HYPERLANE_API_URL}/{message_id}")
            response.raise_for_status()  # Raise an error for bad responses
            
            # Log the response data
            logging.info(f"Successfully retrieved message status for ID {message_id}: {response.json()}")
            return response.json()
        
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err} (Attempt {attempt + 1}/{retries})")
        
        except requests.exceptions.RequestException as req_err:
            logging.error(f"Request error occurred: {req_err} (Attempt {attempt + 1}/{retries})")
        
        # Wait before retrying
        time.sleep(delay)
    
    logging.error(f"Failed to retrieve message status for ID {message_id} after {retries} attempts.")
    return None

def monitor_messages(message_ids, polling_interval=60):
    """
    Monitor the status of multiple messages and log the results.

    :param message_ids: A list of message IDs to monitor.
    :param polling_interval: Time interval (in seconds) to wait between status checks.
    """
    while True:
        for message_id in message_ids:
            status = check_message_status(message_id)
            if status:
                logging.info(f"Current status for message ID {message_id}: {status['status']}")
        
        # Wait for the next polling interval
        time.sleep(polling_interval)

if __name__ == "__main__":
    # Example message IDs to monitor (replace with actual message IDs)
    message_ids_to_monitor = ["msg_1", "msg_2", "msg_3"]
    
    # Start monitoring the specified messages
    logging.info("Starting message monitoring...")
    monitor_messages(message_ids_to_monitor)
```
