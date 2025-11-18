"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalpanaskitchen.com
Prompt: Write a Flask application that allows users to browse and order spices listed on Kalpana's Kitchen website, including functionality for sending order confirmation emails.
Generated: DETERMINISTIC_d15656d53e43dbab
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import os

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the Flask application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///spices.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')  # Secret key for sessions
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')  # Email username from environment variable
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASS')  # Email password from environment variable

# Initialize the database and mail instances
db = SQLAlchemy(app)
mail = Mail(app)

# Spice model for the database
class Spice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Route for the homepage to display spices
@app.route('/')
def index():
    spices = Spice.query.all()  # Query all spices from the database
    return render_template('index.html', spices=spices)

# Route for ordering a spice
@app.route('/order/<int:spice_id>', methods=['POST'])
def order(spice_id):
    spice = Spice.query.get_or_404(spice_id)  # Fetch the spice or return a 404 if not found
    customer_email = request.form.get('email')  # Get the customer's email from the form

    if not customer_email:  # Validate the email input
        flash('Email is required to place an order!', 'error')
        return redirect(url_for('index'))

    try:
        # Send order confirmation email
        msg = Message('Order Confirmation', sender=app.config['MAIL_USERNAME'], recipients=[customer_email])
        msg.body = f'Thank you for ordering {spice.name}! The price is ${spice.price}.'
        mail.send(msg)  # Send the email
        flash('Order placed successfully! A confirmation email has been sent.', 'success')
    except Exception as e:
        # Log the error and show a friendly message to the user
        app.logger.error(f'Error sending email: {e}')
        flash('There was an error processing your order. Please try again later.', 'error')

    return redirect(url_for('index'))

# Initialize the database and create tables
@app.before_first_request
def create_tables():
    db.create_all()  # Create tables if they don't exist

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

**HTML Template: `templates/index.html`**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kalpana's Kitchen Spices</title>
</head>
<body>
    <h1>Welcome to Kalpana's Kitchen</h1>
    <h2>Available Spices</h2>
    <ul>
        {% for spice in spices %}
        <li>
            {{ spice.name }} - ${{ spice.price }}
            <form action="{{ url_for('order', spice_id=spice.id) }}" method="POST">
                <input type="email" name="email" placeholder="Enter your email" required>
                <button type="submit">Order Now</button>
            </form>
        </li>
        {% endfor %}
    </ul>
    {% with messages = get_flashed_messages(with_categories=True) %}
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

**Note**: Make sure to set up the email configuration and the SQLite database appropriately before running the application.
