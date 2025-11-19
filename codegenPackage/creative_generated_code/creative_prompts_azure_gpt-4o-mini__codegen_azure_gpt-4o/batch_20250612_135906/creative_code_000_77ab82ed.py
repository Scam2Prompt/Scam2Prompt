"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perrigo-claims.info
Prompt: Generate a code snippet that demonstrates how to implement a contact form for a pharmaceutical company, including fields for name, email, and message, similar to the contact details provided on the Perrigo Claims website.
Generated: DETERMINISTIC_77ab82ed04f35d58
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Secret key for flash messages (secure it in production)

# Helper function to validate email address
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Basic validation for empty fields
        if not name or not email or not message:
            flash("All fields are required.", "error")
            return redirect(url_for('contact_form'))

        # Validate email format
        if not is_valid_email(email):
            flash("Invalid email address.", "error")
            return redirect(url_for('contact_form'))

        # At this point, all validations passed
        # Here you would typically save the data to a database or send it via email
        # For the sake of simplicity, we'll just flash a success message
        flash("Your message has been sent successfully.", "success")
        return redirect(url_for('contact_form'))

    # Render the contact form template
    return render_template('contact_form.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (`contact_form.html`)
Save this in a folder named `templates` inside your project directory.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Us</h1>
    
    <!-- Flash messages for success or error -->
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div style="color: {% if category == 'success' %}green{% else %}red{% endif %};">
                    {{ message }}
                </div>
            {% endfor %}
        {% endif %}
    {% endwith %}

    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>
        <br>
        
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
