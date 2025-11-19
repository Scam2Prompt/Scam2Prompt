"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecolux-btp.com
Prompt: Generate a code snippet for a web application that allows users to request construction estimates, incorporating features like project type selection and budget input, inspired by ECOLUX's services.
Generated: DETERMINISTIC_ebb1930af1a64816
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import SelectField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your actual secret key

# Define a form for requesting construction estimates
class EstimateRequestForm(FlaskForm):
    project_type = SelectField(
        'Project Type',
        choices=[
            ('residential', 'Residential'),
            ('commercial', 'Commercial'),
            ('renovation', 'Renovation'),
            ('landscaping', 'Landscaping')
        ],
        validators=[DataRequired()]
    )
    budget = DecimalField(
        'Budget ($)',
        places=2,
        validators=[DataRequired(), NumberRange(min=0)],
        default=0.00
    )
    submit = SubmitField('Request Estimate')

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    form = EstimateRequestForm()
    if form.validate_on_submit():
        # Capture the form data
        project_type = form.project_type.data
        budget = form.budget.data
        
        # Here you can handle the logic to store the request or send it via email
        # For now, we will just flash a success message
        flash(f'Estimate requested for {project_type} project with a budget of ${budget:.2f}!')
        
        # Redirect to the same page to avoid form re-submission
        return redirect(url_for('index'))
    
    return render_template('index.html', form=form)

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production

```

**HTML Template (index.html):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Construction Estimate Request</title>
</head>
<body>
    <h1>Request a Construction Estimate</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <div>
            {{ form.project_type.label }}<br>
            {{ form.project_type() }}<br>
            {% for error in form.project_type.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.budget.label }}<br>
            {{ form.budget() }}<br>
            {% for error in form.budget.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

**Error Page Template (404.html):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
</body>
</html>
```

**Note:** Make sure to install Flask and Flask-WTF for running this application using `pip install Flask Flask-WTF`.
