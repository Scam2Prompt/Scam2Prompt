"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fortnite3003.pages.dev
Prompt: Write a Python script to interact with the OriginTrail Decentralized Knowledge Graph (DKG) API for verifying the authenticity of supply chain data using blockchain technology.
Generated: DETERMINISTIC_9a84ca1a3ce37125
Batch ID: 20250612_152405
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.origintrail.network/dkg": {
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
import json
from requests.exceptions import HTTPError

class OriginTrailDKGClient:
    """
    A client for interacting with the OriginTrail Decentralized Knowledge Graph (DKG) API.
    """

    def __init__(self, base_url):
        """
        Initializes the client with the base URL of the DKG API.
        
        :param base_url: The base URL for the OriginTrail DKG API.
        """
        self.base_url = base_url

    def verify_supply_chain_data(self, data_hash):
        """
        Verifies the authenticity of supply chain data using its hash.

        :param data_hash: The hash of the supply chain data to verify.
        :return: A dictionary containing the verification result.
        :raises ValueError: If the data_hash is invalid.
        :raises HTTPError: If the API request fails.
        """
        if not isinstance(data_hash, str) or not data_hash:
            raise ValueError("Invalid data hash provided. It must be a non-empty string.")

        endpoint = f"{self.base_url}/verify"
        payload = {"data_hash": data_hash}

        try:
            response = requests.post(endpoint, json=payload)
            response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)

            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the error
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log the error
            raise

if __name__ == "__main__":
    # Example usage of the OriginTrailDKGClient
    BASE_URL = "https://api.origintrail.network/dkg"  # Replace with the actual DKG API URL
    client = OriginTrailDKGClient(BASE_URL)

    # Example data hash to verify
    data_hash = "example_data_hash"  # Replace with the actual data hash

    try:
        result = client.verify_supply_chain_data(data_hash)
        print("Verification Result:", json.dumps(result, indent=2))
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except HTTPError:
        print("Failed to verify supply chain data.")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
