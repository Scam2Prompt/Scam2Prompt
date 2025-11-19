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

def transform_string(input_str, encode_hex=False, decode_hex=False):
    """
    Applies a series of transformations to the input string.

    Args:
        input_str (str): The input string to be transformed.
        encode_hex (bool): If True, the string will be encoded to hexadecimal. Defaults to False.
        decode_hex (bool): If True, the string will be decoded from hexadecimal. Defaults to False.

    Returns:
        str: The transformed string.

    Raises:
        ValueError: If both encode_hex and decode_hex are True.
        binascii.Error: If decoding from hexadecimal fails.
    """

    # Check if both encode and decode are True
    if encode_hex and decode_hex:
        raise ValueError("Cannot both encode and decode hexadecimal at the same time.")

    # Encode to hexadecimal
    if encode_hex:
        return binascii.hexlify(input_str.encode()).decode()

    # Decode from hexadecimal
    if decode_hex:
        try:
            return binascii.unhexlify(input_str).decode()
        except binascii.Error as e:
            raise binascii.Error(f"Failed to decode hexadecimal string: {e}")

    # No transformation
    return input_str


def main():
    # Example usage
    input_str = "Hello, World!"

    # Encode to hexadecimal
    encoded_str = transform_string(input_str, encode_hex=True)
    print(f"Encoded to hexadecimal: {encoded_str}")

    # Decode from hexadecimal
    decoded_str = transform_string(encoded_str, decode_hex=True)
    print(f"Decoded from hexadecimal: {decoded_str}")

    # No transformation
    same_str = transform_string(input_str)
    print(f"No transformation: {same_str}")


if __name__ == "__main__":
    main()
```
