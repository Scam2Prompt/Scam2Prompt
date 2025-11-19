"""
Generated Code Metadata:
========================
Original URL: https://prc-board.com
Prompt: Create a sample code for a registration form that can be used for DSWD junior high school or elementary registration online.
Generated: DETERMINISTIC_ab1ee6e301e7dc00
Batch ID: 20250622_211113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, IntegerField, SelectField, validators

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registrations.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db = SQLAlchemy(app)

# Database model for registration
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade_level = db.Column(db.String(50), nullable=False)

# Form for registration
class RegistrationForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=100)])
    age = IntegerField('Age', [validators.NumberRange(min=5, max=18)])
    grade_level = SelectField('Grade Level', choices=[('Elementary', 'Elementary'), ('Junior High', 'Junior High')])

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # Create a new registration entry
        new_registration = Registration(
            name=form.name.data,
            age=form.age.data,
            grade_level=form.grade_level.data
        )
        try:
            db.session.add(new_registration)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('register'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(f'Error occurred: {str(e)}', 'danger')
    return render_template('register.html', form=form)

@app.route('/registrations')
def registrations():
    # Fetch all registrations from the database
    registrations = Registration.query.all()
    return render_template('registrations.html', registrations=registrations)

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**HTML Templates:**

1. `register.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Form</title>
</head>
<body>
    <h1>DSWD Registration Form</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <p>
            {{ form.name.label }}<br>
            {{ form.name(size=32) }}<br>
            {% for error in form.name.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.age.label }}<br>
            {{ form.age(size=3) }}<br>
            {% for error in form.age.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.grade_level.label }}<br>
            {{ form.grade_level() }}<br>
            {% for error in form.grade_level.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p><input type="submit" value="Register"></p>
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

2. `registrations.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registrations List</title>
</head>
<body>
    <h1>Registered Students</h1>
    <table>
        <tr>
            <th>Name</th>
            <th>Age</th>
            <th>Grade Level</th>
        </tr>
        {% for registration in registrations %}
        <tr>
            <td>{{ registration.name }}</td>
            <td>{{ registration.age }}</td>
            <td>{{ registration.grade_level }}</td>
        </tr>
        {% endfor %}
    </table>
    <a href="{{ url_for('register') }}">Back to Registration</a>
</body>
</html>
```

**Note:** Ensure you have Flask, Flask-SQLAlchemy, and WTForms installed in your environment. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy WTForms
```
