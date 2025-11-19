"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poweredproductions.com.au
Prompt: How can I create a user-friendly interface for a film production service that allows users to request armourer services and uniform hires?
Generated: DETERMINISTIC_67a79d0189388edc
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, flash

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Used for flash messages

# Dummy database (in a production setting, use a proper database like PostgreSQL, MySQL, etc.)
services = []  # List to store service requests

# Route to display the home page
@app.route('/')
def home():
    """
    Render the home page of the film production service.
    """
    return render_template('index.html')

# Route to display the request form
@app.route('/request', methods=['GET', 'POST'])
def request_service():
    """
    Handle service requests (GET: display form, POST: process form submission).
    """
    if request.method == 'POST':
        try:
            # Collect form data
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            service_type = request.form['service_type']
            description = request.form['description']

            # Validate data
            if not name or not email or not phone or not service_type:
                flash("All fields marked with * are required!", "error")
                return redirect(url_for('request_service'))

            # Append request to the database (dummy storage for now)
            services.append({
                'name': name,
                'email': email,
                'phone': phone,
                'service_type': service_type,
                'description': description
            })

            flash("Service request submitted successfully!", "success")
            return redirect(url_for('home'))
        except Exception as e:
            flash(f"An error occurred: {str(e)}", "error")
            return redirect(url_for('request_service'))

    # Render the request form if method == GET
    return render_template('request_form.html')

# Route to display the list of service requests (admin view)
@app.route('/admin')
def admin_view():
    """
    Display all service requests (admin-only view).
    """
    return render_template('admin.html', services=services)

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors gracefully.
    """
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### File: `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Film Production Services</title>
</head>
<body>
    <h1>Welcome to Film Production Services</h1>
    <p>Request armourer services or uniform hires easily.</p>
    <a href="/request">Request a Service</a>
    <a href="/admin">Admin Dashboard</a>
</body>
</html>
```

### File: `templates/request_form.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Request a Service</title>
</head>
<body>
    <h1>Request a Service</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        {% for category, message in messages %}
            <div class="flash {{ category }}">{{ message }}</div>
        {% endfor %}
    {% endif %}
    {% endwith %}
    <form method="POST">
        <label for="name">Name*:</label>
        <input type="text" id="name" name="name" required><br>

        <label for="email">Email*:</label>
        <input type="email" id="email" name="email" required><br>

        <label for="phone">Phone*:</label>
        <input type="text" id="phone" name="phone" required><br>

        <label for="service_type">Service Type*:</label>
        <select id="service_type" name="service_type" required>
            <option value="armourer">Armourer Services</option>
            <option value="uniform">Uniform Hire</option>
        </select><br>

        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br>

        <button type="submit">Submit Request</button>
    </form>
    <a href="/">Back to Home</a>
</body>
</html>
```

### File: `templates/admin.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard</title>
</head>
<body>
    <h1>Admin Dashboard</h1>
    <h2>Service Requests:</h2>
    <ul>
        {% for service in services %}
        <li>
            <strong>Name:</strong> {{ service.name }}<br>
            <strong>Email:</strong> {{ service.email }}<br>
            <strong>Phone:</strong> {{ service.phone }}<br>
            <strong>Service Type:</strong> {{ service.service_type }}<br>
            <strong>Description:</strong> {{ service.description }}
        </li>
        <hr>
        {% endfor %}
    </ul>
    <a href="/">Back to Home</a>
</body>
</html>
```

### File: `templates/404.html`
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
    <p>The page you are looking for does not exist.</p>
    <a href="/">Back to Home</a>
</body>
</html>
```

### Notes:
- This is a simple Flask application with basic routing and templates.
- In production, replace the dummy `services` list with a proper database.
- Ensure proper security measures (e.g., input sanitization, CSRF protection) are in place for production.
