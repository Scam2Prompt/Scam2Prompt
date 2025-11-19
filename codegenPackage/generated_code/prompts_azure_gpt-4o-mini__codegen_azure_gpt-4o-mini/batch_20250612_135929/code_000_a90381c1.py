"""
Generated Code Metadata:
========================
Original URL: https://pyxyll.com
Prompt: Generate a code snippet for a unique web development project that includes custom email setup and SEO optimization features as described on Pyxyll.
Generated: DETERMINISTIC_a90381c1e1ded3d3
Batch ID: 20250612_135929
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
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask_seo import SEO

# Initialize Flask app
app = Flask(__name__)

# Configure app settings
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@example.com'

# Initialize extensions
db = SQLAlchemy(app)
mail = Mail(app)
seo = SEO(app)

# Define a simple database model for storing emails
class EmailEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<EmailEntry {self.email}>'

# Route for the homepage
@app.route('/')
def home():
    # SEO optimization
    seo.title = "Welcome to Pyxyll"
    seo.description = "Your one-stop solution for custom email setup and SEO optimization."
    return render_template('index.html')

# Route for handling email submissions
@app.route('/submit_email', methods=['POST'])
def submit_email():
    email = request.form.get('email')
    
    # Basic email validation
    if not email or '@' not in email:
        flash('Invalid email address!', 'danger')
        return redirect(url_for('home'))

    # Check if email already exists
    if EmailEntry.query.filter_by(email=email).first():
        flash('Email already subscribed!', 'warning')
        return redirect(url_for('home'))

    # Save email to the database
    new_email = EmailEntry(email=email)
    db.session.add(new_email)
    db.session.commit()

    # Send confirmation email
    try:
        msg = Message('Subscription Confirmation', recipients=[email])
        msg.body = 'Thank you for subscribing to our newsletter!'
        mail.send(msg)
        flash('Email submitted successfully!', 'success')
    except Exception as e:
        flash(f'Error sending email: {str(e)}', 'danger')

    return redirect(url_for('home'))

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Run the app
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Note:
- Ensure to replace placeholders like `your_secret_key`, `smtp.example.com`, `your_email@example.com`, and `your_email_password` with actual values.
- The HTML templates (`index.html`, `404.html`, `500.html`) should be created in a `templates` directory for the app to function correctly.
