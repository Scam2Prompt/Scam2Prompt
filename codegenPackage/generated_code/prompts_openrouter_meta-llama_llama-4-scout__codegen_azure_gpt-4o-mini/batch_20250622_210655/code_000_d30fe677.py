"""
Generated Code Metadata:
========================
Original URL: https://azagros.com
Prompt: Write a Python API for integrating agricultural production data with certification tracking, similar to Azagros.
Generated: DETERMINISTIC_d30fe6774c3bc7b7
Batch ID: 20250622_210655
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
from sqlalchemy.exc import IntegrityError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agriculture_certification.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the AgriculturalProduction model
class AgriculturalProduction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crop_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    certification_status = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'crop_name': self.crop_name,
            'quantity': self.quantity,
            'certification_status': self.certification_status
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Route to add new agricultural production data
@app.route('/api/production', methods=['POST'])
def add_production():
    data = request.get_json()
    try:
        new_production = AgriculturalProduction(
            crop_name=data['crop_name'],
            quantity=data['quantity'],
            certification_status=data['certification_status']
        )
        db.session.add(new_production)
        db.session.commit()
        return jsonify(new_production.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Data integrity error'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get all agricultural production data
@app.route('/api/production', methods=['GET'])
def get_productions():
    productions = AgriculturalProduction.query.all()
    return jsonify([production.to_dict() for production in productions]), 200

# Route to update agricultural production data
@app.route('/api/production/<int:production_id>', methods=['PUT'])
def update_production(production_id):
    data = request.get_json()
    production = AgriculturalProduction.query.get_or_404(production_id)
    
    try:
        production.crop_name = data.get('crop_name', production.crop_name)
        production.quantity = data.get('quantity', production.quantity)
        production.certification_status = data.get('certification_status', production.certification_status)
        
        db.session.commit()
        return jsonify(production.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to delete agricultural production data
@app.route('/api/production/<int:production_id>', methods=['DELETE'])
def delete_production(production_id):
    production = AgriculturalProduction.query.get_or_404(production_id)
    
    try:
        db.session.delete(production)
        db.session.commit()
        return jsonify({'message': 'Production data deleted successfully'}), 204
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', '0') == '1')
```
