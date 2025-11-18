"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test.metamask-phishing.io
Prompt: Create a web application that replicates the phishing detection demo functionality described on the MetaMask Phishing Test Page.
Generated: DETERMINISTIC_5401f9f61e3acc35
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing the required libraries
from flask import Flask, request, jsonify, render_template
import requests
import re

# Initialize the Flask application
app = Flask(__name__)

# Function to check if a URL is potentially phishing
def is_phishing_url(url):
    """
    Checks if the provided URL matches common phishing patterns.

    Parameters:
        url (str): The URL to be checked.

    Returns:
        bool: True if the URL is likely phishing, False otherwise.
    """
    # Basic checks for phishing indicators
    phishing_indicators = [
        r'\blogin\b',         # Common phishing keyword
        r'\bsecure\b',        # Common phishing keyword
        r'\bverify\b',        # Common phishing keyword
        r'\baccount\b',       # Common phishing keyword
        r'\bclick\b',         # Common phishing keyword
        r'[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}',  # IP address
        r'\b\.tk\b',          # Free domain service
        r'\b\.ga\b',          # Free domain service
        r'\b\.gq\b',          # Free domain service
    ]

    # Compile the regex patterns
    patterns = [re.compile(indicator) for indicator in phishing_indicators]

    # Check for indicators in the URL
    for pattern in patterns:
        if pattern.search(url):
            return True
    return False

# Route for the main page
@app.route('/')
def home():
    """
    Renders the home page of the web application.
    """
    return render_template('index.html')

# Route for checking the URL
@app.route('/check-url', methods=['POST'])
def check_url():
    """
    Endpoint to check the submitted URL for phishing indicators.

    Returns:
        JSON response with the result of the check.
    """
    data = request.json
    url = data.get('url', '')

    # Validate the URL format
    if not url or not re.match(r'https?://[^\s]+', url):
        return jsonify({'error': 'Invalid URL format'}), 400

    # Check if the URL is a phishing URL
    result = is_phishing_url(url)

    return jsonify({'url': url, 'is_phishing': result})

# Error handling for 404 - Not Found
@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 errors.

    Returns:
        JSON response indicating that the resource was not found.
    """
    return jsonify({'error': 'Resource not found'}), 404

# Error handling for other server errors
@app.errorhandler(500)
def internal_error(error):
    """
    Handles 500 errors.

    Returns:
        JSON response indicating an internal server error.
    """
    return jsonify({'error': 'Internal server error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```

**HTML Template (index.html)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phishing Detection</title>
    <script>
        async function checkUrl() {
            const urlInput = document.getElementById('urlInput').value;
            const response = await fetch('/check-url', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ url: urlInput })
            });

            const result = await response.json();
            const resultDiv = document.getElementById('result');

            if (response.ok) {
                resultDiv.innerText = `The URL "${result.url}" is ${result.is_phishing ? 'likely a phishing site.' : 'safe.'}`;
            } else {
                resultDiv.innerText = `Error: ${result.error}`;
            }
        }
    </script>
</head>
<body>
    <h1>Phishing Detection Tool</h1>
    <input type="text" id="urlInput" placeholder="Enter URL to check" />
    <button onclick="checkUrl()">Check URL</button>
    <div id="result"></div>
</body>
</html>
```

Make sure to install Flask with `pip install Flask` before running the application. Save the HTML template as `index.html` in a folder named `templates` in the same directory where the Flask app script is located.
