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
class Version:
    """
    A class to represent a version of a web application.

    Attributes:
        major (int): The major version number.
        minor (int): The minor version number.
        patch (int): The patch version number.
        build (int): The build number.
    """

    def __init__(self, version_str):
        """
        Initializes the Version object with a version string.

        Args:
            version_str (str): A version string in the format "v X.Y.Z.B".

        Raises:
            ValueError: If the version string is not in the correct format.
        """
        self.major, self.minor, self.patch, self.build = self._parse_version(version_str)

    def _parse_version(self, version_str):
        """
        Parses the version string into its components.

        Args:
            version_str (str): The version string to parse.

        Returns:
            tuple: A tuple containing the major, minor, patch, and build numbers.

        Raises:
            ValueError: If the version string is not in the correct format.
        """
        if not version_str.startswith("v "):
            raise ValueError("Version string must start with 'v '")
        
        version_parts = version_str[2:].split('.')
        
        if len(version_parts) != 4:
            raise ValueError("Version string must contain four components: major.minor.patch.build")
        
        try:
            return tuple(int(part) for part in version_parts)
        except ValueError:
            raise ValueError("All version components must be integers")

    def __str__(self):
        """Returns the string representation of the version."""
        return f"v {self.major}.{self.minor}.{self.patch}.{self.build}"

    def increment_major(self):
        """Increments the major version number and resets minor, patch, and build."""
        self.major += 1
        self.minor = 0
        self.patch = 0
        self.build = 0

    def increment_minor(self):
        """Increments the minor version number and resets patch and build."""
        self.minor += 1
        self.patch = 0
        self.build = 0

    def increment_patch(self):
        """Increments the patch version number and resets build."""
        self.patch += 1
        self.build = 0

    def increment_build(self):
        """Increments the build number."""
        self.build += 1


# Example usage
if __name__ == "__main__":
    try:
        version = Version("v 2.93.8.30141")
        print(version)  # Output: v 2.93.8.30141

        version.increment_patch()
        print(version)  # Output: v 2.93.9.0

        version.increment_major()
        print(version)  # Output: v 3.0.0.0

    except ValueError as e:
        print(f"Error: {e}")
```
