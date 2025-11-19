"""
Generated Code Metadata:
========================
Original URL: https://bip32.net
Prompt: Explain the purpose of the Child Key Derivation Function (CKD) in BIP32 and provide an example implementation.
Generated: DETERMINISTIC_926bd1764c6abb01
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import hmac

def hkdf(ikm, salt, info, length):
    """
    HMAC-based Key Derivation Function (HKDF) implementation.

    :param ikm: Input Key Material
    :param salt: Salt value
    :param info: Context and application specific information
    :param length: Length of the output key material
    :return: Derived key material
    """
    # Initialize the HMAC object
    prk = hmac.new(ikm, salt, hashlib.sha512).digest()
    
    # Initialize the output key material
    okm = b""
    prev = b""
    
    while len(okm) < length:
        prev = hmac.new(prk, prev + info + b'\x00' + bytes([1 + len(okm) // 32]), hashlib.sha512).digest()
        okm += prev
    
    return okm[:length]

def child_key_derivation(parent_private_key, child_number):
    """
    Child Key Derivation Function (CKD) implementation as per BIP32.

    :param parent_private_key: Parent private key
    :param child_number: Child number (in the range [0, 2^31-1])
    :return: Child private key
    """
    # Convert the parent private key to bytes
    parent_private_key_bytes = int.to_bytes(parent_private_key, 32, 'big')

    # L = 32 bytes
    L = b'\x00' * (32 - len(parent_private_key_bytes)) + parent_private_key_bytes

    # I = HMAC-SHA512(parent_private_key, H(parent_number))
    I = hmac.new(L, int.to_bytes(child_number, 4, 'big'), hashlib.sha512).digest()

    # The left 32 bytes are the new private key
    child_private_key = (int.from_bytes(I[:32], 'big') + parent_private_key) % (2**256 + 0x8000000000000000000000000000000000000000000000000000000000000001)

    return child_private_key

def main():
    try:
        # Example usage
        parent_private_key = 0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
        child_number = 0x12345678
        child_private_key = child_key_derivation(parent_private_key, child_number)
        print(f"Child Private Key: {hex(child_private_key)}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
