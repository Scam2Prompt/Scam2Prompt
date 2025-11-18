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
import sys

def parse_version(version_string):
    """
    Parses the version string into its components: environment, version number, and build number.
    
    Args:
        version_string (str): Version string in the format "prod-v1.0.5-002".
    
    Returns:
        dict: A dictionary containing the parsed components.
    """
    try:
        # Define regex pattern to match version format
        pattern = r'^(?P<environment>[a-zA-Z]+)-v(?P<version>(\d+\.\d+\.\d+))-(?P<build>\d+)$'
        match = re.match(pattern, version_string)
        
        if not match:
            raise ValueError("Invalid version format. Expected format: 'prod-v1.0.5-002'.")
        
        # Extract components using named groups
        return {
            'environment': match.group('environment'),
            'version': match.group('version'),
            'build': match.group('build')
        }
    except Exception as e:
        # Handle and log unexpected errors
        print(f"Error parsing version string: {e}", file=sys.stderr)
        return None

def display_version_info(version_string):
    """
    Displays the version information dynamically based on the parsed version string.
    
    Args:
        version_string (str): Version string in the format "prod-v1.0.5-002".
    """
    parsed_version = parse_version(version_string)
    
    if parsed_version:
        print("Gaming Platform Version Information:")
        print(f"  Environment: {parsed_version['environment']}")
        print(f"  Version: {parsed_version['version']}")
        print(f"  Build Number: {parsed_version['build']}")
    else:
        print("Failed to parse version information.")

if __name__ == "__main__":
    # Example version string (can be dynamically replaced with actual version data from a config file or API)
    version_string = "prod-v1.0.5-002"
    
    # Display version information
    display_version_info(version_string)
```
