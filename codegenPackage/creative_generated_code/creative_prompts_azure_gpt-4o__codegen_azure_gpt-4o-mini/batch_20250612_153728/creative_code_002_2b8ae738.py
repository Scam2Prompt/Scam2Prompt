"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www3.celestia.net
Prompt: Generate a Python script to query Celestia's blockchain for data availability proofs using its API or SDK.
Generated: DETERMINISTIC_2b8ae738141172e2
Batch ID: 20250612_153728
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.celestia.network": {
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

class CelestiaAPI:
    """
    A class to interact with the Celestia blockchain API for querying data availability proofs.
    """

    BASE_URL = "https://api.celestia.network"  # Base URL for Celestia API

    def __init__(self):
        pass

    def get_data_availability_proof(self, block_hash: str) -> dict:
        """
        Query the Celestia blockchain for data availability proofs.

        :param block_hash: The hash of the block for which to obtain the data availability proof.
        :return: A dictionary containing the data availability proof.
        :raises ValueError: If the block_hash is invalid.
        :raises Exception: If there is an issue with the API request.
        """
        if not isinstance(block_hash, str) or len(block_hash) != 64:  # Basic validation for a block hash
            raise ValueError("Invalid block hash. It must be a 64-character string.")

        endpoint = f"{self.BASE_URL}/data-availability-proof/{block_hash}"
        try:
            response = requests.get(endpoint)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            return response.json()  # Return the JSON response as a dictionary

        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {e}")  # Handle any request exceptions

def main():
    """
    Main function to execute the script.
    """
    celestia_api = CelestiaAPI()

    # Example block hash (replace with a valid hash for your use case)
    block_hash = "2e8c5e8f4d6e8f7b0e3d8e0b0e8f2e8c5d8e8e0b0e8f2e8c5e8c5e8f4d6e7e8f" 

    try:
        proof = celestia_api.get_data_availability_proof(block_hash)
        print("Data Availability Proof:", json.dumps(proof, indent=4))  # Pretty print the JSON response

    except ValueError as ve:
        print(f"Value Error: {ve}")  # Handle value errors
    except Exception as e:
        print(f"An error occurred: {e}")  # Handle general errors

if __name__ == "__main__":
    main()  # Execute the main function
```
