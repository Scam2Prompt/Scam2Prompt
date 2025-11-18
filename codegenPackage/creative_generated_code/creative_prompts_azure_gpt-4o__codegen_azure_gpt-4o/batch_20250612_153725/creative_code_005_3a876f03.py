"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletguard.pro
Prompt: Suggest libraries or tools for creating a "free-bet-calculator" as mentioned on WalletGuard, and provide example code.
Generated: DETERMINISTIC_3a876f03399c3ac7
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an example code for a "free-bet-calculator" using Python. It utilizes libraries such as `Flask` for the web framework and `Jinja2` for templating. Ensure you install the necessary libraries (`flask`) using `pip install flask` before running this code.

```python
# Import necessary libraries
from flask import Flask, render_template, request

# Initialize Flask app
app = Flask(__name__)

# Function to calculate free bet profit/loss
def calculate_free_bet(stake, odds):
    """
    Calculate the potential profit from a free bet.
    Parameters:
        stake (float): The amount of the free bet.
        odds (float): The decimal odds of the bet.
    Returns:
        float: The potential profit.
    """
    try:
        # Formula for free bet profit: (stake * (odds - 1))
        profit = stake * (odds - 1)
        return round(profit, 2)  # Round to 2 decimal places for clarity
    except Exception as e:
        raise ValueError(f"Error in calculation: {str(e)}")

# Route for the home page
@app.route('/')
def index():
    """
    Render the home page with the free bet form.
    """
    return render_template('index.html')

# Route to handle form submission
@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Handle form input, calculate free bet profit, and return the result.
    """
    try:
        # Get input values from the form
        stake = float(request.form['stake'])
        odds = float(request.form['odds'])

        # Validate input values
        if stake <= 0 or odds <= 1:
            return render_template('index.html', error="Stake must be greater than 0 and odds must be greater than 1.")

        # Perform calculation
        profit = calculate_free_bet(stake, odds)
        return render_template('index.html', profit=profit)

    except ValueError as ve:
        return render_template('index.html', error=f"Invalid input: {str(ve)}")
    except Exception as e:
        return render_template('index.html', error=f"An unexpected error occurred: {str(e)}")

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### `index.html` (Template File)
Place this file in a folder named `templates` in the same directory as the Python script.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Bet Calculator</title>
</head>
<body>
    <h1>Free Bet Calculator</h1>
    <form method="POST" action="/calculate">
        <label for="stake">Free Bet Stake:</label>
        <input type="number" id="stake" name="stake" step="0.01" required>
        <br><br>
        <label for="odds">Decimal Odds:</label>
        <input type="number" id="odds" name="odds" step="0.01" required>
        <br><br>
        <button type="submit">Calculate</button>
    </form>

    {% if profit %}
    <h2>Potential Profit: ${{ profit }}</h2>
    {% endif %}

    {% if error %}
    <h2 style="color: red;">Error: {{ error }}</h2>
    {% endif %}
</body>
</html>
```

### Notes:
- This code follows Python best practices with error handling and clear documentation.
- The `index.html` file is a simple template using Jinja2 for dynamic data rendering.
