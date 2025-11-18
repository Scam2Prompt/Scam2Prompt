"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socrates-gm.com
Prompt: Provide a Python script to check browser compatibility (e.g., Chrome, Safari, Firefox) for accessing the Socrates GM portal and alert the user if an unsupported browser is detected.
Generated: DETERMINISTIC_08204413ba1326bd
Batch ID: 20250612_154854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from flask import Flask, request, jsonify

app = Flask(__name__)

# List of supported browsers with minimum required versions
SUPPORTED_BROWSERS = {
    "Chrome": 90,  # Minimum version 90
    "Firefox": 88,  # Minimum version 88
    "Safari": 14,  # Minimum version 14
}

@app.route('/check-browser', methods=['GET'])
def check_browser_compatibility():
    """
    Endpoint to check browser compatibility for accessing the Socrates GM portal.
    """
    try:
        # Extract User-Agent from request headers
        user_agent = request.headers.get('User-Agent', '')
        
        # Parse the User-Agent to determine the browser and version
        browser_name, browser_version = parse_user_agent(user_agent)
        
        # Check if the browser is supported
        if browser_name in SUPPORTED_BROWSERS:
            min_version = SUPPORTED_BROWSERS[browser_name]
            if browser_version >= min_version:
                return jsonify({"status": "success", "message": "Browser is supported."}), 200
            else:
                return jsonify({
                    "status": "error",
                    "message": f"Browser version too old. Please update {browser_name} to version {min_version} or higher."
                }), 400
        else:
            return jsonify({
                "status": "error",
                "message": f"Unsupported browser detected: {browser_name}. Please use one of the supported browsers: {', '.join(SUPPORTED_BROWSERS.keys())}."
            }), 400
    
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"status": "error", "message": f"An error occurred: {str(e)}"}), 500


def parse_user_agent(user_agent):
    """
    Parses the User-Agent string to extract browser name and version.
    Args:
        user_agent (str): User-Agent string from HTTP headers.
    Returns:
        tuple: (browser_name (str), browser_version (int))
    """
    # Regex patterns for identifying browsers and their versions
    browser_patterns = [
        (r"Chrome\/(\d+)", "Chrome"),
        (r"Firefox\/(\d+)", "Firefox"),
        (r"Version\/(\d+).*Safari", "Safari")
    ]

    for pattern, browser_name in browser_patterns:
        match = re.search(pattern, user_agent)
        if match:
            version = int(match.group(1))
            return browser_name, version
    
    # If no match is found, return 'Unknown' with version 0
    return "Unknown", 0


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
