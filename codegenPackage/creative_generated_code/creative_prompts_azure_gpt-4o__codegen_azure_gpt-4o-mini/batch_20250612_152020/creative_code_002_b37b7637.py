"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.homecareassistancebarrie.ca
Prompt: Generate code for a web application that allows users to request a free in-home consultation for elderly care services, including form submission and backend integration, inspired by the functionality on the Home Care Assistance Barrie site.
Generated: DETERMINISTIC_b37b76378c020093
Batch ID: 20250612_152020
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import smtplib
from email.message import EmailMessage

# Initialize Flask application
app = Flask(__name__)

# Configure the application with a database URI and secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consultations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Consultation model
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=True)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/request-consultation', methods=['POST'])
def request_consultation():
    try:
        # Extract data from the form
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # Validate the data (basic validation)
        if not name or not email or not phone:
            flash('All fields are required!', 'error')
            return redirect(url_for('index'))

        # Create a new consultation request
        consultation = Consultation(name=name, email=email, phone=phone, message=message)
        db.session.add(consultation)
        db.session.commit()

        # Send confirmation email (assuming SMTP server is configured)
        send_confirmation_email(name, email)

        flash('Your consultation request has been submitted successfully!', 'success')
        return redirect(url_for('index'))
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        flash(f'An error occurred: {str(e)}', 'error')
        return redirect(url_for('index'))

# Function to send a confirmation email
def send_confirmation_email(name, recipient_email):
    msg = EmailMessage()
    msg.set_content(f'Dear {name},\n\nThank you for requesting a consultation. We will get back to you shortly.\n\nBest regards,\nElderly Care Services')
    msg['Subject'] = 'Consultation Request Confirmation'
    msg['From'] = 'your_email@example.com'
    msg['To'] = recipient_email

    try:
        # Send the email using SMTP
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login('your_email@example.com', 'your_email_password')
            server.send_message(msg)
    except Exception as e:
        print(f'Failed to send email: {str(e)}')

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)

```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Request a Consultation</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Request a Free In-Home Consultation</h1>

        <!-- Display flash messages -->
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        <form action="{{ url_for('request_consultation') }}" method="POST" class="mt-4">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" class="form-control" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" class="form-control" name="email" required>
            </div>
            <div class="form-group">
                <label for="phone">Phone</label>
                <input type="text" class="form-control" name="phone" required>
            </div>
            <div class="form-group">
                <label for="message">Message</label>
                <textarea class="form-control" name="message"></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</body>
</html>
```
