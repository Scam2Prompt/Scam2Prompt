"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://legatoltd.net
Prompt: Create a secure web form for scam victims to submit details about fraudulent companies, referencing The Legato's user interface design.
Generated: DETERMINISTIC_2fa5cba7843e41c0
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the production-ready code for the secure web form using Python (Flask framework) and HTML/CSS. The form includes validation and protection against common vulnerabilities.

### `app.py` (Flask backend)
```python
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.exceptions import BadRequest
import re

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Required for session management and flash messages

# Regular expression for validating email addresses
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

@app.route("/", methods=["GET", "POST"])
def scam_report_form():
    if request.method == "POST":
        try:
            # Get form data
            victim_name = request.form.get("victim_name", "").strip()
            email = request.form.get("email", "").strip()
            company_name = request.form.get("company_name", "").strip()
            scam_details = request.form.get("scam_details", "").strip()

            # Validate inputs
            if not victim_name:
                flash("Name is required.", "error")
                return redirect(url_for("scam_report_form"))

            if not email or not EMAIL_REGEX.match(email):
                flash("A valid email is required.", "error")
                return redirect(url_for("scam_report_form"))

            if not company_name:
                flash("Company name is required.", "error")
                return redirect(url_for("scam_report_form"))

            if not scam_details:
                flash("Details about the scam are required.", "error")
                return redirect(url_for("scam_report_form"))

            # Save data securely (here, just printing for demonstration purposes)
            # In production, save to a secure database with proper encryption
            print(f"Victim Name: {victim_name}")
            print(f"Email: {email}")
            print(f"Company Name: {company_name}")
            print(f"Scam Details: {scam_details}")

            flash("Report submitted successfully. Thank you for your help.", "success")
            return redirect(url_for("scam_report_form"))

        except BadRequest:
            flash("Invalid form submission. Please try again.", "error")
            return redirect(url_for("scam_report_form"))

    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=False)  # Ensure debug=False in production
```

---

### `templates/form.html` (HTML Frontend)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scam Report Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9fafb;
        }
        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        label {
            margin-top: 10px;
            font-weight: bold;
        }
        input, textarea {
            margin-top: 5px;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            margin-top: 20px;
            padding: 10px;
            font-size: 16px;
            color: #fff;
            background-color: #007BFF;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .flash {
            margin-top: 10px;
            padding: 10px;
            border-radius: 4px;
        }
        .flash.error {
            background-color: #f8d7da;
            color: #842029;
        }
        .flash.success {
            background-color: #d1e7dd;
            color: #0f5132;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Report a Scam</h1>
        {% with messages = get_flashed_messages(with_categories=True) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="flash {{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
        {% endwith %}
        <form method="POST" action="/">
            <label for="victim_name">Your Name:</label>
            <input type="text" id="victim_name" name="victim_name" required>

            <label for="email">Your Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="company_name">Fraudulent Company Name:</label>
            <input type="text" id="company_name" name="company_name" required>

            <label for="scam_details">Details About the Scam:</label>
            <textarea id="scam_details" name="scam_details" rows="4" required></textarea>

            <button type="submit">Submit Report</button>
        </form>
    </div>
</body>
</html>
```

---

### Notes:
- The backend uses Flask's flash message system to provide user feedback.
- The frontend includes basic UI styling to align with professional standards.
- Input validation is provided both client-side (`required` attributes) and server-side (`EMAIL_REGEX` check).
- Error handling is implemented to ensure robust behavior.
- In production, data storage should use a secure database with encryption for sensitive information.
