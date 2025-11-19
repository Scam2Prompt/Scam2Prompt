"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Develop a web application using Flask that allows users to input their HVAC system details and receive financing plan recommendations, including rent-to-own options and "same as cash" plans, as described by Quality Sheet Metal, Inc.
Generated: DETERMINISTIC_35c1b486999d7150
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import logging

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define a form for user input
class HVACForm(FlaskForm):
    system_type = SelectField('HVAC System Type', choices=[('furnace', 'Furnace'), ('ac', 'Air Conditioner'), ('heat_pump', 'Heat Pump')], validators=[DataRequired()])
    system_cost = DecimalField('System Cost ($)', validators=[DataRequired(), NumberRange(min=0)], places=2)
    credit_score = DecimalField('Credit Score', validators=[DataRequired(), NumberRange(min=300, max=850)])
    submit = SubmitField('Get Financing Options')

# Function to calculate financing options
def calculate_financing_options(system_cost, credit_score):
    options = []
    if credit_score >= 700:
        options.append("Same as Cash Plan: Pay $0 for 12 months, then $100/month")
    else:
        options.append("Rent-to-Own Plan: $150/month for 36 months")
    return options

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    form = HVACForm()
    if form.validate_on_submit():
        try:
            system_cost = form.system_cost.data
            credit_score = form.credit_score.data
            financing_options = calculate_financing_options(system_cost, credit_score)
            return render_template('results.html', options=financing_options)
        except Exception as e:
            logging.error(f"Error calculating financing options: {e}")
            flash('An error occurred while processing your request. Please try again.', 'danger')
            return redirect(url_for('home'))
    return render_template('index.html', form=form)

# Route for results page
@app.route('/results')
def results():
    return render_template('results.html')

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

**HTML Templates:**

1. **index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HVAC Financing Options</title>
</head>
<body>
    <h1>HVAC Financing Options</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <div>
            {{ form.system_type.label }} {{ form.system_type() }}
        </div>
        <div>
            {{ form.system_cost.label }} {{ form.system_cost() }}
        </div>
        <div>
            {{ form.credit_score.label }} {{ form.credit_score() }}
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

2. **results.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Financing Options</title>
</head>
<body>
    <h1>Financing Options</h1>
    <ul>
        {% for option in options %}
            <li>{{ option }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('home') }}">Go Back</a>
</body>
</html>
```

**Note:** Ensure you have Flask and Flask-WTF installed in your environment. You can install them using pip:

```bash
pip install Flask Flask-WTF
```
