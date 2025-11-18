"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzocash.com
Prompt: Write code to implement a dashboard for monitoring investment statistics, including total deposits, withdrawals, and daily profits, as shown on Renzo Cash.
Generated: DETERMINISTIC_0b0e97159e30a431
Batch ID: 20250612_150329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import random

# Initialize Flask application
app = Flask(__name__)

# Mock data for investment statistics (sample dynamic data)
investment_statistics = {
    "total_deposits": 0.0,
    "total_withdrawals": 0.0,
    "daily_profit": 0.0,
    "historical_data": []  # Historical data for the dashboard
}

# Utility function to update daily statistics
def update_daily_statistics():
    """
    Generate random daily statistics for demonstration purposes.
    In a real-world use case, this data will come from the database
    or external systems such as a financial API.
    """
    global investment_statistics
    daily_deposit = round(random.uniform(1000, 5000), 2)  # Random deposit
    daily_withdrawal = round(random.uniform(500, 3000), 2)  # Random withdrawal
    daily_profit = round(random.uniform(100, 1500), 2)  # Random profit

    investment_statistics["total_deposits"] += daily_deposit
    investment_statistics["total_withdrawals"] += daily_withdrawal
    investment_statistics["daily_profit"] = daily_profit

    # Store historical entry
    investment_statistics["historical_data"].append({
        "date": datetime.now().strftime('%Y-%m-%d'),
        "daily_deposit": daily_deposit,
        "daily_withdrawal": daily_withdrawal,
        "daily_profit": daily_profit
    })


# Route to view investment statistics summary
@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    """
    Endpoint to retrieve investment statistics summary.
    Returns a JSON object containing total deposits,
    total withdrawals, and daily profit.
    """
    return jsonify({
        "status": "success",
        "data": {
            "total_deposits": investment_statistics["total_deposits"],
            "total_withdrawals": investment_statistics["total_withdrawals"],
            "daily_profit": investment_statistics["daily_profit"],
            "historical_data": investment_statistics["historical_data"]
        }
    })


# Route to update statistics (for demonstration purposes)
@app.route('/api/statistics/update', methods=['POST'])
def update_statistics():
    """
    Endpoint to simulate updating investment statistics.
    This should ideally be done automatically or through an admin interface.
    """
    try:
        update_daily_statistics()
        return jsonify({"status": "success", "message": "Statistics updated successfully."})
    except Exception as e:
        # Handle errors gracefully
        return jsonify({"status": "error", "message": str(e)}), 500


# Route to filter historical data based on date range
@app.route('/api/statistics/history', methods=['GET'])
def filter_historical_data():
    """
    Endpoint to filter historical data based on a date range.
    Expects 'start_date' and 'end_date' as query parameters in YYYY-MM-DD format.
    """
    try:
        # Extract query parameters
        start_date_str = request.args.get('start_date')
        end_date_str = request.args.get('end_date')

        # Validate input
        if not start_date_str or not end_date_str:
            return jsonify({
                "status": "error",
                "message": "Missing 'start_date' or 'end_date' query parameters."
            }), 400

        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

        # Filter historical data
        filtered_data = [
            entry for entry in investment_statistics["historical_data"]
            if start_date <= datetime.strptime(entry['date'], '%Y-%m-%d') <= end_date
        ]

        return jsonify({"status": "success", "data": filtered_data})
    except ValueError:
        # Handle invalid date format
        return jsonify({
            "status": "error",
            "message": "Invalid date format. Use YYYY-MM-DD."
        }), 400
    except Exception as e:
        # Handle general errors
        return jsonify({"status": "error", "message": str(e)}), 500


# Run the application
if __name__ == '__main__':
    # Update daily statistics once at startup (simulate initial data)
    update_daily_statistics()
    app.run(debug=True)
```
