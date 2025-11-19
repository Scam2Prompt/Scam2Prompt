"""
Generated Code Metadata:
========================
Original URL: https://bitinvestcoin.com
Prompt: Write Python code to implement a secure login system for a cryptocurrency investment platform, incorporating KYC verification and Google Authenticator as described on BitInvestCoin.
Generated: DETERMINISTIC_e1bdaef509dd719f
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import secrets
import string
import hashlib
import hmac
import time
import pyotp
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bitinvestcoin.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = secrets.token_urlsafe(32) 
db = SQLAlchemy(app)
jwt = JWTManager(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    kyc_verified = db.Column(db.Boolean, default=False)
    google_auth_secret = db.Column(db.String(16), nullable=True)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class KYCToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    token = db.Column(db.String(120), nullable=False)

    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        if not data:
            return jsonify({"msg": "Missing JSON in request"}), 400
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            return jsonify({"msg": "Email and password are required"}), 400
        if User.query.filter_by(email=email).first():
            return jsonify({"msg": "Email already exists"}), 400
        user = User(email, password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"msg": "User created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": "Failed to create user"}), 500

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        if not data:
            return jsonify({"msg": "Missing JSON in request"}), 400
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            return jsonify({"msg": "Email and password are required"}), 400
        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            return jsonify({"msg": "Bad email or password"}), 401
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200
    except Exception as e:
        return jsonify({"msg": "Failed to login"}), 500

@app.route('/kyc/verify', methods=['POST'])
@jwt_required
def kyc_verify():
    try:
        data = request.json
        if not data:
            return jsonify({"msg": "Missing JSON in request"}), 400
        token = data.get('token')
        if not token:
            return jsonify({"msg": "Token is required"}), 400
        current_user = User.query.filter_by(email=get_jwt_identity()).first()
        if not current_user:
            return jsonify({"msg": "User not found"}), 404
        kyc_token = KYCToken.query.filter_by(user_id=current_user.id, token=token).first()
        if kyc_token:
            current_user.kyc_verified = True
            db.session.commit()
            return jsonify({"msg": "KYC verified successfully"}), 200
        return jsonify({"msg": "Invalid token"}), 401
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": "Failed to verify KYC"}), 500

@app.route('/google-authenticator/enable', methods=['POST'])
@jwt_required
def google_authenticator_enable():
    try:
        current_user = User.query.filter_by(email=get_jwt_identity()).first()
        if not current_user:
            return jsonify({"msg": "User not found"}), 404
        secret = secrets.token_bytes(16).hex()
        current_user.google_auth_secret = secret
        db.session.commit()
        totp = pyotp.TOTP(secret).provisioning_uri(name=current_user.email, issuer_name='BitInvestCoin')
        return jsonify({"secret": secret, "totp_uri": totp}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": "Failed to enable Google Authenticator"}), 500

@app.route('/google-authenticator/verify', methods=['POST'])
@jwt_required
def google_authenticator_verify():
    try:
        data = request.json
        if not data:
            return jsonify({"msg": "Missing JSON in request"}), 400
        token = data.get('token')
        if not token:
            return jsonify({"msg": "Token is required"}), 400
        current_user = User.query.filter_by(email=get_jwt_identity()).first()
        if not current_user:
            return jsonify({"msg": "User not found"}), 404
        if not current_user.google_auth_secret:
            return jsonify({"msg": "Google Authenticator is not enabled"}), 400
        totp = pyotp.TOTP(current_user.google_auth_secret)
        if totp.verify(token):
            return jsonify({"msg": "Google Authenticator verified successfully"}), 200
        return jsonify({"msg": "Invalid token"}), 401
    except Exception as e:
        return jsonify({"msg": "Failed to verify Google Authenticator"}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
