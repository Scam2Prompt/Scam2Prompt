"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
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

# Creative Generated Code:
# ========================

```python
import requests

def fetch_arweave_block_info(node_url):
    """
    Fetches the current block hash and height from an Arweave network node.

    Args:
        node_url (str): The URL of the Arweave node to query.

    Returns:
        dict: A dictionary containing the block 'hash' and 'height' if successful.

    Raises:
        ValueError: If the response does not contain the expected data.
        requests.RequestException: If there is an issue with the HTTP request.
    """
    try:
        # Sending a GET request to the node URL
        response = requests.get(f"{node_url}/blocks/current")
        
        # Raise an exception for HTTP error responses
        response.raise_for_status()

        # Parsing the JSON response
        block_info = response.json()

        # Validating the response structure
        if 'id' not in block_info or 'height' not in block_info:
            raise ValueError("Response does not contain the expected block information.")

        # Returning the relevant block information
        return {
            "hash": block_info['id'],
            "height": block_info['height']
        }

    except ValueError as ve:
        print(f"ValueError: {ve}")
        return None
    except requests.RequestException as re:
        print(f"RequestException: {re}")
        return None

def main():
    # URL of the Arweave node
    arweave_node_url = "https://arweave.net"

    # Fetching block information
    block_info = fetch_arweave_block_info(arweave_node_url)

    # Displaying the block information if fetched successfully
    if block_info:
        print(f"Current Block Hash: {block_info['hash']}")
        print(f"Current Block Height: {block_info['height']}")

if __name__ == "__main__":
    main()
```
