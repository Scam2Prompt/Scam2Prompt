"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chayatime.com
Prompt: Recommend a library to implement a newsletter subscription feature for the ChayaTime website, ensuring compliance with privacy policies.
Generated: DETERMINISTIC_5fbb3a080bd2d21d
Batch ID: 20250612_153246
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
from flask_mail import Mail, Message
import re

# Create Flask application instance
app = Flask(__name__)

# Configure Database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure Mail (use appropriate SMTP settings)
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your SMTP server
app.config['MAIL_PORT'] = 587  # Replace with the appropriate port
app.config['MAIL_USERNAME'] = 'your_email@example.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your_password'  # Replace with your password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

# Define the Subscription model
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Subscription {self.email}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Email validation regex
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Endpoint to handle newsletter subscription."""
    try:
        # Extract email from request
        data = request.get_json()
        email = data.get('email')
        
        # Validate email format
        if not email or not re.match(EMAIL_REGEX, email):
            return jsonify({'error': 'Invalid email address.'}), 400
        
        # Check if email already exists
        if Subscription.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already subscribed.'}), 400
            
        # Create new subscription
        new_subscription = Subscription(email=email)
        db.session.add(new_subscription)
        db.session.commit()
        
        # Send confirmation email
        msg = Message('Subscription Confirmation',
                      sender='your_email@example.com',
                      recipients=[email])
        msg.body = 'Thank you for subscribing to ChayaTime newsletter!'
        mail.send(msg)

        return jsonify({'message': 'Subscription successful!'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return generic error message on failure

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application
```
