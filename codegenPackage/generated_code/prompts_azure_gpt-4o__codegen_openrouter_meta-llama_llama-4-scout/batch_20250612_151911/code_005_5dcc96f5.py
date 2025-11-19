"""
Generated Code Metadata:
========================
Original URL: https://ksp.onsiteapp.co
Prompt: Create a versioning system for a web application, referencing the version format "v 2.93.8.30141" used on the King Salman Park portal.
Generated: DETERMINISTIC_5dcc96f5b55dc5b5
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class Version:
    """
    Represents a version of a web application.

    The version format is inspired by "v 2.93.8.30141" used on the King Salman Park portal.
    It consists of a major version, minor version, patch version, and build number.
    """

    def __init__(self, major, minor, patch, build):
        """
        Initializes a Version object.

        Args:
            major (int): The major version.
            minor (int): The minor version.
            patch (int): The patch version.
            build (int): The build number.

        Raises:
            TypeError: If any of the version components are not integers.
        """
        if not all(isinstance(component, int) for component in [major, minor, patch, build]):
            raise TypeError("All version components must be integers")

        self.major = major
        self.minor = minor
        self.patch = patch
        self.build = build

    def __str__(self):
        """
        Returns a string representation of the version.

        Returns:
            str: A string in the format "v X.Y.Z.BUILD".
        """
        return f"v {self.major}.{self.minor}.{self.patch}.{self.build}"

    def __repr__(self):
        """
        Returns a string representation of the version for debugging.

        Returns:
            str: A string in the format "Version(major=X, minor=Y, patch=Z, build=BUILD)".
        """
        return f"Version(major={self.major}, minor={self.minor}, patch={self.patch}, build={self.build})"

    def to_dict(self):
        """
        Returns a dictionary representation of the version.

        Returns:
            dict: A dictionary with keys "major", "minor", "patch", and "build".
        """
        return {
            "major": self.major,
            "minor": self.minor,
            "patch": self.patch,
            "build": self.build,
        }

    @classmethod
    def from_string(cls, version_string):
        """
        Creates a Version object from a string.

        Args:
            version_string (str): A string in the format "v X.Y.Z.BUILD".

        Returns:
            Version: A Version object.

        Raises:
            ValueError: If the version string is not in the correct format.
        """
        match = re.match(r"^v (\d+)\.(\d+)\.(\d+)\.(\d+)$", version_string)
        if match:
            major, minor, patch, build = map(int, match.groups())
            return cls(major, minor, patch, build)
        else:
            raise ValueError("Invalid version string")

def main():
    try:
        version = Version(2, 93, 8, 30141)
        print(version)  # Output: v 2.93.8.30141
        print(version.to_dict())  # Output: {'major': 2, 'minor': 93, 'patch': 8, 'build': 30141}

        version_string = "v 2.93.8.30141"
        version_from_string = Version.from_string(version_string)
        print(version_from_string)  # Output: v 2.93.8.30141

        invalid_version_string = "invalid version"
        try:
            Version.from_string(invalid_version_string)
        except ValueError as e:
            print(e)  # Output: Invalid version string
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
