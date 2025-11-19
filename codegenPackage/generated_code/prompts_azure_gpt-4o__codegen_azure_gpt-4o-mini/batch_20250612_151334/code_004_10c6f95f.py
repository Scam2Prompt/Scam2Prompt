"""
Generated Code Metadata:
========================
Original URL: https://usdtclaim.com
Prompt: Provide a solution for securely managing user accounts on a cryptocurrency faucet platform, ensuring compliance with rules against multiple accounts, proxy usage, and public computer access as outlined by USDT Claim.
Generated: DETERMINISTIC_10c6f95fe7e31830
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import os
import re
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///faucet.db'
app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    ip_address = db.Column(db.String(45), nullable=False)  # IPv6 support
    is_active = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()

# Initialize the database
with app.app_context():
    db.create_all()

# Function to validate IP address
def is_valid_ip(ip):
    ip_regex = re.compile(
        r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$|'
        r'^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$|'
        r'^(?:[0-9a-fA-F]{1,4}:){1,7}:$|'
        r'^(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|'
        r'^(?:[0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|'
        r'^(?:[0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|'
        r'^(?:[0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|'
        r'^(?:[0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|'
        r'^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6}|:)$|'
        r'^:((:[0-9a-fA-F]{1,4}){1,7}|:)$|'
        r'^fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|'
        r'^::(ffff(:0{1,4}){0,1}:){0,1}'
        r'((25[0-5]|(2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}'
        r'(25[0-5]|(2[0-4][0-9]|[01]?[0-9][0-9]?))|'
        r'([0-9a-fA-F]{1,4}:){1,4}:|'
        r'([0-9a-fA-F]{1,4}:){1,5}:([0-9a-fA-F]{1,4}:){1,4}|'
        r'([0-9a-fA-F]{1,4}:){1,6}:([0-9a-fA-F]{1,4}:){1,3}|'
        r'([0-9a-fA-F]{1,4}:){1,7}:([0-9a-fA-F]{1,4}:){1,2}|'
        r'([0-9a-fA-F]{1,4}:){1,8}:([0-9a-fA-F]{1,4}:){1,1}|'
        r'([0-9a-fA-F]{1,4}:){1,9}:([0-9a-fA-F]{1,4}:){1,0})$'
    )
    return ip_regex.match(ip) is not None

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    ip_address = request.remote_addr

    if not username or not password or not is_valid_ip(ip_address):
        return jsonify({"error": "Invalid input or IP address."}), 400

    new_user = User(username=username, ip_address=ip_address)
    new_user.set_password(password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully."}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Username already exists."}), 409

# Route to login a user
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    ip_address = request.remote_addr

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        session['user_id'] = user.id
        return jsonify({"message": "Login successful."}), 200
    return jsonify({"error": "Invalid username or password."}), 401

# Route to logout a user
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logout successful."}), 200

# Route to check user status
@app.route('/status', methods=['GET'])
def status():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return jsonify({"username": user.username, "active": user.is_active}), 200
    return jsonify({"error": "User not logged in."}), 401

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
