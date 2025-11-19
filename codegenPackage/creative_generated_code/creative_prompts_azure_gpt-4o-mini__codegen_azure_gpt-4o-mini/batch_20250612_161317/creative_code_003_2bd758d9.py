"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ccbase.net
Prompt: How can I create a phishing warning system for a web application like the one mentioned on CCBase.net?
Generated: DETERMINISTIC_2bd758d92b52a268
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, request, jsonify, render_template
import logging

# Initialize Flask application
app = Flask(__name__)

# Enable logging for warnings and errors
logging.basicConfig(level=logging.WARNING)

# List of known phishing domains (In production, use a more dynamic and comprehensive list)
PHISHING_DOMAINS = {'example-phishing.com', 'malicious-site.net'}

def is_phishing_url(url):
    """
    Check if the given URL is in the list of known phishing domains.
    
    :param url: The URL to be checked.
    :return: True if the URL is a phishing site, False otherwise.
    """
    domain = url.split('/')[2]  # Extract domain from URL
    return domain in PHISHING_DOMAINS

@app.route('/', methods=['GET'])
def home():
    """
    Render the home page.
    """
    return render_template('index.html')

@app.route('/check-url', methods=['POST'])
def check_url():
    """
    Check the provided URL for phishing attempts.
    
    :return: JSON response indicating whether the URL is safe or phishing.
    """
    try:
        # Get the URL from the form data
        data = request.json
        url = data.get('url', '').strip()

        if not url:
            return jsonify({'error': 'URL is required'}), 400

        # Check if the URL is a phishing URL
        if is_phishing_url(url):
            return jsonify({'status': 'phishing', 'message': 'This URL is a known phishing site.'}), 200
        else:
            return jsonify({'status': 'safe', 'message': 'This URL is safe to visit.'}), 200

    except Exception as e:
        logging.error(f"Error checking URL: {e}")
        return jsonify({'error': 'An error occurred while checking the URL.'}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=False)
```

### HTML Template (`index.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phishing Warning System</title>
</head>
<body>
    <h1>Phishing Warning System</h1>
    <form id="url-form">
        <label for="url">Enter a URL to check:</label>
        <input type="text" id="url" name="url" required>
        <button type="submit">Check URL</button>
    </form>
    <div id="result"></div>
    
    <script>
        document.getElementById('url-form').onsubmit = async function (event) {
            event.preventDefault(); // Prevent default form submission
            const url = document.getElementById('url').value;
            const response = await fetch('/check-url', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({url: url})
            });

            const result = await response.json();
            document.getElementById('result').textContent = result.message || result.error;
        };
    </script>
</body>
</html>
```

### Notes
- This code includes a simple web application that checks if a URL belongs to a known phishing domain.
- The list of phishing domains is for demonstration purposes; in production, it should be sourced from a reliable database.
- The `index.html` file should be placed in a folder named `templates` relative to the Python script for Flask to render it correctly.
