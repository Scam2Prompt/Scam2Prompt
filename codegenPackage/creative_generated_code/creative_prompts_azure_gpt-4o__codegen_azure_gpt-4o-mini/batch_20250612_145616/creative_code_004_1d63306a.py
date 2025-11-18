"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.gmx-oracle.io
Prompt: Write a Python function to verify the integrity of GMX oracle price feeds using cryptographic signatures.
Generated: DETERMINISTIC_1d63306aa731498e
Batch ID: 20250612_145616
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.gmx.io/oracle/price_feed": {
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
import hashlib
import json
import requests
from ecdsa import VerifyingKey, BadSignature

class OraclePriceFeedIntegrityVerifier:
    """
    A class to verify the integrity of GMX oracle price feeds using cryptographic signatures.
    """

    def __init__(self, oracle_url: str):
        """
        Initializes the verifier with the oracle URL.

        :param oracle_url: The URL of the GMX oracle price feed.
        """
        self.oracle_url = oracle_url

    def fetch_price_feed(self) -> dict:
        """
        Fetches the price feed from the GMX oracle.

        :return: Parsed JSON response from the oracle.
        :raises Exception: If the request fails or returns an error.
        """
        try:
            response = requests.get(self.oracle_url)
            response.raise_for_status()  # Raises an error for bad responses
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch price feed: {e}")

    def verify_signature(self, price_feed: dict) -> bool:
        """
        Verifies the cryptographic signature of the price feed.

        :param price_feed: The price feed data containing 'data' and 'signature'.
        :return: True if the signature is valid, False otherwise.
        """
        data = price_feed['data']
        signature = bytes.fromhex(price_feed['signature'])
        public_key_hex = price_feed['public_key']  # Assume public_key is provided in the price_feed

        # Hash the price feed data
        data_hash = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).digest()

        # Create a verifying key object from the public key
        try:
            public_key = VerifyingKey.from_string(bytes.fromhex(public_key_hex), curve=ecdsa.SECP256k1)

            # Verify the signature
            return public_key.verify(signature, data_hash)
        except (BadSignature, ValueError) as e:
            print(f"Signature verification failed: {e}")
            return False

    def verify_integrity(self) -> bool:
        """
        Main method to verify the integrity of the price feed.

        :return: True if the integrity checks out, False otherwise.
        """
        try:
            price_feed = self.fetch_price_feed()
            return self.verify_signature(price_feed)
        except Exception as e:
            print(f"Error during verification: {e}")
            return False

# Example usage
if __name__ == "__main__":
    oracle_url = "https://api.gmx.io/oracle/price_feed"  # Replace with the actual price feed URL
    verifier = OraclePriceFeedIntegrityVerifier(oracle_url)
    
    if verifier.verify_integrity():
        print("Price feed integrity verified successfully.")
    else:
        print("Price feed integrity verification failed.")
```
