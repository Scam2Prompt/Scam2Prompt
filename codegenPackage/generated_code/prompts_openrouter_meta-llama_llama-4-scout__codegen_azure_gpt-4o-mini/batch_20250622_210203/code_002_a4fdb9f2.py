"""
Generated Code Metadata:
========================
Original URL: https://icrossingappxyz.com
Prompt: Generate a Python script to automate the process of registering users and verifying their identities through a QR code scan, as described in the "Identitas Kependudukan Digital" app.
Generated: DETERMINISTIC_a4fdb9f2c54355f8
Batch ID: 20250622_210203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
import sqlite3
import os
import uuid
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# User model
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    qr_code = db.Column(db.String(255), nullable=False)

    def __init__(self, username, password):
        self.id = str(uuid.uuid4())
        self.username = username
        self.password = generate_password_hash(password)
        self.qr_code = self.generate_qr_code()

    def generate_qr_code(self):
        """Generate a QR code for the user."""
        qr_data = f"{self.id}:{self.username}"
        qr_img = qrcode.make(qr_data)
        qr_code_path = f"qr_codes/{self.id}.png"
        qr_img.save(qr_code_path)
        return qr_code_path

# User schema for serialization
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Create the database and tables
@app.before_first_request
def create_tables():
    if not os.path.exists('qr_codes'):
        os.makedirs('qr_codes')
    db.create_all()

# Register a new user
@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user and generate a QR code."""
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists."}), 400

    new_user = User(username, password)
    db.session.add(new_user)
    db.session.commit()

    return UserSchema().jsonify(new_user), 201

# Verify user identity through QR code
@app.route('/verify', methods=['POST'])
def verify_user():
    """Verify user identity using QR code data."""
    qr_data = request.json.get('qr_data')

    if not qr_data:
        return jsonify({"error": "QR data is required."}), 400

    try:
        user_id, username = qr_data.split(':')
        user = User.query.get(user_id)

        if user and user.username == username:
            return jsonify({"message": "User verified successfully."}), 200
        else:
            return jsonify({"error": "Invalid QR code."}), 401
    except ValueError:
        return jsonify({"error": "Invalid QR data format."}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install the required packages before running the script:
```bash
pip install Flask Flask-SQLAlchemy Flask-Marshmallow qrcode[pil] Werkzeug
```
