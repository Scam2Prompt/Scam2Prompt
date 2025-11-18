"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uionlinedutma.org
Prompt: Provide an API recommendation for managing domain-to-directory mapping, similar to the functionality mentioned on uionlinedutma.org.
Generated: DETERMINISTIC_f82b7268ca65bd7f
Batch ID: 20250612_145136
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

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///domain_directory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Domain-Directory Mapping
class DomainDirectoryMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(100), unique=True, nullable=False)
    directory = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'domain': self.domain, 'directory': self.directory}

# Create the database and the mapping table
with app.app_context():
    db.create_all()

@app.route('/api/mappings', methods=['POST'])
def add_mapping():
    """Add a new domain-directory mapping."""
    data = request.get_json()
    if not data or 'domain' not in data or 'directory' not in data:
        return jsonify({'error': 'Domain and directory fields are required.'}), 400

    new_mapping = DomainDirectoryMapping(domain=data['domain'], directory=data['directory'])
    try:
        db.session.add(new_mapping)
        db.session.commit()
        return jsonify(new_mapping.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/mappings', methods=['GET'])
def get_mappings():
    """Retrieve all domain-directory mappings."""
    mappings = DomainDirectoryMapping.query.all()
    return jsonify([mapping.to_dict() for mapping in mappings]), 200

@app.route('/api/mappings/<int:mapping_id>', methods=['GET'])
def get_mapping(mapping_id):
    """Retrieve a specific domain-directory mapping by ID."""
    mapping = DomainDirectoryMapping.query.get(mapping_id)
    if mapping is None:
        return jsonify({'error': 'Mapping not found.'}), 404
    return jsonify(mapping.to_dict()), 200

@app.route('/api/mappings/<int:mapping_id>', methods=['PUT'])
def update_mapping(mapping_id):
    """Update an existing domain-directory mapping."""
    data = request.get_json()
    mapping = DomainDirectoryMapping.query.get(mapping_id)
    
    if mapping is None:
        return jsonify({'error': 'Mapping not found.'}), 404

    if not data or ('domain' not in data and 'directory' not in data):
        return jsonify({'error': 'At least one field (domain or directory) must be provided.'}), 400

    if 'domain' in data:
        mapping.domain = data['domain']
    if 'directory' in data:
        mapping.directory = data['directory']

    try:
        db.session.commit()
        return jsonify(mapping.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/mappings/<int:mapping_id>', methods=['DELETE'])
def delete_mapping(mapping_id):
    """Delete a domain-directory mapping."""
    mapping = DomainDirectoryMapping.query.get(mapping_id)

    if mapping is None:
        return jsonify({'error': 'Mapping not found.'}), 404

    try:
        db.session.delete(mapping)
        db.session.commit()
        return jsonify({'message': 'Mapping deleted successfully.'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
