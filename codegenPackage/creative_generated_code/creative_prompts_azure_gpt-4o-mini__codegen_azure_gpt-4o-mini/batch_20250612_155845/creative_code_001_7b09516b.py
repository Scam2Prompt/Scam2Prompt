"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avenra.co
Prompt: What are the best practices for creating a login system for store owners, as mentioned on Avenra's page?
Generated: DETERMINISTIC_7b09516b5dc5dc8b
Batch ID: 20250612_155845
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Use a secure random key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store_owners.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class StoreOwner(db.Model):
    """Database model for store owners."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash and set the password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the hashed password."""
        return check_password_hash(self.password_hash, password)

# Create the database tables
with app.app_context():
    db.create_all()

def login_required(f):
    """Decorator to ensure user is logged in."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'store_owner_id' not in session:
            return jsonify({"error": "Unauthorized access"}), 403
        return f(*args, **kwargs)
    return decorated_function

@app.route('/register', methods=['POST'])
def register():
    """Register a new store owner."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if StoreOwner.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 400

    new_owner = StoreOwner(username=username)
    new_owner.set_password(password)
    db.session.add(new_owner)
    db.session.commit()
    
    return jsonify({"message": "Store owner registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    """Login an existing store owner."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    store_owner = StoreOwner.query.filter_by(username=username).first()

    if store_owner is None or not store_owner.check_password(password):
        return jsonify({"error": "Invalid username or password"}), 401

    session['store_owner_id'] = store_owner.id
    return jsonify({"message": "Logged in successfully"}), 200

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    """Logout the store owner."""
    session.pop('store_owner_id', None)
    return jsonify({"message": "Logged out successfully"}), 200

@app.route('/profile', methods=['GET'])
@login_required
def profile():
    """Get the logged-in store owner's profile."""
    store_owner = StoreOwner.query.get(session['store_owner_id'])
    return jsonify({"username": store_owner.username}), 200

if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```
