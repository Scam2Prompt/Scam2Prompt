"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tubalife.me
Prompt: Create a RESTful API that lists all the beauty services offered by TUBA SPA, including pricing and descriptions for each service.
Generated: DETERMINISTIC_e17d8e1952c2f3b1
Batch ID: 20250612_161520
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
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tubaspa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Beauty Service model
class BeautyService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Schema for serializing beauty services
class BeautyServiceSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)

# Initialize the schema
beauty_service_schema = BeautyServiceSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to get all beauty services
@app.route('/api/services', methods=['GET'])
def get_services():
    """
    Retrieve all beauty services offered by TUBA SPA.
    Returns a JSON array of services including their pricing and descriptions.
    """
    try:
        services = BeautyService.query.all()
        return jsonify(beauty_service_schema.dump(services)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to add a new beauty service
@app.route('/api/services', methods=['POST'])
def add_service():
    """
    Add a new beauty service to TUBA SPA.
    Expects a JSON object with name, description, and price.
    """
    try:
        # Validate and deserialize input
        new_service_data = request.json
        service = BeautyServiceSchema().load(new_service_data)
        
        # Create new service instance
        new_service = BeautyService(**service)
        db.session.add(new_service)
        db.session.commit()
        
        return jsonify(beauty_service_schema.dump(new_service)), 201
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
