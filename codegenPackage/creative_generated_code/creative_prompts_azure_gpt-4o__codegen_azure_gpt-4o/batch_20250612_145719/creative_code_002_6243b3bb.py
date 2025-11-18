"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://netsecurity.pages.dev
Prompt: Create a Python function to parse and validate `tlsClientExtensionsSha1` and `tlsClientCiphersSha1` values for security analysis, as described on netsecurity.pages.dev.
Generated: DETERMINISTIC_6243b3bb593be4bc
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def parse_and_validate_tls_values(tlsClientExtensionsSha1, tlsClientCiphersSha1):
    """
    Parses and validates TLS Client Extensions SHA1 and TLS Client Ciphers SHA1 values.

    Args:
        tlsClientExtensionsSha1 (str): SHA1 value for TLS client extensions.
        tlsClientCiphersSha1 (str): SHA1 value for TLS client ciphers.

    Returns:
        dict: A dictionary containing validation results for both values.

    Raises:
        ValueError: If either of the SHA1 values are invalid.
    """
    
    # Regular expression to match a valid SHA1 hash (40 hexadecimal characters)
    sha1_pattern = re.compile(r'^[a-fA-F0-9]{40}$')

    # Validate TLS Client Extensions SHA1
    if not sha1_pattern.match(tlsClientExtensionsSha1):
        raise ValueError(f"Invalid tlsClientExtensionsSha1 value: {tlsClientExtensionsSha1}")

    # Validate TLS Client Ciphers SHA1
    if not sha1_pattern.match(tlsClientCiphersSha1):
        raise ValueError(f"Invalid tlsClientCiphersSha1 value: {tlsClientCiphersSha1}")
    
    # Return the validation results
    return {
        "tlsClientExtensionsSha1": "Valid",
        "tlsClientCiphersSha1": "Valid"
    }

# Example usage:
if __name__ == "__main__":
    try:
        result = parse_and_validate_tls_values(
            "7b8f465a8b7c263dabf1e5be9e3e3169b2e7c5db",
            "5d41402abc4b2a76b9719d911017c592"
        )
        print("Validation results:", result)
    except ValueError as e:
        print("Error:", e)
```
