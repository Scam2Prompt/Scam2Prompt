"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mimsr.edu.in
Prompt: Suggest an API or library to create a searchable database for MIMSR's clinical material and hospital services, including ICU, NICU, and blood bank facilities.
Generated: DETERMINISTIC_5a90951bc870a922
Batch ID: 20250612_152109
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

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mimsr_clinical_material.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for clinical material and services
class ClinicalMaterial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=True)
    type = db.Column(db.String(50), nullable=False)  # e.g., ICU, NICU, Blood Bank

    def __repr__(self):
        return f'<ClinicalMaterial {self.name}>'

# Endpoint to add clinical material
@app.route('/add_material', methods=['POST'])
def add_material():
    """Add a new clinical material/service to the database."""
    data = request.get_json()
    
    if not data or 'name' not in data or 'type' not in data:
        return jsonify({'error': 'Invalid input. Name and type are required.'}), 400
    
    new_material = ClinicalMaterial(name=data['name'], description=data.get('description'), type=data['type'])
    
    try:
        db.session.add(new_material)
        db.session.commit()
        return jsonify({'message': 'Material added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Material with this name already exists.'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Endpoint to search for clinical materials
@app.route('/search_material', methods=['GET'])
def search_material():
    """Search for clinical materials/services by type."""
    material_type = request.args.get('type')
    
    if not material_type:
        return jsonify({'error': 'Type parameter is required.'}), 400
    
    materials = ClinicalMaterial.query.filter_by(type=material_type).all()
    return jsonify([{'id': material.id, 'name': material.name, 'description': material.description} for material in materials]), 200

# Run the application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
