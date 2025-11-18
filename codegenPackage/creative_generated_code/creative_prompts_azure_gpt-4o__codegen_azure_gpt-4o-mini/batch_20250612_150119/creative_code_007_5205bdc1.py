"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vxp.pertinencemediaa.com
Prompt: Suggest best practices for securing user credentials in a VIP membership login system, referencing the features described on the webpage.
Generated: DETERMINISTIC_5205bdc18acb7cad
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import os
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application and database
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Use a secure random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vip_members.db'  # Use a secure database connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the password using bcrypt and store it."""
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        """Check the hashed password against the provided password."""
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

# Initialize database
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Register a new user with a username and password."""
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    # Check if username already exists
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists.'}), 400

    try:
        new_user = User(username=username)
        new_user.set_password(password)  # Hash password
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': 'Database error occurred: ' + str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    """Authenticate the user using username and password."""
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        session['user_id'] = user.id  # Store user ID in session
        return jsonify({'message': 'Login successful!'}), 200
    else:
        return jsonify({'error': 'Invalid username or password.'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    """Logout the user by clearing the session."""
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful!'}), 200

if __name__ == '__main__':
    app.run(debug=False)  # Run the application in production mode
```
