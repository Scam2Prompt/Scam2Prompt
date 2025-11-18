"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: Suggest an API for monitoring the environmental impact of Styrofoam recycling, focusing on metrics like energy savings and pollution reduction, as highlighted on the website.
Generated: DETERMINISTIC_1bafcb6a358921fd
Batch ID: 20250612_153224
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
from marshmallow import Schema, fields, validate, ValidationError

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///environmental_impact.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model for Environmental Impact
class EnvironmentalImpact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    energy_savings = db.Column(db.Float, nullable=False)
    pollution_reduction = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<EnvironmentalImpact {self.id}>"

# Schema for input validation and serialization
class EnvironmentalImpactSchema(Schema):
    energy_savings = fields.Float(required=True, validate=validate.Range(min=0))
    pollution_reduction = fields.Float(required=True, validate=validate.Range(min=0))
    description = fields.Str()

impact_schema = EnvironmentalImpactSchema()

# Endpoint to create a new environmental impact record
@app.route('/impact', methods=['POST'])
def add_impact():
    """Create a new environmental impact record."""
    try:
        # Validate and deserialize input data
        data = impact_schema.load(request.json)
        new_impact = EnvironmentalImpact(**data)
        
        # Add to database
        db.session.add(new_impact)
        db.session.commit()
        
        return impact_schema.dump(new_impact), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint to get all environmental impact records
@app.route('/impact', methods=['GET'])
def get_impacts():
    """Retrieve all environmental impact records."""
    impacts = EnvironmentalImpact.query.all()
    return jsonify(impact_schema.dump(impacts, many=True)), 200

# Initialize the database before starting the app
@app.before_first_request
def create_tables():
    """Create database tables."""
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```
