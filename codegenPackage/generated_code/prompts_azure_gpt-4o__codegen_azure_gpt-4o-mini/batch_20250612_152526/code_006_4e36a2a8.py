"""
Generated Code Metadata:
========================
Original URL: https://thebookkeepingdiaries.com
Prompt: Create a system that enables communication between bookkeepers and clients, allowing clients to make smart business decisions based on real-time financial data, as emphasized by "The Bookkeeping Diaries."
Generated: DETERMINISTIC_4e36a2a8da98f9d6
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookkeeping.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Client model
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Client {self.name}>'

# Define the FinancialData model
class FinancialData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    data = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    client = db.relationship('Client', backref=db.backref('financial_data', lazy=True))

    def __repr__(self):
        return f'<FinancialData {self.id} for Client {self.client_id}>'

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a new client
@app.route('/clients', methods=['POST'])
def add_client():
    try:
        data = request.get_json()
        new_client = Client(name=data['name'], email=data['email'])
        db.session.add(new_client)
        db.session.commit()
        return jsonify({'message': 'Client added successfully!'}), 201
    except Exception as e:
        logging.error(f"Error adding client: {e}")
        return jsonify({'error': 'Failed to add client'}), 400

# Endpoint to get all clients
@app.route('/clients', methods=['GET'])
def get_clients():
    try:
        clients = Client.query.all()
        return jsonify([{'id': client.id, 'name': client.name, 'email': client.email} for client in clients]), 200
    except Exception as e:
        logging.error(f"Error fetching clients: {e}")
        return jsonify({'error': 'Failed to fetch clients'}), 500

# Endpoint to add financial data for a client
@app.route('/financial_data', methods=['POST'])
def add_financial_data():
    try:
        data = request.get_json()
        new_data = FinancialData(client_id=data['client_id'], data=data['data'])
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'message': 'Financial data added successfully!'}), 201
    except Exception as e:
        logging.error(f"Error adding financial data: {e}")
        return jsonify({'error': 'Failed to add financial data'}), 400

# Endpoint to get financial data for a specific client
@app.route('/financial_data/<int:client_id>', methods=['GET'])
def get_financial_data(client_id):
    try:
        financial_data = FinancialData.query.filter_by(client_id=client_id).all()
        return jsonify([{'id': data.id, 'data': data.data, 'created_at': data.created_at} for data in financial_data]), 200
    except Exception as e:
        logging.error(f"Error fetching financial data for client {client_id}: {e}")
        return jsonify({'error': 'Failed to fetch financial data'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
