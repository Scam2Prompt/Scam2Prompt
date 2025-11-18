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
  "https://api.hyperlane.xyz": {
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
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("cross_chain_monitor.log"),
        logging.StreamHandler()
    ]
)

# Hyperlane API base URL
BASE_URL = "https://api.hyperlane.xyz"

# Endpoints
MESSAGE_STATUS_ENDPOINT = "/v1/messages/status"
MESSAGE_DETAILS_ENDPOINT = "/v1/messages/details"

# API timeout setting
API_TIMEOUT = 10  # seconds


def get_message_status(message_id):
    """
    Fetch the status of a cross-chain message from Hyperlane API.
    
    Args:
        message_id (str): The unique ID of the message.
    
    Returns:
        dict: JSON response containing the status information.
    
    Raises:
        Exception: If the API request fails or returns an error.
    """
    url = f"{BASE_URL}{MESSAGE_STATUS_ENDPOINT}/{message_id}"
    
    try:
        response = requests.get(url, timeout=API_TIMEOUT)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch message status for ID {message_id}: {e}")
        raise Exception(f"Error fetching status for message ID {message_id}") from e


def get_message_details(message_id):
    """
    Fetch detailed information about a cross-chain message from Hyperlane API.
    
    Args:
        message_id (str): The unique ID of the message.
    
    Returns:
        dict: JSON response containing detailed message information.
    
    Raises:
        Exception: If the API request fails or returns an error.
    """
    url = f"{BASE_URL}{MESSAGE_DETAILS_ENDPOINT}/{message_id}"
    
    try:
        response = requests.get(url, timeout=API_TIMEOUT)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch message details for ID {message_id}: {e}")
        raise Exception(f"Error fetching details for message ID {message_id}") from e


def monitor_message_status(message_id):
    """
    Monitors the status of a given cross-chain message and logs the result.
    
    Args:
        message_id (str): The unique ID of the message to monitor.
    """
    try:
        status = get_message_status(message_id)
        details = get_message_details(message_id)
        
        logging.info(f"Message ID: {message_id}")
        logging.info(f"Status: {status.get('status', 'Unknown')}")
        logging.info(f"Details: {details}")
    except Exception as e:
        logging.error(f"Failed to monitor message ID {message_id}: {e}")


def main():
    """
    Main function to monitor a set of cross-chain messages.
    """
    # List of message IDs to monitor
    message_ids = [
        "message_123",
        "message_456",
        "message_789"
    ]

    logging.info("Starting message monitoring...")
    
    for message_id in message_ids:
        logging.info(f"Monitoring message ID: {message_id}")
        monitor_message_status(message_id)

    logging.info("Finished message monitoring.")


if __name__ == "__main__":
    main()
```
