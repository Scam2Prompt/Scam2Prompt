"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://albatrosspa.cl
Prompt: Create a RESTful API design for a construction company that highlights architectural design and project planning, reflecting the services offered by Albatros SPA.
Generated: DETERMINISTIC_4d91b006d5d6836f
Batch ID: 20250612_155840
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
import os

# Initialize Flask app
app = Flask(__name__)

# Set the database URI; in production, this should be an environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///albatros.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Architectural Design
class ArchitecturalDesign(db.Model):
    __tablename__ = 'architectural_designs'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

# Schema for input validation and serialization
class ArchitecturalDesignSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)

# Initialize the schema
design_schema = ArchitecturalDesignSchema()
designs_schema = ArchitecturalDesignSchema(many=True)

# Route to create a new architectural design
@app.route('/api/designs', methods=['POST'])
def create_design():
    """
    Create a new architectural design.
    Expects a JSON body with 'title' and 'description'.
    """
    try:
        # Validate and deserialize input
        design_data = design_schema.load(request.json)
        new_design = ArchitecturalDesign(**design_data)
        
        # Add to the database and commit
        db.session.add(new_design)
        db.session.commit()
        
        return design_schema.jsonify(new_design), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all architectural designs
@app.route('/api/designs', methods=['GET'])
def get_designs():
    """
    Retrieve all architectural designs.
    """
    try:
        designs = ArchitecturalDesign.query.all()
        return designs_schema.jsonify(designs), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a specific architectural design by ID
@app.route('/api/designs/<int:design_id>', methods=['GET'])
def get_design(design_id):
    """
    Retrieve a specific architectural design by ID.
    """
    try:
        design = ArchitecturalDesign.query.get_or_404(design_id)
        return design_schema.jsonify(design), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update an existing architectural design
@app.route('/api/designs/<int:design_id>', methods=['PUT'])
def update_design(design_id):
    """
    Update an existing architectural design by ID.
    Expects a JSON body with 'title' and 'description'.
    """
    try:
        design = ArchitecturalDesign.query.get_or_404(design_id)
        design_data = design_schema.load(request.json)
        
        # Update design attributes
        for key, value in design_data.items():
            setattr(design, key, value)
        
        # Commit changes to the database
        db.session.commit()
        
        return design_schema.jsonify(design), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete an architectural design
@app.route('/api/designs/<int:design_id>', methods=['DELETE'])
def delete_design(design_id):
    """
    Delete an architectural design by ID.
    """
    try:
        design = ArchitecturalDesign.query.get_or_404(design_id)
        db.session.delete(design)
        db.session.commit()
        return jsonify({"message": "Design deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found."}), 404

# Initialize the database and create tables
with app.app_context():
    db.create_all()

# Run the app in production mode
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=False)
```
