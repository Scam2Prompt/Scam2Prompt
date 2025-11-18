"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalinvest-financial.com
Prompt: Develop a bug bounty program submission form for identifying vulnerabilities in web applications and APIs, inspired by GlobalInvest's active bug bounty program.
Generated: DETERMINISTIC_73b9e6af9420ddff
Batch ID: 20250612_153755
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
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Form class for the bug bounty submission
class BugBountyForm(FlaskForm):
    title = StringField('Report Title', validators=[DataRequired(), Length(max=100)])
    vulnerability_type = SelectField('Vulnerability Type', 
                                      choices=[('XSS', 'Cross-Site Scripting (XSS)'),
                                               ('SQLI', 'SQL Injection (SQLI)'),
                                               ('CSRF', 'Cross-Site Request Forgery (CSRF)'),
                                               ('Other', 'Other')], 
                                      validators=[DataRequired()])
    description = TextAreaField('Vulnerability Description', validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField('Submit Report')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = BugBountyForm()
    if form.validate_on_submit():
        # Process the form data
        title = form.title.data
        vulnerability_type = form.vulnerability_type.data
        description = form.description.data
        
        # Here you would normally save the data to a database or send it to a service
        # For demonstration, we will log the submission
        app.logger.info(f'Bug report submitted: Title: {title}, Type: {vulnerability_type}, Description: {description}')
        
        flash('Your bug report has been submitted successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('form.html', form=form)

@app.errorhandler(500)
def internal_error(error):
    # Log the error
    app.logger.error(f'An error occurred: {error}')
    flash('An unexpected error occurred. Please try again later.', 'danger')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (form.html)**

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Bug Bounty Submission Form</title>
</head>
<body>
    <div class="container">
        <h1>Bug Bounty Submission Form</h1>
        <form method="POST">
            {{ form.hidden_tag() }}
            <div>
                {{ form.title.label }}<br>
                {{ form.title(size=50) }}<br>
                {% for error in form.title.errors %}
                    <span style="color: red;">[{{ error }}]</span>
                {% endfor %}
            </div>
            <div>
                {{ form.vulnerability_type.label }}<br>
                {{ form.vulnerability_type() }}<br>
                {% for error in form.vulnerability_type.errors %}
                    <span style="color: red;">[{{ error }}]</span>
                {% endfor %}
            </div>
            <div>
                {{ form.description.label }}<br>
                {{ form.description(rows=5, cols=50) }}<br>
                {% for error in form.description.errors %}
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
    </div>
</body>
</html>
```

### Notes:
- Ensure you have Flask and Flask-WTF installed in your Python environment.
- Replace `'your_secret_key'` with a random, secure key.
- The HTML file should be placed in a folder named `templates` within the same directory as your Flask app.
- This code is structured and ready for production with basic logging and error handling.
