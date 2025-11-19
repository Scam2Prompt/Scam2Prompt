"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hsrenterprises.co.in
Prompt: Suggest a library for building a contact form that captures inquiries for Royal Enfield pre-owned motorcycles, ensuring it includes validation for phone numbers and emails.
Generated: DETERMINISTIC_ddac151a3ea220cf
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, request, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inquiries.db'
db = SQLAlchemy(app)

# Define the Inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(15), nullable=False)

# Create a form for inquiries
class InquiryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired(), Regexp(r'^\+?1?\d{9,15}$', message="Invalid phone number")])
    submit = SubmitField('Submit Inquiry')

# Route to display and process the contact form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = InquiryForm()
    if form.validate_on_submit():
        try:
            # Create a new inquiry instance
            new_inquiry = Inquiry(name=form.name.data, email=form.email.data, phone=form.phone.data)
            db.session.add(new_inquiry)
            db.session.commit()
            flash('Inquiry submitted successfully!', 'success')
            return redirect(url_for('contact'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash('An error occurred while submitting your inquiry. Please try again.', 'danger')
            app.logger.error(f'Error submitting inquiry: {e}')
    return render_template('contact.html', form=form)

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
```

**Note:** This code requires Flask, Flask-WTF, and Flask-SQLAlchemy to be installed. Ensure you have a `contact.html` template to render the form. Remember to set `SECRET_KEY` to a strong, unique value for production use.
