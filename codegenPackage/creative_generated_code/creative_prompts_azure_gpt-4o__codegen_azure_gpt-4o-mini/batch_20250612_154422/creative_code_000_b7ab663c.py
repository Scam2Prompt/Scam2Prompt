"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tbayr543dvr2hxnf25hjxnm4rpzjhw3c7mwvzwj6oatzilgnxqqq.arweave.net
Prompt: Write a script to query the "arweave.N.1" network for the current block height and block details using the data structure provided in the webpage content.
Generated: DETERMINISTIC_b7ab663c0afcefd5
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

class ArweaveClient:
    """
    A client to interact with the Arweave network to fetch block details.
    """

    BASE_URL = "https://arweave.net"

    def __init__(self):
        pass

    def get_block_height(self):
        """
        Queries the Arweave network for the current block height.

        Returns:
            int: The current block height.
        Raises:
            Exception: If the request to the Arweave network fails.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/block/height")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('height')
        except requests.RequestException as e:
            raise Exception(f"Error fetching block height: {e}")

    def get_block_details(self, block_height):
        """
        Fetches the details of a specific block given its height.

        Args:
            block_height (int): The height of the block to retrieve details for.

        Returns:
            dict: The details of the specified block.
        Raises:
            Exception: If the request for block details fails.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/block/{block_height}")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the block details as a dictionary
        except requests.RequestException as e:
            raise Exception(f"Error fetching block details for height {block_height}: {e}")

def main():
    """
    Main function to execute the block height query and block details retrieval.
    """
    client = ArweaveClient()

    try:
        # Get the current block height
        block_height = client.get_block_height()
        print(f"Current Block Height: {block_height}")

        # Get the details for the current block
        block_details = client.get_block_details(block_height)
        print("Block Details:", block_details)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
