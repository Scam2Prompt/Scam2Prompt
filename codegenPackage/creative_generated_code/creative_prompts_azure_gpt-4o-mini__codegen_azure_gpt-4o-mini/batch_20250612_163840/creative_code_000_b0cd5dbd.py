"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://camelot.netlify.app
Prompt: Generate a code snippet for a web application that allows users to apply for a Fix and Flip loan, including fields for purchase price and rehab costs.
Generated: DETERMINISTIC_b0cd5dbd39d895e2
Batch ID: 20250612_163840
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
from wtforms import DecimalField, SubmitField, StringField, validators

# Create an instance of the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a strong secret key

# Define a form using Flask-WTF for the loan application
class LoanApplicationForm(FlaskForm):
    purchase_price = DecimalField('Purchase Price',
                                   validators=[validators.InputRequired(), validators.NumberRange(min=0)])
    rehab_costs = DecimalField('Rehab Costs',
                                validators=[validators.InputRequired(), validators.NumberRange(min=0)])
    submit = SubmitField('Apply for Loan')

# Route for the loan application page
@app.route('/apply', methods=['GET', 'POST'])
def apply():
    form = LoanApplicationForm()
    
    if form.validate_on_submit():
        # Process the loan application
        purchase_price = form.purchase_price.data
        rehab_costs = form.rehab_costs.data
        
        # Here you would typically save the information to the database
        # For demonstration purposes, we are just showing a flash message
        flash(f'Loan application submitted successfully! Purchase Price: ${purchase_price}, Rehab Costs: ${rehab_costs}')
        
        return redirect(url_for('apply'))  # Redirect after successful submission

    return render_template('loan_application.html', form=form)

# Error handling for the application
@app.errorhandler(500)
def internal_error(error):
    return "An internal error occurred. Please try again later.", 500

# Main function to run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- loan_application.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fix and Flip Loan Application</title>
</head>
<body>
    <h1>Apply for Fix and Flip Loan</h1>
    
    <!-- Display any flash messages -->
    {% with messages = get_flashed_messages() %}
      {% if messages %}
        <ul>
          {% for message in messages %}
            <li>{{ message }}</li>
          {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    
    <!-- Form for loan application -->
    <form method="POST" action="">
        {{ form.hidden_tag() }}
        <div>
            {{ form.purchase_price.label }} {{ form.purchase_price(size=20) }}
            {% for error in form.purchase_price.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.rehab_costs.label }} {{ form.rehab_costs(size=20) }}
            {% for error in form.rehab_costs.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>
</body>
</html>
```

**Note**: This code is structured for a Flask web application. Make sure to install Flask and Flask-WTF using pip, and create a proper directory structure with templates to make it runnable. Adjust the secret key and database interactions as needed for a production environment.
