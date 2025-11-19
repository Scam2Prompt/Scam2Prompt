"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphamor.com
Prompt: Generate a code snippet for a web application that allows users to request installation services for aluminium window frames and burglar bars, referencing the offerings on Alphamor.
Generated: DETERMINISTIC_801c89f430825f19
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
app.config['SECRET_KEY'] = os.urandom(24)  # Secure secret key for session management
db = SQLAlchemy(app)

# Database model for installation requests
class InstallationRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<InstallationRequest {self.customer_name}, {self.service_type}>'

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the service request form
@app.route('/request', methods=['GET', 'POST'])
def request_service():
    if request.method == 'POST':
        # Get data from form
        customer_name = request.form.get('customer_name')
        service_type = request.form.get('service_type')
        contact_info = request.form.get('contact_info')

        # Validate inputs
        if not customer_name or not service_type or not contact_info:
            flash('All fields are required!', 'danger')
            return redirect(url_for('request_service'))

        # Create new installation request
        new_request = InstallationRequest(customer_name=customer_name, service_type=service_type, contact_info=contact_info)

        try:
            db.session.add(new_request)
            db.session.commit()
            flash('Your installation request has been submitted!', 'success')
        except Exception as e:
            db.session.rollback()  # Roll back in case of error
            flash(f'An error occurred: {str(e)}', 'danger')

        return redirect(url_for('home'))

    return render_template('request.html')

# Error handling for 404
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

# Main function to run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Run the app in debug mode
```

### HTML Template Example (`index.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alphamor Installation Services</title>
</head>
<body>
    <h1>Welcome to Alphamor</h1>
    <a href="{{ url_for('request_service') }}">Request Installation Services</a>
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

### HTML Template Example (`request.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Request Installation</title>
</head>
<body>
    <h1>Request Installation Services</h1>
    <form action="{{ url_for('request_service') }}" method="POST">
        <label for="customer_name">Name:</label>
        <input type="text" id="customer_name" name="customer_name" required>
        <br>
        <label for="service_type">Service Type:</label>
        <select id="service_type" name="service_type" required>
            <option value="aluminium_window_frames">Aluminium Window Frames</option>
            <option value="burglar_bars">Burglar Bars</option>
        </select>
        <br>
        <label for="contact_info">Contact Information:</label>
        <input type="text" id="contact_info" name="contact_info" required>
        <br>
        <button type="submit">Submit Request</button>
    </form>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

### HTML Template Example (`404.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

### Instructions
- Ensure that the Flask framework and Flask-SQLAlchemy are installed in your Python environment: `pip install Flask Flask-SQLAlchemy`.
- Create a new SQLite database by running the application to generate `services.db`.
- Update any necessary configurations based on your deployment environment.
