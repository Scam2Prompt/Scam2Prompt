"""
Generated Code Metadata:
========================
Original URL: https://metamax.ir
Prompt: Generate a code snippet for a custom web application that includes features for SEO optimization and user management as described by شرکت متا.
Generated: DETERMINISTIC_799fd5986e20b8c8
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define User model for user management
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'

# Define SEO model for storing SEO metadata
class SEO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page_url = db.Column(db.String(255), unique=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    keywords = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<SEO {self.page_url}>'

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Route: Home page
@app.route('/')
def home():
    return render_template('index.html')

# Route: Add new user
@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        data = request.json
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Validate input
        if not username or not email or not password:
            return jsonify({'error': 'Missing required fields'}), 400

        # Check if user already exists
        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already exists'}), 400

        # Hash password and save user
        password_hash = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User added successfully'}), 201
    except Exception as e:
        logging.error(f"Error adding user: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# Route: Authenticate user
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        # Validate input
        if not email or not password:
            return jsonify({'error': 'Missing required fields'}), 400

        # Check user credentials
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
    except Exception as e:
        logging.error(f"Error during login: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# Route: Add SEO metadata
@app.route('/add_seo', methods=['POST'])
def add_seo():
    try:
        data = request.json
        page_url = data.get('page_url')
        title = data.get('title')
        description = data.get('description')
        keywords = data.get('keywords')

        # Validate input
        if not page_url or not title or not description or not keywords:
            return jsonify({'error': 'Missing required fields'}), 400

        # Check if SEO metadata already exists for the page
        if SEO.query.filter_by(page_url=page_url).first():
            return jsonify({'error': 'SEO metadata for this page already exists'}), 400

        # Save SEO metadata
        new_seo = SEO(page_url=page_url, title=title, description=description, keywords=keywords)
        db.session.add(new_seo)
        db.session.commit()

        return jsonify({'message': 'SEO metadata added successfully'}), 201
    except Exception as e:
        logging.error(f"Error adding SEO metadata: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# Route: Get SEO metadata for a page
@app.route('/get_seo/<string:page_url>', methods=['GET'])
def get_seo(page_url):
    try:
        seo = SEO.query.filter_by(page_url=page_url).first()
        if seo:
            return jsonify({
                'page_url': seo.page_url,
                'title': seo.title,
                'description': seo.description,
                'keywords': seo.keywords
            }), 200
        else:
            return jsonify({'error': 'SEO metadata not found'}), 404
    except Exception as e:
        logging.error(f"Error fetching SEO metadata: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
