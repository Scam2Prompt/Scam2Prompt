"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arweave.ar
Prompt: Provide an example of how to use the Arweave API to interact with supported manifest versions and retrieve metadata.
Generated: DETERMINISTIC_95834d31ef0c10ff
Batch ID: 20250612_154603
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

# Constants
ARWEAVE_GATEWAY = "https://arweave.net"
MANIFEST_ENDPOINT = "/tx/{transaction_id}/index.json"

def get_manifest_metadata(transaction_id):
    """
    Fetches the metadata of a manifest from Arweave.
    
    Args:
        transaction_id (str): The ID of the transaction containing the manifest.
    
    Returns:
        dict: Metadata of the manifest if available, or None.
    """
    try:
        # Construct the URL for the manifest
        manifest_url = f"{ARWEAVE_GATEWAY}{MANIFEST_ENDPOINT.format(transaction_id=transaction_id)}"
        
        # Make a GET request to fetch the manifest metadata
        response = requests.get(manifest_url)
        
        # Check if the response status code indicates success
        if response.status_code == 200:
            # Parse metadata as JSON and return
            return response.json()
        else:
            # Handle errors gracefully
            print(f"Failed to fetch manifest metadata. HTTP Status Code: {response.status_code}")
            return None
    except requests.RequestException as e:
        # Handle request-related errors
        print(f"An error occurred while trying to fetch manifest metadata: {e}")
        return None

# Example Usage
if __name__ == "__main__":
    # Replace 'transaction_id' with a valid Arweave transaction ID for testing
    transaction_id = "your_transaction_id_here"
    
    # Fetch the manifest metadata
    metadata = get_manifest_metadata(transaction_id)
    
    if metadata:
        # Output the fetched metadata
        print("Manifest Metadata:")
        print(metadata)
    else:
        print("No metadata found or an error occurred.")
```
