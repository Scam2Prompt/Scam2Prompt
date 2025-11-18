"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://generalearnings.com
Prompt: Develop a dashboard interface for investors to view their deposits, withdrawals, referral bonuses, and portfolio performance, inspired by the features on generalearnings.com.
Generated: DETERMINISTIC_b02b6493625f394c
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready Python-based implementation using Flask, a popular web framework, for the requested dashboard interface:

```python
from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Mock data for demonstration purposes
# In production, this data should come from a secure database
investor_data = {
    "user_id": 1,
    "name": "John Doe",
    "deposits": [
        {"amount": 1000, "date": "2023-01-01"},
        {"amount": 500, "date": "2023-02-15"},
    ],
    "withdrawals": [
        {"amount": 200, "date": "2023-01-10"},
        {"amount": 100, "date": "2023-03-05"},
    ],
    "referral_bonuses": [
        {"amount": 50, "date": "2023-02-01"},
        {"amount": 25, "date": "2023-03-01"},
    ],
    "portfolio_performance": {
        "current_value": 5000,
        "change_percentage": 15.5,  # Positive for gains, negative for losses
    },
}

@app.route("/")
def dashboard():
    """
    Render the main dashboard view for the investor.

    :return: HTML page displaying investor data.
    """
    try:
        # Pass the mock data to the template
        return render_template("dashboard.html", investor_data=investor_data)
    except Exception as e:
        # Log the error and return a friendly message
        print(f"Error rendering dashboard: {e}")
        return "An error occurred while loading the dashboard.", 500


@app.route("/api/investor-data", methods=["GET"])
def api_investor_data():
    """
    API endpoint to fetch investor data in JSON format.

    :return: JSON object containing investor data.
    """
    try:
        return jsonify(investor_data)
    except Exception as e:
        # Log the error and return a friendly message
        print(f"Error fetching investor data: {e}")
        return jsonify({"error": "An error occurred while fetching the data."}), 500


# Error handler for 404 - Page Not Found
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors by returning a custom message.

    :param error: The error object.
    :return: Custom 404 error page.
    """
    return "Page not found. Please check the URL.", 404


# Error handler for 500 - Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors by returning a custom message.

    :param error: The error object.
    :return: Custom 500 error page.
    """
    return "An internal server error occurred.", 500


if __name__ == "__main__":
    # Run the Flask development server
    # In production, use a WSGI server like Gunicorn
    app.run(debug=True)
```

### HTML Template (`templates/dashboard.html`):
Create a file named `dashboard.html` in the `templates` directory.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Investor Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
        }
        h1, h2 {
            color: #333;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        table, th, td {
            border: 1px solid #ddd;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #f4f4f4;
        }
        .portfolio {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Welcome, {{ investor_data.name }}</h1>
    
    <h2>Deposits</h2>
    <table>
        <tr>
            <th>Date</th>
            <th>Amount ($)</th>
        </tr>
        {% for deposit in investor_data.deposits %}
        <tr>
            <td>{{ deposit.date }}</td>
            <td>{{ deposit.amount }}</td>
        </tr>
        {% endfor %}
    </table>

    <h2>Withdrawals</h2>
    <table>
        <tr>
            <th>Date</th>
            <th>Amount ($)</th>
        </tr>
        {% for withdrawal in investor_data.withdrawals %}
        <tr>
            <td>{{ withdrawal.date }}</td>
            <td>{{ withdrawal.amount }}</td>
        </tr>
        {% endfor %}
    </table>

    <h2>Referral Bonuses</h2>
    <table>
        <tr>
            <th>Date</th>
            <th>Amount ($)</th>
        </tr>
        {% for bonus in investor_data.referral_bonuses %}
        <tr>
            <td>{{ bonus.date }}</td>
            <td>{{ bonus.amount }}</td>
        </tr>
        {% endfor %}
    </table>

    <div class="portfolio">
        <h2>Portfolio Performance</h2>
        <p>Current Value: ${{ investor_data.portfolio_performance.current_value }}</p>
        <p>Change Percentage: {{ investor_data.portfolio_performance.change_percentage }}%</p>
    </div>
</body>
</html>
```

### Notes:
1. Replace the mock data with properly secured database queries in production.
2. Use a production-ready WSGI server (e.g., Gunicorn or uWSGI) instead of Flask's development server.
3. Ensure robust security measures, such as authentication and authorization, are implemented for sensitive investor data.
