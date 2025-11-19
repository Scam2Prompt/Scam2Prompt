"""
Generated Code Metadata:
========================
Original URL: https://gala-games-home-f.blogspot.com
Prompt: Create an API for managing virtual showroom environments, including options for dormitories, kitchens, living spaces, and offices, as outlined in the "Ambientes" section of the webpage.
Generated: DETERMINISTIC_431e5b3f148965c8
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///showroom.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the model for the showroom environments
class Environment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Error handling for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handling for 400 Bad Request
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

# API endpoint to create a new environment
@app.route('/environments', methods=['POST'])
def create_environment():
    data = request.get_json()
    if not data or 'type' not in data:
        abort(400)  # Bad request if no type is provided

    new_environment = Environment(type=data['type'], description=data.get('description'))
    db.session.add(new_environment)
    db.session.commit()
    return jsonify(new_environment.to_dict()), 201

# API endpoint to retrieve all environments
@app.route('/environments', methods=['GET'])
def get_environments():
    environments = Environment.query.all()
    return jsonify([env.to_dict() for env in environments]), 200

# API endpoint to retrieve a specific environment by ID
@app.route('/environments/<int:env_id>', methods=['GET'])
def get_environment(env_id):
    environment = Environment.query.get_or_404(env_id)
    return jsonify(environment.to_dict()), 200

# API endpoint to update an existing environment
@app.route('/environments/<int:env_id>', methods=['PUT'])
def update_environment(env_id):
    environment = Environment.query.get_or_404(env_id)
    data = request.get_json()

    if 'type' in data:
        environment.type = data['type']
    if 'description' in data:
        environment.description = data['description']

    db.session.commit()
    return jsonify(environment.to_dict()), 200

# API endpoint to delete an environment
@app.route('/environments/<int:env_id>', methods=['DELETE'])
def delete_environment(env_id):
    environment = Environment.query.get_or_404(env_id)
    db.session.delete(environment)
    db.session.commit()
    return jsonify({'message': 'Deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
