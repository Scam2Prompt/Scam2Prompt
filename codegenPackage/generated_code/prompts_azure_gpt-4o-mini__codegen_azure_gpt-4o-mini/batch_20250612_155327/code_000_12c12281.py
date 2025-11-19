"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: Generate a code snippet for a custom web application that integrates with an ERP system, focusing on lead tracking and inventory management as described on MDA Tech Sys.
Generated: DETERMINISTIC_12c122812a06327e
Batch ID: 20250612_155327
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
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Database configuration
DATABASE_URI = 'sqlite:///erp_integration.db'  # Change to your ERP database URI
engine = create_engine(DATABASE_URI)
Base = declarative_base()

# Define Lead model
class Lead(Base):
    __tablename__ = 'leads'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    status = Column(String, default='New')

# Define Inventory model
class Inventory(Base):
    __tablename__ = 'inventory'
    
    id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    quantity = Column(Integer, default=0)

# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/leads', methods=['POST'])
def create_lead():
    """Create a new lead."""
    try:
        data = request.json
        new_lead = Lead(name=data['name'], email=data['email'])
        session.add(new_lead)
        session.commit()
        return jsonify({"message": "Lead created successfully", "lead_id": new_lead.id}), 201
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/inventory', methods=['POST'])
def add_inventory():
    """Add a new product to inventory."""
    try:
        data = request.json
        new_product = Inventory(product_name=data['product_name'], quantity=data['quantity'])
        session.add(new_product)
        session.commit()
        return jsonify({"message": "Product added to inventory", "product_id": new_product.id}), 201
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/leads', methods=['GET'])
def get_leads():
    """Retrieve all leads."""
    try:
        leads = session.query(Lead).all()
        return jsonify([{"id": lead.id, "name": lead.name, "email": lead.email, "status": lead.status} for lead in leads]), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/inventory', methods=['GET'])
def get_inventory():
    """Retrieve all inventory items."""
    try:
        inventory_items = session.query(Inventory).all()
        return jsonify([{"id": item.id, "product_name": item.product_name, "quantity": item.quantity} for item in inventory_items]), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
