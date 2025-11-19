"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arweave.ar
Prompt: Create a function that checks for supported manifest versions in Arweave, specifically for versions "0.1.0" and "0.2.0".
Generated: DETERMINISTIC_75eb40eddf10d1fa
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def is_supported_manifest_version(version: str) -> bool:
    """
    Checks if the given manifest version is supported in Arweave.

    Supported versions are:
    - "0.1.0"
    - "0.2.0"

    Args:
        version (str): The manifest version to check.

    Returns:
        bool: True if the version is supported, False otherwise.

    Raises:
        ValueError: If the version is not a valid string format.
    """
    # Define the set of supported versions
    supported_versions = {"0.1.0", "0.2.0"}

    # Validate input type
    if not isinstance(version, str):
        raise ValueError("The version must be a string.")

    # Check if the version is in the supported versions
    return version in supported_versions

# Example usage:
if __name__ == "__main__":
    try:
        print(is_supported_manifest_version("0.1.0"))  # True
        print(is_supported_manifest_version("0.3.0"))  # False
        print(is_supported_manifest_version(0.2))        # Raises ValueError
    except ValueError as e:
        print(f"Error: {e}")
```
