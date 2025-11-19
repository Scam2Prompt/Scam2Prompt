"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgcaugiay.com
Prompt: Generate a code snippet for a web application that allows users to register for a test drive of the MG G50, including fields for customer name, email, and vehicle model.
Generated: DETERMINISTIC_3564f13340665f0d
Batch ID: 20250612_162325
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
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email

# Create a new Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_drive.db'  # Database configuration
db = SQLAlchemy(app)

# Database model for Test Drive Registration
class TestDrive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    vehicle_model = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<TestDrive {self.customer_name}, {self.email}>'

# WTForms Form for registration
class TestDriveForm(FlaskForm):
    customer_name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    vehicle_model = StringField('Vehicle Model', default='MG G50', validators=[DataRequired()])
    submit = SubmitField('Register for Test Drive')

# Route for the registration page
@app.route('/', methods=['GET', 'POST'])
def register():
    form = TestDriveForm()
    if form.validate_on_submit():
        # Create a new registration entry
        new_registration = TestDrive(
            customer_name=form.customer_name.data,
            email=form.email.data,
            vehicle_model=form.vehicle_model.data
        )
        try:
            db.session.add(new_registration)
            db.session.commit()
            flash('Registration successful! We will contact you soon.', 'success')
            return redirect(url_for('register'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash('Error occurred while registering. Please try again.', 'danger')

    return render_template('register.html', form=form)

# Error handling for database initialization
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

**HTML Template (register.html)**:
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Test Drive Registration</title>
</head>
<body>
    <h1>Register for a Test Drive of MG G50</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <div>
            {{ form.customer_name.label }}<br>
            {{ form.customer_name(size=32) }}<br>
            {% for error in form.customer_name.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.email.label }}<br>
            {{ form.email(size=32) }}<br>
            {% for error in form.email.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.vehicle_model.label }}<br>
            {{ form.vehicle_model(size=32) }}<br>
            {% for error in form.vehicle_model.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.submit() }}
        </div>
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
```
