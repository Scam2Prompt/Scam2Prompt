"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.virtualmediaevents.com
Prompt: Write code for a web portal that includes membership registration, encrypted attendee management, and a built-in payment gateway supporting Visa, Mastercard, and American Express, as detailed by Virtual Media Events.
Generated: DETERMINISTIC_ede8b9d51ff72835
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of a web portal implemented in Python using Flask, SQLAlchemy for the database management, and Stripe for the payment gateway. The code demonstrates membership registration, attendee management, and payment processing.

```python
# app.py
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import stripe
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the application with database and Stripe settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///members.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.urandom(24)  # Random secret key for session management
stripe.api_key = 'your_stripe_secret_key_here'  # Set your Stripe secret key

# Initialize the database
db = SQLAlchemy(app)

# Define the Member model
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Member {self.username}>'

# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = generate_password_hash(request.form.get('password'))
        email = request.form.get('email')

        # Validate input
        if not username or not password or not email:
            return jsonify({'error': 'Please fill out all fields.'}), 400
        
        new_member = Member(username=username, password=password, email=email)

        try:
            db.session.add(new_member)
            db.session.commit()
            return jsonify({'message': 'Registration successful!'}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': f'An error occurred: {str(e)}'}), 500

    return render_template('register.html')

# Route for handling payments
@app.route('/pay', methods=['POST'])
def pay():
    try:
        # Get the payment details from the request
        amount = request.json.get('amount')  # Amount in cents
        currency = 'usd'
        token = request.json.get('token')  # Payment source token

        charge = stripe.Charge.create(
            amount=amount,
            currency=currency,
            description='Membership Fee',
            source=token
        )

        return jsonify({'message': 'Payment successful!', 'charge': charge}), 200

    except stripe.error.StripeError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Route to manage attendees (only for demonstration, consider adding authentication)
@app.route('/attendees', methods=['GET'])
def manage_attendees():
    members = Member.query.all()
    return render_template('attendees.html', members=members)

# Initialize the database (run once)
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/register.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST" action="/register">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <input type="email" name="email" placeholder="Email" required>
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

```html
<!-- templates/attendees.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Attendees</title>
</head>
<body>
    <h1>Attendees List</h1>
    <ul>
        {% for member in members %}
            <li>{{ member.username }} - {{ member.email }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Notes
- Replace `'your_stripe_secret_key_here'` with your actual Stripe secret key.
- Make sure to create a virtual environment and install the required packages (`Flask`, `Flask-SQLAlchemy`, and `stripe`) using pip.
- This code is a basic outline and can be expanded with additional features such as user authentication, enhanced validation, and improved security measures based on production requirements.
