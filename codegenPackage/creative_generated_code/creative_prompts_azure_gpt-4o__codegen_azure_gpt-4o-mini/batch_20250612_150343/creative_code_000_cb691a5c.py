"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wingerrandr.ca
Prompt: Write a Python script to create a web form for customers to request services like "window and door installation" or "bathroom updating" from Winger R&R, including fields for name, contact information, and service type.
Generated: DETERMINISTIC_cb691a5c23ccd0bb
Batch ID: 20250612_150343
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

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key in production

# Define the service request form using Flask-WTF
class ServiceRequestForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    service_type = SelectField('Service Type', choices=[
        ('window_door_installation', 'Window and Door Installation'),
        ('bathroom_updating', 'Bathroom Updating')
    ], validators=[DataRequired()])
    submit = SubmitField('Request Service')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ServiceRequestForm()
    if form.validate_on_submit():
        # Process the form data
        name = form.name.data
        email = form.email.data
        service_type = form.service_type.data
        
        # Here you would typically handle saving the request to a database or sending an email

        flash('Service request submitted successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('index.html', form=form)

if __name__ == '__main__':
    # Run the application in debug mode for development; set to False in production
    app.run(debug=True)
```

**HTML Template (templates/index.html):**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Request Form</title>
</head>
<body>
    <h1>Request a Service from Winger R&R</h1>
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
            {{ form.service_type.label }}<br>
            {{ form.service_type() }}<br>
            {% for error in form.service_type.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>{{ form.submit() }}</p>
    </form>
    {% with messages = get_flashed_messages(with_categories=True) %}
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

**Requirements to run the code:**
- Install Flask and Flask-WTF:
```bash
pip install Flask Flask-WTF
```

**Note:** Ensure to replace `'your_secret_key'` with a strong, unique secret key in a production environment.
