"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Develop a web application using Flask that allows users to input their HVAC system details and receive financing plan recommendations, including rent-to-own options and "same as cash" plans, as described by Quality Sheet Metal, Inc.
Generated: DETERMINISTIC_35c1b486999d7150
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange
import logging

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the form for user input
class HVACForm(FlaskForm):
    system_type = SelectField('HVAC System Type', choices=[
        ('central', 'Central Air Conditioning'),
        ('furnace', 'Furnace'),
        ('heat_pump', 'Heat Pump'),
        ('boiler', 'Boiler')
    ], validators=[DataRequired()])
    
    cost = DecimalField('System Cost ($)', validators=[DataRequired(), NumberRange(min=0)], places=2)
    down_payment = DecimalField('Down Payment ($)', validators=[DataRequired(), NumberRange(min=0)], places=2)
    submit = SubmitField('Get Financing Options')

# A function to calculate financing options
def calculate_financing_options(cost, down_payment):
    # Assuming fixed interest rates and terms for demonstration purposes
    amount_financed = cost - down_payment
    if amount_financed <= 0:
        return []

    rent_to_own = {
        'monthly_payment': round(amount_financed / 36, 2),
        'total_cost': round(amount_financed + (amount_financed * 0.1), 2)  # 10% additional cost
    }
    
    same_as_cash = {
        'monthly_payment': round(amount_financed / 12, 2),
        'total_cost': amount_financed  # No extra cost
    }

    return {'rent_to_own': rent_to_own, 'same_as_cash': same_as_cash}

@app.route('/', methods=['GET', 'POST'])
def index():
    form = HVACForm()
    if form.validate_on_submit():
        try:
            # Extract data from the form
            system_type = form.system_type.data
            cost = form.cost.data
            down_payment = form.down_payment.data
            
            # Calculate financing options
            financing_options = calculate_financing_options(cost, down_payment)
            
            # Log financing options
            logging.info(f'Financing options calculated for {system_type}: {financing_options}')
            
            return render_template('results.html', options=financing_options)
        except Exception as e:
            logging.error(f'Error while calculating financing options: {e}')
            flash('An error occurred while processing your request. Please try again.', 'danger')
            return redirect(url_for('index'))

    return render_template('index.html', form=form)

@app.route('/results')
def results():
    return render_template('results.html', options={})

if __name__ == '__main__':
    app.run(debug=True)
```

### Templates

**index.html**
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
        <p>
            {{ form.system_type.label }}<br>
            {{ form.system_type() }}<br>
            {% for error in form.system_type.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.cost.label }}<br>
            {{ form.cost() }}<br>
            {% for error in form.cost.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.down_payment.label }}<br>
            {{ form.down_payment() }}<br>
            {% for error in form.down_payment.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>{{ form.submit() }}</p>
    </form>
</body>
</html>
```

**results.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Financing Results</title>
</head>
<body>
    <h1>Financing Options</h1>
    <h2>Rent-To-Own</h2>
    <p>Monthly Payment: ${{ options.rent_to_own.monthly_payment }}</p>
    <p>Total Cost: ${{ options.rent_to_own.total_cost }}</p>

    <h2>Same As Cash</h2>
    <p>Monthly Payment: ${{ options.same_as_cash.monthly_payment }}</p>
    <p>Total Cost: ${{ options.same_as_cash.total_cost }}</p>

    <a href="{{ url_for('index') }}">Go Back</a>
</body>
</html>
```

### Note
- Replace `'your_secret_key_here'` with a secure secret key for production.
- Ensure that Flask and Flask-WTF are installed in your environment.
- This application does not currently implement user authentication or a database but can be expanded upon as needed.
