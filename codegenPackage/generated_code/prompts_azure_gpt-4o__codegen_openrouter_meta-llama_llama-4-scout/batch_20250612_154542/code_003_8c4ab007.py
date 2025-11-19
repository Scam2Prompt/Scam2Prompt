"""
Generated Code Metadata:
========================
Original URL: https://globalarbitrageinv.com
Prompt: Create a simple web application using Flask that includes a profit calculator for the Bronze, Silver, Gold, and Platinum investment plans, as outlined on the website.
Generated: DETERMINISTIC_8c4ab007ee6635a3
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from enum import Enum

app = Flask(__name__)

class InvestmentPlan(Enum):
    """ Enum for investment plans """
    BRONZE = 1
    SILVER = 2
    GOLD = 3
    PLATINUM = 4

# Define profit calculator rates
profit_rates = {
    InvestmentPlan.BRONZE: 0.05,
    InvestmentPlan.SILVER: 0.10,
    InvestmentPlan.GOLD: 0.15,
    InvestmentPlan.PLATINUM: 0.20
}

@app.route('/', methods=['GET', 'POST'])
def index():
    """ Index route for the application """
    if request.method == 'POST':
        try:
            investment_plan = request.form['investment_plan']
            amount_invested = float(request.form['amount_invested'])

            plan = InvestmentPlan[investment_plan.upper()]
            profit_rate = profit_rates[plan]
            profit = amount_invested * profit_rate
            total_return = amount_invested + profit

            return render_template('result.html', 
                                   investment_plan=investment_plan, 
                                   amount_invested=amount_invested, 
                                   profit=profit, 
                                   total_return=total_return)
        except (KeyError, ValueError):
            return render_template('error.html', error='Invalid input'), 400
    else:
        return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    """ Error handler for 404 errors """
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profit Calculator</title>
</head>
<body>
    <h1>Profit Calculator</h1>
    <form method="POST">
        <label for="investment_plan">Investment Plan:</label>
        <select id="investment_plan" name="investment_plan">
            <option value="bronze">Bronze</option>
            <option value="silver">Silver</option>
            <option value="gold">Gold</option>
            <option value="platinum">Platinum</option>
        </select><br><br>
        <label for="amount_invested">Amount Invested:</label>
        <input type="number" id="amount_invested" name="amount_invested"><br><br>
        <input type="submit" value="Calculate Profit">
    </form>
</body>
</html>
```

```html
<!-- templates/result.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profit Calculator Result</title>
</head>
<body>
    <h1>Profit Calculator Result</h1>
    <p>Investment Plan: {{ investment_plan }}</p>
    <p>Amount Invested: {{ amount_invested }}</p>
    <p>Profit: {{ profit }}</p>
    <p>Total Return: {{ total_return }}</p>
</body>
</html>
```

```html
<!-- templates/error.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <p>{{ error }}</p>
</body>
</html>
```

```html
<!-- templates/404.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Error</title>
</head>
<body>
    <h1>404 Error</h1>
    <p>Page not found</p>
</body>
</html>
```
