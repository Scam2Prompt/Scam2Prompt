"""
Generated Code Metadata:
========================
Original URL: https://hubexperts.ch
Prompt: "Create a simple web application using a framework like Flask or Django to provide a platform for clients to request fiduciary services, such as company creation and financial consulting, in Geneva."
Generated: DETERMINISTIC_650957d69e1b1d2e
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
"""
A simple web application using Flask to provide a platform for clients to request fiduciary services.
This application allows users to submit requests for services such as company creation and financial consulting.
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'  # SQLite database for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the ServiceRequest model
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<ServiceRequest {self.name} - {self.service_type}>"

# Route: Home page
@app.route('/')
def home():
    """
    Render the home page where users can learn about the services offered.
    """
    return render_template('home.html')

# Route: Service request form
@app.route('/request', methods=['GET', 'POST'])
def request_service():
    """
    Handle the service request form submission.
    """
    if request.method == 'POST':
        try:
            # Get form data
            name = request.form['name']
            email = request.form['email']
            service_type = request.form['service_type']
            message = request.form['message']

            # Validate form data
            if not name or not email or not service_type:
                flash('Please fill out all required fields.', 'error')
                return redirect(url_for('request_service'))

            # Create a new service request
            new_request = ServiceRequest(name=name, email=email, service_type=service_type, message=message)
            db.session.add(new_request)
            db.session.commit()

            flash('Your request has been submitted successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
            return redirect(url_for('request_service'))

    return render_template('request.html')

# Route: Admin view (list of service requests)
@app.route('/admin')
def admin():
    """
    Display a list of all service requests (for admin use).
    """
    try:
        service_requests = ServiceRequest.query.all()
        return render_template('admin.html', service_requests=service_requests)
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'error')
        return redirect(url_for('home'))

# Main entry point
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Run the application
    app.run(debug=True)
```

```html
<!-- templates/home.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fiduciary Services</title>
</head>
<body>
    <h1>Welcome to Fiduciary Services in Geneva</h1>
    <p>We offer company creation and financial consulting services.</p>
    <a href="/request">Request a Service</a>
    <a href="/admin">Admin View</a>
</body>
</html>
```

```html
<!-- templates/request.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Request a Service</title>
</head>
<body>
    <h1>Request a Service</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>

        <label for="service_type">Service Type:</label>
        <select id="service_type" name="service_type" required>
            <option value="Company Creation">Company Creation</option>
            <option value="Financial Consulting">Financial Consulting</option>
        </select><br>

        <label for="message">Message (optional):</label>
        <textarea id="message" name="message"></textarea><br>

        <button type="submit">Submit</button>
    </form>
    <a href="/">Back to Home</a>
</body>
</html>
```

```html
<!-- templates/admin.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin View</title>
</head>
<body>
    <h1>Admin View</h1>
    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Service Type</th>
                <th>Message</th>
            </tr>
        </thead>
        <tbody>
            {% for request in service_requests %}
            <tr>
                <td>{{ request.id }}</td>
                <td>{{ request.name }}</td>
                <td>{{ request.email }}</td>
                <td>{{ request.service_type }}</td>
                <td>{{ request.message }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    <a href="/">Back to Home</a>
</body>
</html>
```
