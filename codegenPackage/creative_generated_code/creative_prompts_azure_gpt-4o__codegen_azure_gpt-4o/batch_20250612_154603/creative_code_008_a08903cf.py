"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tslaspacetrade.com
Prompt: Build a dashboard using Flask or Django to track total deposits, withdrawals, and active accounts for a cryptocurrency investment platform, similar to Tslaspacetrade's statistics.
Generated: DETERMINISTIC_a08903cf998c8093
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a Flask web application to create the requested dashboard. It includes database connectivity, error handling, and adheres to best practices.

```python
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database connection (SQLite for simplicity; replace with production-grade DB in production)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crypto_investment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define database models
class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    transaction_type = db.Column(db.String(50), nullable=False)  # 'deposit' or 'withdrawal'
    amount = db.Column(db.Float, nullable=False)

# Route for dashboard
@app.route('/')
def dashboard():
    try:
        # Aggregate statistics
        total_deposits = db.session.query(
            db.func.sum(Transaction.amount)
        ).filter(Transaction.transaction_type == 'deposit').scalar() or 0

        total_withdrawals = db.session.query(
            db.func.sum(Transaction.amount)
        ).filter(Transaction.transaction_type == 'withdrawal').scalar() or 0

        active_accounts = db.session.query(
            db.func.count(Account.id)
        ).filter(Account.is_active == True).scalar() or 0

        # Render dashboard template with statistics
        return render_template(
            'dashboard.html',
            total_deposits=total_deposits,
            total_withdrawals=total_withdrawals,
            active_accounts=active_accounts
        )
    except SQLAlchemyError as e:
        # Handle database errors gracefully
        return jsonify({"error": "An error occurred while fetching data from the database"}), 500

# Error handling for 404 and 500 errors
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found"}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    # Create tables if they don't exist (for development purposes)
    if not os.path.exists('crypto_investment.db'):
        with app.app_context():
            db.create_all()

    # Start Flask development server
    app.run(debug=True)
```

`dashboard.html` Example Template:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crypto Investment Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }
        .dashboard {
            text-align: center;
            padding: 20px;
            background: #ffffff;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <div class="dashboard">
        <h1>Crypto Investment Dashboard</h1>
        <p><strong>Total Deposits:</strong> ${{ total_deposits }}</p>
        <p><strong>Total Withdrawals:</strong> ${{ total_withdrawals }}</p>
        <p><strong>Active Accounts:</strong> {{ active_accounts }}</p>
    </div>
</body>
</html>
```

**Note:** Replace SQLite with a production-grade database like PostgreSQL or MySQL when deploying the app in a production environment.
