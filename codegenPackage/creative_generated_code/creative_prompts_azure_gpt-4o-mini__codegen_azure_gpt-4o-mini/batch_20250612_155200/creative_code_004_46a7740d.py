"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://url-shortener.me
Prompt: Explain how to implement multi-redirect functionality with the URL Shortener service described on url-shortener.me.
Generated: DETERMINISTIC_46a7740d446d21c7
Batch ID: 20250612_155200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, redirect, jsonify, abort
from urllib.parse import urlparse
from werkzeug.exceptions import BadRequest
import hashlib
import json

app = Flask(__name__)

# In-memory storage for URL mappings
url_mapping = {}
# In-memory storage for multi-redirect mappings
multi_redirect_mapping = {}


def is_valid_url(url):
    """Validate the given URL."""
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)


def generate_short_url(long_url):
    """Generate a short URL using a hash function."""
    # Use a hash of the URL to create a unique short URL
    return hashlib.md5(long_url.encode()).hexdigest()[:6]


@app.route('/shorten', methods=['POST'])
def shorten_url():
    """Shorten a given long URL."""
    data = request.json
    long_url = data.get('long_url')

    # Validate input
    if not long_url or not is_valid_url(long_url):
        raise BadRequest("Invalid URL provided.")

    short_url = generate_short_url(long_url)
    url_mapping[short_url] = long_url
    return jsonify({'short_url': short_url}), 201


@app.route('/multi-redirect', methods=['POST'])
def create_multi_redirect():
    """Create a multi-redirect from a short URL to multiple long URLs."""
    data = request.json
    short_url = data.get('short_url')
    long_urls = data.get('long_urls')

    # Validate input
    if not short_url or not long_urls or not isinstance(long_urls, list):
        raise BadRequest("Invalid input. 'short_url' and 'long_urls' are required.")

    # Store multi-redirect mapping
    multi_redirect_mapping[short_url] = long_urls
    return jsonify({'message': 'Multi-redirect created successfully.'}), 201


@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
    """Redirect to the long URL or handle multi-redirects if applicable."""
    if short_url in multi_redirect_mapping:
        # Handle multi-redirect
        long_urls = multi_redirect_mapping[short_url]
        return jsonify({'long_urls': long_urls}), 302

    long_url = url_mapping.get(short_url)
    if long_url:
        return redirect(long_url)
    
    # If the short URL does not exist, return a 404 error
    abort(404, description="Short URL not found.")


@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """Handle bad requests with a proper response."""
    return jsonify({'error': str(error)}), 400


@app.errorhandler(404)
def handle_not_found(error):
    """Handle not found errors."""
    return jsonify({'error': str(error)}), 404


if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
