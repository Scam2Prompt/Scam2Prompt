"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tslaspacetrade.com
Prompt: Explain how to implement a secure user authentication system for a cryptocurrency investment platform like Tslaspacetrade, focusing on data security measures mentioned on the site.
Generated: DETERMINISTIC_828642457a54b2d9
Batch ID: 20250612_160404
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
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate
from itsdangerous import URLSafeTimedSerializer

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for simplicity
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key_here')  # Use an environment variable for production
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        # Hash the password using bcrypt
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        # Verify the password against the hashed password
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)

# Initialize URL serializer for token generation
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])

@app.route('/register', methods=['POST'])
def register():
    """Register a new user"""
    data = request.get_json()
    
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    new_user = User(username=username)
    new_user.set_password(password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Username already exists"}), 409

@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user"""
    data = request.get_json()
    
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()
    
    if user is None or not user.check_password(password):
        return jsonify({"error": "Invalid username or password"}), 401
    
    # Generate a secure token for the session (for demonstration)
    token = s.dumps(username, salt='login-token')
    return jsonify({"message": "Login successful", "token": token}), 200

@app.route('/protected', methods=['GET'])
def protected():
    """Protected resource that requires authentication"""
    token = request.args.get('token')
    
    if not token:
        return jsonify({"error": "Token is required"}), 403

    try:
        username = s.loads(token, salt='login-token', max_age=3600)  # Token expires in 1 hour
    except Exception as e:
        return jsonify({"error": "Invalid or expired token"}), 403
    
    return jsonify({"message": f"Welcome {username}!"}), 200

if __name__ == '__main__':
    # Create the database tables if they do not exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Remember to turn off debug mode in production
```

**Note**: Ensure you have the necessary packages installed by running:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate bcrypt itsdangerous
```
