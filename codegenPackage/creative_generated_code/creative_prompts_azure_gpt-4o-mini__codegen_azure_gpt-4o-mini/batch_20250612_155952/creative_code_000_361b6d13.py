"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lzero.us
Prompt: Generate a code snippet for a registration form that allows users to sign up for basketball leagues at Courtside Fitness, incorporating fields for name, email, skill level, and preferred league.
Generated: DETERMINISTIC_361b6d13918c8406
Batch ID: 20250612_155952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leagues.db'  # Change to your database setup
db = SQLAlchemy(app)

# Create a database model for User Registration
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    skill_level = db.Column(db.String(50), nullable=False)
    preferred_league = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Registration {self.name}>'

# Define a Flask-WTF form for registration
class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    skill_level = SelectField('Skill Level', choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], validators=[DataRequired()])
    preferred_league = StringField('Preferred League', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Register')

# Route for the registration form
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Create a new registration entry
        new_registration = Registration(
            name=form.name.data,
            email=form.email.data,
            skill_level=form.skill_level.data,
            preferred_league=form.preferred_league.data
        )
        try:
            # Add new registration to the database
            db.session.add(new_registration)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('register'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash('Error occurred during registration. Please try again.', 'danger')

    return render_template('register.html', form=form)

# Create database tables
with app.app_context():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- register.html -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register for Basketball Leagues</title>
</head>
<body>
    <h1>Register for Basketball Leagues at Courtside Fitness</h1>
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
            {{ form.email.label }}<br>
            {{ form.email(size=32) }}<br>
            {% for error in form.email.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.skill_level.label }}<br>
            {{ form.skill_level() }}<br>
            {% for error in form.skill_level.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.preferred_league.label }}<br>
            {{ form.preferred_league(size=32) }}<br>
            {% for error in form.preferred_league.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>
    <a href="{{ url_for('register') }}">Back to registration</a>
</body>
</html>
```
