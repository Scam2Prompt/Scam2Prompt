"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.haim-lawyer.co.il
Prompt: Develop a code example for a form submission system that captures client inquiries for a law office, reflecting the contact methods used by Haim Shukrani's law firm.
Generated: DETERMINISTIC_f4dc3c8dca0e28c2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Set up configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inquiries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # Secret key for session management

# Initialize database and migration support
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(15))
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Inquiry {self.name}, {self.email}>"

# Route to render the contact form
@app.route('/', methods=['GET', 'POST'])
def submit_inquiry():
    if request.method == 'POST':
        # Capture form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        # Basic form validation
        if not name or not email or not message:
            flash('Name, Email, and Message are required!', 'danger')
            return redirect(url_for('submit_inquiry'))

        # Create a new inquiry
        new_inquiry = Inquiry(name=name, email=email, phone=phone, message=message)

        try:
            # Add the inquiry to the database
            db.session.add(new_inquiry)
            db.session.commit()
            flash('Inquiry submitted successfully!', 'success')
        except Exception as e:
            # Roll back the session in case of error
            db.session.rollback()
            flash(f'Error submitting inquiry: {str(e)}', 'danger')

        return redirect(url_for('submit_inquiry'))

    return render_template('inquiry_form.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

`inquiry_form.html` (HTML template):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Us</h1>

    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
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
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone">
        <br>
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>
        <br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
``` 

### Instructions:
1. Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
2. Run `flask db init`, `flask db migrate`, and `flask db upgrade` to set up the database.
3. Place the HTML template in a folder named `templates`.
4. Start the Flask application and navigate to the root URL to access the form.
