"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://askcardiologist.in
Prompt: Create a Flask application with a contact form for patients to request appointments and send inquiries to Dr. S. Nagendra Boopathy's email ([email protected]).
Generated: DETERMINISTIC_0dc308f6b8fdb2bd
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Set up secret key for flash messages
app.secret_key = os.urandom(24)

# Flask-Mail configuration for email sending
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Replace with sender's email
app.config['MAIL_PASSWORD'] = 'your-email-password'   # Replace with sender's email password
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'  # Replace with sender's email

mail = Mail(app)

# Route for the homepage with the contact form
@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        try:
            # Extract form data
            name = request.form.get('name')
            email = request.form.get('email')
            message = request.form.get('message')
            phone = request.form.get('phone')

            # Validate form data
            if not name or not email or not message:
                flash('All fields (Name, Email, and Message) are required!', 'error')
                return render_template('contact_form.html')

            # Create the email message
            msg = Message(
                subject=f"Appointment Request/Inquiry from {name}",
                recipients=['[email protected]'],  # Send to Dr. Nagendra Boopathy's email
                body=f"Name: {name}\nEmail: {email}\nPhone: {phone or 'N/A'}\n\nMessage:\n{message}"
            )

            # Send the email
            mail.send(msg)
            flash('Your inquiry has been sent successfully!', 'success')
        except Exception as e:
            flash(f"An error occurred while sending your message: {str(e)}", 'error')

    # Render the contact form template
    return render_template('contact_form.html')

# Contact form template (Inline here for complete solution; separate in production)
@app.route('/templates/contact_form.html')
def contact_form_template():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contact Dr. Nagendra Boopathy</title>
    </head>
    <body>
        <h1>Contact Dr. Nagendra Boopathy</h1>
        <form method="POST" action="/">
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name" required><br><br>

            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email" required><br><br>

            <label for="phone">Phone (Optional):</label><br>
            <input type="text" id="phone" name="phone"><br><br>

            <label for="message">Message:</label><br>
            <textarea id="message" name="message" required></textarea><br><br>

            <button type="submit">Submit</button>
        </form>
        {% with messages = get_flashed_messages(with_categories=true) %}
          {% if messages %}
            <ul>
              {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
              {% endfor %}
            </ul>
          {% endif %}
        {% endwith %}
    </body>
    </html>
    '''

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
