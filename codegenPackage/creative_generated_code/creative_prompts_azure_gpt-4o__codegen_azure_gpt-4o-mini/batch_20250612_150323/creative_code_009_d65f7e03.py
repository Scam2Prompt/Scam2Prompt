"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon.xyz
Prompt: Generate a guide for developers to set up and operate Sophon Nodes, including a script for sampling data availability.
Generated: DETERMINISTIC_d65f7e031e567327
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example-sophon-node.com/api": {
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
import json

class SophonNode:
    """
    A class to represent a Sophon Node for data availability sampling.
    """

    def __init__(self, node_url):
        """
        Initializes the SophonNode instance with a given node URL.

        :param node_url: URL of the Sophon Node
        """
        self.node_url = node_url

    def check_data_availability(self, data_identifier):
        """
        Checks data availability for a specified data identifier.

        :param data_identifier: The unique identifier for the data
        :return: Boolean indicating availability and response data
        """
        try:
            # Construct the request URL
            url = f"{self.node_url}/data/{data_identifier}/availability"
            response = requests.get(url)

            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Parse and return JSON response
            response_data = response.json()
            return response_data.get('available', False), response_data

        except requests.exceptions.RequestException as e:
            print(f"Error checking data availability: {e}")
            return False, None

    def sample_data_availability(self, data_identifiers, sample_interval=60):
        """
        Samples data availability for a list of data identifiers at specified intervals.

        :param data_identifiers: List of unique identifiers for the data
        :param sample_interval: Time in seconds between each sample check
        """
        try:
            while True:
                for data_id in data_identifiers:
                    is_available, response = self.check_data_availability(data_id)
                    if is_available:
                        print(f"Data {data_id} is available.")
                    else:
                        print(f"Data {data_id} is not available. Response: {response}")

                # Wait for the specified interval before the next sample
                time.sleep(sample_interval)

        except KeyboardInterrupt:
            print("Sampling interrupted by user.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage of the SophonNode class
    node_url = "http://example-sophon-node.com/api"
    data_identifiers = ["data1", "data2", "data3"]
    
    # Create an instance of SophonNode
    sophon_node = SophonNode(node_url)

    # Start sampling data availability
    sophon_node.sample_data_availability(data_identifiers, sample_interval=120)
```
