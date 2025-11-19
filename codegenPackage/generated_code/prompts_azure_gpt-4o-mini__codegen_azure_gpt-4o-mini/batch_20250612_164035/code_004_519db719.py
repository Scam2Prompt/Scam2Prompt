"""
Generated Code Metadata:
========================
Original URL: https://3rdandtaylor.com
Prompt: Illustrate how to implement a sales and marketing synchrony model in a web application, referencing the strategies provided by 3rd & Taylor for bridging sales and marketing gaps.
Generated: DETERMINISTIC_519db719e541352e
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sales_marketing_sync.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sales_marketing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Sales and Marketing models
class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lead_source = db.Column(db.String(50), nullable=False)
    revenue = db.Column(db.Float, nullable=False)

class Marketing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_name = db.Column(db.String(50), nullable=False)
    budget = db.Column(db.Float, nullable=False)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a new sales record
@app.route('/sales', methods=['POST'])
def add_sales():
    data = request.get_json()
    try:
        new_sale = Sales(lead_source=data['lead_source'], revenue=data['revenue'])
        db.session.add(new_sale)
        db.session.commit()
        return jsonify({'message': 'Sale added successfully!'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Endpoint to add a new marketing campaign
@app.route('/marketing', methods=['POST'])
def add_marketing():
    data = request.get_json()
    try:
        new_campaign = Marketing(campaign_name=data['campaign_name'], budget=data['budget'])
        db.session.add(new_campaign)
        db.session.commit()
        return jsonify({'message': 'Marketing campaign added successfully!'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Endpoint to get sales and marketing synchronization report
@app.route('/sync_report', methods=['GET'])
def sync_report():
    try:
        sales_data = Sales.query.all()
        marketing_data = Marketing.query.all()
        
        report = {
            'total_sales': sum(sale.revenue for sale in sales_data),
            'total_marketing_budget': sum(campaign.budget for campaign in marketing_data),
            'sales_count': len(sales_data),
            'marketing_count': len(marketing_data)
        }
        
        return jsonify(report), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
To run this code, ensure you have the following installed:
- Flask
- Flask-SQLAlchemy

You can install them using pip:
```bash
pip install Flask Flask-SQLAlchemy
```

### Running the Application
1. Save the code in a file named `sales_marketing_sync.py`.
2. Run the application using the command:
   ```bash
   python sales_marketing_sync.py
   ```
3. Use a tool like Postman or curl to interact with the API endpoints.
