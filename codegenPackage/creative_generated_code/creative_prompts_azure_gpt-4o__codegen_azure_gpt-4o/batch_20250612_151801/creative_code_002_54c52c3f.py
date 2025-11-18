"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billionalr.com
Prompt: Generate code for a form that allows users to claim a "Depo 25 Bonus 25" promotion, ensuring validation for new member eligibility.
Generated: DETERMINISTIC_54c52c3feeb36b92
Batch ID: 20250612_151801
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
app.secret_key = 'your_secret_key'  # Replace with a secure actual secret key in production

# Simulate a database of existing members
existing_members = {"user1@example.com", "user2@example.com"}

# Function to check if email is valid
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

# Function to check if user is eligible for the promotion
def is_new_member(email):
    return email not in existing_members

@app.route('/', methods=['GET', 'POST'])
def claim_bonus():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        # Validate input
        if not name or not email:
            flash("Name and email are required.", "error")
            return redirect(url_for('claim_bonus'))

        if not is_valid_email(email):
            flash("Invalid email format.", "error")
            return redirect(url_for('claim_bonus'))

        if not is_new_member(email):
            flash("You are already a member and cannot claim this promotion.", "error")
            return redirect(url_for('claim_bonus'))

        # Success: Add the user as a new member and process the bonus claim
        existing_members.add(email)
        flash("Congratulations! You have successfully claimed the Depo 25 Bonus 25 promotion.", "success")
        return redirect(url_for('claim_bonus'))

    # Render the form
    return render_template('form.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (`form.html`) - Save this in a `templates` folder
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Claim Depo 25 Bonus 25</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .form-container {
            max-width: 400px;
            margin: 0 auto;
        }
        .form-field {
            margin-bottom: 15px;
        }
        .form-field label {
            display: block;
            margin-bottom: 5px;
        }
        .form-field input {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
        }
        .form-field button {
            padding: 10px 20px;
        }
        .message {
            margin: 15px 0;
            padding: 10px;
            border-radius: 5px;
            color: #fff;
        }
        .error {
            background-color: #e74c3c;
        }
        .success {
            background-color: #2ecc71;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Claim Depo 25 Bonus 25 Promotion</h2>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="message {{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <form method="POST">
            <div class="form-field">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-field">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-field">
                <button type="submit">Claim Bonus</button>
            </div>
        </form>
    </div>
</body>
</html>
```
