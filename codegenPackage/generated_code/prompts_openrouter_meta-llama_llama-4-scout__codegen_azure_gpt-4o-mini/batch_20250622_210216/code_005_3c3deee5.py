"""
Generated Code Metadata:
========================
Original URL: https://dop-en.web.app
Prompt: Design a system for customized data disclosure permissions tailored to each app and context, using the Data Ownership Protocol (DOP) and zero-knowledge proofs.
Generated: DETERMINISTIC_3c3deee5f6c206c0
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import hashlib
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature

class DataOwner:
    def __init__(self):
        # Generate a new RSA key pair for the data owner
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()

    def serialize_public_key(self):
        # Serialize the public key to a PEM format
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def sign_data(self, data):
        # Sign the data using the private key
        return self.private_key.sign(
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

class DataConsumer:
    def __init__(self, public_key_pem):
        # Load the public key from PEM format
        self.public_key = serialization.load_pem_public_key(public_key_pem)

    def verify_signature(self, data, signature):
        # Verify the signature using the public key
        try:
            self.public_key.verify(
                signature,
                data,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False

class DataDisclosureSystem:
    def __init__(self):
        self.permissions = {}

    def set_permission(self, app_id, context, permission):
        # Set permissions for a specific app and context
        self.permissions[(app_id, context)] = permission

    def get_permission(self, app_id, context):
        # Get permissions for a specific app and context
        return self.permissions.get((app_id, context), None)

    def disclose_data(self, app_id, context, data_owner, data):
        # Disclose data if permission is granted
        permission = self.get_permission(app_id, context)
        if permission:
            signature = data_owner.sign_data(data)
            return {
                "data": data,
                "signature": signature.hex()
            }
        else:
            raise PermissionError("Permission denied for this app and context.")

# Example usage
if __name__ == "__main__":
    # Create a data owner
    owner = DataOwner()
    public_key_pem = owner.serialize_public_key()

    # Create a data consumer with the owner's public key
    consumer = DataConsumer(public_key_pem)

    # Set permissions for an app and context
    disclosure_system = DataDisclosureSystem()
    disclosure_system.set_permission("app_123", "context_abc", True)

    # Data to be disclosed
    data = json.dumps({"sensitive_info": "This is confidential."}).encode()

    try:
        # Attempt to disclose data
        result = disclosure_system.disclose_data("app_123", "context_abc", owner, data)
        print("Data disclosed successfully:", result)

        # Verify the signature
        is_valid = consumer.verify_signature(data, bytes.fromhex(result["signature"]))
        print("Signature valid:", is_valid)

    except PermissionError as e:
        print(e)
    except Exception as e:
        print("An error occurred:", str(e))
```
