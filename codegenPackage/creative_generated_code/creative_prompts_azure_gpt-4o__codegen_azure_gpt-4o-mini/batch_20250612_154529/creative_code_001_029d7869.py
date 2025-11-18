"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://p3gnmpkzz7bdg3pxf7p4hgpwb4d7u77rhdcllh4h54gp7m5pl2qa.arweave.net
Prompt: Create a function that parses the JSON response from an Arweave node and extracts the `current` block hash and `height` values.
Generated: DETERMINISTIC_029d7869c7643992
Batch ID: 20250612_154529
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
import json
import requests

def get_arweave_block_info(node_url):
    """
    Fetches the current block information from an Arweave node and extracts the
    current block hash and height.

    Args:
        node_url (str): The URL of the Arweave node to query.

    Returns:
        dict: A dictionary containing the 'current' block hash and 'height'.

    Raises:
        ValueError: If the response data does not contain the expected fields.
        requests.exceptions.RequestException: If the request to the node fails.
    """
    try:
        # Send a GET request to the Arweave node
        response = requests.get(f"{node_url}/info")
        response.raise_for_status()  # Raise an error for HTTP error responses

        # Parse the JSON response
        data = response.json()

        # Extract the 'current' block hash and 'height'
        current_block_hash = data.get('current', {}).get('block', {}).get('hash')
        height = data.get('current', {}).get('block', {}).get('height')

        # Validate extracted values
        if current_block_hash is None or height is None:
            raise ValueError("Missing 'current' block hash or height in the response.")

        return {
            'current_block_hash': current_block_hash,
            'height': height
        }

    except requests.exceptions.RequestException as e:
        # Handle request exceptions (e.g., connection errors, timeouts)
        print(f"Error fetching data from Arweave node: {e}")
        raise
    except ValueError as ve:
        # Handle value errors related to missing data
        print(f"Value error: {ve}")
        raise
    except json.JSONDecodeError as e:
        # Handle JSON decode errors
        print("Error decoding JSON response.")
        raise

# Example usage:
# node_url = "https://arweave.net"
# block_info = get_arweave_block_info(node_url)
# print(block_info)
```
