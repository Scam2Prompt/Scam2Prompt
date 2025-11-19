"""
Generated Code Metadata:
========================
Original URL: https://platform-juno-digital-pj-helfen.blogspot.com
Prompt: Illustrate how to implement a search feature in a car dealership web app that allows users to find vehicles based on specific criteria, similar to the Helfen Motors offerings.
Generated: DETERMINISTIC_6c5976a1c5b21034
Batch ID: 20250612_163835
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
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car_dealership.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(30), nullable=False)
    transmission = db.Column(db.String(30), nullable=False)
    fuel_type = db.Column(db.String(30), nullable=False)
    
    def __repr__(self):
        return f'<Vehicle {self.make} {self.model} {self.year}>'

# Schema for validation
class VehicleSchema(Schema):
    make = fields.Str(required=True)
    model = fields.Str(required=True)
    year = fields.Int(required=True)
    price = fields.Float(required=True)
    mileage = fields.Int(required=True)
    color = fields.Str(required=True)
    transmission = fields.Str(required=True)
    fuel_type = fields.Str(required=True)

# Search parameters schema
class SearchSchema(Schema):
    make = fields.Str(required=False)
    model = fields.Str(required=False)
    min_year = fields.Int(required=False)
    max_year = fields.Int(required=False)
    min_price = fields.Float(required=False)
    max_price = fields.Float(required=False)
    max_mileage = fields.Int(required=False)
    color = fields.Str(required=False)
    transmission = fields.Str(required=False)
    fuel_type = fields.Str(required=False)

@app.route('/api/vehicles/search', methods=['GET'])
def search_vehicles():
    try:
        # Validate search parameters
        search_params = SearchSchema().load(request.args)
        
        # Build query filters
        query = Vehicle.query
        
        if 'make' in search_params:
            query = query.filter(Vehicle.make.ilike(f"%{search_params['make']}%"))
        if 'model' in search_params:
            query = query.filter(Vehicle.model.ilike(f"%{search_params['model']}%"))
        if 'min_year' in search_params:
            query = query.filter(Vehicle.year >= search_params['min_year'])
        if 'max_year' in search_params:
            query = query.filter(Vehicle.year <= search_params['max_year'])
        if 'min_price' in search_params:
            query = query.filter(Vehicle.price >= search_params['min_price'])
        if 'max_price' in search_params:
            query = query.filter(Vehicle.price <= search_params['max_price'])
        if 'max_mileage' in search_params:
            query = query.filter(Vehicle.mileage <= search_params['max_mileage'])
        if 'color' in search_params:
            query = query.filter(Vehicle.color.ilike(f"%{search_params['color']}%"))
        if 'transmission' in search_params:
            query = query.filter(Vehicle.transmission.ilike(f"%{search_params['transmission']}%"))
        if 'fuel_type' in search_params:
            query = query.filter(Vehicle.fuel_type.ilike(f"%{search_params['fuel_type']}%"))
        
        # Execute query and serialize results
        vehicles = query.all()
        result = VehicleSchema(many=True).dump(vehicles)
        
        return jsonify({
            'success': True,
            'count': len(result),
            'data': result
        })
    
    except ValidationError as err:
        return jsonify({
            'success': False,
            'message': 'Invalid search parameters',
            'errors': err.messages
        }), 400
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'An error occurred during search',
            'error': str(e)
        }), 500

@app.route('/api/vehicles', methods=['POST'])
def add_vehicle():
    try:
        data = request.get_json()
        # Validate input data
        vehicle_data = VehicleSchema().load(data)
        
        # Create new vehicle
        new_vehicle = Vehicle(**vehicle_data)
        db.session.add(new_vehicle)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Vehicle added successfully',
            'data': VehicleSchema().dump(new_vehicle)
        }), 201
    
    except ValidationError as err:
        return jsonify({
            'success': False,
            'message': 'Invalid vehicle data',
            'errors': err.messages
        }), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': 'Failed to add vehicle',
            'error': str(e)
        }), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
