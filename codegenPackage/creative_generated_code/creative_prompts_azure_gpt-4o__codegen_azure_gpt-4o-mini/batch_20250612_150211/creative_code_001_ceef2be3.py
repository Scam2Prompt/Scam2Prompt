"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.app.pavonal.com
Prompt: Recommend libraries or APIs for securely handling user authentication using email or username, as seen on Pavonal's platform.
Generated: DETERMINISTIC_ceef2be331bd90ed
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for user authentication
import bcrypt  # For hashing passwords
from flask import Flask, request, jsonify  # For creating the API
from flask_sqlalchemy import SQLAlchemy  # For database management
from flask_migrate import Migrate  # For handling database migrations
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer  # For generating tokens
from werkzeug.exceptions import BadRequest, Unauthorized  # For error handling

# Initialize the Flask application
app = Flask(__name__)

# Configure the application with a secret key and database URI
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Use a secure key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use your preferred database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define User model
class User(db.Model):
    """User model for storing user information."""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the password for secure storage."""
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        """Check a provided password against the stored hash."""
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)

    def generate_token(self, expiration=600):
        """Generate a token for the user with a specified expiration in seconds."""
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'user_id': self.id}).decode('utf-8')

# Create database tables
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

# User registration route
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    if not data or 'email' not in data or 'username' not in data or 'password' not in data:
        raise BadRequest("Missing required fields: email, username, password")

    # Check if the user already exists
    if User.query.filter((User.email == data['email']) | (User.username == data['username'])).first():
        raise BadRequest("User with this email or username already exists")

    # Create new user
    new_user = User(email=data['email'], username=data['username'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully"}), 201

# User login route
@app.route('/login', methods=['POST'])
def login():
    """Login user and return a JWT token."""
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        raise BadRequest("Missing required fields: username, password")

    user = User.query.filter_by(username=data['username']).first()
    if not user or not user.check_password(data['password']):
        raise Unauthorized("Invalid username or password")

    token = user.generate_token()
    return jsonify({"token": token}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```
