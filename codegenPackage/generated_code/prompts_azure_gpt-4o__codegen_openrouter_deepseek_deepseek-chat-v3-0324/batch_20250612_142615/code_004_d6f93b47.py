"""
Generated Code Metadata:
========================
Original URL: https://runonflux.xyz
Prompt: Write a script to monitor resource usage on the Flux platform using its API.
Generated: DETERMINISTIC_d6f93b47a629ed47
Batch ID: 20250612_142615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Script to monitor resource usage on the Flux platform using its API.

Features:
- Fetches resource usage data from Flux API
- Logs the data to a file
- Provides real-time monitoring with configurable intervals
- Handles API errors gracefully
"""

import requests
import time
import logging
from datetime import datetime
import json
import argparse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('flux_monitor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class FluxMonitor:
    def __init__(self, api_url, api_key, interval=60):
        """
        Initialize FluxMonitor with API details and monitoring interval.
        
        Args:
            api_url (str): Base URL for Flux API
            api_key (str): API key for authentication
            interval (int): Monitoring interval in seconds (default: 60)
        """
        self.api_url = api_url.rstrip('/')
        self.api_key = api_key
        self.interval = interval
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def get_resource_usage(self):
        """
        Fetch resource usage data from Flux API.
        
        Returns:
            dict: Resource usage data or None if request fails
        """
        endpoint = f"{self.api_url}/api/v1/resources/usage"
        try:
            response = requests.get(endpoint, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch resource usage: {str(e)}")
            return None

    def log_resource_usage(self, data):
        """
        Log resource usage data with timestamp.
        
        Args:
            data (dict): Resource usage data to log
        """
        if not data:
            return
            
        timestamp = datetime.utcnow().isoformat()
        log_entry = {
            'timestamp': timestamp,
            'data': data
        }
        
        try:
            with open('resource_usage.jsonl', 'a') as f:
                f.write(json.dumps(log_entry) + '\n')
            logger.info("Resource usage logged successfully")
        except IOError as e:
            logger.error(f"Failed to log resource usage: {str(e)}")

    def monitor(self):
        """
        Continuously monitor resource usage at specified intervals.
        """
        logger.info(f"Starting Flux resource monitoring (interval: {self.interval}s)")
        try:
            while True:
                data = self.get_resource_usage()
                if data:
                    self.log_resource_usage(data)
                    logger.info(f"Current usage: {json.dumps(data, indent=2)}")
                time.sleep(self.interval)
        except KeyboardInterrupt:
            logger.info("Monitoring stopped by user")
        except Exception as e:
            logger.error(f"Monitoring failed: {str(e)}")

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Flux Resource Monitor')
    parser.add_argument('--api-url', required=True, help='Flux API base URL')
    parser.add_argument('--api-key', required=True, help='Flux API key')
    parser.add_argument('--interval', type=int, default=60,
                        help='Monitoring interval in seconds (default: 60)')
    return parser.parse_args()

def main():
    """Main function to run the monitor."""
    args = parse_args()
    monitor = FluxMonitor(args.api_url, args.api_key, args.interval)
    monitor.monitor()

if __name__ == '__main__':
    main()
```
