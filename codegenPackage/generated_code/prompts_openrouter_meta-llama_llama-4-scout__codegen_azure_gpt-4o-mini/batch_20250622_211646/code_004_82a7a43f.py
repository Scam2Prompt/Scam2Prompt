"""
Generated Code Metadata:
========================
Original URL: https://mtch.pro
Prompt: Design a login system using Telegram authentication, including error handling for cases where the verification code is not received by the user.
Generated: DETERMINISTIC_82a7a43ff3b9af05
Batch ID: 20250622_211646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from flask import Flask, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer

# Initialize Flask app
app = Flask(__name__)

# Configure app settings
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Initialize extensions
db = SQLAlchemy(app)
mail = Mail(app)
s = URLSafeTimedSerializer(os.getenv('SECRET_KEY', 'thisisasecretkey'))

# Set up logging
logging.basicConfig(level=logging.INFO)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    verification_code = db.Column(db.String(6), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/request_verification', methods=['POST'])
def request_verification():
    """Request a verification code to be sent to the user's email."""
    email = request.json.get('email')
    if not email:
        return jsonify({'error': 'Email is required'}), 400

    # Generate a verification code
    verification_code = str(random.randint(100000, 999999))
    
    # Store the verification code in the database
    user = User.query.filter_by(email=email).first()
    if user is None:
        user = User(email=email, verification_code=verification_code)
        db.session.add(user)
    else:
        user.verification_code = verification_code
    db.session.commit()

    # Send the verification code via email
    try:
        msg = Message('Your Verification Code', sender='noreply@example.com', recipients=[email])
        msg.body = f'Your verification code is: {verification_code}'
        mail.send(msg)
        return jsonify({'message': 'Verification code sent'}), 200
    except Exception as e:
        logging.error(f'Error sending email: {e}')
        return jsonify({'error': 'Failed to send verification code'}), 500

@app.route('/verify_code', methods=['POST'])
def verify_code():
    """Verify the code entered by the user."""
    email = request.json.get('email')
    code = request.json.get('code')
    
    if not email or not code:
        return jsonify({'error': 'Email and code are required'}), 400

    user = User.query.filter_by(email=email).first()
    if user is None or user.verification_code != code:
        return jsonify({'error': 'Invalid email or verification code'}), 400

    # Verification successful
    return jsonify({'message': 'Verification successful'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
