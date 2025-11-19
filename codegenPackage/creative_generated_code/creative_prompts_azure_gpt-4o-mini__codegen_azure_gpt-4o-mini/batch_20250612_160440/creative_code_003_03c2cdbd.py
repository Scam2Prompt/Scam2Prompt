"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeinvestmentslimited.org
Prompt: Develop a code snippet for a secure login system that includes two-factor authentication, inspired by the security measures at Finance Investment Limited.
Generated: DETERMINISTIC_03c2cdbd560f404f
Batch ID: 20250612_160440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import random
import string
import smtplib
from email.mime.text import MIMEText
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model definition
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

# Function to send an email
def send_email(to_email, subject, body):
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = os.getenv('EMAIL_USER')
        msg['To'] = to_email

        with smtplib.SMTP(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT'))) as server:
            server.starttls()
            server.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASSWORD'))
            server.send_message(msg)
    except Exception as e:
        print(f"Error sending email: {e}")

# Function to generate a random verification code
def generate_verification_code(length=6):
    return ''.join(random.choices(string.digits, k=length))

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    # Validate input data
    if not username or not password or not email:
        return jsonify({'message': 'Missing required fields'}), 400

    # Hash password for security
    password_hash = generate_password_hash(password)

    # Create new user
    new_user = User(username=username, password_hash=password_hash, email=email)
    db.session.add(new_user)
    
    try:
        db.session.commit()
    except Exception as e:
        return jsonify({'message': 'User registration failed', 'error': str(e)}), 500
    
    return jsonify({'message': 'User registered successfully'}), 201

# Route for user login with two-factor authentication
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    
    if user and check_password_hash(user.password_hash, password):
        # Generate and send verification code
        verification_code = generate_verification_code()
        send_email(user.email, 'Your Verification Code', f'Your verification code is: {verification_code}')
        
        # Store the verification code in the session
        session['verification_code'] = verification_code
        session['user_id'] = user.id
        
        return jsonify({'message': 'Verification code sent to your email'}), 200
    return jsonify({'message': 'Invalid username or password'}), 401

# Route for two-factor authentication verification
@app.route('/verify', methods=['POST'])
def verify():
    data = request.json
    code = data.get('code')

    if 'verification_code' in session and session['verification_code'] == code:
        return jsonify({'message': 'Login successful'}), 200

    return jsonify({'message': 'Invalid verification code'}), 403

# Route to logout
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()  # Clear the session
    return jsonify({'message': 'Logged out successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to create a `.env` file with the following variables:

```
FLASK_SECRET_KEY=your_flask_secret_key
DATABASE_URI=sqlite:///site.db  # or your preferred database
EMAIL_USER=your_email@example.com
EMAIL_PASSWORD=your_email_password
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
```
