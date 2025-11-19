"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afunabb.cl
Prompt: Generate a code snippet for a web application that allows users to manage social benefits for university staff, similar to the services offered by AFUNABB Chillán.
Generated: DETERMINISTIC_1275e151d180cc25
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///benefits.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database
db = SQLAlchemy(app)

# Model for University Staff Benefits
class StaffBenefit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.String(50), nullable=False)
    benefit_type = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)

# Schema for serializing StaffBenefit instances
class StaffBenefitSchema(Schema):
    id = fields.Int(dump_only=True)
    staff_id = fields.Str(required=True)
    benefit_type = fields.Str(required=True)
    amount = fields.Float(required=True)

# Initialize the schema
staff_benefit_schema = StaffBenefitSchema()
staff_benefits_schema = StaffBenefitSchema(many=True)

# Route to create a new staff benefit
@app.route('/benefits', methods=['POST'])
def create_benefit():
    """Create a new staff benefit."""
    try:
        # Validate and deserialize input
        new_benefit = staff_benefit_schema.load(request.json)
        benefit = StaffBenefit(**new_benefit)

        # Add to database
        db.session.add(benefit)
        db.session.commit()
        
        return staff_benefit_schema.jsonify(benefit), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all staff benefits
@app.route('/benefits', methods=['GET'])
def get_benefits():
    """Retrieve all staff benefits."""
    try:
        benefits = StaffBenefit.query.all()
        return staff_benefits_schema.jsonify(benefits), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a staff benefit
@app.route('/benefits/<int:id>', methods=['PUT'])
def update_benefit(id):
    """Update an existing staff benefit."""
    try:
        benefit = StaffBenefit.query.get_or_404(id)
        updated_data = staff_benefit_schema.load(request.json)
        
        for key, value in updated_data.items():
            setattr(benefit, key, value)
        
        db.session.commit()
        return staff_benefit_schema.jsonify(benefit), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a staff benefit
@app.route('/benefits/<int:id>', methods=['DELETE'])
def delete_benefit(id):
    """Delete a staff benefit."""
    try:
        benefit = StaffBenefit.query.get_or_404(id)
        db.session.delete(benefit)
        db.session.commit()
        return jsonify({"message": "Benefit deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)
```

This code creates a simple web application using Flask to manage social benefits for university staff, including CRUD operations with proper error handling and input validation.
