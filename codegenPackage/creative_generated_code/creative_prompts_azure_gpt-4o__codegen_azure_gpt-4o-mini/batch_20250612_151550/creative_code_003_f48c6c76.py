"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fraudbinance.com
Prompt: Provide code examples for creating a user login and registration system tailored for an online casino platform like DewaCasino.
Generated: DETERMINISTIC_f48c6c76959b2ca6
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
CORS(app)

# Configuration for database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Example with SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this in production

# Initialize database and migrations
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check if the provided password matches the stored hash."""
        return check_password_hash(self.password_hash, password)

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    # Check if the user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists.'}), 400

    # Create new user and save to the database
    new_user = User(username=username)
    new_user.set_password(password)
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully.'}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    """Log a user in."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    user = User.query.filter_by(username=username).first()
    
    if user and user.check_password(password):
        # Create a session for the user
        session['user_id'] = user.id
        return jsonify({'message': 'Login successful.'}), 200

    return jsonify({'error': 'Invalid username or password.'}), 401

# Route for user logout
@app.route('/logout', methods=['POST'])
def logout():
    """Log a user out."""
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful.'}), 200

# Error handling for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle unexpected exceptions."""
    return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()

    # Run the application
    app.run(debug=True)  # Set debug=False in production
```

### Notes:
- Make sure to set the `SECRET_KEY` to a secure value in production.
- For a real application, consider using a more robust database than SQLite.
- Ensure to implement appropriate logging and monitoring for production deployments.
