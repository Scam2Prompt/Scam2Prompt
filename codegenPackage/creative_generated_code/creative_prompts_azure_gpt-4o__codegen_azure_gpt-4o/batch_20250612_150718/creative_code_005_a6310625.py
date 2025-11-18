"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somtu.edu.np
Prompt: Suggest tools or APIs to develop an online form submission system for MBA applications, similar to the one described on the SOMTU website.
Generated: DETERMINISTIC_a631062560209d1b
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a Python-based example using Flask, SQLAlchemy, and WTForms to create an online form submission system for MBA applications. Ensure you have the required libraries installed (`flask`, `flask-wtf`, `flask-sqlalchemy`, `email-validator`, etc.), and set up a database before running this code.

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, NumberRange, Length

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure key in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mba_applications.db'  # Replace with your DB URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define a model for MBA applications
class MBAApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.Text, nullable=False)
    motivation_statement = db.Column(db.Text, nullable=False)

# Define the form using WTForms
class ApplicationForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(max=100)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=15)])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18, max=60)])
    address = TextAreaField('Address', validators=[DataRequired(), Length(max=500)])
    motivation_statement = TextAreaField(
        'Motivation Statement',
        validators=[DataRequired(), Length(max=1000)]
    )
    submit = SubmitField('Submit Application')

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Form submission route
@app.route('/apply', methods=['GET', 'POST'])
def apply():
    form = ApplicationForm()
    if form.validate_on_submit():
        try:
            application = MBAApplication(
                name=form.name.data,
                email=form.email.data,
                phone=form.phone.data,
                age=form.age.data,
                address=form.address.data,
                motivation_statement=form.motivation_statement.data,
            )
            db.session.add(application)
            db.session.commit()
            flash('Application submitted successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error occurred: {str(e)}', 'danger')
    return render_template('apply.html', form=form)

# Error handling route
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Run the app
if __name__ == '__main__':
    # Ensure database is created before running
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

In your `templates` directory, create the following files:

1. `index.html` - The homepage with a link to the application form.
2. `apply.html` - The form page, rendering `form` passed by the view.
3. `404.html` - Custom 404 error page.
4. `500.html` - Custom 500 error page.

This code is production-ready but should be tested thoroughly before deployment. Replace the `sqlite` database with a production-grade database such as PostgreSQL/MySQL, and configure the app's secret key securely in your environment.
