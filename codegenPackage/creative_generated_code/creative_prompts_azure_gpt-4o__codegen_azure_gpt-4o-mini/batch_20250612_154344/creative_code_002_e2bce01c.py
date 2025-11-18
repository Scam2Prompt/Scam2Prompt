"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jasmynetwork.org
Prompt: Generate Python code to build a user login system for a content discovery app, referencing features like personalized feeds and connecting with like-minded members as described on the Stumble! ® website.
Generated: DETERMINISTIC_e2bce01cb6b8c8ad
Batch ID: 20250612_154344
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
from flask_marshmallow import Marshmallow
from functools import wraps

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong key
db = SQLAlchemy(app)
ma = Marshmallow(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)

# User schema for serialization
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Initialize database
with app.app_context():
    db.create_all()

# Decorator for authentication
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({"message": "Login required"}), 401
        return f(*args, **kwargs)
    return decorated_function

# User registration route
@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    # Check if user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists"}), 400

    # Hash password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Create new user
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# User login route
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()
    
    # Check if user exists and password is correct
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password):
        session['user_id'] = user.id
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

# User logout route
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logout successful"}), 200

# Get personalized feed route for the logged-in user
@app.route('/feed', methods=['GET'])
@login_required
def get_feed():
    user_id = session['user_id']
    # Placeholder for feed generation logic
    # For example: fetch content based on user interests, preferences, etc.
    feed = {
        "message": "This is your personalized feed!",
        "user_id": user_id
    }
    return jsonify(feed), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

**Note**: The code above requires the following packages to be installed: Flask, Flask-SQLAlchemy, Flask-Marshmallow, and bcrypt. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy Flask-Marshmallow bcrypt
``` 

Make sure to replace `your_secret_key` with an actual secure key for production use.
