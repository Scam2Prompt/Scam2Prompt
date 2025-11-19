"""
Generated Code Metadata:
========================
Original URL: https://mysoulitude.com
Prompt: Develop a simple web application using a library like Flask or Django that allows users to subscribe to and receive updates from blogs like My Soulitude.
Generated: DETERMINISTIC_d4c8afb2d20111ab
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscribers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

# Initialize extensions
db = SQLAlchemy(app)
mail = Mail(app)
migrate = Migrate(app, db)

# Define the Subscriber model
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Subscriber {self.email}>'

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle subscription
@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    if not email:
        flash('Email is required!', 'error')
        return redirect(url_for('index'))

    # Check if the email is already subscribed
    existing_subscriber = Subscriber.query.filter_by(email=email).first()
    if existing_subscriber:
        flash('You are already subscribed!', 'info')
        return redirect(url_for('index'))

    # Add new subscriber to the database
    new_subscriber = Subscriber(email=email)
    db.session.add(new_subscriber)
    db.session.commit()

    # Send confirmation email
    try:
        msg = Message('Subscription Confirmation', sender=app.config['MAIL_USERNAME'], recipients=[email])
        msg.body = 'Thank you for subscribing to My Soulitude! You will receive updates soon.'
        mail.send(msg)
        flash('Subscription successful! A confirmation email has been sent.', 'success')
    except Exception as e:
        flash(f'Error sending email: {str(e)}', 'error')

    return redirect(url_for('index'))

# Route to view all subscribers (for admin purposes)
@app.route('/subscribers')
def subscribers():
    all_subscribers = Subscriber.query.all()
    return render_template('subscribers.html', subscribers=all_subscribers)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main entry point
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
```

### HTML Templates

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Subscribe to My Soulitude</title>
</head>
<body>
    <h1>Subscribe to My Soulitude</h1>
    <form action="{{ url_for('subscribe') }}" method="post">
        <input type="email" name="email" placeholder="Enter your email" required>
        <button type="submit">Subscribe</button>
    </form>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

**subscribers.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Subscribers List</title>
</head>
<body>
    <h1>Subscribers</h1>
    <ul>
        {% for subscriber in subscribers %}
            <li>{{ subscriber.email }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

**404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

### Notes
- Ensure to set the environment variables `MAIL_USERNAME` and `MAIL_PASSWORD` for email functionality.
- Use a production-ready email service and database for deployment.
- This code is structured for a simple Flask application and can be expanded with additional features as needed.
