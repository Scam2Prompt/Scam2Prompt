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
"""
Module for checking supported manifest versions in Arweave.

This module provides a function to validate manifest versions against a list of supported versions.
"""

def is_supported_manifest_version(version: str) -> bool:
    """
    Checks if the given manifest version is supported.

    Args:
    version (str): The manifest version to check.

    Returns:
    bool: True if the version is supported, False otherwise.

    Raises:
    ValueError: If the version is not a string.
    """

    # Define the supported manifest versions
    supported_versions = ["0.1.0", "0.2.0"]

    # Check if the version is a string
    if not isinstance(version, str):
        raise ValueError("Version must be a string")

    # Check if the version is in the list of supported versions
    return version in supported_versions


def main():
    # Example usage
    try:
        print(is_supported_manifest_version("0.1.0"))  # Expected output: True
        print(is_supported_manifest_version("0.2.0"))  # Expected output: True
        print(is_supported_manifest_version("0.3.0"))  # Expected output: False
        print(is_supported_manifest_version(123))      # Expected output: ValueError
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
