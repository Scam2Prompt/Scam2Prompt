"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uranpres.sk
Prompt: Create an API endpoint for a construction company that manages geodetic work, similar to the services provided by URANPRES in Slovakia.
Generated: DETERMINISTIC_6fc8fc01e66c611f
Batch ID: 20250612_162051
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///geodetic_work.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the GeodeticWork model
class GeodeticWork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), nullable=False)
    client_name = db.Column(db.String(100), nullable=False)
    work_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def to_dict(self):
        """Convert the GeodeticWork instance to a dictionary."""
        return {
            'id': self.id,
            'project_name': self.project_name,
            'client_name': self.client_name,
            'work_type': self.work_type,
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/geodetic_work', methods=['POST'])
def create_geodetic_work():
    """Create a new geodetic work entry."""
    data = request.get_json()

    # Validate incoming data
    if not data or 'project_name' not in data or 'client_name' not in data or 'work_type' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    new_work = GeodeticWork(
        project_name=data['project_name'],
        client_name=data['client_name'],
        work_type=data['work_type'],
        description=data.get('description')
    )

    try:
        db.session.add(new_work)
        db.session.commit()
        return jsonify(new_work.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/geodetic_work/<int:work_id>', methods=['GET'])
def get_geodetic_work(work_id):
    """Retrieve a geodetic work entry by ID."""
    work = GeodeticWork.query.get(work_id)
    
    if not work:
        return jsonify({'error': 'Geodetic work not found'}), 404
    
    return jsonify(work.to_dict()), 200

@app.route('/geodetic_work/<int:work_id>', methods=['PUT'])
def update_geodetic_work(work_id):
    """Update an existing geodetic work entry."""
    work = GeodeticWork.query.get(work_id)
    
    if not work:
        return jsonify({'error': 'Geodetic work not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    if 'project_name' in data:
        work.project_name = data['project_name']
    if 'client_name' in data:
        work.client_name = data['client_name']
    if 'work_type' in data:
        work.work_type = data['work_type']
    if 'description' in data:
        work.description = data['description']

    try:
        db.session.commit()
        return jsonify(work.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/geodetic_work/<int:work_id>', methods=['DELETE'])
def delete_geodetic_work(work_id):
    """Delete a geodetic work entry by ID."""
    work = GeodeticWork.query.get(work_id)
    
    if not work:
        return jsonify({'error': 'Geodetic work not found'}), 404
    
    try:
        db.session.delete(work)
        db.session.commit()
        return jsonify({'message': 'Geodetic work deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```
