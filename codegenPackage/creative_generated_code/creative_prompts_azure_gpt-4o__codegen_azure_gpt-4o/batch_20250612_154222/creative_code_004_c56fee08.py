"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://audifree.duckdns.org
Prompt: Write code to convert Unicode text to different character encodings (e.g., UTF-8, ISO-8859-6, Windows-1256) as outlined in the LuFix.to Sender v1.0 documentation.
Generated: DETERMINISTIC_c56fee0802f5c6d5
Batch ID: 20250612_154222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import codecs

def convert_unicode_to_encoding(text, encoding):
    """
    Converts a Unicode string to the specified character encoding.

    Args:
        text (str): The input Unicode text to be converted.
        encoding (str): The target character encoding (e.g., 'utf-8', 'iso-8859-6', 'windows-1256').

    Returns:
        bytes: The encoded text in the specified character encoding.

    Raises:
        ValueError: If the specified encoding is not supported.
        UnicodeEncodeError: If the text cannot be encoded to the specified encoding.
    """
    try:
        # Validate the encoding
        if encoding not in codecs.available_encodings():
            raise ValueError(f"Unsupported encoding: {encoding}")

        # Convert the Unicode text to the specified encoding
        encoded_text = text.encode(encoding)
        return encoded_text
    except UnicodeEncodeError as e:
        raise UnicodeEncodeError(
            f"Failed to encode text to {encoding}: {str(e)}"
        ) from e


def main():
    """
    Demonstrates the usage of the `convert_unicode_to_encoding` function.
    """
    # Sample Unicode text
    unicode_text = "Hello, مرحبا, 你好, Привет!"

    # List of encodings to convert to
    encodings = ["utf-8", "iso-8859-6", "windows-1256"]

    for encoding in encodings:
        try:
            # Convert and print the result
            encoded_text = convert_unicode_to_encoding(unicode_text, encoding)
            print(f"Text encoded to {encoding}: {encoded_text}")
        except ValueError as ve:
            print(f"Error: {ve}")
        except UnicodeEncodeError as ue:
            print(f"Error: {ue}")


if __name__ == "__main__":
    # Run the demonstration
    main()
```
