"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fli.so
Prompt: Provide a step-by-step guide to self-hosting a cloud-based link management system with features like those offered in Fli.so's "Basic" plan.
Generated: DETERMINISTIC_a95cd7effaa62ce9
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import uuid

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///links.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Link model
class Link(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    original_url = db.Column(db.String(2083), nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return f'<Link {self.short_url}>'

# Route to create a new short link
@app.route('/shorten', methods=['POST'])
def shorten_link():
    try:
        original_url = request.json.get('url')
        if not original_url:
            return jsonify({'error': 'No URL provided'}), 400
        
        # Generate a short URL
        short_url = str(uuid.uuid4())[:6]  # Shorten to 6 characters

        # Create a new link instance
        new_link = Link(original_url=original_url, short_url=short_url)
        db.session.add(new_link)
        db.session.commit()

        return jsonify({'short_url': url_for('redirect_link', short_url=short_url, _external=True)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to redirect to the original URL
@app.route('/<short_url>')
def redirect_link(short_url):
    link = Link.query.filter_by(short_url=short_url).first()
    if link:
        return redirect(link.original_url)
    return jsonify({'error': 'Link not found'}), 404

# Route to display all links
@app.route('/links', methods=['GET'])
def get_links():
    try:
        links = Link.query.all()
        return jsonify([{ 'short_url': link.short_url, 'original_url': link.original_url } for link in links]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'error': 'Page not found'}), 404

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```

### Instructions to Deploy:
1. **Set up your environment**: Ensure you have Python and pip installed. Create a virtual environment and install Flask and SQLAlchemy:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install Flask Flask-SQLAlchemy Flask-Migrate
   ```

2. **Configure your database**: You can set the `DATABASE_URL` environment variable for your preferred database or use the default SQLite database.

3. **Run the application**: Execute the script to start your link management system:
   ```bash
   python your_script_name.py
   ```

4. **Test the endpoints**: Use tools like Postman or cURL to test the `/shorten`, `/links`, and `/<short_url>` endpoints.

5. **Consider security and performance**: Look into securing your application by setting up HTTPS and considering production-ready configurations for Flask, such as using a WSGI server.
