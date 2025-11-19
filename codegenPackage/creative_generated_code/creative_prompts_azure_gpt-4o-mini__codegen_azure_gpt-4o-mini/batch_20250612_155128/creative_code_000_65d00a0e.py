"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ogma.ca
Prompt: Generate a code snippet for a web application that allows users to register for the OGMA Spring Golf Tournament, including fields for name, email, and golf skill level.
Generated: DETERMINISTIC_65d00a0e82754e75
Batch ID: 20250612_155128
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tournament.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for storing participant information
class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    skill_level = db.Column(db.String(50), nullable=False)

# Form for user registration
class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    skill_level = SelectField('Golf Skill Level', choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ], validators=[DataRequired()])
    submit = SubmitField('Register')

# Route for the registration page
@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Try to add the participant to the database
        try:
            participant = Participant(
                name=form.name.data,
                email=form.email.data,
                skill_level=form.skill_level.data
            )
            db.session.add(participant)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('register'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash('Registration failed. Please try again.', 'danger')
            print(f"Error: {e}")  # Log error for debugging
    return render_template('register.html', form=form)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (register.html)**:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OGMA Spring Golf Tournament Registration</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Register for the OGMA Spring Golf Tournament</h1>

        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        <form method="POST" class="mt-3">
            {{ form.hidden_tag() }}
            <div class="form-group">
                {{ form.name.label(class="form-label") }}
                {{ form.name(class="form-control") }}
                {% if form.name.errors %}
                    <div class="text-danger">{{ form.name.errors[0] }}</div>
                {% endif %}
            </div>
            <div class="form-group">
                {{ form.email.label(class="form-label") }}
                {{ form.email(class="form-control") }}
                {% if form.email.errors %}
                    <div class="text-danger">{{ form.email.errors[0] }}</div>
                {% endif %}
            </div>
            <div class="form-group">
                {{ form.skill_level.label(class="form-label") }}
                {{ form.skill_level(class="form-control") }}
                {% if form.skill_level.errors %}
                    <div class="text-danger">{{ form.skill_level.errors[0] }}</div>
                {% endif %}
            </div>
            <div class="form-group">
                {{ form.submit(class="btn btn-primary") }}
            </div>
        </form>
    </div>
</body>
</html>
```
