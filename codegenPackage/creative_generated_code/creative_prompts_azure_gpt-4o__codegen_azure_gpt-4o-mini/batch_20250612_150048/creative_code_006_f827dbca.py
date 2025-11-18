"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ifundsoption.com
Prompt: Develop a dashboard for tracking confirmed and pending withdrawals, inspired by the transaction statuses displayed on iFundsOption.
Generated: DETERMINISTIC_f827dbca075a30a8
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///withdrawals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Withdrawal model
class Withdrawal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)  # 'confirmed' or 'pending'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Withdrawal {self.id} - {self.status}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route to render the dashboard page
@app.route('/')
def dashboard():
    """Render the dashboard for tracking withdrawals."""
    try:
        pending_withdrawals = Withdrawal.query.filter_by(status='pending').all()
        confirmed_withdrawals = Withdrawal.query.filter_by(status='confirmed').all()
        return render_template('dashboard.html', 
                               pending_withdrawals=pending_withdrawals, 
                               confirmed_withdrawals=confirmed_withdrawals)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to add a new withdrawal
@app.route('/add_withdrawal', methods=['POST'])
def add_withdrawal():
    """Endpoint to add a new withdrawal."""
    try:
        amount = request.json.get('amount')
        status = request.json.get('status')
        
        if amount is None or status not in ['confirmed', 'pending']:
            return jsonify({"error": "Invalid input"}), 400

        new_withdrawal = Withdrawal(amount=amount, status=status)
        db.session.add(new_withdrawal)
        db.session.commit()

        return jsonify({"message": "Withdrawal added successfully!"}), 201
    except Exception as e:
        db.session.rollback()  # Rollback any changes on error
        return jsonify({"error": str(e)}), 500

# Route to fetch all withdrawals
@app.route('/withdrawals', methods=['GET'])
def get_withdrawals():
    """Endpoint to fetch all withdrawals."""
    try:
        withdrawals = Withdrawal.query.all()
        return jsonify([{'id': w.id, 'amount': w.amount, 'status': w.status, 'created_at': w.created_at} for w in withdrawals]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

```html
<!-- templates/dashboard.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Withdrawal Dashboard</title>
</head>
<body>
    <h1>Withdrawal Dashboard</h1>
    <h2>Pending Withdrawals</h2>
    <ul>
        {% for withdrawal in pending_withdrawals %}
            <li>Withdrawal ID: {{ withdrawal.id }}, Amount: {{ withdrawal.amount }}, Status: {{ withdrawal.status }}</li>
        {% endfor %}
    </ul>

    <h2>Confirmed Withdrawals</h2>
    <ul>
        {% for withdrawal in confirmed_withdrawals %}
            <li>Withdrawal ID: {{ withdrawal.id }}, Amount: {{ withdrawal.amount }}, Status: {{ withdrawal.status }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```
