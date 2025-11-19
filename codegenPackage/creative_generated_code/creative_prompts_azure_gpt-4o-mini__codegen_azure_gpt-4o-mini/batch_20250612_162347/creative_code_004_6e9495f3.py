"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codyalt.com
Prompt: Suggest a code snippet for implementing a subscription model for a newsletter like The Infinite Game, aimed at self-improvement and entrepreneurship.
Generated: DETERMINISTIC_6e9495f3cbe3c5b4
Batch ID: 20250612_162347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///subscriptions.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for Subscribers
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the password for secure storage."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check a password against the stored hash."""
        return check_password_hash(self.password_hash, password)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Endpoint for subscribing to the newsletter."""
    data = request.get_json()
    
    # Validate input
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Email and password are required.'}), 400
    
    email = data['email']
    password = data['password']
    
    # Check if the subscriber already exists
    existing_subscriber = Subscriber.query.filter_by(email=email).first()
    if existing_subscriber:
        return jsonify({'error': 'Email already subscribed.'}), 409
    
    # Create a new subscriber
    new_subscriber = Subscriber(email=email)
    new_subscriber.set_password(password)
    
    # Add to database and commit
    db.session.add(new_subscriber)
    try:
        db.session.commit()
    except Exception as e:
        # Rollback in case of error
        db.session.rollback()
        return jsonify({'error': 'Could not complete subscription. Please try again later.'}), 500

    return jsonify({'message': 'Subscription successful!'}), 201

@app.route('/login', methods=['POST'])
def login():
    """Endpoint for logging in a subscribed user."""
    data = request.get_json()
    
    # Validate input
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Email and password are required.'}), 400
    
    email = data['email']
    password = data['password']
    
    # Find the subscriber
    subscriber = Subscriber.query.filter_by(email=email).first()
    if not subscriber or not subscriber.check_password(password):
        return jsonify({'error': 'Invalid email or password.'}), 401
    
    return jsonify({'message': 'Login successful!'}), 200

if __name__ == '__main__':
    # Running the application
    app.run(debug=True)
```
