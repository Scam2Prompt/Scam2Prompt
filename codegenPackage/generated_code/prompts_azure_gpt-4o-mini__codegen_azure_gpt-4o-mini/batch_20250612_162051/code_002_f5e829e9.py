"""
Generated Code Metadata:
========================
Original URL: https://itmam.sa
Prompt: Create an API that enhances capacity building by developing skills and talents, as described in the Itmam Consulting's approach to empowering individuals and entities.
Generated: DETERMINISTIC_f5e829e968b45988
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///capacity_building.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Skill model
class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)

# Create a schema for input validation
class SkillSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a new skill
@app.route('/skills', methods=['POST'])
def add_skill():
    try:
        # Validate and deserialize input
        skill_schema = SkillSchema()
        skill_data = skill_schema.load(request.json)

        # Create a new Skill instance
        new_skill = Skill(name=skill_data['name'], description=skill_data.get('description'))
        db.session.add(new_skill)
        db.session.commit()

        return jsonify({"message": "Skill added successfully", "skill": skill_schema.dump(new_skill)}), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        logging.error(f"Error adding skill: {e}")
        return jsonify({"error": "An error occurred while adding the skill."}), 500

# API endpoint to retrieve all skills
@app.route('/skills', methods=['GET'])
def get_skills():
    try:
        skills = Skill.query.all()
        skill_schema = SkillSchema(many=True)
        return jsonify(skill_schema.dump(skills)), 200
    except Exception as e:
        logging.error(f"Error retrieving skills: {e}")
        return jsonify({"error": "An error occurred while retrieving skills."}), 500

# API endpoint to retrieve a specific skill by ID
@app.route('/skills/<int:skill_id>', methods=['GET'])
def get_skill(skill_id):
    try:
        skill = Skill.query.get_or_404(skill_id)
        skill_schema = SkillSchema()
        return jsonify(skill_schema.dump(skill)), 200
    except Exception as e:
        logging.error(f"Error retrieving skill with ID {skill_id}: {e}")
        return jsonify({"error": "An error occurred while retrieving the skill."}), 500

# API endpoint to update a skill
@app.route('/skills/<int:skill_id>', methods=['PUT'])
def update_skill(skill_id):
    try:
        skill = Skill.query.get_or_404(skill_id)
        skill_schema = SkillSchema()
        skill_data = skill_schema.load(request.json)

        # Update skill attributes
        skill.name = skill_data['name']
        skill.description = skill_data.get('description')
        db.session.commit()

        return jsonify({"message": "Skill updated successfully", "skill": skill_schema.dump(skill)}), 200

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        logging.error(f"Error updating skill with ID {skill_id}: {e}")
        return jsonify({"error": "An error occurred while updating the skill."}), 500

# API endpoint to delete a skill
@app.route('/skills/<int:skill_id>', methods=['DELETE'])
def delete_skill(skill_id):
    try:
        skill = Skill.query.get_or_404(skill_id)
        db.session.delete(skill)
        db.session.commit()
        return jsonify({"message": "Skill deleted successfully"}), 204
    except Exception as e:
        logging.error(f"Error deleting skill with ID {skill_id}: {e}")
        return jsonify({"error": "An error occurred while deleting the skill."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
