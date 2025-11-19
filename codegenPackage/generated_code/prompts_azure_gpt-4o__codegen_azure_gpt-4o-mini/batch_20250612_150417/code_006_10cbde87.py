"""
Generated Code Metadata:
========================
Original URL: https://lvhoa.com
Prompt: Provide recommendations for implementing a node-based seismic data collection system similar to the "海脉" equipment mentioned on the site. Include code examples for data collection and processing.
Generated: DETERMINISTIC_10cbde879a52ee06
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import time
import logging
from datetime import datetime
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SeismicNode:
    """
    A class to represent a seismic data collection node.
    """

    def __init__(self, node_id: str, data_directory: str):
        """
        Initialize the seismic node with an ID and a directory for storing data.

        :param node_id: Unique identifier for the seismic node
        :param data_directory: Directory path to store collected data
        """
        self.node_id = node_id
        self.data_directory = data_directory
        self.data_file = os.path.join(data_directory, f"{node_id}_data.json")
        self.data_buffer: List[Dict[str, Any]] = []

        # Ensure the data directory exists
        os.makedirs(data_directory, exist_ok=True)

    def collect_data(self) -> Dict[str, Any]:
        """
        Simulate data collection from the seismic sensor.

        :return: A dictionary containing timestamp and simulated seismic data
        """
        # Simulate seismic data collection
        seismic_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "magnitude": round(random.uniform(0, 10), 2),  # Simulated magnitude
            "location": {
                "latitude": round(random.uniform(-90, 90), 6),
                "longitude": round(random.uniform(-180, 180), 6)
            }
        }
        return seismic_data

    def buffer_data(self, data: Dict[str, Any]):
        """
        Buffer the collected data for later processing.

        :param data: The seismic data to buffer
        """
        self.data_buffer.append(data)
        logging.info(f"Buffered data: {data}")

    def save_data(self):
        """
        Save the buffered data to a JSON file.
        """
        try:
            with open(self.data_file, 'a') as f:
                for entry in self.data_buffer:
                    f.write(json.dumps(entry) + "\n")
            logging.info(f"Data saved to {self.data_file}")
            self.data_buffer.clear()  # Clear the buffer after saving
        except IOError as e:
            logging.error(f"Error saving data to file: {e}")

    def run(self, collection_interval: int):
        """
        Run the data collection process at specified intervals.

        :param collection_interval: Time in seconds between data collections
        """
        logging.info(f"Starting data collection for node {self.node_id}")
        try:
            while True:
                data = self.collect_data()
                self.buffer_data(data)
                self.save_data()
                time.sleep(collection_interval)
        except KeyboardInterrupt:
            logging.info("Data collection stopped by user.")
        except Exception as e:
            logging.error(f"An error occurred during data collection: {e}")

if __name__ == "__main__":
    # Example usage
    seismic_node = SeismicNode(node_id="Node_1", data_directory="./seismic_data")
    seismic_node.run(collection_interval=5)  # Collect data every 5 seconds
```
