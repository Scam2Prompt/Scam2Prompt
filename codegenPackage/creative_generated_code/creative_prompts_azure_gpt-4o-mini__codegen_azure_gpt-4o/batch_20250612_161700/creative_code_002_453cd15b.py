"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ammaparivaar.org
Prompt: Can you provide a code example for a simple web form that allows users to donate to an orphanage, similar to the donation process described on ammaparivaar.org?
Generated: DETERMINISTIC_453cd15bdf1c5054
Batch ID: 20250612_161700
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
app.secret_key = 'your_secret_key'  # Required for flash messages

# Route to render the donation form
@app.route('/')
def donation_form():
    return render_template('donation_form.html')

# Route to handle form submission
@app.route('/donate', methods=['POST'])
def process_donation():
    try:
        # Extract data from the form
        name = request.form.get('name')
        email = request.form.get('email')
        amount = request.form.get('amount')

        # Validate name (must not be empty)
        if not name or len(name.strip()) == 0:
            flash('Name is required.', 'error')
            return redirect(url_for('donation_form'))

        # Validate email format using regex
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not email or not re.match(email_regex, email):
            flash('Please provide a valid email address.', 'error')
            return redirect(url_for('donation_form'))

        # Validate donation amount (must be a positive number)
        try:
            amount = float(amount)
            if amount <= 0:
                flash('Donation amount must be a positive number.', 'error')
                return redirect(url_for('donation_form'))
        except ValueError:
            flash('Donation amount must be a valid number.', 'error')
            return redirect(url_for('donation_form'))

        # Log the donation details (In production, replace with database storage)
        print(f'New Donation - Name: {name}, Email: {email}, Amount: {amount:.2f}')

        # Provide feedback to the user
        flash('Thank you for your donation!', 'success')
        return redirect(url_for('donation_form'))

    except Exception as e:
        # Handle unexpected errors
        flash('An error occurred while processing your donation. Please try again.', 'error')
        print(f'Error: {e}')
        return redirect(url_for('donation_form'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- Save this as templates/donation_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Orphanage Donation Form</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .form-container { max-width: 500px; margin: auto; }
        .form-container label { display: block; margin-bottom: 5px; }
        .form-container input { width: 100%; margin-bottom: 15px; padding: 10px; }
        .flash-message { margin-bottom: 20px; padding: 10px; border-radius: 5px; }
        .success { background-color: #d4edda; color: #155724; }
        .error { background-color: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Donate to the Orphanage</h2>
        {% with messages = get_flashed_messages(with_categories=True) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="flash-message {{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <form action="/donate" method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="amount">Donation Amount:</label>
            <input type="number" id="amount" name="amount" step="0.01" required>

            <button type="submit">Donate</button>
        </form>
    </div>
</body>
</html>
```
