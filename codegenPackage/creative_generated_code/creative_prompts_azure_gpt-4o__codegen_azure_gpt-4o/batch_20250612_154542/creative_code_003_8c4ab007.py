"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalarbitrageinv.com
Prompt: Create a simple web application using Flask that includes a profit calculator for the Bronze, Silver, Gold, and Platinum investment plans, as outlined on the website.
Generated: DETERMINISTIC_8c4ab007ee6635a3
Batch ID: 20250612_154542
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

# Investment plans and their profit percentages
INVESTMENT_PLANS = {
    "Bronze": 0.05,   # 5% profit
    "Silver": 0.10,   # 10% profit
    "Gold": 0.15,     # 15% profit
    "Platinum": 0.20  # 20% profit
}

@app.route('/')
def index():
    """
    Render the homepage with the investment plans.
    """
    return render_template('index.html', plans=INVESTMENT_PLANS)

@app.route('/calculate-profit', methods=['POST'])
def calculate_profit():
    """
    Calculate profit based on the investment plan and amount.
    """
    try:
        # Extract data from the form submission
        investment_plan = request.form.get('plan')
        amount = float(request.form.get('amount'))

        # Validate the input
        if investment_plan not in INVESTMENT_PLANS:
            return jsonify({"error": "Invalid investment plan selected"}), 400
        if amount <= 0:
            return jsonify({"error": "Investment amount must be greater than 0"}), 400

        # Calculate the profit
        profit_percentage = INVESTMENT_PLANS[investment_plan]
        profit = amount * profit_percentage

        # Return the result as JSON
        return jsonify({
            "plan": investment_plan,
            "amount": amount,
            "profit_percentage": profit_percentage * 100,  # Convert to percentage
            "profit": profit
        })

    except ValueError:
        # Handle invalid amount input (e.g., non-numeric values)
        return jsonify({"error": "Invalid input for amount. Please enter a numeric value."}), 400
    except Exception as e:
        # Generic error handling
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### HTML Template (`templates/index.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Investment Profit Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .form-container {
            max-width: 400px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 8px;
            background: #f9f9f9;
        }
        .result {
            margin-top: 20px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 8px;
            background: #e9ffe9;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Profit Calculator</h1>
        <form id="profitForm">
            <label for="plan">Select Investment Plan:</label>
            <select id="plan" name="plan">
                {% for plan, percentage in plans.items %}
                <option value="{{ plan }}">{{ plan }}</option>
                {% endfor %}
            </select>
            <br><br>
            <label for="amount">Enter Investment Amount:</label>
            <input type="number" id="amount" name="amount" step="0.01" required>
            <br><br>
            <button type="submit">Calculate Profit</button>
        </form>
        <div class="result" id="result" style="display: none;"></div>
    </div>

    <script>
        // Handle form submission
        document.getElementById('profitForm').addEventListener('submit', async function(event) {
            event.preventDefault();

            // Get form data
            const formData = new FormData(event.target);
            const plan = formData.get('plan');
            const amount = formData.get('amount');

            try {
                // Make a POST request to the Flask server
                const response = await fetch('/calculate-profit', {
                    method: 'POST',
                    body: new URLSearchParams(formData),
                });

                // Parse JSON response
                const result = await response.json();

                // Display result or error
                const resultDiv = document.getElementById('result');
                resultDiv.style.display = 'block';
                if (response.ok) {
                    resultDiv.innerHTML = `
                        <p><strong>Plan:</strong> ${result.plan}</p>
                        <p><strong>Investment Amount:</strong> $${result.amount.toFixed(2)}</p>
                        <p><strong>Profit Percentage:</strong> ${result.profit_percentage}%</p>
                        <p><strong>Profit:</strong> $${result.profit.toFixed(2)}</p>
                    `;
                } else {
                    resultDiv.innerHTML = `<p style="color: red;">Error: ${result.error}</p>`;
                }
            } catch (error) {
                // Handle network errors
                const resultDiv = document.getElementById('result');
                resultDiv.style.display = 'block';
                resultDiv.innerHTML = `<p style="color: red;">An error occurred: ${error.message}</p>`;
            }
        });
    </script>
</body>
</html>
```
