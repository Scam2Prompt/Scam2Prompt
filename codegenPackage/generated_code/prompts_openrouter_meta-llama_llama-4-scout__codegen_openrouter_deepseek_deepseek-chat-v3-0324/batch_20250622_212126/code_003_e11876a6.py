"""
Generated Code Metadata:
========================
Original URL: https://sha-11x.pages.dev
Prompt: Develop a function that takes a string input and applies a series of transformations, including possible hexadecimal encoding and decoding, similar to the transformations observed in the webpage's content.
Generated: DETERMINISTIC_e11876a6003089a8
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import binascii

def transform_string(input_str):
    """
    Applies a series of transformations to the input string including:
    - Hexadecimal encoding/decoding
    - String reversal
    - Case modification
    
    Args:
        input_str (str): The string to be transformed
        
    Returns:
        str: The transformed string
        
    Raises:
        ValueError: If hex decoding fails due to invalid hex data
    """
    try:
        # Check if input is a hex string and try to decode it
        if re.fullmatch(r'^[0-9a-fA-F]+$', input_str):
            try:
                decoded = binascii.unhexlify(input_str).decode('utf-8')
                return decoded[::-1]  # Reverse the decoded string
            except binascii.Error as e:
                raise ValueError("Invalid hex data") from e
            except UnicodeDecodeError:
                pass  # Not valid UTF-8, proceed with other transformations
        
        # Check if input is ASCII and try to hex encode it
        if all(ord(c) < 128 for c in input_str):
            hex_encoded = binascii.hexlify(input_str.encode('utf-8')).decode('utf-8')
            return hex_encoded.upper()
        
        # Default transformation: reverse and toggle case
        transformed = input_str[::-1]
        transformed = transformed.swapcase()
        return transformed
    
    except Exception as e:
        raise ValueError(f"Transformation failed: {str(e)}") from e
```
