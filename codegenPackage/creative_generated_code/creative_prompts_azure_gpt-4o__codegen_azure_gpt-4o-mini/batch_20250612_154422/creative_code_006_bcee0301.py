"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tbayr543dvr2hxnf25hjxnm4rpzjhw3c7mwvzwj6oatzilgnxqqq.arweave.net
Prompt: Create a function to continuously poll an Arweave node and log changes in the "queue_length" and "peers" count over time.
Generated: DETERMINISTIC_bcee0301139b1b49
Batch ID: 20250612_154422
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:1984": {
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

def poll_arweave_node(node_url, interval=10):
    """
    Continuously polls the specified Arweave node for changes in queue_length and peers count.

    Parameters:
    - node_url (str): The URL of the Arweave node to poll.
    - interval (int): Time in seconds between each poll. Default is 10 seconds.
    """
    last_queue_length = None
    last_peers_count = None

    while True:
        try:
            # Make a request to the Arweave node
            response = requests.get(f"{node_url}/info")

            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Parse the JSON response
            data = response.json()
            current_queue_length = data.get('queue_length')
            current_peers_count = data.get('peers')

            # Log changes in queue_length
            if last_queue_length is None or current_queue_length != last_queue_length:
                logging.info(f"Queue Length changed: {last_queue_length} -> {current_queue_length}")
                last_queue_length = current_queue_length

            # Log changes in peers count
            if last_peers_count is None or current_peers_count != last_peers_count:
                logging.info(f"Peers Count changed: {last_peers_count} -> {current_peers_count}")
                last_peers_count = current_peers_count

        except requests.exceptions.RequestException as e:
            logging.error(f"Error while polling the Arweave node: {e}")

        # Wait for the specified interval before the next poll
        time.sleep(interval)

# Example usage:
# poll_arweave_node("http://localhost:1984", interval=10)
```
