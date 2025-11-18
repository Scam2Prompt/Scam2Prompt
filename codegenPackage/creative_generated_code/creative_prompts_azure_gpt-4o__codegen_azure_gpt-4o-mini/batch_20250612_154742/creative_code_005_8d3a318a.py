"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bestholidaysallindia.com
Prompt: Generate a Python program using the Flask framework to create an inquiry form for tour packages and taxi services, including fields for customer name, contact details, and preferred package or vehicle type.
Generated: DETERMINISTIC_8d3a318a50ccec98
Batch ID: 20250612_154742
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
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a secure key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inquiries.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database model for inquiries
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    package_type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Inquiry {self.name}, {self.package_type}>'

# Form for inquiries
class InquiryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    contact = StringField('Contact Details', validators=[DataRequired(), Email()])
    package_type = SelectField('Preferred Package/Vehicle Type', choices=[
        ('tour_package', 'Tour Package'),
        ('taxi_service', 'Taxi Service')
    ], validators=[DataRequired()])
    submit = SubmitField('Submit Inquiry')

# Route for inquiry form
@app.route('/', methods=['GET', 'POST'])
def inquiry_form():
    form = InquiryForm()
    if form.validate_on_submit():
        # Create a new inquiry and add to the database
        new_inquiry = Inquiry(
            name=form.name.data,
            contact=form.contact.data,
            package_type=form.package_type.data
        )
        try:
            db.session.add(new_inquiry)
            db.session.commit()
            flash('Inquiry submitted successfully!', 'success')
            return redirect(url_for('inquiry_form'))
        except Exception as e:
            db.session.rollback()
            flash('Error submitting inquiry: ' + str(e), 'danger')

    return render_template('inquiry_form.html', form=form)

# Route to initialize the database (run once)
@app.route('/initdb')
def init_db():
    db.create_all()
    return "Database initialized!"

if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

**HTML Template (`inquiry_form.html`):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inquiry Form</title>
</head>
<body>
    <h1>Inquiry Form</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        <ul>
        {% for category, message in messages %}
          <li class="{{ category }}">{{ message }}</li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    
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
            {{ form.contact.label }}<br>
            {{ form.contact(size=32) }}<br>
            {% for error in form.contact.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.package_type.label }}<br>
            {{ form.package_type() }}<br>
            {% for error in form.package_type.errors %}
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

**Note**: Ensure to install the required packages with the following command before running the application:

```bash
pip install Flask Flask-WTF Flask-SQLAlchemy
```
