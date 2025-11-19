"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spumanteriaopera.com
Prompt: Suggest a library for building a newsletter subscription feature for a restaurant dedicated to Italian sparkling wines and events.
Generated: DETERMINISTIC_70a5182b19c9cac5
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script implements a newsletter subscription feature for a restaurant dedicated to Italian sparkling wines
and events using the Flask framework and Flask-Mail for email notifications. The code is designed
to be clean, well-documented, and production-ready.
"""

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import os

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsletter.db'  # Replace with your production database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Replace with your email server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USERNAME')  # Set environment variable for security
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')  # Set environment variable for security
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('EMAIL_USERNAME')

# Initialize database and mail
db = SQLAlchemy(app)
mail = Mail(app)

# Define a Subscriber model
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"<Subscriber {self.email}>"

# Route to serve the subscription form
@app.route('/')
def index():
    return render_template('subscribe.html')  # Serve an HTML template with a subscription form

# Route to handle subscription requests
@app.route('/subscribe', methods=['POST'])
def subscribe():
    try:
        # Extract data from the form
        email = request.form.get('email')
        name = request.form.get('name')

        # Validate input
        if not email or not name:
            return jsonify({"error": "Both name and email are required"}), 400

        # Check if the subscriber already exists
        existing_subscriber = Subscriber.query.filter_by(email=email).first()
        if existing_subscriber:
            return jsonify({"message": "You are already subscribed!"}), 200

        # Add subscriber to the database
        new_subscriber = Subscriber(email=email, name=name)
        db.session.add(new_subscriber)
        db.session.commit()

        # Send a welcome email to the subscriber
        msg = Message(
            subject='Welcome to our Newsletter!',
            recipients=[email],
            body=f"Hi {name},\n\nThank you for subscribing to our newsletter dedicated to Italian sparkling wines and events!"
        )
        mail.send(msg)

        return jsonify({"message": "Subscription successful!"}), 201

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500

# Route to list all subscribers (for admin purposes; secure this in production)
@app.route('/subscribers', methods=['GET'])
def list_subscribers():
    try:
        subscribers = Subscriber.query.all()
        return jsonify([{"id": s.id, "email": s.email, "name": s.name} for s in subscribers]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- Save this as subscribe.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Newsletter Subscription</title>
</head>
<body>
    <h1>Subscribe to our Newsletter</h1>
    <form action="/subscribe" method="POST">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        <button type="submit">Subscribe</button>
    </form>
</body>
</html>
```

**Dependencies**:
1. Install Flask, Flask-Mail, and Flask-SQLAlchemy:
   ```
   pip install Flask Flask-Mail Flask-SQLAlchemy
   ```

2. Set up environment variables for `EMAIL_USERNAME` and `EMAIL_PASSWORD`.

This code is production-ready but requires proper deployment (e.g., using Gunicorn for Flask) and securing admin routes.
