"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanbet.info
Prompt: Suggest libraries or frameworks for developing a secure multi-device gaming experience for an online casino platform like BaxBet.
Generated: DETERMINISTIC_6b2e37e72de65908
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web application and gaming framework
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, jwt_optional, get_jwt_identity

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the database and JWT
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///casino.db'  # Use SQLite for simplicity; switch to production DB in deployment
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a strong secret key
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key_here'  # Change this to a strong JWT secret key

# Initialize database and JWT manager
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Database model for Users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Route for User Registration
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Error handling for missing fields
    if not username or not password:
        return jsonify({"msg": "Username and password are required"}), 400

    # Check if user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "User already exists"}), 400
    
    # Create a new user and hash the password
    new_user = User(username=username, password=generate_password_hash(password))
    
    # Add user to the database
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"msg": "User registered successfully"}), 201

# Route for User Login
@app.route('/login', methods=['POST'])
def login():
    """Log in a user and return a JWT token."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Error handling for missing fields
    if not username or not password:
        return jsonify({"msg": "Username and password are required"}), 400

    # Verify user credentials
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Bad username or password"}), 401

# Protected route example
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    """Access protected route with JWT token."""
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

# Error handler for JWT errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"msg": "Resource not found"}), 404

@app.errorhandler(Exception)
def handle_exception(e):
    """Handle exceptions and return JSON response."""
    return jsonify({"msg": str(e)}), 500

# Start the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True, host='0.0.0.0', port=5000)  # Run the application in debug mode
```

### Dependencies:
To run this code, you need the following Python packages:
```bash
pip install Flask Flask-SQLAlchemy Flask-JWT-Extended
```

**Note:** Make sure to replace `'your_secret_key_here'` and `'your_jwt_secret_key_here'` with actual strong secret keys in a production environment.
