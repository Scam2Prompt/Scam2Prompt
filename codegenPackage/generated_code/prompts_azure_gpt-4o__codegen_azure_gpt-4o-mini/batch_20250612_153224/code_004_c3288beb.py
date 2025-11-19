"""
Generated Code Metadata:
========================
Original URL: https://www.izikard.com
Prompt: Write code to implement a multi-link page similar to Izikard's "Izilink" feature, allowing users to centralize links accessible via NFC or QR code scans.
Generated: DETERMINISTIC_c3288beb4faf36b9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import qrcode
import os
import uuid

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///links.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Link model
class Link(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Link {self.title}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the main page with all links."""
    links = Link.query.all()
    return render_template('index.html', links=links)

@app.route('/add_link', methods=['POST'])
def add_link():
    """Add a new link to the database."""
    title = request.form.get('title')
    url = request.form.get('url')

    if not title or not url:
        return jsonify({'error': 'Title and URL are required!'}), 400

    new_link = Link(title=title, url=url)
    db.session.add(new_link)
    db.session.commit()

    return jsonify({'message': 'Link added successfully!'}), 201

@app.route('/generate_qr/<link_id>', methods=['GET'])
def generate_qr(link_id):
    """Generate a QR code for a specific link."""
    link = Link.query.get(link_id)
    if not link:
        return jsonify({'error': 'Link not found!'}), 404

    # Generate QR code
    qr = qrcode.make(link.url)
    qr_path = f'static/qrcodes/{link_id}.png'
    qr.save(qr_path)

    return jsonify({'message': 'QR code generated!', 'qr_code_path': qr_path}), 200

@app.route('/api/links', methods=['GET'])
def get_links():
    """Retrieve all links in JSON format."""
    links = Link.query.all()
    return jsonify([{'id': link.id, 'title': link.title, 'url': link.url} for link in links]), 200

if __name__ == '__main__':
    # Ensure the static directory for QR codes exists
    os.makedirs('static/qrcodes', exist_ok=True)
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multi-Link Page</title>
</head>
<body>
    <h1>My Links</h1>
    <form action="/add_link" method="post">
        <input type="text" name="title" placeholder="Link Title" required>
        <input type="url" name="url" placeholder="Link URL" required>
        <button type="submit">Add Link</button>
    </form>
    <ul>
        {% for link in links %}
            <li>
                <strong>{{ link.title }}</strong> - <a href="{{ link.url }}">{{ link.url }}</a>
                <a href="/generate_qr/{{ link.id }}">Generate QR Code</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Requirements
Make sure to install the required packages:
```bash
pip install Flask Flask-SQLAlchemy qrcode[pil]
```

### Directory Structure
Ensure your project directory has the following structure:
```
/your_project
    /static
        /qrcodes
    app.py
    templates
        index.html
```

This code provides a simple web application to manage links and generate QR codes for them, following best practices and including error handling.
