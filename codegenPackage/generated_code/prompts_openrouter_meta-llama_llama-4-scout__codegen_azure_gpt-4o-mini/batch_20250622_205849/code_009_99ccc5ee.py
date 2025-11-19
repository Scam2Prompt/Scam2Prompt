"""
Generated Code Metadata:
========================
Original URL: https://rspbharat.com
Prompt: "Outline a basic structure for a career guidance and counseling website, inspired by RSP Bharat's Diploma in Career Guidance & Counseling course."
Generated: DETERMINISTIC_99ccc5ee14a9e2ef
Batch ID: 20250622_205849
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
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import ContactForm  # Assuming forms.py contains the ContactForm class

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///career_guidance.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the database model for user inquiries
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Inquiry {self.name}>'

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Render the home page template

# Route for the career guidance page
@app.route('/career-guidance')
def career_guidance():
    return render_template('career_guidance.html')  # Render the career guidance page

# Route for the contact form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()  # Instantiate the contact form
    if form.validate_on_submit():  # Check if the form is submitted and valid
        try:
            # Create a new inquiry and add it to the database
            new_inquiry = Inquiry(name=form.name.data, email=form.email.data, message=form.message.data)
            db.session.add(new_inquiry)
            db.session.commit()
            flash('Your inquiry has been submitted successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash('An error occurred while submitting your inquiry. Please try again.', 'danger')
            app.logger.error(f'Error while submitting inquiry: {e}')  # Log the error
    return render_template('contact.html', form=form)  # Render the contact page with the form

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404  # Render a custom 404 error page

# Error handling for 500
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500  # Render a custom 500 error page

# Main entry point for the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```

### Directory Structure
```
/career_guidance_website
│
├── app.py                # Main application file
├── forms.py              # Contains form classes
├── templates/            # HTML templates
│   ├── index.html        # Home page template
│   ├── career_guidance.html  # Career guidance page template
│   ├── contact.html      # Contact form template
│   ├── 404.html          # Custom 404 error page
│   └── 500.html          # Custom 500 error page
└── requirements.txt      # List of dependencies
```

### requirements.txt
```
Flask
Flask-SQLAlchemy
Flask-Migrate
Flask-WTF
```

### forms.py
```python
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')
```
