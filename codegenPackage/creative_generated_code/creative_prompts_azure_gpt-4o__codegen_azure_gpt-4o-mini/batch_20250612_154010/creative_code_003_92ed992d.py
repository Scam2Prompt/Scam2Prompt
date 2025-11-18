"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fli.so
Prompt: How can I implement custom domain branding for shortened URLs, similar to the branding features described on Fli.so? Provide code examples.
Generated: DETERMINISTIC_92ed992d934fc527
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import urlparse
import string
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for storing URL mappings
class URLMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)
    custom_domain = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<URLMapping(original_url='{self.original_url}', short_url='{self.short_url}', custom_domain='{self.custom_domain}')>"

# Function to generate a random short code
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a shortened URL with optional custom domain
@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json
    original_url = data.get('url')
    custom_domain = data.get('custom_domain')

    # Validate original URL
    if not original_url or not is_valid_url(original_url):
        return jsonify({"error": "Invalid original URL"}), 400

    # Generate a unique short code
    short_code = generate_short_code()
    while URLMapping.query.filter_by(short_url=short_code).first():
        short_code = generate_short_code()

    # Create new URL mapping
    new_mapping = URLMapping(original_url=original_url, short_url=short_code, custom_domain=custom_domain)
    db.session.add(new_mapping)
    db.session.commit()

    return jsonify({"short_url": f"{custom_domain or request.host}/{short_code}"}), 201

# Function to validate the URL
def is_valid_url(url):
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])  # Check scheme and netloc

# Endpoint to redirect to the original URL
@app.route('/<short_code>', methods=['GET'])
def redirect_to_url(short_code):
    mapping = URLMapping.query.filter_by(short_url=short_code).first()
    
    if mapping:
        return redirect(mapping.original_url, code=302)
    
    return jsonify({"error": "Short URL not found"}), 404

# Error handler for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This code uses Flask and SQLAlchemy for a simple URL shortening service.
- The `shorten_url` endpoint accepts a JSON payload containing a URL and an optional custom domain.
- The `redirect_to_url` endpoint redirects users to the original URL when visiting the shortened link.
- Error handling is included for various scenarios such as invalid URLs and non-existent short URLs.
