"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeinvestmentslimited.org
Prompt: Create a REST API endpoint that allows users to retrieve personalized financial advice, similar to the services provided by Finance Investment Limited.
Generated: DETERMINISTIC_b9a532148c19e14c
Batch ID: 20250612_160440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Example function to generate financial advice
def generate_financial_advice(user_data):
    """
    Generate personalized financial advice based on user data.
    
    :param user_data: Dictionary containing user's financial information.
    :return: String containing financial advice.
    """
    income = user_data.get("income", 0)
    expenses = user_data.get("expenses", 0)
    savings_goal = user_data.get("savings_goal", 0)

    if income <= 0:
        return "Please provide a valid income amount."
    if expenses < 0:
        return "Expenses cannot be negative."

    disposable_income = income - expenses

    if disposable_income <= 0:
        return "Your expenses exceed your income. Consider reducing expenses to achieve your financial goals."
    elif disposable_income < savings_goal:
        return (
            f"You are saving less than your goal of ${savings_goal}. "
            f"Consider reducing unnecessary expenses or increasing your income to meet your savings target."
        )
    else:
        return (
            f"Great job! You have a disposable income of ${disposable_income}, which meets your savings goal of ${savings_goal}. "
            "Consider investing in low-risk options to grow your wealth."
        )

# Route: Financial advice endpoint
@app.route('/api/financial-advice', methods=['POST'])
def financial_advice():
    """
    REST API endpoint to retrieve personalized financial advice.
    Expects a POST request with JSON payload containing user financial data.
    Example payload:
    {
        "income": 5000,
        "expenses": 3000,
        "savings_goal": 1000
    }
    
    :return: JSON response containing personalized financial advice.
    """
    try:
        # Parse JSON payload from the request
        user_data = request.get_json()
        if not user_data:
            return jsonify({"error": "Invalid input. Expected JSON payload."}), 400

        # Validate required keys
        if "income" not in user_data or "expenses" not in user_data or "savings_goal" not in user_data:
            return jsonify({"error": "Missing required fields: 'income', 'expenses', 'savings_goal'."}), 400

        # Generate financial advice
        advice = generate_financial_advice(user_data)

        # Return the advice in the response
        return jsonify({"advice": advice}), 200

    except Exception as e:
        logging.error(f"Error processing financial advice request: {e}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500


# Application entry point
if __name__ == '__main__':
    app.run(debug=True)
```
