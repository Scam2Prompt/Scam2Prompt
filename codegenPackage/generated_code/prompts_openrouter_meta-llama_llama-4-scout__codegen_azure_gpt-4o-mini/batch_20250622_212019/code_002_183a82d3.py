"""
Generated Code Metadata:
========================
Original URL: https://memetic.digital
Prompt: How would you recommend using APIs or libraries to build a platform for venture builders to manage startup investments and provide strategic guidance, inspired by Memetic Digital's approach?
Generated: DETERMINISTIC_183a82d3bffd0611
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///venture_builder.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Investment model
class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    startup_name = db.Column(db.String(100), nullable=False)
    amount_invested = db.Column(db.Float, nullable=False)
    strategic_guidance = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Investment {self.startup_name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to create a new investment
@app.route('/investments', methods=['POST'])
def create_investment():
    try:
        data = request.get_json()
        new_investment = Investment(
            startup_name=data['startup_name'],
            amount_invested=data['amount_invested'],
            strategic_guidance=data.get('strategic_guidance')
        )
        db.session.add(new_investment)
        db.session.commit()
        return jsonify({'message': 'Investment created successfully!'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400

# API endpoint to retrieve all investments
@app.route('/investments', methods=['GET'])
def get_investments():
    try:
        investments = Investment.query.all()
        return jsonify([{
            'id': inv.id,
            'startup_name': inv.startup_name,
            'amount_invested': inv.amount_invested,
            'strategic_guidance': inv.strategic_guidance
        } for inv in investments]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to update an investment
@app.route('/investments/<int:investment_id>', methods=['PUT'])
def update_investment(investment_id):
    try:
        data = request.get_json()
        investment = Investment.query.get_or_404(investment_id)
        investment.startup_name = data.get('startup_name', investment.startup_name)
        investment.amount_invested = data.get('amount_invested', investment.amount_invested)
        investment.strategic_guidance = data.get('strategic_guidance', investment.strategic_guidance)
        db.session.commit()
        return jsonify({'message': 'Investment updated successfully!'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# API endpoint to delete an investment
@app.route('/investments/<int:investment_id>', methods=['DELETE'])
def delete_investment(investment_id):
    try:
        investment = Investment.query.get_or_404(investment_id)
        db.session.delete(investment)
        db.session.commit()
        return jsonify({'message': 'Investment deleted successfully!'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
