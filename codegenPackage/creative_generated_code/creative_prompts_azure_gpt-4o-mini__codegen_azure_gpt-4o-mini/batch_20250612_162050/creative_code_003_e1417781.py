"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://volport.com
Prompt: Develop a REST API endpoint for managing inventory of car chargers, inspired by the product categories listed on Volport's website.
Generated: DETERMINISTIC_e1417781284ef76e
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chargers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Car Charger
class CarCharger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<CarCharger {self.name}>'

# Schema for validating input data
class ChargerSchema(Schema):
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    price = fields.Float(required=True)
    stock = fields.Int(required=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Initialize the schema
charger_schema = ChargerSchema()
chargers_schema = ChargerSchema(many=True)

@app.route('/api/chargers', methods=['POST'])
def add_charger():
    """Add a new car charger to the inventory."""
    try:
        # Validate and deserialize input data
        data = charger_schema.load(request.json)
        new_charger = CarCharger(**data)
        db.session.add(new_charger)
        db.session.commit()
        return charger_schema.dump(new_charger), 201
    except ValidationError as err:
        # Return validation errors
        return jsonify(err.messages), 400
    except Exception as e:
        # Handle any other exceptions
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/chargers', methods=['GET'])
def get_chargers():
    """Retrieve a list of all car chargers in the inventory."""
    chargers = CarCharger.query.all()
    return chargers_schema.dump(chargers), 200

@app.route('/api/chargers/<int:charger_id>', methods=['GET'])
def get_charger(charger_id):
    """Retrieve a specific car charger by ID."""
    charger = CarCharger.query.get_or_404(charger_id)
    return charger_schema.dump(charger), 200

@app.route('/api/chargers/<int:charger_id>', methods=['PUT'])
def update_charger(charger_id):
    """Update an existing car charger in the inventory."""
    charger = CarCharger.query.get_or_404(charger_id)
    try:
        data = charger_schema.load(request.json)
        for key, value in data.items():
            setattr(charger, key, value)
        db.session.commit()
        return charger_schema.dump(charger), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/chargers/<int:charger_id>', methods=['DELETE'])
def delete_charger(charger_id):
    """Delete a car charger from the inventory."""
    charger = CarCharger.query.get_or_404(charger_id)
    db.session.delete(charger)
    db.session.commit()
    return jsonify({'message': 'Charger deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
