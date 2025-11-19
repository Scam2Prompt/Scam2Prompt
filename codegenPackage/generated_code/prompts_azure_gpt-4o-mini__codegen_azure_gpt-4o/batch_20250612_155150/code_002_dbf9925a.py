"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: Create a sample code to implement a web form that allows users to submit inquiries about Duplex Steel Pipes, referencing the features provided by Dinkar Alloys.
Generated: DETERMINISTIC_dbf9925afc3642e0
Batch ID: 20250612_155150
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
import re

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for flash messages

# Route to display the inquiry form
@app.route('/')
def inquiry_form():
    return render_template('form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_inquiry():
    try:
        # Extract form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Validate form data
        if not name or not email or not message:
            flash('All fields are required!', 'error')
            return redirect(url_for('inquiry_form'))

        # Validate email format
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            flash('Invalid email format!', 'error')
            return redirect(url_for('inquiry_form'))

        # Simulate saving the inquiry (e.g., to a database or sending an email)
        # In production, replace this with actual database or email logic
        print(f"Inquiry received:\nName: {name}\nEmail: {email}\nMessage: {message}")

        # Provide feedback to the user
        flash('Inquiry submitted successfully!', 'success')
        return redirect(url_for('inquiry_form'))

    except Exception as e:
        # Handle unexpected errors
        flash(f'An error occurred: {str(e)}', 'error')
        return redirect(url_for('inquiry_form'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- Save this file as templates/form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Duplex Steel Pipes Inquiry Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .form-container {
            max-width: 500px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .form-container h2 {
            text-align: center;
        }
        .form-container input, .form-container textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .form-container button {
            width: 100%;
            padding: 10px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .form-container button:hover {
            background-color: #0056b3;
        }
        .flash-message {
            text-align: center;
            margin: 10px 0;
            padding: 10px;
            border-radius: 5px;
        }
        .flash-message.success {
            background-color: #d4edda;
            color: #155724;
        }
        .flash-message.error {
            background-color: #f8d7da;
            color: #721c24;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Duplex Steel Pipes Inquiry Form</h2>
        <!-- Display flash messages -->
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="flash-message {{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <!-- Inquiry form -->
        <form action="{{ url_for('submit_inquiry') }}" method="POST">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your Inquiry Message" rows="5" required></textarea>
            <button type="submit">Submit Inquiry</button>
        </form>
    </div>
</body>
</html>
```
