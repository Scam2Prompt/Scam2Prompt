"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: Suggest tools or frameworks to develop a subscription-based notification system for exam preparation updates, as highlighted in Educar Comitán's "Suscríbete" section.
Generated: DETERMINISTIC_4c31379f99dd4371
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configure Flask-Mail for sending notifications
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
mail = Mail(app)

# Define the Subscription model
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Subscription {self.email}>'

# Route to subscribe for notifications
@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()
    email = data.get('email')

    # Validate email
    if not email or '@' not in email:
        return jsonify({'error': 'Invalid email address'}), 400

    # Check if the email is already subscribed
    existing_subscription = Subscription.query.filter_by(email=email).first()
    if existing_subscription:
        return jsonify({'message': 'Already subscribed'}), 409

    # Create a new subscription
    new_subscription = Subscription(email=email)
    db.session.add(new_subscription)
    db.session.commit()

    return jsonify({'message': 'Subscription successful'}), 201

# Function to send notifications
def send_notification(subject, body):
    with app.app_context():
        subscribers = Subscription.query.all()
        for subscriber in subscribers:
            msg = Message(subject, sender='noreply@example.com', recipients=[subscriber.email])
            msg.body = body
            try:
                mail.send(msg)
            except Exception as e:
                print(f'Failed to send email to {subscriber.email}: {e}')

# Route to trigger notifications
@app.route('/notify', methods=['POST'])
def notify():
    data = request.get_json()
    subject = data.get('subject')
    body = data.get('body')

    # Validate input
    if not subject or not body:
        return jsonify({'error': 'Subject and body are required'}), 400

    # Send notifications
    send_notification(subject, body)
    return jsonify({'message': 'Notifications sent'}), 200

# Error handling for database errors
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': str(e)}), 500

# Main entry point
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
