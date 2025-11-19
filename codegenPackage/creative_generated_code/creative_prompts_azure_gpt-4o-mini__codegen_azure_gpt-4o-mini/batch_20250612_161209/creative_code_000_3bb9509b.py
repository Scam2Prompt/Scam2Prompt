"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starmissteenindia.com
Prompt: How can I implement a registration form for a modeling competition similar to Star Miss Teen India 2025, including fields for personal details and payment confirmation?
Generated: DETERMINISTIC_3bb9509bdf6c7f89
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registrations.db'  # Database URI
db = SQLAlchemy(app)

# Model for storing registration data
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    payment_confirmed = db.Column(db.Boolean, default=False)

# Form for user registration
class RegistrationForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(max=100)])
    age = IntegerField('Age', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    payment_confirmed = BooleanField('Payment Confirmed')
    submit = SubmitField('Register')

# Home route to display the registration form
@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            # Create a new registration entry
            new_registration = Registration(
                name=form.name.data,
                age=form.age.data,
                email=form.email.data,
                payment_confirmed=form.payment_confirmed.data
            )
            # Add and commit the new registration to the database
            db.session.add(new_registration)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('register'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(f'Error occurred: {str(e)}', 'danger')
    return render_template('registration_form.html', form=form)

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug to False in production
```

**HTML Template (templates/registration_form.html):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modeling Competition Registration</title>
</head>
<body>
    <h1>Modeling Competition Registration</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <div>
            {{ form.name.label }}<br>
            {{ form.name(size=32) }}<br>
            {% for error in form.name.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.age.label }}<br>
            {{ form.age(size=32) }}<br>
            {% for error in form.age.errors %}
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
            {{ form.payment_confirmed.label }} {{ form.payment_confirmed() }}
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

**Note:** Make sure to install the necessary packages using pip before running the application:
```bash
pip install Flask Flask-WTF Flask-SQLAlchemy
```
