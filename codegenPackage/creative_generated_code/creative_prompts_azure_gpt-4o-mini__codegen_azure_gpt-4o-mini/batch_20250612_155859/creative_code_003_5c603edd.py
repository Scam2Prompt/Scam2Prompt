"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cocfinance.com
Prompt: Develop an API integration that tracks the balance of work-life dynamics in the workplace, inspired by the debate on TikTok highlighted in the article about millennial CEO Lindsey Carter.
Generated: DETERMINISTIC_5c603edddee531ea
Batch ID: 20250612_155859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///work_life_balance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing balance entries
class BalanceEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(50), nullable=False)
    balance_score = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<BalanceEntry {self.id} - Employee {self.employee_id}>'

# Create the database
with app.app_context():
    db.create_all()

# Route to track work-life balance
@app.route('/api/balance', methods=['POST'])
def track_balance():
    """Track the work-life balance score for an employee."""
    try:
        data = request.get_json()

        # Validate incoming data
        if 'employee_id' not in data or 'balance_score' not in data:
            return jsonify({"error": "Missing employee_id or balance_score"}), 400
        
        employee_id = data['employee_id']
        balance_score = data['balance_score']

        # Validate the balance score
        if not isinstance(balance_score, (int, float)) or not (0 <= balance_score <= 10):
            return jsonify({"error": "balance_score must be a number between 0 and 10"}), 400
        
        # Create a new balance entry
        new_entry = BalanceEntry(employee_id=employee_id, balance_score=balance_score)
        db.session.add(new_entry)
        db.session.commit()

        return jsonify({"message": "Balance score recorded successfully", "entry_id": new_entry.id}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to fetch balance history for an employee
@app.route('/api/balance/<employee_id>', methods=['GET'])
def get_balance_history(employee_id):
    """Fetch the balance history for a specific employee."""
    try:
        entries = BalanceEntry.query.filter_by(employee_id=employee_id).all()
        if not entries:
            return jsonify({"message": "No entries found for this employee"}), 404
        
        # Prepare response data
        balance_history = [
            {"id": entry.id, "balance_score": entry.balance_score, "timestamp": entry.timestamp}
            for entry in entries
        ]

        return jsonify(balance_history), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main driver function
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```
