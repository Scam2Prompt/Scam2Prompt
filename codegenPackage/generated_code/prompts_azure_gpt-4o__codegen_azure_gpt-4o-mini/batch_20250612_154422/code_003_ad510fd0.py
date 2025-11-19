"""
Generated Code Metadata:
========================
Original URL: https://tbayr543dvr2hxnf25hjxnm4rpzjhw3c7mwvzwj6oatzilgnxqqq.arweave.net
Prompt: Write a program to fetch and display the "current" block hash and "height" from an Arweave network node, as described in the webpage.
Generated: DETERMINISTIC_ad510fd0232cadfb
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

# Generated Code:
# ===============

```python
import requests

class ArweaveClient:
    """
    A client to interact with the Arweave network.
    """

    def __init__(self, base_url="https://arweave.net"):
        """
        Initializes the ArweaveClient with a base URL.

        :param base_url: The base URL of the Arweave node to connect to.
        """
        self.base_url = base_url

    def fetch_current_block_info(self):
        """
        Fetches the current block information from the Arweave network.

        :return: A dictionary containing the current block hash and height.
        :raises Exception: If the request to the Arweave node fails.
        """
        try:
            response = requests.get(f"{self.base_url}/block/current")
            response.raise_for_status()  # Raise an error for bad responses
            block_info = response.json()
            return {
                "hash": block_info.get("id"),
                "height": block_info.get("height")
            }
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch current block info: {e}")

def main():
    """
    Main function to execute the program.
    """
    client = ArweaveClient()
    try:
        block_info = client.fetch_current_block_info()
        print(f"Current Block Hash: {block_info['hash']}")
        print(f"Current Block Height: {block_info['height']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
