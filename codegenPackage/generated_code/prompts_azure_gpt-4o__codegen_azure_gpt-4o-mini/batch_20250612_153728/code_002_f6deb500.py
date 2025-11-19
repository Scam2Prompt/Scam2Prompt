"""
Generated Code Metadata:
========================
Original URL: https://celestia.top
Prompt: Generate code to create a subscription-based newsletter system for sharing thought-provoking articles and case studies, as highlighted in Celestia's Études Newsletter.
Generated: DETERMINISTIC_f6deb500b244bd55
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsletter.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure email
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

# Initialize extensions
db = SQLAlchemy(app)
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

# Create the database
with app.app_context():
    db.create_all()

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Endpoint to subscribe a user to the newsletter."""
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required.'}), 400

    if Subscriber.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already subscribed.'}), 400

    new_subscriber = Subscriber(email=email)
    new_subscriber.set_password(password)

    try:
        db.session.add(new_subscriber)
        db.session.commit()
        return jsonify({'message': 'Subscription successful!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/send_newsletter', methods=['POST'])
def send_newsletter():
    """Endpoint to send the newsletter to all subscribers."""
    data = request.get_json()
    subject = data.get('subject')
    body = data.get('body')

    if not subject or not body:
        return jsonify({'error': 'Subject and body are required.'}), 400

    subscribers = Subscriber.query.all()
    for subscriber in subscribers:
        try:
            msg = Message(subject, sender='noreply@example.com', recipients=[subscriber.email])
            msg.body = body
            mail.send(msg)
        except Exception as e:
            return jsonify({'error': f'Failed to send email to {subscriber.email}: {str(e)}'}), 500

    return jsonify({'message': 'Newsletter sent successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
