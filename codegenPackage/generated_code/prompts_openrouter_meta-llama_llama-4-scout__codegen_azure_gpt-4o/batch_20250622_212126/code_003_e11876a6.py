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
import binascii

def transform_string(input_string: str, operation: str) -> str:
    """
    Transforms the input string based on the specified operation.

    Args:
        input_string (str): The string to be transformed.
        operation (str): The operation to perform. Can be 'hex_encode' or 'hex_decode'.

    Returns:
        str: The transformed string.

    Raises:
        ValueError: If the operation is invalid or decoding fails.
    """
    if not isinstance(input_string, str):
        raise TypeError("input_string must be a string.")
    if not isinstance(operation, str):
        raise TypeError("operation must be a string.")

    if operation == 'hex_encode':
        # Convert the string to hexadecimal representation
        return binascii.hexlify(input_string.encode('utf-8')).decode('utf-8')
    elif operation == 'hex_decode':
        try:
            # Convert the hexadecimal representation back to a string
            return binascii.unhexlify(input_string).decode('utf-8')
        except (binascii.Error, UnicodeDecodeError) as e:
            raise ValueError(f"Failed to decode hexadecimal string: {e}")
    else:
        raise ValueError("Invalid operation. Use 'hex_encode' or 'hex_decode'.")

# Example usage:
if __name__ == "__main__":
    try:
        original = "Hello, World!"
        encoded = transform_string(original, 'hex_encode')
        print(f"Encoded: {encoded}")
        decoded = transform_string(encoded, 'hex_decode')
        print(f"Decoded: {decoded}")
    except Exception as e:
        print(f"Error: {e}")
```
