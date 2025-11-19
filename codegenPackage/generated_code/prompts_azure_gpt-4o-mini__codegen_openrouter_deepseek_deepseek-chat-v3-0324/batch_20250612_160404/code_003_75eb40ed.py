"""
Generated Code Metadata:
========================
Original URL: https://arweave.ar
Prompt: Create a function that checks for supported manifest versions in Arweave, specifically for versions "0.1.0" and "0.2.0".
Generated: DETERMINISTIC_75eb40eddf10d1fa
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def is_supported_manifest_version(version: str) -> bool:
    """
    Checks if the provided manifest version is supported by Arweave.
    
    Args:
        version (str): The manifest version to check.
        
    Returns:
        bool: True if the version is supported ("0.1.0" or "0.2.0"), False otherwise.
        
    Examples:
        >>> is_supported_manifest_version("0.1.0")
        True
        >>> is_supported_manifest_version("0.3.0")
        False
    """
    supported_versions = {"0.1.0", "0.2.0"}
    return version in supported_versions
```
