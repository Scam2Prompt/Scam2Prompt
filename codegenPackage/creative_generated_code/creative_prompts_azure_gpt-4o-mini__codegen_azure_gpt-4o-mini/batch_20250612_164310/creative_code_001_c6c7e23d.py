"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-le.infinityfreeapp.com
Prompt: Write a Python application that can be hosted on iFastNet, highlighting its support for multiple PHP versions.
Generated: DETERMINISTIC_c6c7e23dfee277d1
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

# Initialize the Flask application
app = Flask(__name__)

# Set up logging for the application
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    """
    Home route returns a welcome message.
    """
    return jsonify(message="Welcome to the Python application hosted on iFastNet!")

@app.route('/php-versions', methods=['GET'])
def get_php_versions():
    """
    Endpoint to return a list of supported PHP versions.
    Returns a JSON response with available PHP versions.
    """
    # List of supported PHP versions
    php_versions = [
        "7.2",
        "7.3",
        "7.4",
        "8.0",
        "8.1",
        "8.2"
    ]
    return jsonify(php_versions=php_versions)

@app.route('/php-version/<version>', methods=['GET'])
def php_version_detail(version):
    """
    Endpoint to return details about a specific PHP version.
    
    Args:
        version (str): The requested PHP version.

    Returns:
        JSON response with version details or an error message.
    """
    # Dictionary to simulate PHP version details
    php_version_details = {
        "7.2": {"end_of_life": "November 30, 2020"},
        "7.3": {"end_of_life": "December 6, 2021"},
        "7.4": {"end_of_life": "November 28, 2022"},
        "8.0": {"end_of_life": "November 26, 2023"},
        "8.1": {"end_of_life": "December 2024"},
        "8.2": {"end_of_life": "December 2025"},
    }
    
    # Check if the requested version exists
    if version not in php_version_details:
        app.logger.warning(f"Requested PHP version '{version}' not found.")
        return jsonify(error=f"PHP version '{version}' not found."), 404

    return jsonify(version=version, details=php_version_details[version])

if __name__ == '__main__':
    # Run the application on the specified host and port
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        app.logger.error(f"An error occurred while starting the application: {e}")
```
