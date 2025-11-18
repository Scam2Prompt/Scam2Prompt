"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tbayr543dvr2hxnf25hjxnm4rpzjhw3c7mwvzwj6oatzilgnxqqq.arweave.net
Prompt: Provide code to parse and display the "blocks" value from an Arweave node API response, ensuring compatibility with the JSON structure provided.
Generated: DETERMINISTIC_4f8c8c0d01c08d06
Batch ID: 20250612_154422
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://arweave.net": {
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

class ArweaveAPI:
    """
    A class to interact with the Arweave node API.
    """

    BASE_URL = "https://arweave.net"

    def __init__(self):
        """
        Initializes the ArweaveAPI instance.
        """
        pass

    def get_blocks_data(self):
        """
        Fetches the blocks data from the Arweave API.

        Returns:
            dict: A dictionary containing the blocks information if successful, None otherwise.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/blocks")
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()  # Parse and return JSON data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching blocks data: {e}")
            return None

    def display_blocks(self):
        """
        Fetches and displays the blocks value from the Arweave API response.
        """
        blocks_data = self.get_blocks_data()
        if blocks_data is not None and "blocks" in blocks_data:
            blocks = blocks_data["blocks"]
            print("Blocks Information:")
            for block in blocks:
                print(f"Block ID: {block.get('id', 'N/A')}, Timestamp: {block.get('timestamp', 'N/A')}")
        else:
            print("No blocks data available.")

if __name__ == "__main__":
    arweave_api = ArweaveAPI()
    arweave_api.display_blocks()
```
