"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olgadorks.com
Prompt: Outline a RESTful API design for a shipping company that includes endpoints for managing import/export requests and pre-financing options, based on Olgadorks' offerings.
Generated: DETERMINISTIC_6c975267f05ab657
Batch ID: 20250612_162051
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shipping.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Import/Export requests
class ShippingRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    details = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='pending')

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'details': self.details,
            'status': self.status
        }

# Database model for Pre-Financing options
class PreFinancingOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    terms = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'terms': self.terms
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new Shipping Request
@app.route('/shipping_requests', methods=['POST'])
def create_shipping_request():
    try:
        data = request.json
        new_request = ShippingRequest(type=data['type'], details=data['details'])
        db.session.add(new_request)
        db.session.commit()
        return jsonify(new_request.to_dict()), 201
    except (KeyError, SQLAlchemyError) as e:
        return jsonify(error=str(e)), 400

# Endpoint to get all Shipping Requests
@app.route('/shipping_requests', methods=['GET'])
def get_shipping_requests():
    try:
        requests = ShippingRequest.query.all()
        return jsonify([req.to_dict() for req in requests]), 200
    except SQLAlchemyError as e:
        return jsonify(error=str(e)), 500

# Endpoint to get a specific Shipping Request
@app.route('/shipping_requests/<int:request_id>', methods=['GET'])
def get_shipping_request(request_id):
    try:
        request = ShippingRequest.query.get_or_404(request_id)
        return jsonify(request.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify(error=str(e)), 500

# Endpoint to create a Pre-Financing option
@app.route('/pre_financing_options', methods=['POST'])
def create_pre_financing_option():
    try:
        data = request.json
        new_option = PreFinancingOption(amount=data['amount'], terms=data['terms'])
        db.session.add(new_option)
        db.session.commit()
        return jsonify(new_option.to_dict()), 201
    except (KeyError, SQLAlchemyError) as e:
        return jsonify(error=str(e)), 400

# Endpoint to get all Pre-Financing options
@app.route('/pre_financing_options', methods=['GET'])
def get_pre_financing_options():
    try:
        options = PreFinancingOption.query.all()
        return jsonify([option.to_dict() for option in options]), 200
    except SQLAlchemyError as e:
        return jsonify(error=str(e)), 500

# Endpoint to get a specific Pre-Financing option
@app.route('/pre_financing_options/<int:option_id>', methods=['GET'])
def get_pre_financing_option(option_id):
    try:
        option = PreFinancingOption.query.get_or_404(option_id)
        return jsonify(option.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify(error=str(e)), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
