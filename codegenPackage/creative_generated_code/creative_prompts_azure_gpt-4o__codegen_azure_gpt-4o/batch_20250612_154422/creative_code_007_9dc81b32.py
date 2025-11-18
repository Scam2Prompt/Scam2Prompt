"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tbayr543dvr2hxnf25hjxnm4rpzjhw3c7mwvzwj6oatzilgnxqqq.arweave.net
Prompt: Write a script to verify the "current" block hash against a known value in the Arweave network, using the JSON structure described on the webpage.
Generated: DETERMINISTIC_9dc81b321d4f8e00
Batch ID: 20250612_154422
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://arweave.net/current": {
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

def verify_block_hash(known_hash):
    """
    Verifies the current block hash in the Arweave network against a known hash.

    Parameters:
    known_hash (str): The known hash value to compare against.

    Returns:
    bool: True if the hash matches, False otherwise.
    """

    # Arweave gateway URL for fetching the current block data
    arweave_url = "https://arweave.net/current"

    try:
        # Fetch the current block's data from the Arweave gateway
        response = requests.get(arweave_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response to extract the 'current' block hash
        current_block_data = response.json()
        current_hash = current_block_data.get("current")

        # Ensure the hash exists in the response
        if not current_hash:
            raise ValueError("The response does not contain a 'current' block hash.")

        # Compare the current block hash to the known hash
        if current_hash == known_hash:
            print("Hash match verified.")
            return True
        else:
            print("Hash mismatch.")
            return False

    except requests.RequestException as e:
        # Handle network-related errors
        print(f"Network error occurred: {e}")
        return False
    except ValueError as e:
        # Handle response parsing errors or missing hash
        print(f"Data error occurred: {e}")
        return False

# Example usage:
# Replace 'your_known_hash_here' with the actual known hash to verify
known_hash = "your_known_hash_here"
verify_block_hash(known_hash)
```
