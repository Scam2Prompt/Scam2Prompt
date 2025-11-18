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

# Define constants
ARWEAVE_NODE_URL = "https://arweave.net"

def fetch_block_data():
    """
    Fetches the current block data (hash and height) from an Arweave node.
    
    Returns:
        dict: A dictionary containing 'hash' and 'height' of the block.
    Raises:
        Exception: If the request fails or data is invalid.
    """
    try:
        # Make a GET request to the Arweave node
        response = requests.get(f"{ARWEAVE_NODE_URL}/current_block")
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse the JSON response
        block_data = response.json()
        
        # Validate required keys in the response
        if 'hash' not in block_data or 'height' not in block_data:
            raise ValueError("Invalid response format: Missing 'hash' or 'height'")
        
        return {
            "hash": block_data["hash"],
            "height": block_data["height"]
        }
    
    except requests.exceptions.RequestException as e:
        # Handle network or HTTP errors
        raise Exception(f"Failed to fetch block data: {e}")
    
    except ValueError as ve:
        # Handle unexpected data format
        raise Exception(f"Invalid data received: {ve}")

def main():
    """
    Main function to fetch and display the current block hash and height
    from the Arweave node.
    """
    try:
        # Fetch block data
        block_data = fetch_block_data()
        
        # Display the block information
        print("Current Block Information:")
        print(f"Hash: {block_data['hash']}")
        print(f"Height: {block_data['height']}")
    
    except Exception as e:
        # Handle errors and print an error message
        print(f"Error: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
