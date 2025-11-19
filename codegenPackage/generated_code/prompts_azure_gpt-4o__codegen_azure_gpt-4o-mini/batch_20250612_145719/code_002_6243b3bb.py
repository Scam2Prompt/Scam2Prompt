"""
Generated Code Metadata:
========================
Original URL: https://netsecurity.pages.dev
Prompt: Create a Python function to parse and validate `tlsClientExtensionsSha1` and `tlsClientCiphersSha1` values for security analysis, as described on netsecurity.pages.dev.
Generated: DETERMINISTIC_6243b3bb593be4bc
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import List, Tuple

class TLSValidationError(Exception):
    """Custom exception for TLS validation errors."""
    pass

def parse_tls_client_extensions_sha1(extensions: str) -> List[str]:
    """
    Parse and validate the tlsClientExtensionsSha1 value.

    Args:
        extensions (str): A string containing the SHA1 hash of TLS client extensions.

    Returns:
        List[str]: A list of validated extensions.

    Raises:
        TLSValidationError: If the input format is invalid.
    """
    # Validate the input format using a regex for SHA1
    if not re.match(r'^[0-9a-fA-F]{40}$', extensions):
        raise TLSValidationError("Invalid tlsClientExtensionsSha1 format. Must be a 40-character hex string.")

    # Split the extensions into a list (assuming they are separated by commas)
    return [ext.strip() for ext in extensions.split(',') if ext.strip()]

def parse_tls_client_ciphers_sha1(ciphers: str) -> List[str]:
    """
    Parse and validate the tlsClientCiphersSha1 value.

    Args:
        ciphers (str): A string containing the SHA1 hash of TLS client ciphers.

    Returns:
        List[str]: A list of validated ciphers.

    Raises:
        TLSValidationError: If the input format is invalid.
    """
    # Validate the input format using a regex for SHA1
    if not re.match(r'^[0-9a-fA-F]{40}$', ciphers):
        raise TLSValidationError("Invalid tlsClientCiphersSha1 format. Must be a 40-character hex string.")

    # Split the ciphers into a list (assuming they are separated by commas)
    return [cipher.strip() for cipher in ciphers.split(',') if cipher.strip()]

def validate_tls_values(extensions: str, ciphers: str) -> Tuple[List[str], List[str]]:
    """
    Validate and parse both tlsClientExtensionsSha1 and tlsClientCiphersSha1 values.

    Args:
        extensions (str): The tlsClientExtensionsSha1 value.
        ciphers (str): The tlsClientCiphersSha1 value.

    Returns:
        Tuple[List[str], List[str]]: A tuple containing lists of validated extensions and ciphers.

    Raises:
        TLSValidationError: If any of the input formats are invalid.
    """
    try:
        validated_extensions = parse_tls_client_extensions_sha1(extensions)
        validated_ciphers = parse_tls_client_ciphers_sha1(ciphers)
        return validated_extensions, validated_ciphers
    except TLSValidationError as e:
        # Log the error or handle it as needed
        raise TLSValidationError(f"Validation error: {str(e)}")

# Example usage (commented out for production)
# if __name__ == "__main__":
#     try:
#         extensions = "abc123... (40 hex characters)"
#         ciphers = "def456... (40 hex characters)"
#         valid_extensions, valid_ciphers = validate_tls_values(extensions, ciphers)
#         print("Valid Extensions:", valid_extensions)
#         print("Valid Ciphers:", valid_ciphers)
#     except TLSValidationError as e:
#         print(e)
```
