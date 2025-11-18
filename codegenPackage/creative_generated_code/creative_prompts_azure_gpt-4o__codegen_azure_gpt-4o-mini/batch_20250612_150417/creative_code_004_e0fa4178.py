"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myantispyware.com
Prompt: Create a Python script to detect and remove malicious browser extensions like "HyperPlasmel" and "Bull Checker," following the removal guide on MyAntiSpyware.com.
Generated: DETERMINISTIC_e0fa417857801261
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import sys
import re

# Define the malicious extensions and their respective paths
MALICIOUS_EXTENSIONS = {
    "HyperPlasmel": {
        "path": "/path/to/chrome/extensions/hyperplasmel",
        "regex": r"hyperplasmel.*\.crx"
    },
    "Bull Checker": {
        "path": "/path/to/chrome/extensions/bullchecker",
        "regex": r"bullchecker.*\.crx"
    }
}

def is_extension_installed(extension_path):
    """Check if the extension directory exists."""
    return os.path.exists(extension_path)

def remove_extension(extension_name, extension_path):
    """Remove the specified extension directory."""
    try:
        if is_extension_installed(extension_path):
            shutil.rmtree(extension_path)
            print(f"Successfully removed {extension_name} extension.")
        else:
            print(f"{extension_name} extension not found at {extension_path}.")
    except Exception as e:
        print(f"Error while removing {extension_name}: {e}")

def main():
    """Main function to detect and remove malicious extensions."""
    for extension_name, details in MALICIOUS_EXTENSIONS.items():
        # Check for installation and remove if present
        remove_extension(extension_name, details['path'])

        # Additionally check for .crx files using regex
        try:
            for file in os.listdir(details['path']):
                if re.match(details['regex'], file):
                    file_path = os.path.join(details['path'], file)
                    os.remove(file_path)
                    print(f"Removed malicious file: {file_path}")
        except FileNotFoundError:
            print(f"No files found in {details['path']}.")
        except Exception as e:
            print(f"Error while checking files in {details['path']}: {e}")

if __name__ == "__main__":
    main()
```

**Note**: Please replace the `"/path/to/chrome/extensions/hyperplasmel"` and `"/path/to/chrome/extensions/bullchecker"` with the actual paths where Chrome extensions are installed on your system. Ensure you have the necessary permissions to perform these operations.
