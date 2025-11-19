"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Develop a web application that integrates investment portfolio tracking and analysis tools, allowing users to monitor long-term investment performance, as described in TSM Wealth's services.
Generated: DETERMINISTIC_7744e93928b73879
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Investment model
class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount_invested = db.Column(db.Float, nullable=False)
    current_value = db.Column(db.Float, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Investment {self.name}>'

# Create the database
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to add a new investment
@app.route('/add_investment', methods=['POST'])
def add_investment():
    try:
        data = request.json
        new_investment = Investment(
            name=data['name'],
            amount_invested=data['amount_invested'],
            current_value=data['current_value']
        )
        db.session.add(new_investment)
        db.session.commit()
        return jsonify({'message': 'Investment added successfully!'}), 201
    except Exception as e:
        logging.error(f"Error adding investment: {e}")
        return jsonify({'error': 'Failed to add investment'}), 400

# Route to get all investments
@app.route('/investments', methods=['GET'])
def get_investments():
    try:
        investments = Investment.query.all()
        return jsonify([{
            'id': inv.id,
            'name': inv.name,
            'amount_invested': inv.amount_invested,
            'current_value': inv.current_value,
            'date_added': inv.date_added
        } for inv in investments]), 200
    except Exception as e:
        logging.error(f"Error retrieving investments: {e}")
        return jsonify({'error': 'Failed to retrieve investments'}), 500

# Route to analyze investment performance
@app.route('/analyze', methods=['GET'])
def analyze_performance():
    try:
        investments = Investment.query.all()
        total_invested = sum(inv.amount_invested for inv in investments)
        total_value = sum(inv.current_value for inv in investments)
        performance = {
            'total_invested': total_invested,
            'total_value': total_value,
            'performance': total_value - total_invested
        }
        return jsonify(performance), 200
    except Exception as e:
        logging.error(f"Error analyzing performance: {e}")
        return jsonify({'error': 'Failed to analyze performance'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (index.html)
```html
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
    <div id="investments"></div>
    <script>
        document.getElementById('investment-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const name = document.getElementById('name').value;
            const amount_invested = parseFloat(document.getElementById('amount_invested').value);
            const current_value = parseFloat(document.getElementById('current_value').value);
            const response = await fetch('/add_investment', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, amount_invested, current_value })
            });
            const result = await response.json();
            alert(result.message || result.error);
            loadInvestments();
        });

        async function loadInvestments() {
            const response = await fetch('/investments');
            const investments = await response.json();
            const investmentsDiv = document.getElementById('investments');
            investmentsDiv.innerHTML = investments.map(inv => `<p>${inv.name}: $${inv.current_value} (Invested: $${inv.amount_invested})</p>`).join('');
        }

        loadInvestments();
    </script>
</body>
</html>
```

### Notes
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- The application uses SQLite for simplicity; for production, consider using a more robust database.
- The HTML template is included for a basic user interface.
