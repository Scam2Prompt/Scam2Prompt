"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casadelospastes.com
Prompt: Develop a RESTful API that provides information about different types of pastes and their historical significance, similar to the content found on La Casa de los Pastes.
Generated: DETERMINISTIC_a2beff2c9ab81958
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
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the Database URI (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pastes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Paste model
class Paste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    historical_significance = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        """Convert the Paste object to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'historical_significance': self.historical_significance
        }

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to retrieve all pastes
@app.route('/api/pastes', methods=['GET'])
def get_pastes():
    """Retrieve a list of all pastes."""
    pastes = Paste.query.all()
    return jsonify([paste.to_dict() for paste in pastes]), 200

# Endpoint to retrieve a specific paste by ID
@app.route('/api/pastes/<int:paste_id>', methods=['GET'])
def get_paste(paste_id):
    """Retrieve a specific paste by its ID."""
    paste = Paste.query.get(paste_id)
    if paste is None:
        return jsonify({'error': 'Paste not found'}), 404
    return jsonify(paste.to_dict()), 200

# Endpoint to create a new paste
@app.route('/api/pastes', methods=['POST'])
def create_paste():
    """Create a new paste."""
    data = request.json
    if not data or 'name' not in data or 'description' not in data or 'historical_significance' not in data:
        return jsonify({'error': 'Bad request, missing fields'}), 400
    
    new_paste = Paste(
        name=data['name'],
        description=data['description'],
        historical_significance=data['historical_significance']
    )
    
    try:
        db.session.add(new_paste)
        db.session.commit()
        return jsonify(new_paste.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Paste with this name already exists'}), 409
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred'}), 500

# Endpoint to update an existing paste
@app.route('/api/pastes/<int:paste_id>', methods=['PUT'])
def update_paste(paste_id):
    """Update an existing paste."""
    paste = Paste.query.get(paste_id)
    if paste is None:
        return jsonify({'error': 'Paste not found'}), 404
    
    data = request.json
    if not data:
        return jsonify({'error': 'Bad request, missing fields'}), 400

    paste.name = data.get('name', paste.name)
    paste.description = data.get('description', paste.description)
    paste.historical_significance = data.get('historical_significance', paste.historical_significance)

    try:
        db.session.commit()
        return jsonify(paste.to_dict()), 200
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred'}), 500

# Endpoint to delete a paste
@app.route('/api/pastes/<int:paste_id>', methods=['DELETE'])
def delete_paste(paste_id):
    """Delete a paste by its ID."""
    paste = Paste.query.get(paste_id)
    if paste is None:
        return jsonify({'error': 'Paste not found'}), 404

    try:
        db.session.delete(paste)
        db.session.commit()
        return jsonify({'message': 'Paste deleted successfully'}), 200
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred'}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
