"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bip32.net
Prompt: Implement a Python function to generate a 512-bit hash containing the master private key and master chain code using HMAC SHA512, as outlined in the BIP32 documentation.
Generated: DETERMINISTIC_342e45cd5c062d0e
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hmac
import hashlib

def generate_master_key_and_chain_code(seed: bytes) -> tuple:
    """
    Generate a 512-bit hash containing the master private key and master chain code using HMAC-SHA512.

    Args:
        seed (bytes): A secure random seed to initialize the master key and chain code. 
                      Typically between 128 and 512 bits as per BIP32 recommendations.

    Returns:
        tuple: A tuple containing:
            - master_private_key (bytes): The first 256 bits of the HMAC-SHA512 hash.
            - master_chain_code (bytes): The last 256 bits of the HMAC-SHA512 hash.

    Raises:
        ValueError: If the seed is not between 128 and 512 bits in length.
    """
    # Verify the seed length is between 128 and 512 bits (16 to 64 bytes)
    if not (16 <= len(seed) <= 64):
        raise ValueError("Seed must be between 128 and 512 bits (16 to 64 bytes).")

    # Define the key for HMAC-SHA512 as per BIP32
    hmac_key = b"Bitcoin seed"

    # Perform HMAC-SHA512 with the seed and key
    hmac_result = hmac.new(hmac_key, seed, hashlib.sha512).digest()

    # Split the HMAC result into master private key and master chain code
    master_private_key = hmac_result[:32]  # First 256 bits
    master_chain_code = hmac_result[32:]  # Last 256 bits

    return master_private_key, master_chain_code


# Example usage
if __name__ == "__main__":
    # Example seed (should be securely generated in a real application)
    example_seed = b"This is a secure seed for testing purposes."
    
    try:
        private_key, chain_code = generate_master_key_and_chain_code(example_seed)
        print(f"Master Private Key: {private_key.hex()}")
        print(f"Master Chain Code: {chain_code.hex()}")
    except ValueError as e:
        print(f"Error: {e}")
```
