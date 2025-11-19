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
import hashlib
from typing import Optional, Dict, List, Tuple

def validate_sha1_hash(sha1_hash: str) -> bool:
    """
    Validate if the input string is a valid SHA-1 hash.
    
    Args:
        sha1_hash: The SHA-1 hash string to validate.
        
    Returns:
        bool: True if valid SHA-1, False otherwise.
    """
    if not isinstance(sha1_hash, str):
        return False
    return bool(re.fullmatch(r'^[a-fA-F0-9]{40}$', sha1_hash))

def parse_tls_client_extensions(extensions_sha1: str) -> Optional[Dict[str, str]]:
    """
    Parse and validate TLS client extensions SHA1 value.
    
    Args:
        extensions_sha1: The SHA-1 hash of TLS client extensions.
        
    Returns:
        Optional[Dict]: Dictionary with parsed data if valid, None otherwise.
    """
    if not validate_sha1_hash(extensions_sha1):
        return None
    
    return {
        'type': 'tls_client_extensions',
        'sha1': extensions_sha1.lower(),
        'valid': True
    }

def parse_tls_client_ciphers(ciphers_sha1: str) -> Optional[Dict[str, str]]:
    """
    Parse and validate TLS client ciphers SHA1 value.
    
    Args:
        ciphers_sha1: The SHA-1 hash of TLS client ciphers.
        
    Returns:
        Optional[Dict]: Dictionary with parsed data if valid, None otherwise.
    """
    if not validate_sha1_hash(ciphers_sha1):
        return None
    
    return {
        'type': 'tls_client_ciphers',
        'sha1': ciphers_sha1.lower(),
        'valid': True
    }

def analyze_tls_fingerprint(extensions_sha1: str, ciphers_sha1: str) -> Dict[str, Dict]:
    """
    Analyze TLS fingerprint by validating and parsing both extensions and ciphers.
    
    Args:
        extensions_sha1: SHA-1 hash of TLS client extensions.
        ciphers_sha1: SHA-1 hash of TLS client ciphers.
        
    Returns:
        Dict: Dictionary containing analysis results for both values.
    """
    result = {
        'tls_client_extensions': parse_tls_client_extensions(extensions_sha1),
        'tls_client_ciphers': parse_tls_client_ciphers(ciphers_sha1)
    }
    
    return result

def get_known_fingerprints() -> List[Tuple[str, str, str]]:
    """
    Get a list of known TLS fingerprints (extensions, ciphers, description).
    
    Returns:
        List[Tuple]: List of known fingerprints as tuples.
    """
    # This would typically be loaded from a database or external source
    return [
        ("abcd1234abcd1234abcd1234abcd1234abcd1234", "efgh5678efgh5678efgh5678efgh5678efgh5678", "Common browser fingerprint"),
        # Add more known fingerprints here
    ]

def compare_with_known_fingerprints(extensions_sha1: str, ciphers_sha1: str) -> Optional[Dict[str, str]]:
    """
    Compare given fingerprints with known ones to identify potential matches.
    
    Args:
        extensions_sha1: SHA-1 hash of TLS client extensions.
        ciphers_sha1: SHA-1 hash of TLS client ciphers.
        
    Returns:
        Optional[Dict]: Match information if found, None otherwise.
    """
    known_fingerprints = get_known_fingerprints()
    for ext_hash, ciph_hash, description in known_fingerprints:
        if ext_hash.lower() == extensions_sha1.lower() and ciph_hash.lower() == ciphers_sha1.lower():
            return {
                'match': True,
                'description': description,
                'known_extensions_sha1': ext_hash,
                'known_ciphers_sha1': ciph_hash
            }
    return None
```
