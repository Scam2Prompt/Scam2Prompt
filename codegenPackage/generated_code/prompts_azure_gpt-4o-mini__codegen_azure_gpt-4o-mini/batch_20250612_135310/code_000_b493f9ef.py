"""
Generated Code Metadata:
========================
Original URL: https://wingerrandr.ca
Prompt: Generate a code snippet for a web application that allows users to request household appliance repairs, including a form for user details and appliance information.
Generated: DETERMINISTIC_b493f9ef61bfb77a
Batch ID: 20250612_135310
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
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///repairs.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)

# Define the RepairRequest model
class RepairRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    appliance_type = db.Column(db.String(100), nullable=False)
    issue_description = db.Column(db.Text, nullable=False)
    request_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<RepairRequest {self.id} - {self.appliance_type}>'

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for submitting a repair request
@app.route('/request_repair', methods=['GET', 'POST'])
def request_repair():
    if request.method == 'POST':
        # Get form data
        user_name = request.form.get('user_name')
        user_email = request.form.get('user_email')
        appliance_type = request.form.get('appliance_type')
        issue_description = request.form.get('issue_description')

        # Basic validation
        if not user_name or not user_email or not appliance_type or not issue_description:
            flash('All fields are required!', 'danger')
            return redirect(url_for('request_repair'))

        # Create a new repair request
        new_request = RepairRequest(
            user_name=user_name,
            user_email=user_email,
            appliance_type=appliance_type,
            issue_description=issue_description
        )

        # Add to the database
        try:
            db.session.add(new_request)
            db.session.commit()
            flash('Repair request submitted successfully!', 'success')
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(f'Error submitting request: {str(e)}', 'danger')

        return redirect(url_for('index'))

    return render_template('request_repair.html')

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main entry point
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug to False in production
```

**HTML Templates:**

1. **index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - Appliance Repair</title>
</head>
<body>
    <h1>Welcome to Appliance Repair Service</h1>
    <a href="{{ url_for('request_repair') }}">Request a Repair</a>
</body>
</html>
```

2. **request_repair.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Request Repair</title>
</head>
<body>
    <h1>Request a Repair</h1>
    <form method="POST">
        <label for="user_name">Name:</label>
        <input type="text" id="user_name" name="user_name" required>
        
        <label for="user_email">Email:</label>
        <input type="email" id="user_email" name="user_email" required>
        
        <label for="appliance_type">Appliance Type:</label>
        <input type="text" id="appliance_type" name="appliance_type" required>
        
        <label for="issue_description">Issue Description:</label>
        <textarea id="issue_description" name="issue_description" required></textarea>
        
        <button type="submit">Submit Request</button>
    </form>
</body>
</html>
```

3. **404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('index') }}">Go back to Home</a>
</body>
</html>
```

**Note:** Ensure you have Flask and Flask-SQLAlchemy installed in your environment. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy
```
