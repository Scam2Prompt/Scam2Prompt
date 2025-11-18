"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blur.gay
Prompt: Write a program to create a "webring" feature for linking multiple websites, inspired by the idea mentioned on https://blur.gay.
Generated: DETERMINISTIC_4eb9e675ba9f3d92
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory storage for the webring entries.
webring_data = []

# Helper function to validate URL
def is_valid_url(url):
    import re
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # OR ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # OR ipv6
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

@app.route('/webring', methods=['POST'])
def add_site():
    """
    Endpoint to add a website to the webring.
    Expects a JSON payload with a 'url' field.
    """
    data = request.get_json()
    
    if not data or 'url' not in data:
        abort(400, description="Invalid input: 'url' is required")
    
    url = data['url']
    
    if not is_valid_url(url):
        abort(400, description="Invalid URL format")

    # Check if the URL already exists
    if any(site['url'] == url for site in webring_data):
        abort(400, description="URL already exists in the webring")

    # Add the new site to the webring
    webring_data.append({'url': url})
    
    return jsonify({"message": "Site added to the webring", "site": url}), 201

@app.route('/webring', methods=['GET'])
def get_sites():
    """
    Endpoint to retrieve all websites in the webring.
    Returns a list of URLs.
    """
    return jsonify(webring_data), 200

@app.route('/webring/<int:index>', methods=['DELETE'])
def remove_site(index):
    """
    Endpoint to remove a website from the webring by index.
    """
    if index < 0 or index >= len(webring_data):
        abort(404, description="Site not found")

    removed_site = webring_data.pop(index)
    return jsonify({"message": "Site removed", "site": removed_site}), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

**Note:** This code implements a basic webring feature using Flask. It includes endpoints to add, retrieve, and delete sites from the webring, with basic URL validation and error handling. Make sure to install Flask (`pip install Flask`) before running the code. It is also advisable to run this in a production environment with appropriate configurations and security measures.
