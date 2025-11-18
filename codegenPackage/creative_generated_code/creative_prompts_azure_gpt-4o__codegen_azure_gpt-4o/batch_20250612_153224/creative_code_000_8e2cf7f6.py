"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topgraininteriors.com
Prompt: Write a script to generate a contact form for a custom cabinetry business, including fields for name, email, phone number, and project details, and ensure the form sends submissions to "misho@topgraininteriors.com".
Generated: DETERMINISTIC_8e2cf7f6a4047ad0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, render_template, redirect, flash
from flask_mail import Mail, Message
import os

# Initialize Flask app
app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Use your email provider's SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # Set environment variable with your email
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  # Set environment variable with your email password
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')  # Default sender email
mail = Mail(app)

# Secret key for flash messages
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

@app.route('/')
def contact_form():
    """
    Render the contact form page.
    """
    return render_template('contact_form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    """
    Handle form submission and send the email.
    """
    try:
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        project_details = request.form.get('project_details')

        # Validate form data
        if not name or not email or not phone or not project_details:
            flash("All fields are required.", "error")
            return redirect('/')

        # Create email message
        msg = Message(
            subject="New Contact Form Submission",
            recipients=["misho@topgraininteriors.com"],  # Target email
            body=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nProject Details: {project_details}"
        )

        # Send email
        mail.send(msg)

        flash("Your message has been sent successfully!", "success")
        return redirect('/')
    except Exception as e:
        # Log error (optional) and show error message
        flash("An error occurred while sending your message. Please try again later.", "error")
        print(f"Error: {e}")
        return redirect('/')

# HTML template for the contact form
@app.route('/contact_form.html')
def contact_form_template():
    """
    Serve the contact form HTML template.
    """
    # This is the HTML template. Save this content in a file named `templates/contact_form.html` in your project folder.
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contact Form</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            form { max-width: 600px; margin: auto; }
            label { display: block; margin: 10px 0 5px; }
            input, textarea { width: 100%; padding: 10px; margin-bottom: 20px; border: 1px solid #ccc; border-radius: 5px; }
            button { padding: 10px 15px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer; }
            button:hover { background-color: #0056b3; }
            .flash { margin: 20px 0; padding: 10px; border-radius: 5px; }
            .flash.success { background-color: #d4edda; color: #155724; }
            .flash.error { background-color: #f8d7da; color: #721c24; }
        </style>
    </head>
    <body>
        <h1>Contact Us</h1>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="flash {{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <form action="/submit" method="POST">
            <label for="name">Name</label>
            <input type="text" id="name" name="name" required>
            
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required>
            
            <label for="phone">Phone Number</label>
            <input type="tel" id="phone" name="phone" required>
            
            <label for="project_details">Project Details</label>
            <textarea id="project_details" name="project_details" rows="5" required></textarea>
            
            <button type="submit">Submit</button>
        </form>
    </body>
    </html>
    """

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
