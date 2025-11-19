"""
Generated Code Metadata:
========================
Original URL: https://plus.endeavorschools.com
Prompt: Illustrate how to implement a web form for parents to enroll their children in the Endeavor Plus programs, focusing on the required fields and validation.
Generated: DETERMINISTIC_e488cdd49dc66014
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from wtforms import Form, StringField, IntegerField, SelectField, validators

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

# Define the enrollment form using WTForms
class EnrollmentForm(Form):
    parent_name = StringField('Parent Name', [
        validators.DataRequired(message="Parent name is required."),
        validators.Length(min=2, max=50, message="Name must be between 2 and 50 characters.")
    ])
    email = StringField('Email', [
        validators.DataRequired(message="Email is required."),
        validators.Email(message="Invalid email address.")
    ])
    phone = StringField('Phone Number', [
        validators.DataRequired(message="Phone number is required."),
        validators.Regexp(r'^\+?1?\d{9,15}$', message="Invalid phone number format.")
    ])
    child_name = StringField('Child Name', [
        validators.DataRequired(message="Child name is required."),
        validators.Length(min=2, max=50, message="Name must be between 2 and 50 characters.")
    ])
    child_age = IntegerField('Child Age', [
        validators.DataRequired(message="Child age is required."),
        validators.NumberRange(min=3, max=18, message="Age must be between 3 and 18.")
    ])
    program = SelectField('Program', choices=[
        ('science', 'Science Exploration'),
        ('math', 'Math Enrichment'),
        ('art', 'Creative Arts'),
        ('sports', 'Sports and Fitness')
    ], validators=[validators.DataRequired(message="Please select a program.")])

# Route to display the enrollment form
@app.route('/enroll', methods=['GET', 'POST'])
def enroll():
    form = EnrollmentForm(request.form)
    if request.method == 'POST' and form.validate():
        # Process the form data (e.g., save to database)
        parent_name = form.parent_name.data
        email = form.email.data
        phone = form.phone.data
        child_name = form.child_name.data
        child_age = form.child_age.data
        program = form.program.data

        # Simulate saving to a database or performing other actions
        flash(f"Enrollment successful for {child_name} in the {program} program!", 'success')
        return redirect(url_for('enroll'))

    # If GET request or validation fails, render the form
    return render_template('enroll.html', form=form)

# HTML template for the form (to be saved as 'templates/enroll.html')
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Endeavor Plus Enrollment</title>
</head>
<body>
    <h1>Enroll Your Child in Endeavor Plus Programs</h1>
    <form method="POST" action="/enroll">
        {{ form.hidden_tag() }}
        <p>
            {{ form.parent_name.label }}<br>
            {{ form.parent_name(size=50) }}<br>
            {% for error in form.parent_name.errors %}
                <span style="color: red;">{{ error }}</span><br>
            {% endfor %}
        </p>
        <p>
            {{ form.email.label }}<br>
            {{ form.email(size=50) }}<br>
            {% for error in form.email.errors %}
                <span style="color: red;">{{ error }}</span><br>
            {% endfor %}
        </p>
        <p>
            {{ form.phone.label }}<br>
            {{ form.phone(size=15) }}<br>
            {% for error in form.phone.errors %}
                <span style="color: red;">{{ error }}</span><br>
            {% endfor %}
        </p>
        <p>
            {{ form.child_name.label }}<br>
            {{ form.child_name(size=50) }}<br>
            {% for error in form.child_name.errors %}
                <span style="color: red;">{{ error }}</span><br>
            {% endfor %}
        </p>
        <p>
            {{ form.child_age.label }}<br>
            {{ form.child_age() }}<br>
            {% for error in form.child_age.errors %}
                <span style="color: red;">{{ error }}</span><br>
            {% endfor %}
        </p>
        <p>
            {{ form.program.label }}<br>
            {{ form.program() }}<br>
            {% for error in form.program.errors %}
                <span style="color: red;">{{ error }}</span><br>
            {% endfor %}
        </p>
        <p>
            <button type="submit">Submit</button>
        </p>
    </form>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li style="color: green;">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
"""

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
