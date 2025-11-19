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
from typing import Optional, Tuple, List
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Version:
    major: int
    minor: int
    patch: int
    build: int

    @classmethod
    def from_string(cls, version_str: str) -> Optional['Version']:
        """
        Parse version string in format "v X.Y.Z.B" into Version object.
        Returns None if string is invalid.
        """
        match = re.match(r'^v?\s*(\d+)\.(\d+)\.(\d+)\.(\d+)$', version_str.strip())
        if not match:
            return None
        
        try:
            return cls(
                major=int(match.group(1)),
                minor=int(match.group(2)),
                patch=int(match.group(3)),
                build=int(match.group(4))
            )
        except (ValueError, IndexError):
            return None

    def __str__(self) -> str:
        return f"v {self.major}.{self.minor}.{self.patch}.{self.build}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Version):
            return False
        return (self.major, self.minor, self.patch, self.build) == \
               (other.major, other.minor, other.patch, other.build)

    def __lt__(self, other: 'Version') -> bool:
        return (self.major, self.minor, self.patch, self.build) < \
               (other.major, other.minor, other.patch, other.build)

    def __le__(self, other: 'Version') -> bool:
        return self < other or self == other

    def __gt__(self, other: 'Version') -> bool:
        return not self <= other

    def __ge__(self, other: 'Version') -> bool:
        return not self < other

class VersionManager:
    def __init__(self, current_version: str):
        self.current_version = Version.from_string(current_version)
        if self.current_version is None:
            raise ValueError("Invalid initial version format")

    def get_current_version(self) -> str:
        """Returns current version as string"""
        return str(self.current_version)

    def increment_major(self) -> 'Version':
        """Increments major version and resets lower parts"""
        self.current_version.major += 1
        self.current_version.minor = 0
        self.current_version.patch = 0
        self.current_version.build = 0
        return self.current_version

    def increment_minor(self) -> 'Version':
        """Increments minor version and resets lower parts"""
        self.current_version.minor += 1
        self.current_version.patch = 0
        self.current_version.build = 0
        return self.current_version

    def increment_patch(self) -> 'Version':
        """Increments patch version and resets build number"""
        self.current_version.patch += 1
        self.current_version.build = 0
        return self.current_version

    def increment_build(self) -> 'Version':
        """Increments build number"""
        self.current_version.build += 1
        return self.current_version

    def generate_build_number(self) -> 'Version':
        """Generates build number from current date (YYMMDD)"""
        today = datetime.now()
        build_number = int(today.strftime("%y%m%d"))
        self.current_version.build = build_number
        return self.current_version

    def compare_versions(self, version_str: str) -> int:
        """
        Compare with another version string.
        Returns:
            -1 if current is older
            0 if equal
            1 if current is newer
        """
        other_version = Version.from_string(version_str)
        if other_version is None:
            raise ValueError("Invalid version format for comparison")

        if self.current_version < other_version:
            return -1
        elif self.current_version > other_version:
            return 1
        return 0
```
