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
from typing import List, Tuple

class TLSValidationError(Exception):
    """Custom exception raised for TLS validation errors."""
    pass

def parse_tls_values(tls_client_extensions: str, tls_client_ciphers: str) -> Tuple[List[str], List[str]]:
    """
    Parse and validate tlsClientExtensionsSha1 and tlsClientCiphersSha1 values.

    Args:
        tls_client_extensions (str): A string representation of the TLS client extensions.
        tls_client_ciphers (str): A string representation of the TLS client ciphers.

    Returns:
        Tuple[List[str], List[str]]: A tuple containing two lists:
            - List of validated client extensions.
            - List of validated ciphers.

    Raises:
        TLSValidationError: If any of the input values are malformed or invalid.
    """
    
    # Define regular expressions for validation
    extension_pattern = re.compile(r'^[0-9a-fA-F]{40}$')  # SHA1 hash should be 40 hex characters
    ciphers_pattern = re.compile(r'^[0-9a-fA-F]{40}$')    # SHA1 hash should be 40 hex characters

    # Split the input strings into individual values
    extensions = tls_client_extensions.split(',')
    ciphers = tls_client_ciphers.split(',')

    # Validate extensions
    validated_extensions = []
    for ext in extensions:
        ext = ext.strip()
        if extension_pattern.match(ext):
            validated_extensions.append(ext)
        else:
            raise TLSValidationError(f"Invalid client extension SHA1: '{ext}'")

    # Validate ciphers
    validated_ciphers = []
    for cipher in ciphers:
        cipher = cipher.strip()
        if ciphers_pattern.match(cipher):
            validated_ciphers.append(cipher)
        else:
            raise TLSValidationError(f"Invalid cipher SHA1: '{cipher}'")

    return validated_extensions, validated_ciphers

# Example usage with error handling
if __name__ == "__main__":
    try:
        extensions_str = "abcdefabcdefabcdefabcdefabcdefabcdefabcdef, 1234567890abcdef1234567890abcdef12345678"
        ciphers_str = "abcdefabcdefabcdefabcdefabcdefabcdefabcdef, 1234567890abcdef1234567890abcdef12345678"
        
        extensions, ciphers = parse_tls_values(extensions_str, ciphers_str)
        print("Validated Extensions:", extensions)
        print("Validated Ciphers:", ciphers)
        
    except TLSValidationError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
```
