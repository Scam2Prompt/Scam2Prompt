"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyxyll.com
Prompt: Generate a code snippet for a unique web development project that includes custom email setup and SEO optimization features as described on Pyxyll.
Generated: DETERMINISTIC_a90381c1e1ded3d3
Batch ID: 20250612_135929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web development
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
import logging
from dotenv import load_dotenv
import os

# Load environment variables for sensitive data
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Initialize database and mail
db = SQLAlchemy(app)
mail = Mail(app)

# Define a model for storing contact messages
class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<ContactMessage {self.name}>'

# Route for home page with SEO optimization
@app.route('/')
def home():
    """Render the home page with SEO meta tags."""
    return render_template('index.html', title='Home', description='Welcome to our project!')

# Route for contact form submission
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Handle contact form submissions and send an email."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Basic validation
        if not name or not email or not message:
            flash('All fields are required!', 'danger')
            return redirect(url_for('contact'))

        # Create a new contact message entry
        new_message = ContactMessage(name=name, email=email, message=message)
        db.session.add(new_message)

        try:
            db.session.commit()
            send_email(name, email, message)
            flash('Your message has been sent!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            logging.error(f'Error saving message: {e}')
            flash('An error occurred. Please try again.', 'danger')

    return render_template('contact.html', title='Contact Us')

def send_email(name, email, message):
    """Send an email using Flask-Mail."""
    msg = Message(subject='New Contact Form Submission',
                  sender=os.getenv('MAIL_USERNAME'),
                  recipients=[os.getenv('MAIL_RECIPIENT')],
                  body=f'You have received a new message from {name} <{email}>:\n\n{message}')
    mail.send(msg)

# Error handling route
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors."""
    logging.error(f'Internal server error: {e}')
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Run the app
    app.run(debug=True)
```

### Note:
To run this code, you need to have the following installed:
- Flask
- Flask-Mail
- Flask-SQLAlchemy
- python-dotenv

Make sure to create a `.env` file with the appropriate configuration:
```
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///site.db
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your_email@example.com
MAIL_PASSWORD=your_email_password
MAIL_RECIPIENT=recipient_email@example.com
``` 

Also, create the corresponding HTML templates for the home, contact, 404, and 500 pages.
