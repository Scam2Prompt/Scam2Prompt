"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atlas3io-aphrodao.web.app
Prompt: How do I create a seamless user experience for members joining the AphroDAO community?
Generated: DETERMINISTIC_217c7357fd0e2a30
Batch ID: 20250612_162531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries and frameworks
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aphrodao.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure Flask-Mail settings
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to handle user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Validate input data
    if not data or not all(key in data for key in ('username', 'email', 'password')):
        return jsonify({'message': 'Invalid input data'}), 400

    username = data['username']
    email = data['email']
    password = data['password']

    # Check for existing user
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({'message': 'Username or email already exists'}), 400

    # Hash the password
    hashed_password = generate_password_hash(password, method='sha256')

    # Create a new user
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    
    try:
        db.session.commit()
        send_welcome_email(email)
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Registration failed', 'error': str(e)}), 500

    return jsonify({'message': 'User registered successfully'}), 201

# Function to send welcome email
def send_welcome_email(email):
    try:
        msg = Message('Welcome to AphroDAO!', sender=os.getenv('MAIL_USERNAME'), recipients=[email])
        msg.body = 'Thank you for joining the AphroDAO community!'
        mail.send(msg)
    except Exception as e:
        print(f"Error sending email: {e}")

# Main block to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
