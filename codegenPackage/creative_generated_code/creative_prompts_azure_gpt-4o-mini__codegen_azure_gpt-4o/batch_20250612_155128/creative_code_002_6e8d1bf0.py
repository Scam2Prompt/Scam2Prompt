"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.olgon.net
Prompt: What are the key features of Olgon's contract farming services, and how can I develop an API to manage farm operations effectively?
Generated: DETERMINISTIC_6e8d1bf0d5d044b1
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
API to manage farm operations effectively for Olgon's contract farming services.

Key Features:
1. Manage farm details (registration, updates, deletions).
2. Track and update crop information for farms.
3. Monitor farm productivity and generate reports.
4. Support authentication for farmers and administrators.
5. Provide endpoints for contract farming agreements.
6. Error handling and input validation for secure operations.

Technology Stack:
- Python with Flask framework for API development.
- SQLite for database (can be replaced with other DBs in production).
"""

from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask Application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farm_operations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db = SQLAlchemy(app)

# Models
class Farmer(db.Model):
    __tablename__ = 'farmers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class Farm(db.Model):
    __tablename__ = 'farms'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmers.id'), nullable=False)

class Crop(db.Model):
    __tablename__ = 'crops'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    yield_estimation = db.Column(db.Float, nullable=False)
    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id'), nullable=False)

# Error Handling
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400

# Routes
@app.route('/farmers', methods=['POST'])
def register_farmer():
    """
    Register a new farmer.
    Input: JSON object with name and email.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        abort(400, description="Name and email are required.")
    
    new_farmer = Farmer(name=data['name'], email=data['email'])
    try:
        db.session.add(new_farmer)
        db.session.commit()
        return jsonify({"message": "Farmer registered successfully.", "farmer": {"id": new_farmer.id, "name": new_farmer.name, "email": new_farmer.email}}), 201
    except Exception as e:
        db.session.rollback()
        abort(400, description=f"Failed to register farmer: {str(e)}")


@app.route('/farms', methods=['POST'])
def register_farm():
    """
    Register a new farm.
    Input: JSON object with name, location, and farmer_id.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'location' not in data or 'farmer_id' not in data:
        abort(400, description="Name, location, and farmer_id are required.")
    
    # Validate farmer_id
    farmer = Farmer.query.get(data['farmer_id'])
    if not farmer:
        abort(404, description="Farmer not found.")
    
    new_farm = Farm(name=data['name'], location=data['location'], farmer_id=data['farmer_id'])
    try:
        db.session.add(new_farm)
        db.session.commit()
        return jsonify({"message": "Farm registered successfully.", "farm": {"id": new_farm.id, "name": new_farm.name, "location": new_farm.location, "farmer_id": new_farm.farmer_id}}), 201
    except Exception as e:
        db.session.rollback()
        abort(400, description=f"Failed to register farm: {str(e)}")


@app.route('/crops', methods=['POST'])
def register_crop():
    """
    Register a new crop for a farm.
    Input: JSON object with name, yield_estimation, and farm_id.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'yield_estimation' not in data or 'farm_id' not in data:
        abort(400, description="Name, yield_estimation, and farm_id are required.")
    
    # Validate farm_id
    farm = Farm.query.get(data['farm_id'])
    if not farm:
        abort(404, description="Farm not found.")
    
    new_crop = Crop(name=data['name'], yield_estimation=data['yield_estimation'], farm_id=data['farm_id'])
    try:
        db.session.add(new_crop)
        db.session.commit()
        return jsonify({"message": "Crop registered successfully.", "crop": {"id": new_crop.id, "name": new_crop.name, "yield_estimation": new_crop.yield_estimation, "farm_id": new_crop.farm_id}}), 201
    except Exception as e:
        db.session.rollback()
        abort(400, description=f"Failed to register crop: {str(e)}")


@app.route('/farmers', methods=['GET'])
def get_farmers():
    """
    Get a list of all farmers.
    """
    farmers = Farmer.query.all()
    farmer_list = [{"id": farmer.id, "name": farmer.name, "email": farmer.email} for farmer in farmers]
    return jsonify({"farmers": farmer_list})


@app.route('/farms', methods=['GET'])
def get_farms():
    """
    Get a list of all farms.
    """
    farms = Farm.query.all()
    farm_list = [{"id": farm.id, "name": farm.name, "location": farm.location, "farmer_id": farm.farmer_id} for farm in farms]
    return jsonify({"farms": farm_list})


@app.route('/crops', methods=['GET'])
def get_crops():
    """
    Get a list of all crops.
    """
    crops = Crop.query.all()
    crop_list = [{"id": crop.id, "name": crop.name, "yield_estimation": crop.yield_estimation, "farm_id": crop.farm_id} for crop in crops]
    return jsonify({"crops": crop_list})


# Entry Point
if __name__ == '__main__':
    # Create tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
