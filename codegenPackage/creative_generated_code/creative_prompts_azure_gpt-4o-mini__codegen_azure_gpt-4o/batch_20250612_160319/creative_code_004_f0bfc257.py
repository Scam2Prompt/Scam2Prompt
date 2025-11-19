"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sfassetinnovation.com.smalltalk.com.ng
Prompt: Construct a simple web application using Flask that allows users to select an investment plan from Steadfast Asset Innovation and calculates the total profit based on their investment amount.
Generated: DETERMINISTIC_f0bfc25779cb0057
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define investment plans with their respective profit rates (in percentage)
investment_plans = {
    "Silver": 5.0,   # 5% profit
    "Gold": 10.0,    # 10% profit
    "Platinum": 20.0 # 20% profit
}

@app.route("/")
def home():
    """
    Render the homepage where users can choose an investment plan and enter the investment amount.
    """
    return render_template("index.html", plans=investment_plans.keys())

@app.route("/calculate", methods=["POST"])
def calculate_profit():
    """
    Calculate the profit based on user-selected investment plan and amount.
    """
    try:
        # Get data from the form
        investment_plan = request.form.get("plan")
        investment_amount = request.form.get("amount", type=float)

        # Validate inputs
        if investment_plan not in investment_plans:
            return jsonify({"error": "Invalid investment plan selected"}), 400
        if investment_amount is None or investment_amount <= 0:
            return jsonify({"error": "Investment amount must be a positive number"}), 400

        # Calculate profit
        profit_rate = investment_plans[investment_plan]
        total_profit = investment_amount * (profit_rate / 100)

        # Return the result as JSON
        return jsonify({
            "investment_plan": investment_plan,
            "investment_amount": investment_amount,
            "profit_rate": profit_rate,
            "total_profit": total_profit
        })

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# main entry point
if __name__ == "__main__":
    # Debug mode should be turned off in production
    app.run(debug=True)
```

```html
<!-- Save this file as templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Steadfast Asset Innovation - Investment Calculator</title>
</head>
<body>
    <h1>Investment Calculator</h1>
    <form action="/calculate" method="post">
        <label for="plan">Select Investment Plan:</label>
        <select id="plan" name="plan" required>
            {% for plan in plans %}
                <option value="{{ plan }}">{{ plan }}</option>
            {% endfor %}
        </select>
        <br><br>
        <label for="amount">Enter Investment Amount (USD):</label>
        <input type="number" id="amount" name="amount" step="0.01" required>
        <br><br>
        <button type="submit">Calculate Profit</button>
    </form>
</body>
</html>
```
