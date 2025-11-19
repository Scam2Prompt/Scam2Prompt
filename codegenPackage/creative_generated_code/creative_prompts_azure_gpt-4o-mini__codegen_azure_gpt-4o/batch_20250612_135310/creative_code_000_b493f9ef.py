"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wingerrandr.ca
Prompt: Generate a code snippet for a web application that allows users to request household appliance repairs, including a form for user details and appliance information.
Generated: DETERMINISTIC_b493f9ef61bfb77a
Batch ID: 20250612_135310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure, random key in production

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the repair request form
@app.route('/request-repair', methods=['GET', 'POST'])
def request_repair():
    if request.method == 'POST':
        try:
            # Extract form data
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            appliance = request.form.get('appliance')
            issue = request.form.get('issue')

            # Validate required fields
            if not name or not email or not phone or not appliance or not issue:
                flash('All fields are required!', 'error')
                return redirect(url_for('request_repair'))

            # Simulated storage (would connect to a database in production)
            # Here we just print to console as a placeholder
            print(f"New repair request submitted:\n"
                  f"Name: {name}, Email: {email}, Phone: {phone}, Appliance: {appliance}, Issue: {issue}")

            # Provide feedback to the user
            flash('Your repair request has been submitted!', 'success')
            return redirect(url_for('home'))
        except HTTPException as e:
            flash(f"An error occurred: {e}", 'error')
            return redirect(url_for('request_repair'))
        except Exception as e:
            flash('An unexpected error occurred. Please try again later.', 'error')
            return redirect(url_for('request_repair'))

    # Render the form template for GET requests
    return render_template('request_repair.html')

# Error handler for 404 - Page not found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
```

### Template: `home.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Appliance Repair</title>
</head>
<body>
    <h1>Welcome to the Appliance Repair Service</h1>
    <a href="/request-repair">Request a Repair</a>
</body>
</html>
```

### Template: `request_repair.html`
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
    
    <!-- Flash messages -->
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
                {% for category, message in messages %}
                    <li style="color: {% if category == 'error' %}red{% elif category == 'success' %}green{% endif %};">
                        {{ message }}
                    </li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    
    <form method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        
        <label for="phone">Phone Number:</label>
        <input type="text" id="phone" name="phone" required>
        <br>
        
        <label for="appliance">Appliance:</label>
        <input type="text" id="appliance" name="appliance" required>
        <br>
        
        <label for="issue">Describe the Issue:</label>
        <textarea id="issue" name="issue" required></textarea>
        <br>
        
        <button type="submit">Submit Request</button>
    </form>
    
    <a href="/">Back to Home</a>
</body>
</html>
```

### Template: `404.html`
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
    <a href="/">Go Back to Home</a>
</body>
</html>
```
