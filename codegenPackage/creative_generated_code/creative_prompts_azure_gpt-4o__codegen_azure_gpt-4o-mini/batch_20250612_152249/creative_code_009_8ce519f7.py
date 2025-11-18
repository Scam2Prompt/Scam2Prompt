"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeih4xykf2fco4vzc7pigr5cqil62o4tbex5tpjg3tjheermgf4llpu.ipfs.dweb.link
Prompt: Generate a Python script for monitoring the performance and emissions of rNodes and zNodes in the Rivalz ecosystem, including staking upgrades.
Generated: DETERMINISTIC_8ce519f768336f68
Batch ID: 20250612_152249
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.rivalz.com/rnodes": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.rivalz.com/znodes": {
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
import time
import logging
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NodeMonitor:
    def __init__(self, rnode_url, znode_url):
        """
        Initialize NodeMonitor with the URLs for rNodes and zNodes.
        
        :param rnode_url: URL for the rNode API
        :param znode_url: URL for the zNode API
        """
        self.rnode_url = rnode_url
        self.znode_url = znode_url

    def fetch_node_data(self, url):
        """
        Fetch data from a specified node URL.
        
        :param url: The API endpoint to fetch data from
        :return: JSON data if successful, None otherwise
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching data from {url}: {e}")
            return None

    def monitor_nodes(self):
        """
        Continuously monitor the performance and emissions of rNodes and zNodes.
        """
        while True:
            # Fetch rNode data
            rnode_data = self.fetch_node_data(self.rnode_url)
            if rnode_data:
                self.process_rnode_data(rnode_data)

            # Fetch zNode data
            znode_data = self.fetch_node_data(self.znode_url)
            if znode_data:
                self.process_znode_data(znode_data)

            # Sleep for a defined interval before the next check
            time.sleep(60)  # Check every 60 seconds

    def process_rnode_data(self, data):
        """
        Process and log rNode performance and emissions data.
        
        :param data: JSON data containing rNode performance metrics
        """
        logging.info("Processing rNode data...")
        try:
            performance = data.get('performance', {})
            emissions = data.get('emissions', {})
            logging.info(f"rNode Performance: {performance}")
            logging.info(f"rNode Emissions: {emissions}")
        except Exception as e:
            logging.error(f"Error processing rNode data: {e}")

    def process_znode_data(self, data):
        """
        Process and log zNode performance and emissions data.
        
        :param data: JSON data containing zNode performance metrics
        """
        logging.info("Processing zNode data...")
        try:
            performance = data.get('performance', {})
            emissions = data.get('emissions', {})
            logging.info(f"zNode Performance: {performance}")
            logging.info(f"zNode Emissions: {emissions}")
        except Exception as e:
            logging.error(f"Error processing zNode data: {e}")

if __name__ == "__main__":
    # Replace these URLs with the actual API endpoints for rNodes and zNodes
    RNODE_URL = "https://api.rivalz.com/rnodes"
    ZNODE_URL = "https://api.rivalz.com/znodes"

    # Create an instance of NodeMonitor and start monitoring
    monitor = NodeMonitor(RNODE_URL, ZNODE_URL)
    monitor.monitor_nodes()
```
