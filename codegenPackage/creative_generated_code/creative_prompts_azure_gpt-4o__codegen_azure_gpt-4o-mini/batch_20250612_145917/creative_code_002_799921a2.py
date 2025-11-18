"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polyhedra-web.pages.dev
Prompt: Generate a Python script utilizing Polyhedra Network's ZK proof tools to verify data integrity in real-time.
Generated: DETERMINISTIC_799921a25032c0d5
Batch ID: 20250612_145917
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.polyhedra.network": {
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
import hashlib
from typing import Any, Dict, Optional

class PolyhedraZK:
    """
    Class to interact with Polyhedra Network's ZK proof tools for data integrity verification.
    """

    def __init__(self, api_url: str):
        """
        Initialize the PolyhedraZK instance.

        :param api_url: The base URL for Polyhedra Network's API.
        """
        self.api_url = api_url

    def _compute_hash(self, data: Any) -> str:
        """
        Compute the SHA256 hash of the given data.

        :param data: The data to hash, can be any serializable type.
        :return: The hexadecimal representation of the hash.
        """
        json_data = json.dumps(data, sort_keys=True).encode()  # Serialize and encode
        return hashlib.sha256(json_data).hexdigest()  # Compute SHA256 hash

    def generate_proof(self, data: Any) -> Optional[str]:
        """
        Generate a ZK proof for the provided data.

        :param data: The data for which to generate the proof.
        :return: The proof as a string, or None if the request failed.
        """
        try:
            # Compute the data hash
            data_hash = self._compute_hash(data)
            payload = {
                "data_hash": data_hash
            }

            # Send request to the Polyhedra API
            response = requests.post(f"{self.api_url}/generate-proof", json=payload)
            response.raise_for_status()  # Raise an error for bad HTTP responses

            proof = response.json().get('proof')
            return proof
        except requests.RequestException as e:
            print(f"Error generating proof: {e}")
            return None

    def verify_proof(self, proof: str, data: Any) -> bool:
        """
        Verify the ZK proof against the provided data.

        :param proof: The proof to verify.
        :param data: The original data to verify against.
        :return: True if the proof is valid, False otherwise.
        """
        try:
            # Compute the data hash
            data_hash = self._compute_hash(data)
            payload = {
                "proof": proof,
                "data_hash": data_hash
            }

            # Send request to the Polyhedra API
            response = requests.post(f"{self.api_url}/verify-proof", json=payload)
            response.raise_for_status()  # Raise an error for bad HTTP responses

            result = response.json().get('valid')
            return result is True
        except requests.RequestException as e:
            print(f"Error verifying proof: {e}")
            return False


if __name__ == "__main__":
    # Example usage of the PolyhedraZK class
    api_url = "https://api.polyhedra.network"  # Replace with the actual Polyhedra API URL
    zk_tool = PolyhedraZK(api_url)

    # Sample data to verify
    sample_data = {
        "user_id": 123,
        "transaction_amount": 1000,
        "timestamp": "2023-10-01T12:00:00Z"
    }

    # Generate a ZK proof for the sample data
    proof = zk_tool.generate_proof(sample_data)
    if proof:
        print(f"Generated proof: {proof}")

        # Verify the generated proof
        is_valid = zk_tool.verify_proof(proof, sample_data)
        print(f"Is the proof valid? {is_valid}")
    else:
        print("Failed to generate proof.")
```
