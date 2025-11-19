"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://restaking-traderjoe.app
Prompt: Can you provide a code example that demonstrates how to validate user input to protect against phishing in a web application?
Generated: DETERMINISTIC_740af4e1a284bd4a
Batch ID: 20250612_162531
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

# Regular expression to validate URLs (basic structure)
URL_REGEX = re.compile(
    r'^(https?:\/\/)?'              # Optional scheme (http or https)
    r'(([a-zA-Z0-9_-]+\.)+[a-zA-Z]{2,})'  # Domain name
    r'(\/[a-zA-Z0-9._~:/?#[\]@!$&\'()*+,;=%-]*)?$'  # Path, query, fragment (optional)
)

# A list of allowed domains (whitelist) for added security
ALLOWED_DOMAINS = {"example.com", "trusted-site.com", "mywebsite.org"}

def is_safe_url(url):
    """
    Validate the URL and check if it belongs to an allowed domain.
    :param url: The user-provided URL.
    :return: True if URL is valid and safe, False otherwise.
    """
    if not url:
        return False  # URL cannot be empty
    
    # Check if the URL matches the regex
    match = URL_REGEX.match(url)
    if not match:
        return False
    
    # Extract the domain from the URL
    domain = match.group(2)
    if not domain or domain.lower() not in ALLOWED_DOMAINS:
        return False  # Domain is not in the whitelist
    
    return True

@app.route('/submit-url', methods=['POST'])
def submit_url():
    """
    Endpoint to handle user-provided URLs and validate them.
    """
    try:
        # Extract the URL from the request body
        data = request.get_json()
        if not data or 'url' not in data:
            return jsonify({"error": "URL is required"}), 400
        
        url = data['url']
        
        # Validate the URL
        if is_safe_url(url):
            return jsonify({"message": "URL is safe"}), 200
        else:
            return jsonify({"error": "URL is invalid or unsafe"}), 400
    
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
