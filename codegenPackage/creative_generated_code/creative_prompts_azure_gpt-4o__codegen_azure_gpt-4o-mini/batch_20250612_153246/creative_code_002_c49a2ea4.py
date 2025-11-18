"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalityholistic.co.uk
Prompt: Generate code using a web development framework (e.g., Django or Flask) to implement a contact form for a holistic therapy clinic, ensuring fields for therapy type, preferred appointment time, and client details.
Generated: DETERMINISTIC_c49a2ea4214b5369
Batch ID: 20250612_153246
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
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TimeField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application and configure the database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact_form.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Contact model to store form submissions
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    therapy_type = db.Column(db.String(100), nullable=False)
    appointment_time = db.Column(db.String(5), nullable=False)
    client_details = db.Column(db.String(200), nullable=False)

# Define the form class for the contact form
class ContactForm(FlaskForm):
    therapy_type = SelectField('Therapy Type', choices=[
        ('massage', 'Massage Therapy'),
        ('acupuncture', 'Acupuncture'),
        ('counseling', 'Counseling'),
        ('yoga', 'Yoga')
    ], validators=[DataRequired()])
    appointment_time = TimeField('Preferred Appointment Time', format='%H:%M', validators=[DataRequired()])
    client_details = StringField('Client Details', validators=[DataRequired(), Length(max=200)])
    submit = SubmitField('Submit')

# Route to display and handle the contact form
@app.route('/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        try:
            # Create a new Contact entry
            new_contact = Contact(
                therapy_type=form.therapy_type.data,
                appointment_time=form.appointment_time.data.strftime('%H:%M'),
                client_details=form.client_details.data
            )
            db.session.add(new_contact)
            db.session.commit()
            flash('Your request has been submitted successfully!', 'success')
            return redirect(url_for('contact'))
        except Exception as e:
            # Handle any errors that occur during database operations
            db.session.rollback()
            flash(f'An error occurred: {str(e)}', 'danger')
    return render_template('contact.html', form=form)

# Ensure database tables are created
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/contact.html -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Contact Form</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Contact Us</h1>
        <form method="POST" class="mt-4">
            {{ form.hidden_tag() }}
            <div class="form-group">
                {{ form.therapy_type.label(class="form-label") }}
                {{ form.therapy_type(class="form-control") }}
                {% for error in form.therapy_type.errors %}
                    <div class="alert alert-danger">{{ error }}</div>
                {% endfor %}
            </div>
            <div class="form-group">
                {{ form.appointment_time.label(class="form-label") }}
                {{ form.appointment_time(class="form-control") }}
                {% for error in form.appointment_time.errors %}
                    <div class="alert alert-danger">{{ error }}</div>
                {% endfor %}
            </div>
            <div class="form-group">
                {{ form.client_details.label(class="form-label") }}
                {{ form.client_details(class="form-control") }}
                {% for error in form.client_details.errors %}
                    <div class="alert alert-danger">{{ error }}</div>
                {% endfor %}
            </div>
            <div class="form-group">
                {{ form.submit(class="btn btn-primary") }}
            </div>
        </form>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <div class="mt-3">
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

### Instructions for Setup:
- Install the required packages:
    ```bash
    pip install flask flask-wtf flask-sqlalchemy
    ```
- Save the provided Python code in a file named `app.py`.
- Save the HTML code in a folder named `templates` as `contact.html`.
- Run the application:
    ```bash
    python app.py
    ```

### Note:
Make sure to replace `'your_secret_key'` with a proper secret key in a production setting.
