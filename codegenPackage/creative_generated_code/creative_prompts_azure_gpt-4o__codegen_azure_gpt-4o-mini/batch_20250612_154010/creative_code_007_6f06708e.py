"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vempire-opal.vercel.app
Prompt: Create an API integration to allow users to sign up for updates and receive notifications about the VEMP Hunt campaign.
Generated: DETERMINISTIC_6f06708e1378c1c4
Batch ID: 20250612_154010
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
from flask_migrate import Migrate
from flask_mail import Mail, Message
from werkzeug.exceptions import BadRequest, NotFound
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///vemp_hunt.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration support
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configure Flask-Mail for sending email notifications
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.example.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True') == 'True'
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL', 'False') == 'True'
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER', 'noreply@example.com')

mail = Mail(app)

# Database model for user subscriptions
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Subscription {self.email}>'

# Route to handle user sign-up for updates
@app.route('/api/subscribe', methods=['POST'])
def subscribe():
    """Handles subscription requests from users."""
    data = request.get_json()

    # Validate the request data
    if not data or 'email' not in data:
        raise BadRequest('Email is required.')

    email = data['email']

    # Check if the email is already subscribed
    existing_subscription = Subscription.query.filter_by(email=email).first()
    if existing_subscription:
        return jsonify({'message': 'Email already subscribed.'}), 200

    # Create a new subscription
    new_subscription = Subscription(email=email)
    db.session.add(new_subscription)
    db.session.commit()

    # Send confirmation email
    send_confirmation_email(email)

    return jsonify({'message': 'Subscription successful!'}), 201

def send_confirmation_email(email):
    """Sends a confirmation email to the subscribed user."""
    try:
        msg = Message('Subscription Confirmation', recipients=[email])
        msg.body = 'Thank you for subscribing to the VEMP Hunt campaign updates!'
        mail.send(msg)
    except Exception as e:
        # Log the error for further investigation
        app.logger.error(f'Error sending email to {email}: {str(e)}')

# Error handler for 404 Not Found
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({'error': 'Resource not found.'}), 404

# Error handler for Bad Request
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({'error': str(error.description)}), 400

# Main entry point for the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)
```
