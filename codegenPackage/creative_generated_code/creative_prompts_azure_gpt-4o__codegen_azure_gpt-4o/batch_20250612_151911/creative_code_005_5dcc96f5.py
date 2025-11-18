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
import semver

class VersioningSystem:
    """
    A versioning system to manage application versions in the format "v <major>.<minor>.<patch>.<build>".

    Example format: "v 2.93.8.30141"
    """

    VERSION_REGEX = r'^v\s(\d+)\.(\d+)\.(\d+)\.(\d+)$'

    def __init__(self, version: str):
        """
        Initialize the VersioningSystem with a version.

        :param version: The initial version string in the format "v <major>.<minor>.<patch>.<build>".
        :raises ValueError: If the version string is invalid.
        """
        if not self._is_valid_version(version):
            raise ValueError(f"Invalid version format: {version}")
        self.version = version

    def _is_valid_version(self, version: str) -> bool:
        """
        Validate the version string format.

        :param version: Version string to validate.
        :return: True if the format is valid, False otherwise.
        """
        return bool(re.match(self.VERSION_REGEX, version))

    def _parse_version(self) -> tuple:
        """
        Parse the version string into components.

        :return: A tuple of (major, minor, patch, build).
        """
        match = re.match(self.VERSION_REGEX, self.version)
        if not match:
            raise ValueError(f"Invalid version format: {self.version}")
        return tuple(map(int, match.groups()))

    def increment_major(self):
        """
        Increment the major version number and reset other components to zero.
        """
        major, _, _, _ = self._parse_version()
        self.version = f"v {major + 1}.0.0.0"

    def increment_minor(self):
        """
        Increment the minor version number and reset patch and build numbers to zero.
        """
        major, minor, _, _ = self._parse_version()
        self.version = f"v {major}.{minor + 1}.0.0"

    def increment_patch(self):
        """
        Increment the patch version number and reset the build number to zero.
        """
        major, minor, patch, _ = self._parse_version()
        self.version = f"v {major}.{minor}.{patch + 1}.0"

    def increment_build(self):
        """
        Increment the build version number.
        """
        major, minor, patch, build = self._parse_version()
        self.version = f"v {major}.{minor}.{patch}.{build + 1}"

    def get_version(self) -> str:
        """
        Get the current version string.

        :return: The current version string.
        """
        return self.version

# Example usage:
if __name__ == '__main__':
    try:
        # Initialize the versioning system
        system = VersioningSystem("v 2.93.8.30141")

        # Increment different components
        system.increment_major()
        print("After major increment:", system.get_version())

        system.increment_minor()
        print("After minor increment:", system.get_version())

        system.increment_patch()
        print("After patch increment:", system.get_version())

        system.increment_build()
        print("After build increment:", system.get_version())
    except ValueError as error:
        print(f"Error: {error}")
```
