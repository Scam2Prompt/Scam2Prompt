"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkcapitalmarkets.com
Prompt: Create a REST API for managing client accounts and investment packages, similar to the functionality offered by Ark Capital Markets.
Generated: DETERMINISTIC_8ede3e2d4e16b96c
Batch ID: 20250612_152249
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
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Client model
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

# Investment package model
class InvestmentPackage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    return_rate = db.Column(db.Float, nullable=False)

    def __init__(self, name, return_rate):
        self.name = name
        self.return_rate = return_rate

# Client schema for serialization
class ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Client

# Investment package schema for serialization
class InvestmentPackageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = InvestmentPackage

# Initialize database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new client
@app.route('/clients', methods=['POST'])
def add_client():
    try:
        name = request.json['name']
        email = request.json['email']
        new_client = Client(name, email)
        db.session.add(new_client)
        db.session.commit()
        return ClientSchema().dump(new_client), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Client with this email already exists."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all clients
@app.route('/clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return ClientSchema(many=True).dump(clients), 200

# Endpoint to create a new investment package
@app.route('/investment-packages', methods=['POST'])
def add_investment_package():
    try:
        name = request.json['name']
        return_rate = request.json['return_rate']
        new_package = InvestmentPackage(name, return_rate)
        db.session.add(new_package)
        db.session.commit()
        return InvestmentPackageSchema().dump(new_package), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all investment packages
@app.route('/investment-packages', methods=['GET'])
def get_investment_packages():
    packages = InvestmentPackage.query.all()
    return InvestmentPackageSchema(many=True).dump(packages), 200

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found."}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "An internal error occurred."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```
