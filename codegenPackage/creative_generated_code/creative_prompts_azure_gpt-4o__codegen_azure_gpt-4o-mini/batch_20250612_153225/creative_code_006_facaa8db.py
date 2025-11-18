"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hooshmand-teb.ir
Prompt: Write code to implement a user authentication system for a smart healthcare portal, ensuring secure access for patients and medical staff, inspired by Hooshmand Teb's portal system.
Generated: DETERMINISTIC_facaa8db892b52f8
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from itsdangerous import URLSafeTimedSerializer
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask application and database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthcare_portal.db'  # Example SQLite DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'patient' or 'staff'

    def set_password(self, password):
        """Hash the password and store it."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check if the provided password matches the stored hash."""
        return check_password_hash(self.password_hash, password)

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    # Validate input
    if not username or not password or role not in ['patient', 'staff']:
        return jsonify({'error': 'Invalid input'}), 400

    # Check if username already exists
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 409

    # Create new user
    new_user = User(username=username, role=role)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    """Authenticate user and create session."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({'error': 'Invalid input'}), 400

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['user_id'] = user.id
        session['role'] = user.role
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

# User logout endpoint
@app.route('/logout', methods=['POST'])
def logout():
    """Log out the user."""
    session.pop('user_id', None)
    session.pop('role', None)
    return jsonify({'message': 'Logout successful'}), 200

# Protected route example
@app.route('/protected', methods=['GET'])
def protected():
    """An example of a protected route for authenticated users."""
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized access'}), 403

    return jsonify({'message': 'Welcome to the protected route!'}), 200

# Running the app
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Set debug to False in production
```
