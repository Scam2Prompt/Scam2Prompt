"""
Generated Code Metadata:
========================
Original URL: https://gam3searly.pages.dev
Prompt: Generate code for a newsletter subscription form that collects email addresses and sends updates about gaming news, similar to the functionality on GAM3S.GG.
Generated: DETERMINISTIC_f08c7518deec5d7f
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import re

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your mail server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your_password'  # Replace with your email password
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@example.com'  # Replace with your email

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

# Function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Route to render the subscription form
@app.route('/')
def index():
    return render_template('subscribe.html')

# Route to handle subscription form submission
@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')

    # Validate email format
    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email address'}), 400

    # Check if the email is already subscribed
    if Subscription.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already subscribed'}), 400

    # Create a new subscription
    new_subscription = Subscription(email=email)
    db.session.add(new_subscription)

    try:
        db.session.commit()
        # Send confirmation email
        msg = Message('Subscription Confirmation', recipients=[email])
        msg.body = 'Thank you for subscribing to our gaming news updates!'
        mail.send(msg)
        return jsonify({'message': 'Subscription successful!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Could not process subscription', 'details': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (subscribe.html)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Newsletter Subscription</title>
</head>
<body>
    <h1>Subscribe to Gaming News</h1>
    <form action="/subscribe" method="post">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <button type="submit">Subscribe</button>
    </form>
</body>
</html>
```

**Note**: Make sure to replace the email configuration details with your actual SMTP server settings and credentials.
