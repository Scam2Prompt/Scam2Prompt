"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xionburnt.app
Prompt: What steps should I take to secure my website against phishing, based on the warning message from Cloudflare regarding xionburnt.app?
Generated: DETERMINISTIC_3bcece5c57639339
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Sample configuration for a secure application
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')
    DEBUG = False
    TESTING = False

app.config.from_object(Config)

# Middleware to check for phishing attempts
@app.before_request
def check_phishing():
    # List of known phishing domains
    phishing_domains = ['example.com', 'malicious.com']
    referer = request.headers.get('Referer')

    if referer:
        for domain in phishing_domains:
            if domain in referer:
                logging.warning(f'Phishing attempt detected from domain: {referer}')
                return jsonify({'error': 'Access denied due to suspected phishing attempt'}), 403

@app.route('/secure-endpoint', methods=['GET'])
def secure_endpoint():
    return jsonify({'message': 'This is a secure endpoint.'})

# Function to handle errors gracefully
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    logging.error(f'Internal error: {error}')
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=5000)
```
