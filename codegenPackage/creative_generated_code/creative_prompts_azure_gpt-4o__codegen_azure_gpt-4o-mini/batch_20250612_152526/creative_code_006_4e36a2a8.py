"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebookkeepingdiaries.com
Prompt: Create a system that enables communication between bookkeepers and clients, allowing clients to make smart business decisions based on real-time financial data, as emphasized by "The Bookkeeping Diaries."
Generated: DETERMINISTIC_4e36a2a8da98f9d6
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application and the SQLAlchemy ORM
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookkeeping.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for the Bookkeeper
class Bookkeeper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Model for the Client
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    bookkeeper_id = db.Column(db.Integer, db.ForeignKey('bookkeeper.id'), nullable=False)
    bookkeeper = db.relationship('Bookkeeper', backref='clients')

# Model for Financial Data
class FinancialData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    data = db.Column(db.JSON, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new bookkeeper
@app.route('/bookkeeper', methods=['POST'])
def create_bookkeeper():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        abort(400, 'Name and email are required')
    
    new_bookkeeper = Bookkeeper(name=data['name'], email=data['email'])
    db.session.add(new_bookkeeper)
    db.session.commit()
    return jsonify({'id': new_bookkeeper.id}), 201

# Route to create a new client
@app.route('/client', methods=['POST'])
def create_client():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data or 'bookkeeper_id' not in data:
        abort(400, 'Name, email and bookkeeper_id are required')
    
    new_client = Client(name=data['name'], email=data['email'], bookkeeper_id=data['bookkeeper_id'])
    db.session.add(new_client)
    db.session.commit()
    return jsonify({'id': new_client.id}), 201

# Route to submit financial data for a client
@app.route('/financial-data', methods=['POST'])
def submit_financial_data():
    data = request.get_json()
    if not data or 'client_id' not in data or 'data' not in data:
        abort(400, 'Client ID and financial data are required')

    new_financial_data = FinancialData(client_id=data['client_id'], data=data['data'])
    db.session.add(new_financial_data)
    db.session.commit()
    return jsonify({'id': new_financial_data.id}), 201

# Route to get financial data for a client
@app.route('/financial-data/<int:client_id>', methods=['GET'])
def get_financial_data(client_id):
    financial_data = FinancialData.query.filter_by(client_id=client_id).all()
    if not financial_data:
        abort(404, 'No financial data found for this client')

    return jsonify([{'id': fd.id, 'data': fd.data, 'timestamp': fd.timestamp} for fd in financial_data])

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handling for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```
