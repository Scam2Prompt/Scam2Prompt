"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icetrade-inv.com
Prompt: Develop a dashboard interface that displays investment plans, account balances, and transaction history, similar to Ice Investment Company's platform.
Generated: DETERMINISTIC_7066ac00b61cf734
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investments.db'  # Database configuration
app.config['SECRET_KEY'] = 'your_secret_key'  # Security key for session management
db = SQLAlchemy(app)

# Define a model for storing investment plans
class InvestmentPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    return_rate = db.Column(db.Float, nullable=False)
    duration_months = db.Column(db.Integer, nullable=False)

# Define a model for storing user accounts
class UserAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0)

# Define a model for storing transactions
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_account.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Route for the dashboard interface
@app.route('/')
def dashboard():
    try:
        # Fetch all investment plans, user accounts, and transaction history
        investment_plans = InvestmentPlan.query.all()
        user_accounts = UserAccount.query.all()
        transactions = Transaction.query.all()
        return render_template('dashboard.html', 
                               investment_plans=investment_plans, 
                               user_accounts=user_accounts, 
                               transactions=transactions)
    except Exception as e:
        flash('Error fetching data: {}'.format(str(e)), 'danger')
        return redirect('/')

# Run the application
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug to False in production

# Sample HTML Template (dashboard.html)
'''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Investment Dashboard</title>
</head>
<body>
    <h1>Investment Plans</h1>
    <table>
        <tr>
            <th>Name</th>
            <th>Return Rate</th>
            <th>Duration (Months)</th>
        </tr>
        {% for plan in investment_plans %}
        <tr>
            <td>{{ plan.name }}</td>
            <td>{{ plan.return_rate }}%</td>
            <td>{{ plan.duration_months }}</td>
        </tr>
        {% endfor %}
    </table>

    <h1>User Accounts</h1>
    <table>
        <tr>
            <th>Username</th>
            <th>Balance</th>
        </tr>
        {% for account in user_accounts %}
        <tr>
            <td>{{ account.username }}</td>
            <td>${{ account.balance }}</td>
        </tr>
        {% endfor %}
    </table>

    <h1>Transaction History</h1>
    <table>
        <tr>
            <th>User ID</th>
            <th>Amount</th>
            <th>Timestamp</th>
        </tr>
        {% for transaction in transactions %}
        <tr>
            <td>{{ transaction.user_id }}</td>
            <td>${{ transaction.amount }}</td>
            <td>{{ transaction.timestamp }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
'''
```
