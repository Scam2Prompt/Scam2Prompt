"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pvufarmland.com
Prompt: Generate code to display version information dynamically on a gaming platform, using the versioning format "prod-v1.0.5-002" as seen in PVU Farmland.
Generated: DETERMINISTIC_950e6e1f7b45551d
Batch ID: 20250612_145836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class VersionInfo:
    """
    A class to retrieve and display version information for a gaming platform.
    
    Attributes:
        version (str): The version string in the format "prod-vX.X.X-XXX".
    """

    def __init__(self, version: str):
        """
        Initializes the VersionInfo object with a version string.
        
        Args:
            version (str): The version string to initialize.
        
        Raises:
            ValueError: If the version format is invalid.
        """
        if not self._is_valid_version_format(version):
            raise ValueError("Invalid version format. Expected format 'prod-vX.X.X-XXX'.")
        self.version = version

    @staticmethod
    def _is_valid_version_format(version: str) -> bool:
        """
        Validates the version string format.
        
        Args:
            version (str): The version string to validate.
        
        Returns:
            bool: True if the format is valid, False otherwise.
        """
        pattern = r'^prod-v\d+\.\d+\.\d+-\d{3}$'
        return re.match(pattern, version) is not None

    def display_version(self):
        """
        Displays the version information in a user-friendly format.
        """
        try:
            print(f"Current Version: {self.version}")
        except Exception as e:
            print(f"An error occurred while displaying the version: {e}")

def main():
    """
    Main function to run the version information display.
    """
    # Example version string
    version_string = "prod-v1.0.5-002"
    
    try:
        version_info = VersionInfo(version_string)
        version_info.display_version()
    except ValueError as ve:
        print(f"Version error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
