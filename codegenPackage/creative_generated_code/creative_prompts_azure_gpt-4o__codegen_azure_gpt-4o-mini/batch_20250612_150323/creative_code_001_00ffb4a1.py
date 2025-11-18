"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.ru
Prompt: Generate an API recommendation for managing inventory of diving gear, including items like "регуляторы и октопусы" and "компенсаторы плавучести," based on the catalog structure from https://opensea.ru.
Generated: DETERMINISTIC_00ffb4a1bdc1097a
Batch ID: 20250612_150323
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

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Gear model for the inventory table
class Gear(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Gear {self.name}>'

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/api/gear', methods=['GET'])
def get_gear():
    """Retrieve the list of all gear items in the inventory."""
    try:
        gear_list = Gear.query.all()
        result = [
            {"id": gear.id, "name": gear.name, "category": gear.category, "quantity": gear.quantity}
            for gear in gear_list
        ]
        return jsonify(result), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/gear', methods=['POST'])
def add_gear():
    """Add a new gear item to the inventory."""
    data = request.get_json()
    
    if not data or 'name' not in data or 'category' not in data or 'quantity' not in data:
        return jsonify({"error": "Invalid data. Please provide name, category, and quantity."}), 400
    
    new_gear = Gear(name=data['name'], category=data['category'], quantity=data['quantity'])
    try:
        db.session.add(new_gear)
        db.session.commit()
        return jsonify({"message": "Gear added successfully", "id": new_gear.id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/gear/<int:gear_id>', methods=['DELETE'])
def delete_gear(gear_id):
    """Delete a gear item from the inventory by ID."""
    gear = Gear.query.get(gear_id)
    
    if gear is None:
        return jsonify({"error": "Gear not found."}), 404

    try:
        db.session.delete(gear)
        db.session.commit()
        return jsonify({"message": "Gear deleted successfully"}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
