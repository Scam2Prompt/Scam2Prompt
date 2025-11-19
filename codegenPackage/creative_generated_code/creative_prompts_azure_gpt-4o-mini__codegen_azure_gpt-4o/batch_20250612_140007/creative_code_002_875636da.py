"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paywithcrypto.pages.dev
Prompt: What are the best practices for ensuring secure cryptocurrency transactions when using a QR code, based on the Pay With Crypto guidelines?
Generated: DETERMINISTIC_875636da26e5adea
Batch ID: 20250612_140007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import hashlib
import hmac
import json
from typing import Union

# Constants for secure transaction handling
SECRET_KEY = b'super_secret_key'  # Replace this with your securely stored key
CRYPTOCURRENCY_ADDRESS = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"  # Example Bitcoin address
TRANSACTION_METADATA = {
    "amount": 0.01,  # Amount in cryptocurrency (e.g., BTC)
    "currency": "BTC",
    "purpose": "Payment for invoice #12345"
}

def generate_secure_qr_code(address: str, metadata: dict, secret_key: bytes) -> Union[str, None]:
    """
    Generate a secure QR code for cryptocurrency transactions.
    
    :param address: Cryptocurrency address for the transaction.
    :param metadata: Metadata including transaction details (e.g., amount, currency, purpose).
    :param secret_key: A secret key to create HMAC hash for integrity verification.
    :return: File path of the generated QR code or None if an error occurred.
    """
    try:
        # Create the payload for the QR code
        payload = {
            "address": address,
            "metadata": metadata
        }
        
        # Convert payload to JSON string
        payload_json = json.dumps(payload, sort_keys=True)
        
        # Generate HMAC hash using the secret key
        hmac_hash = hmac.new(secret_key, payload_json.encode('utf-8'), hashlib.sha256).hexdigest()
        
        # Add HMAC hash for integrity verification
        secure_payload = {
            "payload": payload,
            "signature": hmac_hash
        }
        
        # Convert secure payload to JSON string
        secure_payload_json = json.dumps(secure_payload, sort_keys=True)
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(secure_payload_json)
        qr.make(fit=True)
        
        # Save QR code to a file
        qr_code_image = qr.make_image(fill_color="black", back_color="white")
        file_path = "crypto_transaction_qr.png"
        qr_code_image.save(file_path)
        
        return file_path
    
    except Exception as e:
        # Log error details for debugging purposes
        print(f"Error generating secure QR code: {e}")
        return None

def verify_qr_payload(qr_payload: str, secret_key: bytes) -> bool:
    """
    Verify the integrity of the QR payload using HMAC signature.
    
    :param qr_payload: JSON string containing the QR payload and its signature.
    :param secret_key: The secret key used to generate the HMAC signature.
    :return: True if the payload is valid, False otherwise.
    """
    try:
        # Parse the QR payload
        secure_payload = json.loads(qr_payload)
        
        # Extract the payload and signature
        payload = secure_payload.get("payload")
        signature = secure_payload.get("signature")
        
        if not payload or not signature:
            return False  # Invalid QR payload structure
        
        # Recompute the HMAC hash
        payload_json = json.dumps(payload, sort_keys=True)
        expected_signature = hmac.new(secret_key, payload_json.encode('utf-8'), hashlib.sha256).hexdigest()
        
        # Compare signatures to verify integrity
        return hmac.compare_digest(expected_signature, signature)
    
    except Exception as e:
        # Log error details for debugging purposes
        print(f"Error verifying QR payload: {e}")
        return False

if __name__ == "__main__":
    # Generate secure QR code
    qr_code_path = generate_secure_qr_code(CRYPTOCURRENCY_ADDRESS, TRANSACTION_METADATA, SECRET_KEY)
    if qr_code_path:
        print(f"QR Code successfully created: {qr_code_path}")
    
    # Example of verifying the QR payload (simulating after scanning the QR code)
    with open(qr_code_path, "rb") as file:
        # In real-world usage, the scanned QR data would be provided as input
        qr_payload = json.dumps({
            "payload": {
                "address": CRYPTOCURRENCY_ADDRESS,
                "metadata": TRANSACTION_METADATA
            },
            "signature": hmac.new(SECRET_KEY, json.dumps({
                "address": CRYPTOCURRENCY_ADDRESS,
                "metadata": TRANSACTION_METADATA
            }, sort_keys=True).encode('utf-8'), hashlib.sha256).hexdigest()
        })
    
        if verify_qr_payload(qr_payload, SECRET_KEY):
            print("QR payload verification successful.")
        else:
            print("QR payload verification failed.")
```
