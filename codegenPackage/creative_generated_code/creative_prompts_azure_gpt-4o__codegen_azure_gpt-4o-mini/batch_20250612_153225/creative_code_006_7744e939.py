"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsmwealth.co.za
Prompt: Develop a web application that integrates investment portfolio tracking and analysis tools, allowing users to monitor long-term investment performance, as described in TSM Wealth's services.
Generated: DETERMINISTIC_7744e93928b73879
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# investment_tracker.py

from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Investment Model
class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount_invested = db.Column(db.Float, nullable=False)
    current_value = db.Column(db.Float, nullable=False)
    date_invested = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Investment {self.name}>"

# Create the database
with app.app_context():
    db.create_all()

# Route to render the main dashboard
@app.route('/')
def index():
    investments = Investment.query.all()  # Retrieve all investments
    return render_template('index.html', investments=investments)

# API route to add a new investment
@app.route('/add_investment', methods=['POST'])
def add_investment():
    try:
        data = request.get_json()
        new_investment = Investment(
            name=data['name'],
            amount_invested=data['amount_invested'],
            current_value=data['current_value']
        )
        db.session.add(new_investment)
        db.session.commit()
        return jsonify({"message": "Investment added successfully!"}), 201
    except Exception as e:
        logging.error(f"Error adding investment: {e}")
        return jsonify({"error": str(e)}), 500

# API route to get the investment performance
@app.route('/investment_performance', methods=['GET'])
def investment_performance():
    try:
        investments = Investment.query.all()
        performance_data = [{
            "name": inv.name,
            "amount_invested": inv.amount_invested,
            "current_value": inv.current_value,
            "performance": (inv.current_value - inv.amount_invested) / inv.amount_invested * 100
        } for inv in investments]
        return jsonify(performance_data), 200
    except Exception as e:
        logging.error(f"Error retrieving performance data: {e}")
        return jsonify({"error": str(e)}), 500

# Entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Investment Portfolio Tracker</title>
</head>
<body>
    <h1>Investment Portfolio Tracker</h1>
    <form id="investment-form">
        <input type="text" id="name" placeholder="Investment Name" required>
        <input type="number" id="amount_invested" placeholder="Amount Invested" required>
        <input type="number" id="current_value" placeholder="Current Value" required>
        <button type="submit">Add Investment</button>
    </form>

    <h2>Your Investments</h2>
    <ul id="investment-list">
        {% for investment in investments %}
        <li>{{ investment.name }} - Amount Invested: {{ investment.amount_invested }} - Current Value: {{ investment.current_value }}</li>
        {% endfor %}
    </ul>

    <script>
        document.getElementById('investment-form').addEventListener('submit', function(event) {
            event.preventDefault();
            const name = document.getElementById('name').value;
            const amount_invested = parseFloat(document.getElementById('amount_invested').value);
            const current_value = parseFloat(document.getElementById('current_value').value);

            fetch('/add_investment', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, amount_invested, current_value })
            })
            .then(response => {
                if (response.ok) {
                    alert('Investment added successfully!');
                    location.reload();  // Reload the page to see the new investment
                } else {
                    alert('Error adding investment.');
                }
            });
        });
    </script>
</body>
</html>
```
