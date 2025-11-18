"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ranchioffline.com
Prompt: Create a REST API that allows users to query RanchiOffline's services, such as product availability, government documentation assistance, and exclusive deals.
Generated: DETERMINISTIC_e29029b8bf56e847
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ranchi_offline.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    available = db.Column(db.Boolean, default=True)

# Model for Government Documentation Assistance
class DocumentationAssistance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

# Model for Exclusive Deals
class ExclusiveDeal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deal_name = db.Column(db.String(100), nullable=False)
    discount_percentage = db.Column(db.Float, nullable=False)

# Initialize the database and create tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to get product availability
@app.route('/api/products', methods=['GET'])
def get_products():
    try:
        products = Product.query.all()
        return jsonify([{'id': p.id, 'name': p.name, 'available': p.available} for p in products]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get government documentation assistance
@app.route('/api/documentation-assistance', methods=['GET'])
def get_documentation_assistance():
    try:
        services = DocumentationAssistance.query.all()
        return jsonify([{'id': s.id, 'service_name': s.service_name, 'description': s.description} for s in services]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get exclusive deals
@app.route('/api/exclusive-deals', methods=['GET'])
def get_exclusive_deals():
    try:
        deals = ExclusiveDeal.query.all()
        return jsonify([{'id': d.id, 'deal_name': d.deal_name, 'discount_percentage': d.discount_percentage} for d in deals]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

Make sure to install the required packages by running:
```bash
pip install Flask Flask-SQLAlchemy
``` 

Before running the API, ensure you have the SQLite database set up, or it will be created automatically on the first run. You can interact with the API using tools like Postman or cURL.
