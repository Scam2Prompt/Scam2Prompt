"""
Generated Code Metadata:
========================
Original URL: https://tradezeenetwork.com
Prompt: Create a dashboard interface to display active users, total deposits, and total withdrawals for a trading platform, similar to the statistics section on Tradezeenetwork.
Generated: DETERMINISTIC_27ff0fa5addeb764
Batch ID: 20250612_151752
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trading_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, default=True)

# Define the Deposit model
class Deposit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)

# Define the Withdrawal model
class Withdrawal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)

# Route to render the dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# API endpoint to get statistics
@app.route('/api/stats', methods=['GET'])
def get_stats():
    try:
        # Count active users
        active_users_count = User.query.filter_by(is_active=True).count()
        
        # Calculate total deposits
        total_deposits = db.session.query(db.func.sum(Deposit.amount)).scalar() or 0
        
        # Calculate total withdrawals
        total_withdrawals = db.session.query(db.func.sum(Withdrawal.amount)).scalar() or 0
        
        # Prepare the response data
        stats = {
            'active_users': active_users_count,
            'total_deposits': total_deposits,
            'total_withdrawals': total_withdrawals
        }
        
        return jsonify(stats), 200
    except Exception as e:
        # Log the error (in production, use a logging framework)
        print(f"Error fetching statistics: {e}")
        return jsonify({'error': 'Failed to fetch statistics'}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=True)
```

```html
<!-- dashboard.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trading Platform Dashboard</title>
    <script>
        // Function to fetch statistics from the API
        async function fetchStats() {
            try {
                const response = await fetch('/api/stats');
                if (!response.ok) throw new Error('Network response was not ok');
                const stats = await response.json();
                document.getElementById('active-users').innerText = stats.active_users;
                document.getElementById('total-deposits').innerText = stats.total_deposits;
                document.getElementById('total-withdrawals').innerText = stats.total_withdrawals;
            } catch (error) {
                console.error('Error fetching stats:', error);
            }
        }

        // Fetch statistics when the page loads
        window.onload = fetchStats;
    </script>
</head>
<body>
    <h1>Trading Platform Dashboard</h1>
    <div>
        <h2>Active Users: <span id="active-users">0</span></h2>
        <h2>Total Deposits: $<span id="total-deposits">0</span></h2>
        <h2>Total Withdrawals: $<span id="total-withdrawals">0</span></h2>
    </div>
</body>
</html>
```
