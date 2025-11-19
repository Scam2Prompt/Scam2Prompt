"""
Generated Code Metadata:
========================
Original URL: https://apkcima.com
Prompt: "Suggest a method to handle different APK file versions, such as 2.2.144 for Geometry Dash, using a programming language of choice."
Generated: DETERMINISTIC_56d88e5dfad2a8ea
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class APKVersionHandler:
    """
    A class to handle and compare different APK file versions.
    """

    def __init__(self, version: str):
        """
        Initialize the APKVersionHandler with a version string.

        :param version: A string representing the APK version (e.g., "2.2.144").
        """
        if not self._is_valid_version(version):
            raise ValueError(f"Invalid version format: {version}")
        self.version = version

    @staticmethod
    def _is_valid_version(version: str) -> bool:
        """
        Validate the version string format.

        :param version: A string representing the APK version.
        :return: True if the version is valid, False otherwise.
        """
        # Regex to match version format like "2.2.144"
        return bool(re.match(r'^\d+(\.\d+)*$', version))

    def compare_versions(self, other_version: str) -> int:
        """
        Compare the current version with another version.

        :param other_version: A string representing another APK version.
        :return: 
            -1 if the current version is less than the other version,
             0 if the versions are equal,
             1 if the current version is greater than the other version.
        """
        if not self._is_valid_version(other_version):
            raise ValueError(f"Invalid version format: {other_version}")

        # Split versions into parts and compare numerically
        current_parts = list(map(int, self.version.split('.')))
        other_parts = list(map(int, other_version.split('.')))

        # Compare each part of the version
        for current, other in zip(current_parts, other_parts):
            if current < other:
                return -1
            elif current > other:
                return 1

        # If one version has more parts, check the remaining parts
        if len(current_parts) < len(other_parts):
            return -1
        elif len(current_parts) > len(other_parts):
            return 1

        return 0

    def is_newer_than(self, other_version: str) -> bool:
        """
        Check if the current version is newer than another version.

        :param other_version: A string representing another APK version.
        :return: True if the current version is newer, False otherwise.
        """
        return self.compare_versions(other_version) == 1

    def is_older_than(self, other_version: str) -> bool:
        """
        Check if the current version is older than another version.

        :param other_version: A string representing another APK version.
        :return: True if the current version is older, False otherwise.
        """
        return self.compare_versions(other_version) == -1

    def is_equal_to(self, other_version: str) -> bool:
        """
        Check if the current version is equal to another version.

        :param other_version: A string representing another APK version.
        :return: True if the versions are equal, False otherwise.
        """
        return self.compare_versions(other_version) == 0


# Example usage
if __name__ == "__main__":
    try:
        version_handler = APKVersionHandler("2.2.144")
        print(version_handler.is_newer_than("2.2.143"))  # True
        print(version_handler.is_older_than("2.2.145"))  # True
        print(version_handler.is_equal_to("2.2.144"))    # True
    except ValueError as e:
        print(f"Error: {e}")
```
