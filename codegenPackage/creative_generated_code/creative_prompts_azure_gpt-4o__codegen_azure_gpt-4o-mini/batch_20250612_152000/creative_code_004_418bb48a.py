"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corgiaixyz.pages.dev
Prompt: Write code to implement an AI marketplace similar to the "Don’t let your boss know" initiative mentioned on the CorgiAI roadmap, using Python and Flask.
Generated: DETERMINISTIC_418bb48ac126fdc9
Batch ID: 20250612_152000
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
from flask_cors import CORS
import os

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///ai_marketplace.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the AI Model entity
class AIModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    creator = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert AIModel instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'creator': self.creator
        }

# Initialize the database
@app.before_first_request
def create_tables():
    """Create database tables if they don't exist."""
    db.create_all()

# Route to get all AI models
@app.route('/api/models', methods=['GET'])
def get_models():
    """GET endpoint to retrieve all AI models."""
    models = AIModel.query.all()
    return jsonify([model.to_dict() for model in models]), 200

# Route to add a new AI model
@app.route('/api/models', methods=['POST'])
def add_model():
    """POST endpoint to add a new AI model."""
    if not request.json or not 'name' in request.json:
        abort(400, description="Missing model name in request.")

    new_model = AIModel(
        name=request.json['name'],
        description=request.json.get('description', ''),
        creator=request.json.get('creator', 'unknown')
    )
    
    db.session.add(new_model)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(500, description=f"Error adding model: {str(e)}")

    return jsonify(new_model.to_dict()), 201

# Route to get a specific AI model by ID
@app.route('/api/models/<int:model_id>', methods=['GET'])
def get_model(model_id):
    """GET endpoint to retrieve a specific AI model by ID."""
    model = AIModel.query.get(model_id)
    if model is None:
        abort(404, description="Model not found.")
    return jsonify(model.to_dict()), 200

# Route to update an existing AI model
@app.route('/api/models/<int:model_id>', methods=['PUT'])
def update_model(model_id):
    """PUT endpoint to update an existing AI model."""
    model = AIModel.query.get(model_id)
    if model is None:
        abort(404, description="Model not found.")
    
    if not request.json:
        abort(400, description="Invalid request.")

    model.name = request.json.get('name', model.name)
    model.description = request.json.get('description', model.description)
    model.creator = request.json.get('creator', model.creator)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(500, description=f"Error updating model: {str(e)}")

    return jsonify(model.to_dict()), 200

# Route to delete an AI model
@app.route('/api/models/<int:model_id>', methods=['DELETE'])
def delete_model(model_id):
    """DELETE endpoint to remove an AI model."""
    model = AIModel.query.get(model_id)
    if model is None:
        abort(404, description="Model not found.")
    
    db.session.delete(model)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(500, description=f"Error deleting model: {str(e)}")

    return jsonify({'result': True}), 204

# Main entry point
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
```

**Note**: Ensure you set the environment variable `DATABASE_URL` to your preferred database URI for production use. The code is designed to work with SQLite for simplicity, but can easily be adapted to other databases.
