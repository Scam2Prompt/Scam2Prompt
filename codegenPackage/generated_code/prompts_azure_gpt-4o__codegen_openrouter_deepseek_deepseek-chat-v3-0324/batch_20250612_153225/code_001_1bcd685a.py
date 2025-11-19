"""
Generated Code Metadata:
========================
Original URL: https://padmavatienterprise.org
Prompt: Create a REST API using Flask that allows users to request quotes for products such as "Offset Multi Colour Printers," "Xerox Paper," and "Gift Items," and includes endpoints for managing client information.
Generated: DETERMINISTIC_1bcd685a537ae143
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class Client(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<Client {self.name}>'

class Quote(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    client_id = db.Column(db.String(36), db.ForeignKey('client.id'), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, approved, rejected
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

    client = db.relationship('Client', backref=db.backref('quotes', lazy=True))

    def __repr__(self):
        return f'<Quote {self.product_name}>'

# Helper Functions
def validate_client_data(data):
    required_fields = ['name', 'email', 'password']
    for field in required_fields:
        if field not in data:
            return False, f'{field} is required'
    return True, ''

def validate_quote_data(data):
    required_fields = ['client_id', 'product_name', 'quantity']
    for field in required_fields:
        if field not in data:
            return False, f'{field} is required'
    return True, ''

# Client Endpoints
@app.route('/api/clients', methods=['POST'])
def create_client():
    data = request.get_json()
    valid, message = validate_client_data(data)
    if not valid:
        return jsonify({'error': message}), 400

    if Client.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 400

    hashed_password = generate_password_hash(data['password'], method='sha256')
    client = Client(
        name=data['name'],
        email=data['email'],
        password=hashed_password,
        phone=data.get('phone', ''),
        address=data.get('address', '')
    )

    try:
        db.session.add(client)
        db.session.commit()
        return jsonify({'message': 'Client created successfully', 'client_id': client.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/clients/<client_id>', methods=['GET'])
def get_client(client_id):
    client = Client.query.get(client_id)
    if not client:
        return jsonify({'error': 'Client not found'}), 404

    client_data = {
        'id': client.id,
        'name': client.name,
        'email': client.email,
        'phone': client.phone,
        'address': client.address,
        'created_at': client.created_at.isoformat()
    }
    return jsonify(client_data), 200

@app.route('/api/clients/<client_id>', methods=['PUT'])
def update_client(client_id):
    client = Client.query.get(client_id)
    if not client:
        return jsonify({'error': 'Client not found'}), 404

    data = request.get_json()
    if 'email' in data and data['email'] != client.email:
        if Client.query.filter_by(email=data['email']).first():
            return jsonify({'error': 'Email already exists'}), 400

    try:
        client.name = data.get('name', client.name)
        client.email = data.get('email', client.email)
        if 'password' in data:
            client.password = generate_password_hash(data['password'], method='sha256')
        client.phone = data.get('phone', client.phone)
        client.address = data.get('address', client.address)
        db.session.commit()
        return jsonify({'message': 'Client updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/clients/<client_id>', methods=['DELETE'])
def delete_client(client_id):
    client = Client.query.get(client_id)
    if not client:
        return jsonify({'error': 'Client not found'}), 404

    try:
        db.session.delete(client)
        db.session.commit()
        return jsonify({'message': 'Client deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Quote Endpoints
@app.route('/api/quotes', methods=['POST'])
def create_quote():
    data = request.get_json()
    valid, message = validate_quote_data(data)
    if not valid:
        return jsonify({'error': message}), 400

    if not Client.query.get(data['client_id']):
        return jsonify({'error': 'Client not found'}), 404

    quote = Quote(
        client_id=data['client_id'],
        product_name=data['product_name'],
        quantity=data['quantity']
    )

    try:
        db.session.add(quote)
        db.session.commit()
        return jsonify({'message': 'Quote created successfully', 'quote_id': quote.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/quotes/<quote_id>', methods=['GET'])
def get_quote(quote_id):
    quote = Quote.query.get(quote_id)
    if not quote:
        return jsonify({'error': 'Quote not found'}), 404

    quote_data = {
        'id': quote.id,
        'client_id': quote.client_id,
        'product_name': quote.product_name,
        'quantity': quote.quantity,
        'status': quote.status,
        'created_at': quote.created_at.isoformat(),
        'updated_at': quote.updated_at.isoformat() if quote.updated_at else None
    }
    return jsonify(quote_data), 200

@app.route('/api/quotes/<quote_id>', methods=['PUT'])
def update_quote(quote_id):
    quote = Quote.query.get(quote_id)
    if not quote:
        return jsonify({'error': 'Quote not found'}), 404

    data = request.get_json()
    try:
        if 'product_name' in data:
            quote.product_name = data['product_name']
        if 'quantity' in data:
            quote.quantity = data['quantity']
        if 'status' in data:
            quote.status = data['status']
        db.session.commit()
        return jsonify({'message': 'Quote updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/quotes/<quote_id>', methods=['DELETE'])
def delete_quote(quote_id):
    quote = Quote.query.get(quote_id)
    if not quote:
        return jsonify({'error': 'Quote not found'}), 404

    try:
        db.session.delete(quote)
        db.session.commit()
        return jsonify({'message': 'Quote deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/quotes/client/<client_id>', methods=['GET'])
def get_client_quotes(client_id):
    quotes = Quote.query.filter_by(client_id=client_id).all()
    quotes_data = []
    for quote in quotes:
        quotes_data.append({
            'id': quote.id,
            'product_name': quote.product_name,
            'quantity': quote.quantity,
            'status': quote.status,
            'created_at': quote.created_at.isoformat(),
            'updated_at': quote.updated_at.isoformat() if quote.updated_at else None
        })
    return jsonify(quotes_data), 200

# Initialize Database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```
