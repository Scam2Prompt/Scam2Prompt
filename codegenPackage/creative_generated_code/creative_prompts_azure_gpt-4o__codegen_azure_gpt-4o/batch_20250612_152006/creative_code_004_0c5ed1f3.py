"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polyhedra-consulting.com
Prompt: Write a script to monitor server performance metrics on OVHcloud using their API or recommended tools.
Generated: DETERMINISTIC_0c5ed1f3d1f50226
Batch ID: 20250612_152006
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://eu.api.ovh.com/1.0": {
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

# Configure logging
logging.basicConfig(
    filename='server_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# OVHcloud API credentials
API_KEY = "your_api_key_here"
APP_SECRET = "your_app_secret_here"
CONSUMER_KEY = "your_consumer_key_here"
BASE_URL = "https://eu.api.ovh.com/1.0"

# List of server IDs to monitor
SERVER_IDS = ["server1_id", "server2_id"]  # Replace with your OVHcloud server IDs

# Function to get server metrics
def get_server_metrics(server_id):
    """
    Fetch performance metrics for a specific server using OVHcloud API.

    Args:
        server_id (str): The ID of the server to monitor.

    Returns:
        dict: A dictionary containing performance metrics.
    """
    try:
        url = f"{BASE_URL}/dedicated/server/{server_id}/metrics"
        headers = {
            "X-Ovh-Application": API_KEY,
            "X-Ovh-Consumer": CONSUMER_KEY,
            "X-Ovh-Signature": APP_SECRET,
        }
        response = requests.get(url, headers=headers)

        # Raise an exception for HTTP errors
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching metrics for server {server_id}: {e}")
        return None

def monitor_servers(server_ids, interval=60):
    """
    Monitor performance metrics for a list of servers at regular intervals.

    Args:
        server_ids (list): List of server IDs to monitor.
        interval (int): Time interval (in seconds) between metric checks.
    """
    logging.info("Starting server monitoring...")
    while True:
        for server_id in server_ids:
            metrics = get_server_metrics(server_id)
            if metrics:
                # Log metrics (customize based on your needs)
                logging.info(f"Metrics for server {server_id}: {metrics}")
            else:
                logging.warning(f"No metrics available for server {server_id}")
        logging.info(f"Waiting {interval} seconds before next check...")
        time.sleep(interval)

if __name__ == "__main__":
    try:
        # Start monitoring servers
        monitor_servers(SERVER_IDS)
    except KeyboardInterrupt:
        logging.info("Server monitoring stopped by user.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
```

### Notes:
- Replace `your_api_key_here`, `your_app_secret_here`, and `your_consumer_key_here` with actual OVHcloud API credentials.
- Replace `SERVER_IDS` with the IDs of the servers you want to monitor.
- Customize logging and metric processing as needed.
