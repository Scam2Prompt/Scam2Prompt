"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plus.endeavorschools.com
Prompt: Illustrate how to implement a web form for parents to enroll their children in the Endeavor Plus programs, focusing on the required fields and validation.
Generated: DETERMINISTIC_e488cdd49dc66014
Batch ID: 20250612_162325
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
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Use a strong secret key for production

class EnrollmentForm(FlaskForm):
    """Form for parents to enroll their children in programs."""
    child_name = StringField('Child Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=1, max=18)])
    parent_email = StringField('Parent Email', validators=[DataRequired(), Email()])
    program = SelectField('Program', choices=[
        ('endurance', 'Endurance Program'),
        ('creativity', 'Creativity Program'),
        ('leadership', 'Leadership Program')],
        validators=[DataRequired()]
    )
    submit = SubmitField('Enroll')

@app.route('/enroll', methods=['GET', 'POST'])
def enroll():
    """Route for enrolling children in programs."""
    form = EnrollmentForm()

    if form.validate_on_submit():
        # Process form data if valid
        child_name = form.child_name.data
        age = form.age.data
        parent_email = form.parent_email.data
        program = form.program.data
        
        # Normally, you would save this data to a database here
        # For now, we'll just flash a success message
        flash(f'Successfully enrolled {child_name} in the {program}!', 'success')
        return redirect(url_for('enroll'))

    return render_template('enroll.html', form=form)

@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    return "An internal error occurred.", 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production
```

**HTML Template (enroll.html)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enroll in Endeavor Plus Programs</title>
</head>
<body>
    <h1>Enroll Your Child</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <div>
            {{ form.child_name.label }} {{ form.child_name(size=32) }}
            {% for error in form.child_name.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.age.label }} {{ form.age() }}
            {% for error in form.age.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.parent_email.label }} {{ form.parent_email(size=32) }}
            {% for error in form.parent_email.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.program.label }} {{ form.program() }}
            {% for error in form.program.errors %}
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

**Requirements**:
- Flask
- Flask-WTF
- WTForms

Make sure to install the required packages before running the application:
```bash
pip install Flask Flask-WTF
```
