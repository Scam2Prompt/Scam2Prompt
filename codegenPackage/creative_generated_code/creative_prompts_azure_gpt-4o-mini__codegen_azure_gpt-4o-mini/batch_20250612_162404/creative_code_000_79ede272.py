"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mind-vise.info
Prompt: Generate a code snippet for a trading application that allows users to register, login, and manage their accounts on the Mind Vise platform.
Generated: DETERMINISTIC_79ede27291036a5b
Batch ID: 20250612_162404
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
from werkzeug.security import generate_password_hash, check_password_hash
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, jwt_refresh_token_required

# Initialize the application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mind_vise.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this in production

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# User schema for serialization
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Create a new user
@app.route('/register', methods=['POST'])
def register():
    try:
        username = request.json.get('username')
        password = request.json.get('password')

        # Validate input
        if not username or not password:
            return jsonify({"msg": "Username and password are required."}), 400

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Create a new user
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"msg": "User registered successfully."}), 201
    except Exception as e:
        return jsonify({"msg": str(e)}), 500

# User login
@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.json.get('username')
        password = request.json.get('password')

        # Validate input
        if not username or not password:
            return jsonify({"msg": "Username and password are required."}), 400

        # Find the user
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token), 200

        return jsonify({"msg": "Invalid credentials."}), 401
    except Exception as e:
        return jsonify({"msg": str(e)}), 500

# Manage user account (example endpoint)
@app.route('/account', methods=['GET'])
@jwt_required()
def account():
    try:
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        user_schema = UserSchema()
        return user_schema.dump(user), 200
    except Exception as e:
        return jsonify({"msg": str(e)}), 500

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Set to False in production
```

### Note:
- Replace `'your_jwt_secret_key'` with a strong secret key in production.
- This code uses Flask, SQLAlchemy, Marshmallow, and Flask-JWT-Extended. Ensure these packages are installed in your environment.
- Use a production-ready database instead of SQLite.
