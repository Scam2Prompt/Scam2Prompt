"""
Generated Code Metadata:
========================
Original URL: https://rapidresponder.net
Prompt: Suggest libraries or frameworks for building a consultation form similar to Rapid Responder's, with fields for name, email, country, phone number, and optional messages.
Generated: DETERMINISTIC_af940feda4121bd4
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consultations.db'  # Database URI
db = SQLAlchemy(app)

# Define the Consultation model
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    message = db.Column(db.Text, nullable=True)

# Define the form for consultations
class ConsultationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    country = SelectField('Country', choices=[('US', 'United States'), ('CA', 'Canada'), ('UK', 'United Kingdom')], validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(max=15)])
    message = TextAreaField('Message', validators=[Length(max=500)])
    submit = SubmitField('Submit')

# Route for the consultation form
@app.route('/', methods=['GET', 'POST'])
def consultation():
    form = ConsultationForm()
    if form.validate_on_submit():
        # Create a new consultation entry
        new_consultation = Consultation(
            name=form.name.data,
            email=form.email.data,
            country=form.country.data,
            phone_number=form.phone_number.data,
            message=form.message.data
        )
        try:
            db.session.add(new_consultation)
            db.session.commit()
            flash('Your consultation request has been submitted!', 'success')
            return redirect(url_for('consultation'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash('An error occurred while submitting your request. Please try again.', 'danger')
            print(f"Error: {e}")  # Log the error for debugging

    return render_template('consultation.html', form=form)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

**HTML Template (consultation.html)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consultation Form</title>
</head>
<body>
    <h1>Consultation Form</h1>
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
            {{ form.email.label }}<br>
            {{ form.email(size=32) }}<br>
            {% for error in form.email.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.country.label }}<br>
            {{ form.country() }}<br>
            {% for error in form.country.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.phone_number.label }}<br>
            {{ form.phone_number(size=32) }}<br>
            {% for error in form.phone_number.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.message.label }}<br>
            {{ form.message(cols=30, rows=5) }}<br>
            {% for error in form.message.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.submit() }}
        </p>
    </form>
</body>
</html>
```
