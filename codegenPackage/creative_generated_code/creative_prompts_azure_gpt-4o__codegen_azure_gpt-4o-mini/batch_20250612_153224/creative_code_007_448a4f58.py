"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.punpuntoy.com
Prompt: Write code to integrate a catalog of playground equipment, such as BBL playgrounds and preschool furniture, into an e-commerce platform, as outlined on the Pun Pun Toy website.
Generated: DETERMINISTIC_448a4f5825c2a9bb
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLAlchemy Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///playground_catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the PlaygroundEquipment model
class PlaygroundEquipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<PlaygroundEquipment {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to add new playground equipment
@app.route('/add_equipment', methods=['POST'])
def add_equipment():
    """
    Endpoint to add new playground equipment to the catalog.
    Expected JSON payload:
    {
        "name": "Equipment Name",
        "category": "Equipment Category",
        "price": 99.99,
        "description": "Equipment Description"
    }
    """
    data = request.get_json()
    try:
        # Validate input data
        if not all(key in data for key in ('name', 'category', 'price')):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Create new equipment instance
        new_equipment = PlaygroundEquipment(
            name=data['name'],
            category=data['category'],
            price=data['price'],
            description=data.get('description', '')
        )
        
        # Add to the database
        db.session.add(new_equipment)
        db.session.commit()
        
        return jsonify({"message": "Equipment added successfully"}), 201
    
    except Exception as e:
        # Rollback in case of an error
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint to get all playground equipment
@app.route('/equipment', methods=['GET'])
def get_equipment():
    """
    Endpoint to retrieve all playground equipment in the catalog.
    Returns a JSON array of equipment.
    """
    try:
        equipment = PlaygroundEquipment.query.all()
        equipment_list = [
            {
                "id": eq.id,
                "name": eq.name,
                "category": eq.category,
                "price": eq.price,
                "description": eq.description
            } for eq in equipment
        ]
        return jsonify(equipment_list), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
