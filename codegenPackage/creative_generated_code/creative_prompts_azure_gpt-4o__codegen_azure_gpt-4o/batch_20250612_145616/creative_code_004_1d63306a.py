"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.gmx-oracle.io
Prompt: Write a Python function to verify the integrity of GMX oracle price feeds using cryptographic signatures.
Generated: DETERMINISTIC_1d63306aa731498e
Batch ID: 20250612_145616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import hmac
from typing import Dict


def verify_gmx_price_feed(
    price_data: Dict[str, str],
    public_key: bytes,
    signature: str,
) -> bool:
    """
    Verifies the integrity of GMX oracle price feeds using cryptographic signatures.

    Parameters:
        price_data (dict): The price feed data received from the oracle. Expected keys include:
            - "timestamp" (str): The timestamp of the price feed.
            - "price" (str): The price value from the oracle.
            - "asset" (str): The asset name or identifier.
        public_key (bytes): The shared secret/public key used to verify the signature.
        signature (str): The cryptographic signature of the price feed.

    Returns:
        bool: True if the signature is valid and the data is verified, False otherwise.
    """
    try:
        # Validate inputs
        if not isinstance(price_data, dict):
            raise ValueError("price_data must be a dictionary.")
        if not all(key in price_data for key in ["timestamp", "price", "asset"]):
            raise ValueError("price_data must include 'timestamp', 'price', and 'asset'.")
        if not isinstance(signature, str):
            raise ValueError("signature must be a string.")
        if not isinstance(public_key, bytes):
            raise ValueError("public_key must be bytes.")

        # Sort the price_data dictionary to ensure consistent ordering
        sorted_data = ''.join(f"{key}:{price_data[key]}" for key in sorted(price_data.keys()))
        
        # Hash the sorted data using HMAC with the provided public key
        computed_hmac = hmac.new(public_key, sorted_data.encode('utf-8'), hashlib.sha256).hexdigest()

        # Compare the computed HMAC with the provided signature
        return hmac.compare_digest(computed_hmac, signature)

    except Exception as e:
        # Log the error (in production, replace print with actual logging)
        print(f"Error verifying price feed: {e}")
        return False


# Example Usage:
if __name__ == "__main__":
    # Sample price feed data
    sample_data = {
        "timestamp": "2023-10-01T12:30:00Z",
        "price": "12345.67",
        "asset": "BTC"
    }

    # Sample public key and signature
    sample_public_key = b'secret_key_for_testing'  # Replace with actual public key
    sample_signature = "d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2"

    # Verify the price feed
    is_valid = verify_gmx_price_feed(sample_data, sample_public_key, sample_signature)
    print("Price feed valid:", is_valid)
```
