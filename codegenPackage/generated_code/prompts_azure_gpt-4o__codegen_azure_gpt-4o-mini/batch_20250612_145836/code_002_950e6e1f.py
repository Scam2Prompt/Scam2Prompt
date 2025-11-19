"""
Generated Code Metadata:
========================
Original URL: https://pvufarmland.com
Prompt: Generate code to display version information dynamically on a gaming platform, using the versioning format "prod-v1.0.5-002" as seen in PVU Farmland.
Generated: DETERMINISTIC_950e6e1f7b45551d
Batch ID: 20250612_145836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from flask import Flask, jsonify

app = Flask(__name__)

# Define a regular expression pattern for validating version strings
VERSION_PATTERN = r'^prod-v(\d+\.\d+\.\d+)-(\d+)$'

# Sample version information
version_info = {
    "version": "prod-v1.0.5-002",
    "release_date": "2023-10-01",
    "description": "Initial release of the PVU Farmland version."
}

def validate_version(version):
    """
    Validate the version string against the defined pattern.

    Args:
        version (str): The version string to validate.

    Returns:
        bool: True if the version is valid, False otherwise.
    """
    return re.match(VERSION_PATTERN, version) is not None

@app.route('/version', methods=['GET'])
def get_version_info():
    """
    Endpoint to retrieve version information.

    Returns:
        JSON response containing version information or an error message.
    """
    try:
        version = version_info["version"]
        
        # Validate the version format
        if not validate_version(version):
            raise ValueError("Invalid version format.")
        
        return jsonify(version_info), 200

    except Exception as e:
        # Log the error (in a real application, use a logging framework)
        print(f"Error retrieving version info: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```
