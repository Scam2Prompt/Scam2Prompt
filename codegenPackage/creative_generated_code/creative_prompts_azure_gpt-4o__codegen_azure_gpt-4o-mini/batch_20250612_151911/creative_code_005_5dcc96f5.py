"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ksp.onsiteapp.co
Prompt: Create a versioning system for a web application, referencing the version format "v 2.93.8.30141" used on the King Salman Park portal.
Generated: DETERMINISTIC_5dcc96f5b55dc5b5
Batch ID: 20250612_151911
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


class Version:
    """
    A class to represent a version number using the format v X.Y.Z.W.
    """

    def __init__(self, version: str):
        """
        Initializes the version object with a version string.

        :param version: A string in the format 'v X.Y.Z.W'
        :raises ValueError: If the version string is not valid.
        """
        if not self.is_valid_version(version):
            raise ValueError(f"Invalid version format: '{version}'")
        self.version = version

    @staticmethod
    def is_valid_version(version: str) -> bool:
        """
        Validates the version string format.

        :param version: A version string to validate.
        :return: True if the version format is valid, otherwise False.
        """
        version_regex = r"^v \d+\.\d+\.\d+\.\d+$"
        return bool(re.match(version_regex, version))

    def __str__(self) -> str:
        """Returns the version as a string."""
        return self.version

    def increment(self, part: str) -> None:
        """
        Increments the specified part of the version.

        :param part: The part to increment (major, minor, patch, or build).
        :raises ValueError: If the part is not valid.
        """
        parts = self.version.split(' ')[1].split('.')
        version_parts = list(map(int, parts))

        part_dict = {
            "major": 0,
            "minor": 1,
            "patch": 2,
            "build": 3,
        }
        
        if part not in part_dict:
            raise ValueError(f"Invalid part '{part}'. Must be one of {list(part_dict.keys())}.")

        # Increment the specified part
        version_parts[part_dict[part]] += 1
        
        # Reset the following parts to 0
        for i in range(part_dict[part] + 1, len(version_parts)):
            version_parts[i] = 0

        # Rebuild the version string
        self.version = f"v {' '.join(map(str, version_parts))}"

    def compare(self, other: 'Version') -> int:
        """
        Compares this version with another version.

        :param other: Another Version object to compare with.
        :return: 1 if this version is greater, -1 if smaller, 0 if equal.
        """
        self_parts = list(map(int, self.version.split(' ')[1].split('.')))
        other_parts = list(map(int, other.version.split(' ')[1].split('.')))

        for self_part, other_part in zip(self_parts, other_parts):
            if self_part > other_part:
                return 1
            elif self_part < other_part:
                return -1
        return 0


# Example Usage
if __name__ == "__main__":
    try:
        version1 = Version("v 2.93.8.30141")
        print(f"Current Version: {version1}")

        # Incrementing the patch version
        version1.increment("patch")
        print(f"After Incrementing Patch: {version1}")

        version2 = Version("v 2.93.9.0")
        comparison_result = version1.compare(version2)

        if comparison_result == 1:
            print(f"{version1} is greater than {version2}.")
        elif comparison_result == -1:
            print(f"{version1} is less than {version2}.")
        else:
            print(f"{version1} is equal to {version2}.")

    except ValueError as e:
        print(f"Error: {e}")
```
