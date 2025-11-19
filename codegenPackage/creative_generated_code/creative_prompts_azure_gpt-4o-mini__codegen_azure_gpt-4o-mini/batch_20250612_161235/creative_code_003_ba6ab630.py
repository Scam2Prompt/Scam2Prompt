"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fijimaths.com
Prompt: Develop a web application using Flask that allows teachers to submit student registrations for the FMC and TMC competitions.
Generated: DETERMINISTIC_ba6ab630c1d9d016
Batch ID: 20250612_161235
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
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registrations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for student registration
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    competition = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Registration {self.name}, Age: {self.age}, Competition: {self.competition}>'

# Home route that renders the registration form
@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            # Create a new registration instance
            new_registration = Registration(
                name=form.name.data,
                age=form.age.data,
                competition=form.competition.data
            )
            # Add the new registration to the database
            db.session.add(new_registration)
            db.session.commit()
            flash('Registration submitted successfully!', 'success')
            return redirect(url_for('register'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error occurred: {str(e)}', 'danger')
    
    return render_template('register.html', form=form)

# Run the app
if __name__ == '__main__':
    with app.app_context():
        # Create database tables if they don't exist
        db.create_all()
    app.run(debug=True)
```

**forms.py**
```python
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class RegistrationForm(FlaskForm):
    name = StringField('Student Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=5, max=18)])
    competition = SelectField('Competition', choices=[('FMC', 'FMC'), ('TMC', 'TMC')], validators=[DataRequired()])
    submit = SubmitField('Register')
```

**register.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Registration</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Student Registration for FMC/TMC</h1>
        <form method="POST" class="mt-4">
            {{ form.hidden_tag() }}
            <div class="form-group">
                {{ form.name.label(class='form-label') }}
                {{ form.name(class='form-control') }}
            </div>
            <div class="form-group">
                {{ form.age.label(class='form-label') }}
                {{ form.age(class='form-control') }}
            </div>
            <div class="form-group">
                {{ form.competition.label(class='form-label') }}
                {{ form.competition(class='form-control') }}
            </div>
            <div class="form-group">
                {{ form.submit(class='btn btn-primary') }}
            </div>
        </form>
        {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
        <div class="mt-4">
            {% for category, message in messages %}
                <div class="alert alert-{{ category }}">{{ message }}</div>
            {% endfor %}
        </div>
        {% endif %}
        {% endwith %}
    </div>
</body>
</html>
```

**Instructions for Setup:**
1. Install Flask and Flask-WTF:
   ```bash
   pip install Flask Flask-WTF Flask-SQLAlchemy
   ```
2. Create the necessary directories and files:
   - `app.py` for the main application code.
   - `forms.py` for the form handling.
   - `templates/register.html` for the HTML form.
3. Run the Flask application:
   ```bash
   python app.py
   ```
