"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://urlz.fr
Prompt: Develop a REST API in Python that mimics the functionality of URLz.fr, allowing users to submit long URLs and retrieve shortened versions, with optional features like ad-free links.
Generated: DETERMINISTIC_e7921a1572ddc44d
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import string
import random
import os

app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///urls.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class URLMapping(db.Model):
    """Model to store URL mappings."""
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512), nullable=False, unique=True)
    short_url = db.Column(db.String(10), nullable=False, unique=True)
    ad_free = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<URLMapping {self.short_url} -> {self.original_url}>"

def generate_short_url(length=6):
    """Generate a random short URL string."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/shorten', methods=['POST'])
def shorten_url():
    """Endpoint to shorten a long URL."""
    data = request.get_json()
    
    # Check if the request contains the required fields
    if not data or 'url' not in data:
        return jsonify({'error': 'Invalid request, URL is required.'}), 400

    original_url = data['url']
    ad_free = data.get('ad_free', False)

    # Check if URL already exists
    existing_mapping = URLMapping.query.filter_by(original_url=original_url).first()
    if existing_mapping:
        return jsonify({
            'original_url': existing_mapping.original_url,
            'short_url': existing_mapping.short_url,
            'ad_free': existing_mapping.ad_free
        }), 200

    short_url = generate_short_url()
    new_mapping = URLMapping(original_url=original_url, short_url=short_url, ad_free=ad_free)

    try:
        db.session.add(new_mapping)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to shorten URL.'}), 500

    return jsonify({
        'original_url': original_url,
        'short_url': short_url,
        'ad_free': ad_free
    }), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
    """Redirect to the original URL based on the short URL."""
    mapping = URLMapping.query.filter_by(short_url=short_url).first()

    if mapping:
        return jsonify({
            'original_url': mapping.original_url,
            'ad_free': mapping.ad_free
        }), 302  # Use 302 for redirection
    else:
        return jsonify({'error': 'Short URL not found.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
To run this code, ensure you have the following Python packages installed:
- Flask
- Flask-SQLAlchemy

You can install them using:
```bash
pip install Flask Flask-SQLAlchemy
```

### Environment
Make sure to set the `DATABASE_URI` environment variable for the database connection if you're using something other than the default SQLite database.
