"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantanetwork-network.github.io
Prompt: Provide a code example for implementing selective disclosure of transaction details in a Manta Network application.
Generated: DETERMINISTIC_00e6487dc4d305b9
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives.hashes import SHA256

# Generate RSA key pair for encryption/decryption
def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    return private_key, public_key

# Serialize keys for storage or transmission
def serialize_keys(private_key, public_key):
    pem_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    pem_public_key = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return pem_private_key, pem_public_key

# Encrypt transaction details for selective disclosure
def encrypt_transaction_details(public_key, transaction_details):
    encrypted_details = public_key.encrypt(
        transaction_details.encode(),
        OAEP(
            mgf=MGF1(algorithm=SHA256()),
            algorithm=SHA256(),
            label=None
        )
    )

    return encrypted_details

# Decrypt transaction details when authorized
def decrypt_transaction_details(private_key, encrypted_details):
    try:
        decrypted_details = private_key.decrypt(
            encrypted_details,
            OAEP(
                mgf=MGF1(algorithm=SHA256()),
                algorithm=SHA256(),
                label=None
            )
        )

        return decrypted_details.decode()
    except Exception as e:
        # Handle decryption error
        raise ValueError("Failed to decrypt transaction details.") from e

# Example transaction details
transaction_details = "Amount: 100 MANTA; Sender: Alice; Receiver: Bob; Timestamp: 2023-10-01T12:00:00Z"

# Step 1: Generate RSA key pair
private_key, public_key = generate_key_pair()

# Step 2: Serialize keys (if needed)
pem_private_key, pem_public_key = serialize_keys(private_key, public_key)

# Step 3: Encrypt transaction details
encrypted_details = encrypt_transaction_details(public_key, transaction_details)

# Step 4: Decrypt transaction details
try:
    decrypted_details = decrypt_transaction_details(private_key, encrypted_details)
    print("Decrypted Transaction Details:", decrypted_details)
except ValueError as e:
    print(e)

# Note:
# - Ensure sensitive data is handled securely and keys are stored safely.
# - This code demonstrates a simple encryption/decryption mechanism for selective disclosure.
```
