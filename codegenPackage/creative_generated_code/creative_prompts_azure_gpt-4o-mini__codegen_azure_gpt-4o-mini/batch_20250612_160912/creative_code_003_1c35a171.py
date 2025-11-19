"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://niftin.info
Prompt: What libraries or APIs would you recommend for managing user accounts in a web app like Niftin?
Generated: DETERMINISTIC_1c35a1715b3b7220
Batch ID: 20250612_160912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database and other settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change to a more secure key in production

# Initialize the database, bcrypt, and JWT manager
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# User schema for validation
class UserSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Register a new user
@app.route('/register', methods=['POST'])
def register():
    try:
        # Validate and deserialize input
        user_schema = UserSchema()
        user_data = user_schema.load(request.json)

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(user_data['password']).decode('utf-8')

        # Create a new user instance
        new_user = User(username=user_data['username'], email=user_data['email'], password=hashed_password)

        # Add user to the database
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully."}), 201
    except ValidationError as e:
        return jsonify(e.messages), 400
    except Exception as e:
        return jsonify({"message": "User registration failed.", "error": str(e)}), 500

# User login
@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.json.get('username')
        password = request.json.get('password')

        # Fetch the user by username
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            # Create JWT token for the user
            access_token = create_access_token(identity={'username': user.username})
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"message": "Invalid credentials."}), 401
    except Exception as e:
        return jsonify({"message": "Login failed.", "error": str(e)}), 500

# Protected route example
@app.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    return jsonify(current_user), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
