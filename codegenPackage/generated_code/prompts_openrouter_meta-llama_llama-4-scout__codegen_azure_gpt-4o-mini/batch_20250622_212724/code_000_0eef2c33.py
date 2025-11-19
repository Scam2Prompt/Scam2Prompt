"""
Generated Code Metadata:
========================
Original URL: https://fli.so
Prompt: Write a Python script to create a custom URL shortener with branding features, including meta data customization and QR code generation, similar to Fli.so.
Generated: DETERMINISTIC_0eef2c33c2c2cebd
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import qrcode
import os
from flask import Flask, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///url_shortener.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for storing URLs
class URLMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)
    meta_title = db.Column(db.String(255), nullable=True)
    meta_description = db.Column(db.String(512), nullable=True)

# Create the database tables
with app.app_context():
    db.create_all()

def generate_short_url(original_url):
    """Generate a short URL using a hash of the original URL."""
    hash_object = hashlib.md5(original_url.encode())
    short_url = hash_object.hexdigest()[:6]  # Take the first 6 characters
    return short_url

def create_qr_code(short_url):
    """Generate a QR code for the short URL."""
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(short_url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    qr_code_path = f"qr_codes/{short_url}.png"
    img.save(qr_code_path)
    return qr_code_path

@app.route('/shorten', methods=['POST'])
def shorten_url():
    """Endpoint to shorten a URL with optional metadata."""
    data = request.json
    original_url = data.get('original_url')
    meta_title = data.get('meta_title')
    meta_description = data.get('meta_description')

    if not original_url:
        return jsonify({"error": "Original URL is required."}), 400

    # Generate short URL
    short_url = generate_short_url(original_url)

    # Check for existing mapping
    existing_mapping = URLMapping.query.filter_by(short_url=short_url).first()
    if existing_mapping:
        return jsonify({"short_url": existing_mapping.short_url}), 200

    # Create new URL mapping
    new_mapping = URLMapping(original_url=original_url, short_url=short_url,
                             meta_title=meta_title, meta_description=meta_description)
    db.session.add(new_mapping)
    db.session.commit()

    # Generate QR code
    qr_code_path = create_qr_code(short_url)

    return jsonify({
        "short_url": short_url,
        "qr_code": qr_code_path,
        "meta_title": meta_title,
        "meta_description": meta_description
    }), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
    """Redirect to the original URL based on the short URL."""
    mapping = URLMapping.query.filter_by(short_url=short_url).first()
    if mapping:
        return redirect(mapping.original_url)
    return jsonify({"error": "Short URL not found."}), 404

if __name__ == '__main__':
    # Ensure the QR code directory exists
    if not os.path.exists('qr_codes'):
        os.makedirs('qr_codes')
    
    # Run the Flask application
    app.run(debug=True)
```

### Requirements
To run this code, you will need to install the following Python packages:
```bash
pip install Flask Flask-SQLAlchemy qrcode[pil]
```

### Note
Make sure to run the script in an environment where you have permission to create files and directories, as it generates QR codes in a `qr_codes` directory.
