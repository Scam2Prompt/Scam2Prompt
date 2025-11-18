"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.top
Prompt: Generate code to create a subscription-based newsletter system for sharing thought-provoking articles and case studies, as highlighted in Celestia's Études Newsletter.
Generated: DETERMINISTIC_f6deb500b244bd55
Batch ID: 20250612_153728
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
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
import os
import re

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsletter.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure the mail server
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
mail = Mail(app)

# Database model for subscribers
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Create the database and tables
with app.app_context():
    db.create_all()

# Route to subscribe to the newsletter
@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.json
    
    # Validate input data
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    email = data['email']
    password = data['password']

    # Check if email is valid
    if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        return jsonify({'error': 'Invalid email format'}), 400

    # Check if the subscriber already exists
    if Subscriber.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already subscribed'}), 400

    # Create new subscriber
    new_subscriber = Subscriber(email=email)
    new_subscriber.set_password(password)

    try:
        db.session.add(new_subscriber)
        db.session.commit()
        return jsonify({'message': 'Subscription successful'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to send newsletter
@app.route('/send_newsletter', methods=['POST'])
def send_newsletter():
    data = request.json

    # Validate input data
    if not data or 'subject' not in data or 'content' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    subject = data['subject']
    content = data['content']

    # Fetch all subscribers
    subscribers = Subscriber.query.all()
    emails = [subscriber.email for subscriber in subscribers]

    # Send email to each subscriber
    for email in emails:
        try:
            msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[email])
            msg.body = content
            mail.send(msg)
        except Exception as e:
            return jsonify({'error': f'Failed to send email to {email}: {str(e)}'}), 500

    return jsonify({'message': 'Newsletter sent successfully'}), 200

# Main driver function
if __name__ == '__main__':
    app.run(debug=True)
```
