"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-sync.com
Prompt: Generate code for creating a free digital design consultation form, similar to the "Get Started" feature on Sync Media's website.
Generated: DETERMINISTIC_2d902683182b031e
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# digital_consultation_form.py

from flask import Flask, render_template, request, redirect, url_for, flash
import re

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Secret key for flash messages

# Regular expression for validating email addresses
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

# Route for the homepage and form
@app.route("/", methods=["GET", "POST"])
def consultation_form():
    if request.method == "POST":
        # Extract form data
        name = request.form.get("name")
        email = request.form.get("email")
        business_name = request.form.get("business_name")
        design_needs = request.form.get("design_needs")

        # Form validation
        errors = []
        if not name or len(name.strip()) == 0:
            errors.append("Name is required.")
        if not email or not EMAIL_REGEX.match(email):
            errors.append("A valid email address is required.")
        if not business_name or len(business_name.strip()) == 0:
            errors.append("Business name is required.")
        if not design_needs or len(design_needs.strip()) == 0:
            errors.append("Design needs are required.")

        # If there are errors, flash them and reload the form
        if errors:
            for error in errors:
                flash(error, "error")
            return render_template("form.html")

        # Here you can handle the form submission (e.g., save to a database, send an email, etc.)
        # For now, we redirect to a "success" page
        flash("Thank you for your submission! We'll get back to you soon.", "success")
        return redirect(url_for("thank_you"))

    # Render the consultation form
    return render_template("form.html")

# Route for the thank you page
@app.route("/thank-you", methods=["GET"])
def thank_you():
    return render_template("thank_you.html")

# Code execution entry point
if __name__ == "__main__":
    app.run(debug=True)

```

**`templates/form.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Digital Design Consultation</title>
</head>
<body>
    <h1>Get Started with Your Free Digital Design Consultation</h1>
    
    <!-- Display flash messages -->
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
                {% for category, message in messages %}
                    <li style="color: {{ 'red' if category == 'error' else 'green' }}">{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    
    <!-- Consultation form -->
    <form method="POST">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="business_name">Business Name:</label><br>
        <input type="text" id="business_name" name="business_name" required><br><br>

        <label for="design_needs">What are your design needs?</label><br>
        <textarea id="design_needs" name="design_needs" rows="5" required></textarea><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

**`templates/thank_you.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thank You</title>
</head>
<body>
    <h1>Thank You!</h1>
    <p>We appreciate your submission and will get back to you shortly.</p>
    <a href="/">Back to Home</a>
</body>
</html>
```

### Notes:
- Install Flask (`pip install flask`) before running this code.
- Replace `your_secret_key` with a secure random key for production use.
