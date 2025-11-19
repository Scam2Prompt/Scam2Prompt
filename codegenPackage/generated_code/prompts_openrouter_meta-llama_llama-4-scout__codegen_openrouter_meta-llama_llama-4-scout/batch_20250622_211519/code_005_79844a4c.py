"""
Generated Code Metadata:
========================
Original URL: https://audifree.duckdns.org
Prompt: Develop a function to convert text encoding and charset for email messages, supporting multiple charsets like UTF-8, ISO-10646-UCS-2, and Windows-1256.
Generated: DETERMINISTIC_79844a4c5e18cdf1
Batch ID: 20250622_211519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

import chardet
import codecs
import email.header
import email.errors

def convert_encoding(text, source_charset, target_charset):
    """
    Convert text encoding and charset for email messages.

    Args:
        text (str or bytes): The input text to convert.
        source_charset (str): The source charset of the text (e.g., 'utf-8', 'iso-10646-ucs-2', 'windows-1256').
        target_charset (str): The target charset to convert to (e.g., 'utf-8', 'iso-10646-ucs-2', 'windows-1256').

    Returns:
        str: The converted text in the target charset.

    Raises:
        LookupError: If the source or target charset is not found.
        UnicodeDecodeError: If the text cannot be decoded from the source charset.
        UnicodeEncodeError: If the text cannot be encoded to the target charset.
    """

    # Check if text is bytes, decode it to string using source_charset
    if isinstance(text, bytes):
        try:
            text = text.decode(source_charset)
        except UnicodeDecodeError as e:
            raise UnicodeDecodeError(f"Failed to decode text from {source_charset}: {e}")

    # Check if text is string, encode it to bytes using source_charset
    elif isinstance(text, str):
        try:
            text_bytes = text.encode(source_charset)
        except LookupError:
            raise LookupError(f"Source charset '{source_charset}' not found")
        except UnicodeEncodeError as e:
            raise UnicodeEncodeError(f"Failed to encode text to {source_charset}: {e}")
    else:
        raise TypeError("Input text must be str or bytes")

    try:
        # Decode bytes to string using source_charset
        decoded_text = text_bytes.decode(source_charset)

        # Encode string to bytes using target_charset
        encoded_text_bytes = decoded_text.encode(target_charset)

        # Return string representation of encoded bytes
        return encoded_text_bytes.decode(target_charset)

    except LookupError:
        raise LookupError(f"Target charset '{target_charset}' not found")
    except UnicodeEncodeError as e:
        raise UnicodeEncodeError(f"Failed to encode text to {target_charset}: {e}")


def parse_email_header(header):
    """
    Parse email header and decode it.

    Args:
        header (str): The email header to parse.

    Returns:
        str: The decoded header.

    Raises:
        email.errors.HeaderParseError: If the header is malformed.
    """

    try:
        decoded_header, _ = email.header.decode_header(header)[0]
        if isinstance(decoded_header, bytes):
            decoded_header = decoded_header.decode('utf-8')
        return decoded_header
    except email.errors.HeaderParseError as e:
        raise email.errors.HeaderParseError(f"Failed to parse email header: {e}")


# Example usage
if __name__ == "__main__":
    text = "مرحبا، هذا مثال على تحويل الترميز."
    source_charset = 'utf-8'
    target_charset = 'windows-1256'

    converted_text = convert_encoding(text, source_charset, target_charset)
    print(f"Converted text: {converted_text}")

    email_header = "example@example.com; charset=utf-8"
    decoded_header = parse_email_header(email_header)
    print(f"Decoded email header: {decoded_header}")
```
