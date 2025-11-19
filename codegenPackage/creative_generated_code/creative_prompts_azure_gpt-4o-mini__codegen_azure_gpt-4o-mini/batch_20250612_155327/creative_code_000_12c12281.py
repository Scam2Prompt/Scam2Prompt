"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdatechsys.com
Prompt: Generate a code snippet for a custom web application that integrates with an ERP system, focusing on lead tracking and inventory management as described on MDA Tech Sys.
Generated: DETERMINISTIC_12c122812a06327e
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///erp_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Lead model
class Lead(db.Model):
    __tablename__ = 'leads'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    status = db.Column(db.String(50), default='New')

    def __repr__(self):
        return f'<Lead {self.name}>'

# Define the Inventory model
class Inventory(db.Model):
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Inventory {self.product_name}>'

# Route to create a new lead
@app.route('/leads', methods=['POST'])
def create_lead():
    data = request.get_json()
    new_lead = Lead(name=data['name'], email=data['email'], status=data.get('status', 'New'))
    
    try:
        db.session.add(new_lead)
        db.session.commit()
        return jsonify({'message': 'Lead created successfully', 'lead': new_lead.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Lead with this email already exists'}), 400

# Route to get the list of leads
@app.route('/leads', methods=['GET'])
def get_leads():
    leads = Lead.query.all()
    return jsonify([{'id': lead.id, 'name': lead.name, 'email': lead.email, 'status': lead.status} for lead in leads])

# Route to create new inventory item
@app.route('/inventory', methods=['POST'])
def create_inventory():
    data = request.get_json()
    new_item = Inventory(product_name=data['product_name'], quantity=data['quantity'], price=data['price'])
    
    try:
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': 'Inventory item created successfully', 'item_id': new_item.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get the inventory list
@app.route('/inventory', methods=['GET'])
def get_inventory():
    items = Inventory.query.all()
    return jsonify([{'id': item.id, 'product_name': item.product_name, 'quantity': item.quantity, 'price': item.price} for item in items])

# Error handling for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handling for generic server issues
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'An internal error occurred'}), 500

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create the database tables
    app.run(debug=True)  # Set debug to False in production
```
