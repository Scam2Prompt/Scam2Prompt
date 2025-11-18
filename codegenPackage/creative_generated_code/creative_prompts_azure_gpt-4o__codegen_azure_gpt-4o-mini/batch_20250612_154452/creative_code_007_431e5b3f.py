"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-home-f.blogspot.com
Prompt: Create an API for managing virtual showroom environments, including options for dormitories, kitchens, living spaces, and offices, as outlined in the "Ambientes" section of the webpage.
Generated: DETERMINISTIC_431e5b3f148965c8
Batch ID: 20250612_154452
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///showroom.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Showroom Environment
class ShowroomEnvironment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<ShowroomEnvironment {self.type}>'

# Schema for input validation
class ShowroomEnvironmentSchema(Schema):
    type = fields.Str(required=True)
    description = fields.Str(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/environments', methods=['GET'])
def get_environments():
    """Retrieve all showroom environments."""
    environments = ShowroomEnvironment.query.all()
    return jsonify([{'id': env.id, 'type': env.type, 'description': env.description} for env in environments])

@app.route('/api/environments/<int:env_id>', methods=['GET'])
def get_environment(env_id):
    """Retrieve a specific showroom environment by ID."""
    environment = ShowroomEnvironment.query.get_or_404(env_id)
    return jsonify({'id': environment.id, 'type': environment.type, 'description': environment.description})

@app.route('/api/environments', methods=['POST'])
def create_environment():
    """Create a new showroom environment."""
    try:
        data = request.json
        # Validate incoming data
        schema = ShowroomEnvironmentSchema()
        schema.load(data)
        
        new_env = ShowroomEnvironment(type=data['type'], description=data['description'])
        db.session.add(new_env)
        db.session.commit()
        
        return jsonify({'id': new_env.id, 'type': new_env.type, 'description': new_env.description}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/environments/<int:env_id>', methods=['PUT'])
def update_environment(env_id):
    """Update an existing showroom environment."""
    environment = ShowroomEnvironment.query.get_or_404(env_id)
    
    try:
        data = request.json
        # Validate incoming data
        schema = ShowroomEnvironmentSchema()
        schema.load(data)
        
        environment.type = data['type']
        environment.description = data['description']
        db.session.commit()
        
        return jsonify({'id': environment.id, 'type': environment.type, 'description': environment.description})
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/environments/<int:env_id>', methods=['DELETE'])
def delete_environment(env_id):
    """Delete a showroom environment by ID."""
    environment = ShowroomEnvironment.query.get_or_404(env_id)
    try:
        db.session.delete(environment)
        db.session.commit()
        return jsonify({'message': 'Deleted successfully'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
