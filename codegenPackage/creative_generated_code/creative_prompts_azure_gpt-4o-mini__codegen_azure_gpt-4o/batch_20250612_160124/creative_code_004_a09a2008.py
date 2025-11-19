"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadmerch.com
Prompt: What libraries can I use to manage user authentication for a company merchandise store?
Generated: DETERMINISTIC_a09a200802ada0cf
Batch ID: 20250612_160124
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example code snippet using Python and Flask with Flask-JWT-Extended for user authentication in a merchandise store.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# Initialize Flask app
app = Flask(__name__)

# Configure app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    username = db.Column(db.String(80), unique=True, nullable=False)  # Unique username
    password = db.Column(db.String(256), nullable=False)  # Hashed password

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Register endpoint
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']

        # Check if username already exists
        if User.query.filter_by(username=username).first():
            return jsonify({"message": "Username already exists"}), 400

        # Hash password and save to database
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']

        # Find user by username
        user = User.query.filter_by(username=username).first()
        if not user or not bcrypt.check_password_hash(user.password, password):
            return jsonify({"message": "Invalid credentials"}), 401

        # Create JWT token
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

# Protected endpoint (requires authentication)
@app.route('/merchandise', methods=['GET'])
@jwt_required()
def merchandise():
    try:
        current_user = get_jwt_identity()  # Get the identity of the logged-in user
        return jsonify({"message": f"Welcome {current_user}, here is the merchandise list!"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

### Key Points:
1. Install the required libraries before running this code:
   ```
   pip install flask flask-sqlalchemy flask-bcrypt flask-jwt-extended
   ```
2. Replace `'your_secret_key'` in `app.config['JWT_SECRET_KEY']` with a secure key for production.
3. Use HTTPS in production to secure the communication.
4. Consider additional measures such as rate limiting and logging for production deployment.
