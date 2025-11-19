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
    Checks if the given manifest version is supported in Arweave.

    Supported versions:
    - "0.1.0"
    - "0.2.0"

    Args:
        version (str): The manifest version to check.

    Returns:
        bool: True if the version is supported, False otherwise.
    """
    # List of supported manifest versions
    supported_versions = {"0.1.0", "0.2.0"}

    try:
        # Check if the version is in the set of supported versions
        return version in supported_versions
    except Exception as e:
        # Log the error (in production, replace print with proper logging)
        print(f"Error checking manifest version: {e}")
        return False


# Example usage:
if __name__ == "__main__":
    # Test cases
    test_versions = ["0.1.0", "0.2.0", "0.3.0", "invalid_version"]
    for test_version in test_versions:
        print(f"Version {test_version} supported: {is_supported_manifest_version(test_version)}")
```
