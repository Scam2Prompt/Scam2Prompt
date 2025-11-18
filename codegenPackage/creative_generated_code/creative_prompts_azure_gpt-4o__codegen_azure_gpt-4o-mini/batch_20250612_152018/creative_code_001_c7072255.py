"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flarenet.works.app
Prompt: Recommend libraries or APIs for implementing a secure login system with Space ID and Login ID fields, similar to the functionality described on "サスケWorks."
Generated: DETERMINISTIC_c707225516cece8d
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for secure login system
import bcrypt
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    space_id = db.Column(db.String(80), unique=True, nullable=False)
    login_id = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.login_id}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if not data or not all(key in data for key in ('space_id', 'login_id', 'password')):
        return jsonify({'message': 'Invalid input. Please provide space_id, login_id, and password.'}), 400

    # Hash the password for security
    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

    new_user = User(space_id=data['space_id'], login_id=data['login_id'], password_hash=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'User with this space_id or login_id already exists.'}), 409

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or not all(key in data for key in ('login_id', 'password')):
        return jsonify({'message': 'Invalid input. Please provide login_id and password.'}), 400

    user = User.query.filter_by(login_id=data['login_id']).first()
    if user and bcrypt.checkpw(data['password'].encode('utf-8'), user.password_hash):
        return jsonify({'message': 'Login successful!'}), 200
    else:
        return jsonify({'message': 'Invalid login_id or password.'}), 401

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
