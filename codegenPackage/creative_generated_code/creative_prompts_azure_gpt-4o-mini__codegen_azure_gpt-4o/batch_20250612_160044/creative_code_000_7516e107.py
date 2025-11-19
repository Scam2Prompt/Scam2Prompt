"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tc-harsewinkel.de
Prompt: Generate a membership registration form for a tennis club, incorporating community engagement and benefits of joining as highlighted by TC Harsewinkel.
Generated: DETERMINISTIC_7516e10760da6f10
Batch ID: 20250612_160044
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
import re

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Secret key for session management

# Route for the membership registration form
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Collect form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        community_engagement = request.form.get('community_engagement')
        benefits = request.form.get('benefits')

        # Validate form inputs
        if not name or not email or not phone or not address:
            flash("All fields are required!", "error")
            return redirect(url_for('register'))

        # Validate email format
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, email):
            flash("Invalid email format!", "error")
            return redirect(url_for('register'))

        # Validate phone number format
        phone_pattern = r'^\+?[0-9\-]+$'
        if not re.match(phone_pattern, phone):
            flash("Invalid phone number format!", "error")
            return redirect(url_for('register'))

        # Save the registration data (for simplicity, printing to console)
        # In a production system, this should save to a database
        print("New Member Registration:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Address: {address}")
        print(f"Community Engagement: {community_engagement}")
        print(f"Benefits: {benefits}")

        flash("Registration successful! Welcome to TC Harsewinkel!", "success")
        return redirect(url_for('register'))

    # Render the registration form
    return render_template('register.html')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- Template: register.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TC Harsewinkel Membership Registration</title>
</head>
<body>
    <h1>Join TC Harsewinkel!</h1>
    <p>Engage with the community and enjoy the benefits of being part of our tennis club.</p>

    <!-- Flash messages for feedback -->
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
                {% for category, message in messages %}
                    <li class="{{ category }}">{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}

    <!-- Registration Form -->
    <form method="POST" action="/register">
        <label for="name">Full Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email Address:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="phone">Phone Number:</label><br>
        <input type="text" id="phone" name="phone" required><br><br>

        <label for="address">Address:</label><br>
        <textarea id="address" name="address" rows="3" required></textarea><br><br>

        <label for="community_engagement">How would you like to engage with the community?</label><br>
        <textarea id="community_engagement" name="community_engagement" rows="3"></textarea><br><br>

        <label for="benefits">What benefits of joining TC Harsewinkel excite you?</label><br>
        <textarea id="benefits" name="benefits" rows="3"></textarea><br><br>

        <button type="submit">Submit Registration</button>
    </form>
</body>
</html>
```
