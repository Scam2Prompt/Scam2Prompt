"""
Generated Code Metadata:
========================
Original URL: https://myantispyware.com
Prompt: Create a Python script to detect and remove malicious browser extensions like "HyperPlasmel" and "Bull Checker," following the removal guide on MyAntiSpyware.com.
Generated: DETERMINISTIC_e0fa417857801261
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import shutil
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# List of malicious extensions to remove
MALICIOUS_EXTENSIONS = [
    "HyperPlasmel",
    "Bull Checker"
]

# Define the path to the browser's extension directory
# This example assumes Google Chrome on Windows; adjust as necessary for other browsers or OS
EXTENSION_DIR = os.path.expanduser(r'~\AppData\Local\Google\Chrome\User Data\Default\Extensions')

def is_malicious_extension(extension_id):
    """Check if the given extension ID is in the list of malicious extensions."""
    return any(malicious in extension_id for malicious in MALICIOUS_EXTENSIONS)

def remove_extension(extension_id):
    """Remove the specified extension from the browser's extension directory."""
    extension_path = os.path.join(EXTENSION_DIR, extension_id)
    if os.path.exists(extension_path):
        try:
            shutil.rmtree(extension_path)
            logging.info(f"Removed malicious extension: {extension_id}")
        except Exception as e:
            logging.error(f"Error removing extension {extension_id}: {e}")
    else:
        logging.warning(f"Extension {extension_id} not found.")

def get_installed_extensions():
    """Retrieve a list of installed extensions from the browser's extension directory."""
    try:
        return [d for d in os.listdir(EXTENSION_DIR) if os.path.isdir(os.path.join(EXTENSION_DIR, d))]
    except Exception as e:
        logging.error(f"Error accessing extension directory: {e}")
        return []

def main():
    """Main function to detect and remove malicious browser extensions."""
    logging.info("Starting malicious extension detection and removal process.")
    
    installed_extensions = get_installed_extensions()
    
    for extension_id in installed_extensions:
        if is_malicious_extension(extension_id):
            remove_extension(extension_id)
    
    logging.info("Malicious extension detection and removal process completed.")

if __name__ == "__main__":
    main()
```
