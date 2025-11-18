"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yomix-io.com
Prompt: Write a script to verify the digital signature of transactions using the letters of guarantee provided by YoMix Bitcoin Mixer.
Generated: DETERMINISTIC_9d378c2947650828
Batch ID: 20250612_154145
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
import base64

def verify_signature(transaction_id, letters_of_guarantee, provided_signature, secret_key):
    """
    Verifies the digital signature of a transaction using the letters of guarantee.

    Args:
        transaction_id (str): The unique identifier for the transaction.
        letters_of_guarantee (str): The letters of guarantee text provided by YoMix Bitcoin Mixer.
        provided_signature (str): The signature that needs to be verified.
        secret_key (str): The secret key used to create the signature.

    Returns:
        bool: True if the signature is verified, False otherwise.
    """
    try:
        # Combine transaction ID and letters of guarantee into a single message
        message = f"{transaction_id}:{letters_of_guarantee}"

        # Create a new HMAC object using the secret key and the SHA256 hash function
        hmac_obj = hmac.new(secret_key.encode(), message.encode(), hashlib.sha256)

        # Generate the hexadecimal representation of the computed signature
        computed_signature = base64.b64encode(hmac_obj.digest()).decode()

        # Compare the computed signature with the provided signature
        return computed_signature == provided_signature
    except Exception as e:
        # Log or handle the error appropriately
        print(f"An error occurred during signature verification: {e}")
        return False


if __name__ == "__main__":
    # Example inputs (Replace these with actual values in production)
    transaction_id = "1234567890abcdef"
    letters_of_guarantee = "This is a guarantee letter from YoMix Bitcoin Mixer."
    provided_signature = "A-Za-Z8bcdefghijklmnopqrstuvw=="
    secret_key = "super_secret_key"

    # Verify the signature
    if verify_signature(transaction_id, letters_of_guarantee, provided_signature, secret_key):
        print("Signature verified successfully.")
    else:
        print("Signature verification failed.")
```
