"""
Generated Code Metadata:
========================
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

# Generated Code:
# ===============

```python
import requests
import time
import logging

# Set up logging configuration
logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

def get_arweave_node_info(node_url: str) -> dict:
    """
    Retrieves information from an Arweave node.

    Args:
    - node_url (str): The URL of the Arweave node.

    Returns:
    - dict: A dictionary containing the node's information.

    Raises:
    - requests.RequestException: If the request to the node fails.
    """
    try:
        response = requests.get(node_url + "/info")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Failed to retrieve node info: {e}")
        return {}

def poll_arweave_node(node_url: str, poll_interval: int = 60) -> None:
    """
    Continuously polls an Arweave node and logs changes in the "queue_length" and "peers" count.

    Args:
    - node_url (str): The URL of the Arweave node.
    - poll_interval (int): The interval in seconds between polls. Defaults to 60.
    """
    previous_queue_length = None
    previous_peers_count = None

    while True:
        node_info = get_arweave_node_info(node_url)
        if not node_info:
            continue

        queue_length = node_info.get("queueLength", 0)
        peers_count = node_info.get("peers", 0)

        if previous_queue_length is not None:
            if queue_length != previous_queue_length:
                logging.info(f"Queue length changed: {previous_queue_length} -> {queue_length}")
        previous_queue_length = queue_length

        if previous_peers_count is not None:
            if peers_count != previous_peers_count:
                logging.info(f"Peers count changed: {previous_peers_count} -> {peers_count}")
        previous_peers_count = peers_count

        logging.info(f"Current queue length: {queue_length}, Current peers count: {peers_count}")
        time.sleep(poll_interval)

if __name__ == "__main__":
    node_url = "http://localhost:1984"  # replace with your Arweave node URL
    poll_interval = 60  # adjust the poll interval as needed
    poll_arweave_node(node_url, poll_interval)
```
