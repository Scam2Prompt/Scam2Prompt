"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sacredexclusions.com
Prompt: Describe how to set up a server to handle sacred exclusions based on the information from sacredexclusions.com.
Generated: DETERMINISTIC_22ca7642b039157f
Batch ID: 20250612_163826
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Set up the database configuration (SQLite for simplicity, replace with your DB of choice)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sacred_exclusions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database instance
db = SQLAlchemy(app)

# Model representing a sacred exclusion
class SacredExclusion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<SacredExclusion {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/exclusion', methods=['POST'])
def add_exclusion():
    """
    Endpoint to add a new sacred exclusion.
    Expects JSON with 'name' and optional 'description'.
    """
    data = request.json
    name = data.get('name')
    description = data.get('description')

    # Validate input
    if not name:
        return jsonify({'error': 'Name is required.'}), 400

    # Create a new SacredExclusion instance
    new_exclusion = SacredExclusion(name=name, description=description)

    # Attempt to add the new exclusion to the database
    try:
        db.session.add(new_exclusion)
        db.session.commit()
        return jsonify({'message': 'Exclusion added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Exclusion with this name already exists.'}), 400

@app.route('/exclusion/<int:id>', methods=['GET'])
def get_exclusion(id):
    """
    Endpoint to retrieve a sacred exclusion by ID.
    """
    exclusion = SacredExclusion.query.get(id)
    if exclusion is None:
        return jsonify({'error': 'Exclusion not found.'}), 404
    return jsonify({
        'id': exclusion.id,
        'name': exclusion.name,
        'description': exclusion.description
    }), 200

@app.route('/exclusion/<int:id>', methods=['DELETE'])
def delete_exclusion(id):
    """
    Endpoint to delete a sacred exclusion by ID.
    """
    exclusion = SacredExclusion.query.get(id)
    if exclusion is None:
        return jsonify({'error': 'Exclusion not found.'}), 404
    
    db.session.delete(exclusion)
    db.session.commit()
    return jsonify({'message': 'Exclusion deleted successfully!'}), 200

if __name__ == '__main__':
    # Run the server on localhost at port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
```
