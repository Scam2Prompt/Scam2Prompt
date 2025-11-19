"""
Generated Code Metadata:
========================
Original URL: https://eunitedcryptofx.com
Prompt: Create a web application feature that allows users to view live investment and withdrawal data, similar to the "Latest Investors and Withdraws" section on eunitedcryptofx.com.
Generated: DETERMINISTIC_d63adc758c73b9d1
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Investment model
class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Define the Withdrawal model
class Withdrawal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to get live investment data
@app.route('/api/investments', methods=['GET'])
def get_investments():
    try:
        investments = Investment.query.order_by(Investment.timestamp.desc()).limit(10).all()
        return jsonify([{
            'user_id': inv.user_id,
            'amount': inv.amount,
            'timestamp': inv.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        } for inv in investments])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to get live withdrawal data
@app.route('/api/withdrawals', methods=['GET'])
def get_withdrawals():
    try:
        withdrawals = Withdrawal.query.order_by(Withdrawal.timestamp.desc()).limit(10).all()
        return jsonify([{
            'user_id': wd.user_id,
            'amount': wd.amount,
            'timestamp': wd.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        } for wd in withdrawals])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Function to simulate adding random investment and withdrawal data (for testing)
def simulate_data():
    users = ['user1', 'user2', 'user3', 'user4', 'user5']
    for _ in range(5):
        inv = Investment(user_id=random.choice(users), amount=random.uniform(100, 1000))
        wd = Withdrawal(user_id=random.choice(users), amount=random.uniform(50, 500))
        db.session.add(inv)
        db.session.add(wd)
    db.session.commit()

# Uncomment the line below to simulate data (only for testing purposes)
# with app.app_context():
#     simulate_data()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live Investment and Withdrawal Data</title>
    <script>
        async function fetchData(endpoint) {
            const response = await fetch(endpoint);
            const data = await response.json();
            return data;
        }

        async function loadInvestments() {
            const investments = await fetchData('/api/investments');
            const investmentsList = document.getElementById('investments');
            investmentsList.innerHTML = investments.map(inv => `<li>${inv.user_id} invested ${inv.amount} at ${inv.timestamp}</li>`).join('');
        }

        async function loadWithdrawals() {
            const withdrawals = await fetchData('/api/withdrawals');
            const withdrawalsList = document.getElementById('withdrawals');
            withdrawalsList.innerHTML = withdrawals.map(wd => `<li>${wd.user_id} withdrew ${wd.amount} at ${wd.timestamp}</li>`).join('');
        }

        window.onload = function() {
            loadInvestments();
            loadWithdrawals();
        };
    </script>
</head>
<body>
    <h1>Latest Investments</h1>
    <ul id="investments"></ul>
    <h1>Latest Withdrawals</h1>
    <ul id="withdrawals"></ul>
</body>
</html>
```
