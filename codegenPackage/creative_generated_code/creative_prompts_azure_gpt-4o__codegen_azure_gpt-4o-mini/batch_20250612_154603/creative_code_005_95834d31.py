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

class ArweaveAPI:
    """
    A class to interact with the Arweave API for retrieving metadata
    of supported manifest versions.
    """

    BASE_URL = "https://arweave.net"

    def __init__(self):
        """
        Initializes the ArweaveAPI instance.
        """
        pass

    def get_manifest_metadata(self, transaction_id):
        """
        Retrieves metadata from the manifest associated with a given transaction ID.

        Args:
            transaction_id (str): The Arweave transaction ID of the manifest to query.

        Returns:
            dict: A dictionary containing the manifest metadata.

        Raises:
            ValueError: If the transaction ID is invalid or not provided.
            requests.HTTPError: If the request to the Arweave API fails.
        """
        if not transaction_id or not isinstance(transaction_id, str):
            raise ValueError("Invalid transaction ID provided.")

        url = f"{self.BASE_URL}/tx/{transaction_id}/data"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
        except requests.HTTPError as http_err:
            raise requests.HTTPError(f"HTTP error occurred: {http_err}") from http_err
        except Exception as err:
            raise Exception(f"An error occurred: {err}") from err
        
        return response.json()

# Example usage
if __name__ == "__main__":
    arweave_api = ArweaveAPI()
    transaction_id = "YOUR_TRANSACTION_ID_HERE"  # Replace with a valid transaction ID

    try:
        manifest_metadata = arweave_api.get_manifest_metadata(transaction_id)
        print("Manifest Metadata:", manifest_metadata)
    except Exception as e:
        print(f"Error retrieving manifest metadata: {e}")
```
