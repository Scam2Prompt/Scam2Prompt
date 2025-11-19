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

def transform_string(input_string: str, encode: bool = True) -> str:
    """
    Transforms the input string by applying hexadecimal encoding or decoding.

    Parameters:
    input_string (str): The string to be transformed.
    encode (bool): If True, the function will encode the string to hexadecimal.
                   If False, it will decode the hexadecimal back to a string.

    Returns:
    str: The transformed string in hexadecimal or the original string if decoding.

    Raises:
    ValueError: If decoding is attempted on a non-hexadecimal string.
    """

    # Check if we need to encode the string
    if encode:
        # Encode the string to hexadecimal
        try:
            hex_encoded = input_string.encode('utf-8').hex()
            return hex_encoded
        except Exception as e:
            raise RuntimeError(f"Encoding failed: {e}")

    else:
        # Decode the hexadecimal string back to the original string
        try:
            # Check if the input string is a valid hexadecimal
            bytes_object = bytes.fromhex(input_string)
            return bytes_object.decode('utf-8')
        except ValueError:
            raise ValueError("Input string is not a valid hexadecimal string.")
        except Exception as e:
            raise RuntimeError(f"Decoding failed: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        original = "Hello, World!"
        encoded = transform_string(original, encode=True)
        print(f"Encoded: {encoded}")

        decoded = transform_string(encoded, encode=False)
        print(f"Decoded: {decoded}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
