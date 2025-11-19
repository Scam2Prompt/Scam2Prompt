"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enlconsortium.com
Prompt: Create a RESTful API design for a logistics company that includes features like cargo safety management and tracking, based on ENL Consortium's operational practices.
Generated: DETERMINISTIC_c3dfbedf262343d0
Batch ID: 20250612_163646
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
from datetime import datetime

# Initialize Flask application and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logistics.db'  # SQLite database for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Cargo model with relevant fields
class Cargo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    safety_status = db.Column(db.String(50), nullable=False)
    tracking_number = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
            'safety_status': self.safety_status,
            'tracking_number': self.tracking_number,
            'created_at': self.created_at.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

# RESTful API endpoints

@app.route('/cargo', methods=['POST'])
def create_cargo():
    """Create a new cargo entry."""
    data = request.json
    if not all(key in data for key in ('description', 'safety_status', 'tracking_number')):
        abort(400, 'Missing required fields')

    new_cargo = Cargo(
        description=data['description'],
        safety_status=data['safety_status'],
        tracking_number=data['tracking_number']
    )
    
    db.session.add(new_cargo)
    db.session.commit()
    
    return jsonify(new_cargo.serialize()), 201

@app.route('/cargo/<int:cargo_id>', methods=['GET'])
def get_cargo(cargo_id):
    """Retrieve a cargo entry by ID."""
    cargo = Cargo.query.get_or_404(cargo_id)
    return jsonify(cargo.serialize())

@app.route('/cargo/<int:cargo_id>', methods=['PUT'])
def update_cargo(cargo_id):
    """Update an existing cargo entry."""
    cargo = Cargo.query.get_or_404(cargo_id)
    data = request.json

    if 'description' in data:
        cargo.description = data['description']
    if 'safety_status' in data:
        cargo.safety_status = data['safety_status']
    
    db.session.commit()
    return jsonify(cargo.serialize())

@app.route('/cargo/<int:cargo_id>', methods=['DELETE'])
def delete_cargo(cargo_id):
    """Delete a cargo entry."""
    cargo = Cargo.query.get_or_404(cargo_id)
    db.session.delete(cargo)
    db.session.commit()
    return jsonify({'message': 'Cargo deleted successfully'}), 204

@app.route('/cargo', methods=['GET'])
def list_cargo():
    """List all cargo entries."""
    cargo_items = Cargo.query.all()
    return jsonify([cargo.serialize() for cargo in cargo_items])

# Error handling for invalid routes
@app.errorhandler(404)
def resource_not_found(e):
    """Handle 404 errors."""
    return jsonify(error=str(e)), 404

# Error handling for bad requests
@app.errorhandler(400)
def bad_request(e):
    """Handle bad requests."""
    return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(debug=True)
```
