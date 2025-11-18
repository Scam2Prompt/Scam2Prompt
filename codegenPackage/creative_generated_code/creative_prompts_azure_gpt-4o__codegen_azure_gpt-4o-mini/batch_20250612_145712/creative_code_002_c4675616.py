"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microlab.world
Prompt: Recommend libraries or APIs to securely manage user authentication and password recovery for a platform similar to MicroLab.
Generated: DETERMINISTIC_c4675616d1143623
Batch ID: 20250612_145712
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
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, jwt_refresh_token_required
from sqlalchemy.exc import IntegrityError

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change this in production
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the password using Bcrypt."""
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Check a hashed password against a given password."""
        return bcrypt.check_password_hash(self.password_hash, password)

# Initialize the database
with app.app_context():
    db.create_all()

# API endpoint for user registration
@app.route('/register', methods=['POST'])
def register():
    """Endpoint for user registration."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "Username and password are required"}), 400

    new_user = User(username=username)
    new_user.set_password(password)

    try:
        db.session.add(new_user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"msg": "User already exists"}), 409

    return jsonify({"msg": "User registered successfully"}), 201

# API endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    """Endpoint for user login."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Bad username or password"}), 401

# API endpoint for password recovery (dummy implementation)
@app.route('/recover', methods=['POST'])
def recover_password():
    """Endpoint for password recovery."""
    data = request.get_json()
    username = data.get('username')

    user = User.query.filter_by(username=username).first()
    if user:
        # Implement password recovery logic (e.g., send an email)
        return jsonify({"msg": "Recovery instructions sent"}), 200

    return jsonify({"msg": "User not found"}), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to replace `'your_secret_key'` with a strong, unique key before deploying in a production environment. Also, the password recovery endpoint is a placeholder; you should implement actual recovery logic tailored to your application's needs.
