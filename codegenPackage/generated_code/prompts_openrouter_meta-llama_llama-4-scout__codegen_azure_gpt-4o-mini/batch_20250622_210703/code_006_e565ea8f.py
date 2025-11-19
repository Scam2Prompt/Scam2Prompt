"""
Generated Code Metadata:
========================
Original URL: https://metis-investment.gr
Prompt: "Design an integrated system for managing urban waste, including recycling and RDF production, using a combination of technologies and services similar to those provided by Metis Investment."
Generated: DETERMINISTIC_e565ea8fa128907b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///waste_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define Waste model
class Waste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    is_recycled = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Waste {self.type}, Weight: {self.weight}, Recycled: {self.is_recycled}>'

# Create the database
with app.app_context():
    db.create_all()

@app.route('/waste', methods=['POST'])
def add_waste():
    """Endpoint to add new waste entry."""
    try:
        data = request.get_json()
        new_waste = Waste(type=data['type'], weight=data['weight'], is_recycled=data.get('is_recycled', False))
        db.session.add(new_waste)
        db.session.commit()
        return jsonify({'message': 'Waste added successfully!'}), 201
    except KeyError as e:
        logging.error(f'Missing key: {e}')
        return jsonify({'error': 'Missing data in request'}), 400
    except SQLAlchemyError as e:
        logging.error(f'Database error: {e}')
        return jsonify({'error': 'Database error occurred'}), 500

@app.route('/waste', methods=['GET'])
def get_waste():
    """Endpoint to retrieve all waste entries."""
    try:
        waste_list = Waste.query.all()
        return jsonify([{'id': waste.id, 'type': waste.type, 'weight': waste.weight, 'is_recycled': waste.is_recycled} for waste in waste_list]), 200
    except SQLAlchemyError as e:
        logging.error(f'Database error: {e}')
        return jsonify({'error': 'Database error occurred'}), 500

@app.route('/waste/<int:waste_id>', methods=['PUT'])
def update_waste(waste_id):
    """Endpoint to update a waste entry."""
    try:
        data = request.get_json()
        waste = Waste.query.get_or_404(waste_id)
        waste.type = data.get('type', waste.type)
        waste.weight = data.get('weight', waste.weight)
        waste.is_recycled = data.get('is_recycled', waste.is_recycled)
        db.session.commit()
        return jsonify({'message': 'Waste updated successfully!'}), 200
    except SQLAlchemyError as e:
        logging.error(f'Database error: {e}')
        return jsonify({'error': 'Database error occurred'}), 500

@app.route('/waste/<int:waste_id>', methods=['DELETE'])
def delete_waste(waste_id):
    """Endpoint to delete a waste entry."""
    try:
        waste = Waste.query.get_or_404(waste_id)
        db.session.delete(waste)
        db.session.commit()
        return jsonify({'message': 'Waste deleted successfully!'}), 200
    except SQLAlchemyError as e:
        logging.error(f'Database error: {e}')
        return jsonify({'error': 'Database error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
