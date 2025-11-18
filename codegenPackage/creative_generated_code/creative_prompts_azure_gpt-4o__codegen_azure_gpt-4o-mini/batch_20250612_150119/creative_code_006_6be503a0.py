"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://profitproinvest.com
Prompt: Develop a dashboard interface using Flask or Django that mimics the user-friendly multifunctional dashboard described on profitproinvest.com, allowing users to track investments and withdrawals.
Generated: DETERMINISTIC_6be503a05be8e1af
Batch ID: 20250612_150119
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://code.jquery.com/jquery-3.5.1.slim.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dashboard.db'  # Database configuration
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Database migration support

# Database model for tracking investments and withdrawals
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(50), nullable=False)  # 'investment' or 'withdrawal'
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Transaction {self.id} - {self.transaction_type}: {self.amount}>'


@app.route('/')
def index():
    """Render the main dashboard with all transactions."""
    transactions = Transaction.query.all()  # Fetch all transactions from the database
    total_investments = sum(t.amount for t in transactions if t.transaction_type == 'investment')
    total_withdrawals = sum(t.amount for t in transactions if t.transaction_type == 'withdrawal')
    
    return render_template('index.html', transactions=transactions,
                           total_investments=total_investments, total_withdrawals=total_withdrawals)

@app.route('/add', methods=['POST'])
def add_transaction():
    """Add a new transaction based on the user's input."""
    amount = request.form.get('amount')
    transaction_type = request.form.get('transaction_type')

    # Validate input
    if not amount or not transaction_type or transaction_type not in ['investment', 'withdrawal']:
        flash('Invalid input! Please provide a valid amount and transaction type.', 'danger')
        return redirect(url_for('index'))

    try:
        amount = float(amount)  # Convert amount to float
        new_transaction = Transaction(amount=amount, transaction_type=transaction_type)
        db.session.add(new_transaction)
        db.session.commit()  # Commit the transaction to the database
        flash('Transaction added successfully!', 'success')
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        flash(f'An error occurred: {str(e)}', 'danger')

    return redirect(url_for('index'))


@app.route('/delete/<int:transaction_id>', methods=['POST'])
def delete_transaction(transaction_id):
    """Delete a specified transaction."""
    transaction = Transaction.query.get_or_404(transaction_id)  # Get transaction or 404
    try:
        db.session.delete(transaction)
        db.session.commit()  # Commit the deletion
        flash('Transaction deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        flash(f'An error occurred while deleting: {str(e)}', 'danger')

    return redirect(url_for('index'))


if __name__ == '__main__':
    # Run the app in debug mode for development, set to False in production
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Investment Dashboard</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Investment Dashboard</h1>
        <div class="alert alert-info">
            <strong>Total Investments:</strong> {{ total_investments }} &nbsp;
            <strong>Total Withdrawals:</strong> {{ total_withdrawals }}
        </div>

        <form method="POST" action="{{ url_for('add_transaction') }}">
            <div class="form-group">
                <label for="amount">Amount</label>
                <input type="number" step="0.01" class="form-control" name="amount" required>
            </div>
            <div class="form-group">
                <label for="transaction_type">Transaction Type</label>
                <select class="form-control" name="transaction_type" required>
                    <option value="investment">Investment</option>
                    <option value="withdrawal">Withdrawal</option>
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Add Transaction</button>
        </form>

        <h2 class="mt-5">Transaction History</h2>
        <table class="table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Type</th>
                    <th>Amount</th>
                    <th>Date</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                {% for transaction in transactions %}
                <tr>
                    <td>{{ transaction.id }}</td>
                    <td>{{ transaction.transaction_type }}</td>
                    <td>{{ transaction.amount }}</td>
                    <td>{{ transaction.date.strftime('%Y-%m-%d %H:%M:%S') }}</td>
                    <td>
                        <form method="POST" action="{{ url_for('delete_transaction', transaction_id=transaction.id) }}">
                            <button type="submit" class="btn btn-danger">Delete</button>
                        </form>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
``` 

### Setup Instructions
1. Ensure you have Python installed.
2. Install Flask and related packages:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Migrate
   ```
3. Initialize the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```
4. Run the application:
   ```bash
   python app.py
   ```

### Note
- Replace `'your_secret_key'` with an actual secret key for production.
- Adjust database URI and configurations as needed for different environments.
