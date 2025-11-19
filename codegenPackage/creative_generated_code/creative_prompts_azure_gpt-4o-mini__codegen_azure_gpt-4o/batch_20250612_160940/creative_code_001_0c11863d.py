"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azuki.zone
Prompt: Write a code snippet for a contact form that allows users to reach out to a UI/UX designer, incorporating fields for email and social media links.
Generated: DETERMINISTIC_0c11863d4d0b3646
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A simple Flask application for a contact form to allow users to reach out to a UI/UX designer.
The form includes fields for email and social media links.
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Used for flash messages

# Utility function to validate email format
def is_valid_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email)

# Route to display the contact form
@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        # Retrieve form data
        email = request.form.get('email')
        social_links = request.form.get('social_links')

        # Input validation
        if not email or not is_valid_email(email):
            flash("Please provide a valid email address.", "error")
            return redirect(url_for('contact_form'))

        if not social_links:
            flash("Please provide at least one social media link.", "error")
            return redirect(url_for('contact_form'))
        
        # At this point, the input is valid
        flash("Thank you for reaching out! We'll get back to you shortly.", "success")
        # Save data to database or send notification (not implemented for simplicity)

        return redirect(url_for('contact_form'))
    
    # Render the form template
    return render_template('contact_form.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- Save this as 'templates/contact_form.html' -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact UI/UX Designer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: #f9f9f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .form-container {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .form-container h2 {
            margin-bottom: 20px;
        }
        .form-container input, .form-container textarea, .form-container button {
            width: 100%;
            margin-bottom: 10px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .form-container button {
            background: #007BFF;
            color: #fff;
            border: none;
            cursor: pointer;
        }
        .form-container button:hover {
            background: #0056b3;
        }
        .flash-message {
            margin-bottom: 10px;
            color: #d9534f;
        }
        .success-message {
            color: #5cb85c;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Contact UI/UX Designer</h2>
        <!-- Display flash messages -->
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <p class="flash-message {{ 'success-message' if category == 'success' else '' }}">{{ message }}</p>
                {% endfor %}
            {% endif %}
        {% endwith %}
        
        <form method="POST">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" placeholder="Your email address" required>
            
            <label for="social_links">Social Media Links:</label>
            <textarea id="social_links" name="social_links" placeholder="Provide your social media links" required></textarea>
            
            <button type="submit">Submit</button>
        </form>
    </div>
</body>
</html>
```
