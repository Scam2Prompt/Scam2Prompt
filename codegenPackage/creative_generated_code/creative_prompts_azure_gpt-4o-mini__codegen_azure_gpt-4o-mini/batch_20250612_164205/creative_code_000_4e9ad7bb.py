"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fin-flix.me
Prompt: Generate a code snippet that simulates an online application form for a credit service, including fields for customer number, date of birth, and desired loan amount.
Generated: DETERMINISTIC_4e9ad7bb8fed17fd
Batch ID: 20250612_164205
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
from wtforms import StringField, DateField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a real secret key

class CreditApplicationForm(FlaskForm):
    customer_number = StringField('Customer Number', 
                                   validators=[DataRequired(), Length(min=1, max=20)])
    date_of_birth = DateField('Date of Birth', 
                               format='%Y-%m-%d', 
                               validators=[DataRequired()])
    loan_amount = DecimalField('Desired Loan Amount', 
                                validators=[DataRequired(), NumberRange(min=1000, max=1000000)],
                                places=2)
    submit = SubmitField('Submit Application')

@app.route('/', methods=['GET', 'POST'])
def apply():
    form = CreditApplicationForm()
    
    if form.validate_on_submit():
        # Here, you would typically save the application to a database
        customer_number = form.customer_number.data
        date_of_birth = form.date_of_birth.data
        loan_amount = form.loan_amount.data
        
        # Example of processing the application (logging for demo purposes)
        app.logger.info(f'Application submitted: {customer_number}, {date_of_birth}, {loan_amount}')
        
        flash('Application submitted successfully!', 'success')
        return redirect(url_for('apply'))
    
    return render_template('apply.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```

```html
<!-- apply.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Credit Application Form</title>
</head>
<body>
    <h1>Credit Application Form</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <div>
            {{ form.customer_number.label }}<br>
            {{ form.customer_number(size=20) }}<br>
            {% for error in form.customer_number.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.date_of_birth.label }}<br>
            {{ form.date_of_birth() }}<br>
            {% for error in form.date_of_birth.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.loan_amount.label }}<br>
            {{ form.loan_amount(size=10) }}<br>
            {% for error in form.loan_amount.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>
    {% with messages = get_flashed_messages(with_categories=True) %}
        {% if messages %}
            <ul class="flashes">
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

**Note:** Make sure to install the required packages using:
```bash
pip install Flask Flask-WTF
```
