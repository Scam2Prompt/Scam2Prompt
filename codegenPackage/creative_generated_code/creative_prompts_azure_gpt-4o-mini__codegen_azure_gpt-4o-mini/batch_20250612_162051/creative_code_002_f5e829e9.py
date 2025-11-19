"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itmam.sa
Prompt: Create an API that enhances capacity building by developing skills and talents, as described in the Itmam Consulting's approach to empowering individuals and entities.
Generated: DETERMINISTIC_f5e829e968b45988
Batch ID: 20250612_162051
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
from werkzeug.exceptions import NotFound, BadRequest

# Initialize Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///capacity_building.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Skills
class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<Skill {self.name}>"

# Skill schema for serialization/deserialization
class SkillSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()

# Initialize the schema
skill_schema = SkillSchema()
skills_schema = SkillSchema(many=True)

# Create the database table if it doesn't exist
with app.app_context():
    db.create_all()

# API endpoint to create a new skill
@app.route('/skills', methods=['POST'])
def create_skill():
    """Create a new skill."""
    try:
        # Validate and deserialize input
        skill_data = skill_schema.load(request.json)

        # Create a new Skill object
        new_skill = Skill(**skill_data)

        # Add to session and commit to database
        db.session.add(new_skill)
        db.session.commit()

        return skill_schema.jsonify(new_skill), 201
    except ValidationError as err:
        raise BadRequest(f"Input validation error: {err.messages}")
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# API endpoint to get all skills
@app.route('/skills', methods=['GET'])
def get_skills():
    """Retrieve all skills."""
    skills = Skill.query.all()
    return skills_schema.jsonify(skills), 200

# API endpoint to get a specific skill by ID
@app.route('/skills/<int:skill_id>', methods=['GET'])
def get_skill(skill_id):
    """Retrieve a specific skill by ID."""
    skill = Skill.query.get(skill_id)
    if not skill:
        raise NotFound(f"Skill with ID {skill_id} not found.")
    return skill_schema.jsonify(skill), 200

# API endpoint to update a skill
@app.route('/skills/<int:skill_id>', methods=['PUT'])
def update_skill(skill_id):
    """Update an existing skill."""
    skill = Skill.query.get(skill_id)
    if not skill:
        raise NotFound(f"Skill with ID {skill_id} not found.")
    
    try:
        # Validate and deserialize input
        skill_data = skill_schema.load(request.json)
        
        # Update skill attributes
        for key, value in skill_data.items():
            setattr(skill, key, value)

        # Commit the changes to the database
        db.session.commit()
        return skill_schema.jsonify(skill), 200
    except ValidationError as err:
        raise BadRequest(f"Input validation error: {err.messages}")
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# API endpoint to delete a skill
@app.route('/skills/<int:skill_id>', methods=['DELETE'])
def delete_skill(skill_id):
    """Delete a specific skill."""
    skill = Skill.query.get(skill_id)
    if not skill:
        raise NotFound(f"Skill with ID {skill_id} not found.")
    
    db.session.delete(skill)
    db.session.commit()
    return jsonify({"message": "Skill deleted successfully."}), 204

# Error handler for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Error handler for not found
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": str(error)}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
