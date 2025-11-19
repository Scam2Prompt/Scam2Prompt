"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esofa.edu.pe
Prompt: Generate a code snippet for a web application that allows users to apply for admission to the Escuela de Suboficiales de la Fuerza Aérea del Perú, including fields for personal information and program selection.
Generated: DETERMINISTIC_5ab873096d4a3399
Batch ID: 20250612_162220
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
from wtforms import StringField, SelectField, SubmitField, validators
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admissions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database model for admission applications
class AdmissionApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    selected_program = db.Column(db.String(50), nullable=False)

# Form for admission application
class AdmissionForm(FlaskForm):
    full_name = StringField('Full Name', [validators.InputRequired()])
    email = StringField('Email', [validators.InputRequired(), validators.Email()])
    selected_program = SelectField('Program Selection', choices=[
        ('Pilot', 'Pilot'),
        ('Engineer', 'Engineer'),
        ('Technician', 'Technician'),
        ('Navigator', 'Navigator')
    ], validators=[validators.InputRequired()])
    submit = SubmitField('Apply')

@app.route('/', methods=['GET', 'POST'])
def apply():
    form = AdmissionForm()
    if form.validate_on_submit():
        try:
            # Create a new admission application
            new_application = AdmissionApplication(
                full_name=form.full_name.data,
                email=form.email.data,
                selected_program=form.selected_program.data
            )
            db.session.add(new_application)
            db.session.commit()
            flash('Your application has been submitted successfully!', 'success')
            return redirect(url_for('apply'))
        except Exception as e:
            # Handle database errors
            db.session.rollback()
            flash(f'An error occurred while submitting your application: {e}', 'danger')
    return render_template('apply.html', form=form)

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    # Run the Flask application
    app.run(debug=True)
```

```html
<!-- templates/apply.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admission Application</title>
</head>
<body>
    <h1>Apply for Admission</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <div>
            {{ form.full_name.label }}<br>
            {{ form.full_name(size=32) }}<br>
            {% for error in form.full_name.errors %}
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
            {{ form.selected_program.label }}<br>
            {{ form.selected_program() }}<br>
            {% for error in form.selected_program.errors %}
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
