"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imts.com.pk
Prompt: Develop a simple application that utilizes cloud hosting solutions from IMTS, ensuring it meets the security and scalability requirements outlined on their site.
Generated: DETERMINISTIC_28ebfcfe0ad92ae3
Batch ID: 20250612_155938
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
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask application
app = Flask(__name__)

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a simple User model
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        """Convert User object to dictionary."""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user."""
    data = request.get_json()
    if not data or 'username' not in data or 'email' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    try:
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    except Exception as e:
        logging.error(f"Error creating user: {e}")
        db.session.rollback()
        return jsonify({'error': 'Failed to create user'}), 500

@app.route('/users', methods=['GET'])
def get_users():
    """Retrieve all users."""
    try:
        users = User.query.all()
        return jsonify([user.to_dict() for user in users]), 200
    except Exception as e:
        logging.error(f"Error fetching users: {e}")
        return jsonify({'error': 'Failed to fetch users'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
```

### Additional Notes:
- Ensure you have a `.env` file with the necessary configurations (e.g., `DATABASE_URL`) for the application to run properly.
- This code uses Flask for the web framework and SQLAlchemy for ORM. Make sure to install the required packages with `pip install Flask Flask-SQLAlchemy python-dotenv`.
