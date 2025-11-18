"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://on1force.web.app
Prompt: Write a Python script to decrypt lore elements like the "Voice of M0R1A" using cryptographic techniques, as part of the 0N1 Force storytelling experience.
Generated: DETERMINISTIC_f23298f0aea3861e
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import base64
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def decrypt_voice_of_m0r1a(encrypted_text, key):
    """
    Decrypts the given encrypted text using AES encryption in CBC mode.

    Parameters:
        encrypted_text (str): The encrypted base64-encoded text.
        key (str): The decryption key.

    Returns:
        str: The decrypted text.
    """
    try:
        # Decode the base64 encrypted text
        encrypted_bytes = base64.b64decode(encrypted_text)
        
        # Derive a 256-bit key from the given key using SHA256
        derived_key = hashlib.sha256(key.encode()).digest()
        
        # Extract the initialization vector (IV) from the encrypted data (first 16 bytes)
        iv = encrypted_bytes[:16]
        
        # Extract the actual encrypted data (everything after the first 16 bytes)
        cipher_text = encrypted_bytes[16:]
        
        # Setup AES decryption using derived key and IV
        cipher = Cipher(algorithms.AES(derived_key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        
        # Perform decryption
        decrypted_bytes = decryptor.update(cipher_text) + decryptor.finalize()
        
        # Remove padding (assuming PKCS7 padding)
        padding_length = decrypted_bytes[-1]
        decrypted_bytes = decrypted_bytes[:-padding_length]
        
        # Convert decrypted bytes back to string
        return decrypted_bytes.decode('utf-8')
    except Exception as e:
        # Handle any errors during decryption
        print(f"Error during decryption: {e}")
        return None

if __name__ == "__main__":
    # Example encrypted lore element (replace with actual data)
    encrypted_lore = "U2FsdGVkX1+lnvE7oN1hY4Drh2z2rYwA3V46W5RQcnw="
    
    # Example key (replace with actual key from storytelling experience)
    decryption_key = "my_secret_key_123"
    
    # Decrypt the lore element
    decrypted_lore = decrypt_voice_of_m0r1a(encrypted_lore, decryption_key)
    
    if decrypted_lore:
        print("Decrypted Lore Element:")
        print(decrypted_lore)
    else:
        print("Failed to decrypt the lore element.")
```
