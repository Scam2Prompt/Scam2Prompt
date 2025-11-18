"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe-buy.pages.dev
Prompt: Develop a web application that calculates staking rewards for $PEPU tokens based on the 245% annual reward rate mentioned on the Pepe Unchained site.
Generated: DETERMINISTIC_30993aa79d414025
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime
import math

app = Flask(__name__)

# Constants
ANNUAL_REWARD_RATE = 245  # Annual reward rate in percentage
DAYS_IN_YEAR = 365  # Number of days in a year

# Helper function to calculate staking rewards
def calculate_staking_rewards(amount: float, staking_days: int) -> float:
    """
    Calculate staking rewards based on the annual reward rate.

    :param amount: The amount of $PEPU tokens staked.
    :param staking_days: The number of days the tokens are staked.
    :return: Total rewards in $PEPU tokens.
    """
    if amount <= 0 or staking_days <= 0:
        raise ValueError("Amount and staking days must be greater than zero")
    
    # Daily reward rate (annual rate divided by 365)
    daily_reward_rate = ANNUAL_REWARD_RATE / DAYS_IN_YEAR / 100
    
    # Calculate rewards
    rewards = amount * daily_reward_rate * staking_days
    return round(rewards, 2)

@app.route('/calculate-rewards', methods=['POST'])
def calculate_rewards():
    """
    Endpoint to calculate staking rewards for $PEPU tokens.

    Request JSON format:
    {
        "amount": float,  # Amount of $PEPU tokens staked
        "stakingDays": int  # Number of days tokens are staked
    }
    
    Response JSON format:
    {
        "success": bool,  # Status of the operation
        "rewards": float  # Calculated staking rewards (if successful)
        "error": str      # Error message (if failed)
    }
    """
    try:
        # Parse JSON request data
        data = request.json
        if not data or 'amount' not in data or 'stakingDays' not in data:
            raise ValueError("Invalid input format. 'amount' and 'stakingDays' are required.")
        
        amount = float(data['amount'])
        staking_days = int(data['stakingDays'])

        # Calculate rewards
        rewards = calculate_staking_rewards(amount, staking_days)

        # Return successful response
        return jsonify({
            "success": True,
            "rewards": rewards
        }), 200
    except ValueError as ve:
        # Handle invalid input errors
        return jsonify({
            "success": False,
            "error": str(ve)
        }), 400
    except Exception as e:
        # Handle other unexpected errors
        return jsonify({
            "success": False,
            "error": "An unexpected error occurred: " + str(e)
        }), 500

@app.route('/')
def home():
    """
    Default root endpoint for the application.
    """
    return jsonify({
        "message": "Welcome to the $PEPU Staking Rewards Calculator API!"
    }), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
