"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalarbitrageinv.com
Prompt: Create a simple web application using Flask that includes a profit calculator for the Bronze, Silver, Gold, and Platinum investment plans, as outlined on the website.
Generated: DETERMINISTIC_8c4ab007ee6635a3
Batch ID: 20250612_154542
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import DecimalField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a stronger secret key in production

# Define investment plans and their respective rates
INVESTMENT_PLANS = {
    'Bronze': 0.05,
    'Silver': 0.10,
    'Gold': 0.15,
    'Platinum': 0.20
}

# Create a form class using Flask-WTF
class ProfitCalculatorForm(FlaskForm):
    initial_investment = DecimalField('Initial Investment ($)', validators=[DataRequired(), NumberRange(min=0, message='Investment must be positive.')])
    plan = SelectField('Investment Plan', choices=list(INVESTMENT_PLANS.keys()), validators=[DataRequired()])
    submit = SubmitField('Calculate Profit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ProfitCalculatorForm()
    profit = None

    if form.validate_on_submit():
        # Retrieve form data
        initial_investment = form.initial_investment.data
        selected_plan = form.plan.data

        # Calculate profit based on the selected plan
        profit_rate = INVESTMENT_PLANS[selected_plan]
        profit = initial_investment * profit_rate

        # Provide feedback to the user
        flash(f'Calculated Profit for {selected_plan} plan: ${profit:.2f}', 'success')

        # Redirect to the same page to prevent form resubmission
        return redirect(url_for('index'))

    return render_template('index.html', form=form, profit=profit)

# Error handling for runtime errors
@app.errorhandler(500)
def internal_error(error):
    return "An internal error occurred. Please try again later.", 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)  # Set debug=False in production
```

**HTML Template (templates/index.html):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profit Calculator</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Investment Profit Calculator</h1>
        <form method="POST" class="mt-4">
            {{ form.hidden_tag() }}
            <div class="form-group">
                {{ form.initial_investment.label(class="form-label") }}
                {{ form.initial_investment(class="form-control") }}
                {% for error in form.initial_investment.errors %}
                    <div class="alert alert-danger mt-2">{{ error }}</div>
                {% endfor %}
            </div>
            <div class="form-group">
                {{ form.plan.label(class="form-label") }}
                {{ form.plan(class="form-control") }}
                {% for error in form.plan.errors %}
                    <div class="alert alert-danger mt-2">{{ error }}</div>
                {% endfor %}
            </div>
            <div class="form-group">
                {{ form.submit(class="btn btn-primary") }}
            </div>
        </form>

        {% if profit is not none %}
            <div class="alert alert-info mt-4">
                <strong>Profit:</strong> ${{ profit }}
            </div>
        {% endif %}
        
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                <div class="mt-4">
                    {% for message in messages %}
                        <div class="alert alert-success">{{ message }}</div>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}
    </div>
</body>
</html>
```

**Requirements for the application:**
1. Flask
2. Flask-WTF
3. WTForms

**To run the application:**
1. Install required packages:
   ```
   pip install Flask Flask-WTF WTForms
   ```

2. Create a folder named `templates` and save the HTML file as `index.html`.

3. Run the Flask application:
   ```
   python your_script_name.py
   ```
