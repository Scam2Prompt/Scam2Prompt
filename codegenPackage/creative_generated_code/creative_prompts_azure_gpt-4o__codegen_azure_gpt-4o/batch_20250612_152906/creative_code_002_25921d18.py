"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-coin-mixer.com
Prompt: Provide a code example to validate a TONCOIN address checksum and ensure it meets the requirements for the TONCOIN Mixer service.
Generated: DETERMINISTIC_25921d181c2cac45
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import base64
import hashlib

def validate_toncoin_address(address: str) -> bool:
    """
    Validates a TONCOIN address for checksum correctness and format compliance.

    Args:
        address (str): The TONCOIN address to validate.

    Returns:
        bool: True if the address is valid, False otherwise.
    """
    try:
        # Regular expression to check TONCOIN address format
        toncoin_address_regex = r'^EQ[A-Za-z0-9_-]{48}$'

        # Step 1: Check if the address matches the expected format
        if not re.match(toncoin_address_regex, address):
            return False

        # Step 2: Decode the base64-encoded part of the address (excluding the "EQ" prefix)
        base64_part = address[2:]
        try:
            decoded_bytes = base64.urlsafe_b64decode(base64_part + "==")  # Add padding for URL-safe base64
        except Exception:
            return False

        # Step 3: Ensure the decoded data is exactly 36 bytes
        if len(decoded_bytes) != 36:
            return False

        # Step 4: Verify the checksum
        # The first 32 bytes are the actual address, the last 4 bytes are the CRC32 checksum
        address_data = decoded_bytes[:32]
        checksum = decoded_bytes[32:]
        calculated_checksum = hashlib.crc32(address_data).to_bytes(4, byteorder='big')

        if checksum != calculated_checksum:
            return False

        # If all checks pass, the address is valid
        return True

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error occurred during TONCOIN address validation: {e}")
        return False


# Example usage
if __name__ == "__main__":
    test_address = "EQAdk6J8ZtT8ZC1Pojf8Zk1U76qqD4F59GMOR8E8eWmFyn0d"  # Replace with a real TONCOIN address
    if validate_toncoin_address(test_address):
        print("The TONCOIN address is valid.")
    else:
        print("The TONCOIN address is invalid.")
```
