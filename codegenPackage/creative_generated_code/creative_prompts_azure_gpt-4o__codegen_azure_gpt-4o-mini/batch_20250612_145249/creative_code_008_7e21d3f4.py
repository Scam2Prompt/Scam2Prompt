"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.premierpointing.com.au
Prompt: Design a REST API for managing heritage building restoration projects, including endpoints for tracking tuckpointing progress and material usage.
Generated: DETERMINISTIC_7e21d3f40b744f13
Batch ID: 20250612_145249
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
from marshmallow import fields, ValidationError

# Initialize the app
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heritage_buildings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Heritage Building Model
class HeritageBuilding(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    tuckpointing_progress = db.relationship('Tuckpointing', backref='building', lazy=True)

class Tuckpointing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building_id = db.Column(db.Integer, db.ForeignKey('heritage_building.id'), nullable=False)
    progress_percentage = db.Column(db.Float, nullable=False)
    material_usage = db.Column(db.Float, nullable=False)  # in kg

# Heritage Building Schema
class HeritageBuildingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = HeritageBuilding
        load_instance = True

# Tuckpointing Schema
class TuckpointingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tuckpointing
        load_instance = True

# Initialize schemas
building_schema = HeritageBuildingSchema()
buildings_schema = HeritageBuildingSchema(many=True)
tuckpointing_schema = TuckpointingSchema()
tuckpointings_schema = TuckpointingSchema(many=True)

# Create a new heritage building
@app.route('/buildings', methods=['POST'])
def add_building():
    name = request.json.get('name')
    location = request.json.get('location')
    
    if not name or not location:
        return jsonify({'error': 'Name and location are required'}), 400
    
    new_building = HeritageBuilding(name=name, location=location)
    
    try:
        db.session.add(new_building)
        db.session.commit()
        return building_schema.jsonify(new_building), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Get all heritage buildings
@app.route('/buildings', methods=['GET'])
def get_buildings():
    buildings = HeritageBuilding.query.all()
    return buildings_schema.jsonify(buildings), 200

# Track tuckpointing progress for a building
@app.route('/buildings/<int:building_id>/tuckpointing', methods=['POST'])
def add_tuckpointing(building_id):
    progress_percentage = request.json.get('progress_percentage')
    material_usage = request.json.get('material_usage')

    if progress_percentage is None or material_usage is None:
        return jsonify({'error': 'Progress percentage and material usage are required'}), 400
    
    new_tuckpointing = Tuckpointing(building_id=building_id, 
                                     progress_percentage=progress_percentage, 
                                     material_usage=material_usage)

    try:
        db.session.add(new_tuckpointing)
        db.session.commit()
        return tuckpointing_schema.jsonify(new_tuckpointing), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Get all tuckpointing records for a specific building
@app.route('/buildings/<int:building_id>/tuckpointing', methods=['GET'])
def get_tuckpointing(building_id):
    tuckpointings = Tuckpointing.query.filter_by(building_id=building_id).all()
    return tuckpointings_schema.jsonify(tuckpointings), 200

# Error handler for bad requests
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request', 'message': str(error)}), 400

# Error handler for internal server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error', 'message': str(error)}), 500

# Run the app
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set to False in production
```
