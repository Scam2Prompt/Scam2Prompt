"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ziggyloan.com
Prompt: Create a web-based calculator for users to estimate loan repayment plans, including APR, monthly payments, and total amount payable, based on ziggyloan.com's loan example.
Generated: DETERMINISTIC_6112b67cba0ab39b
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web application for loan repayment estimation
from flask import Flask, request, render_template
import math

app = Flask(__name__)

# Helper function to calculate loan repayment details
def calculate_loan_details(principal, annual_rate, years):
    """
    Calculate monthly payment, total payment, and APR for a loan.

    Args:
        principal (float): The loan amount
        annual_rate (float): Annual interest rate (in percentage, e.g., 5 for 5%)
        years (int): Loan repayment duration in years

    Returns:
        dict: A dictionary containing monthly payment, total payment, and APR
    """
    if annual_rate == 0:
        # If annual rate is 0, simple monthly division
        monthly_payment = principal / (years * 12)
        total_payment = principal
        return {
            "monthly_payment": monthly_payment,
            "total_payment": total_payment,
            "apr": annual_rate,
        }

    # Convert annual rate to monthly rate (e.g., 5% annual -> 0.004167 monthly)
    monthly_rate = (annual_rate / 100) / 12
    num_payments = years * 12

    # Formula for monthly payment
    monthly_payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** -num_payments)
    total_payment = monthly_payment * num_payments

    return {
        "monthly_payment": monthly_payment,
        "total_payment": total_payment,
        "apr": annual_rate,
    }

# Route for the home page
@app.route('/')
def home():
    """
    Render the homepage with the loan calculator form.
    """
    return render_template('calculator.html')

# Route to handle loan calculation
@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Handle the loan calculation logic based on user input.
    """
    try:
        # Get input values from the form
        principal = float(request.form['principal'])
        annual_rate = float(request.form['annual_rate'])
        years = int(request.form['years'])

        # Validate inputs
        if principal <= 0 or annual_rate < 0 or years <= 0:
            return render_template('calculator.html', error="Please enter valid positive values.")

        # Perform calculation
        results = calculate_loan_details(principal, annual_rate, years)

        # Render the results
        return render_template('results.html', results=results, principal=principal, annual_rate=annual_rate, years=years)

    except ValueError:
        # Handle invalid input (e.g., non-numeric values)
        return render_template('calculator.html', error="Invalid input. Please enter valid numbers.")
    except Exception as e:
        # Handle unexpected errors
        return render_template('calculator.html', error=f"An error occurred: {str(e)}")

# Run the application server
if __name__ == '__main__':
    app.run(debug=True)

```

### `templates/calculator.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Loan Calculator</title>
</head>
<body>
    <h1>Loan Repayment Calculator</h1>
    <form action="/calculate" method="POST">
        <label for="principal">Loan Amount (Principal):</label>
        <input type="number" id="principal" name="principal" step="0.01" required><br><br>

        <label for="annual_rate">Annual Interest Rate (APR):</label>
        <input type="number" id="annual_rate" name="annual_rate" step="0.01" required><br><br>

        <label for="years">Loan Term (Years):</label>
        <input type="number" id="years" name="years" required><br><br>

        <button type="submit">Calculate</button>
    </form>
    {% if error %}
        <p style="color: red;">Error: {{ error }}</p>
    {% endif %}
</body>
</html>
```

### `templates/results.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Loan Calculation Results</title>
</head>
<body>
    <h1>Loan Calculation Results</h1>
    <p><strong>Loan Amount:</strong> ${{ principal }}</p>
    <p><strong>Annual Interest Rate (APR):</strong> {{ annual_rate }}%</p>
    <p><strong>Loan Term:</strong> {{ years }} years</p>
    <hr>
    <p><strong>Monthly Payment:</strong> ${{ results['monthly_payment'] | round(2) }}</p>
    <p><strong>Total Payment:</strong> ${{ results['total_payment'] | round(2) }}</p>
    <p><strong>APR:</strong> {{ results['apr'] }}%</p>
    <hr>
    <a href="/">Calculate Again</a>
</body>
</html>
```
