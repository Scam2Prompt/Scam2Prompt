"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linktre.me
Prompt: Write code to implement a verification badge system for user profiles, similar to the "selo de autenticidade" feature described on "Bio.links."
Generated: DETERMINISTIC_c4f5a5f94d6dbbf4
Batch ID: 20250612_155000
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
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import os

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    """Model representing a user in the system."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    is_verified = db.Column(db.Boolean, default=False)
    verification_date = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<User {self.username}>"

@app.before_first_request
def create_tables():
    """Create the database tables before the first request."""
    db.create_all()

@app.route('/register', methods=['POST'])
def register_user():
    """Endpoint to register a new user."""
    try:
        username = request.json.get('username')
        if not username:
            return jsonify({'error': 'Username is required'}), 400

        new_user = User(username=username)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/verify/<int:user_id>', methods=['POST'])
def verify_user(user_id):
    """Endpoint to set a user as verified."""
    try:
        user = User.query.get_or_404(user_id)
        user.is_verified = True
        user.verification_date = datetime.utcnow()
        db.session.commit()
        return jsonify({'message': 'User verified successfully'}), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/users', methods=['GET'])
def get_users():
    """Endpoint to retrieve all users with their verification status."""
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'is_verified': user.is_verified} for user in users]), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=os.environ.get('DEBUG', default=True))
```

### Instructions to Run the Code
1. Ensure you have Python and Flask installed. You can install Flask and SQLAlchemy using pip:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```
2. Save the code in a file, e.g., `app.py`.
3. Run the application:
   ```bash
   python app.py
   ```
4. Use a tool like Postman or curl to send requests to the endpoints:
   - Register a user: `POST /register` with JSON body `{"username": "your_username"}`
   - Verify a user: `POST /verify/{user_id}`
   - Get all users: `GET /users`
