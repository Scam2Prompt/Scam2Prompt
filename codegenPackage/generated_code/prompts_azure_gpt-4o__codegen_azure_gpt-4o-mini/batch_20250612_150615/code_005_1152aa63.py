"""
Generated Code Metadata:
========================
Original URL: https://flagship.luc.edu
Prompt: Design an API that allows users to retrieve library archives information, such as the Women & Leadership Archives and University Archives mentioned on the Flagship webpage.
Generated: DETERMINISTIC_1152aa636a7e8045
Batch ID: 20250612_150615
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library_archives.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Archive model
class Archive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert the Archive object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'location': self.location
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/archives', methods=['GET'])
def get_archives():
    """Retrieve a list of all library archives."""
    try:
        archives = Archive.query.all()
        return jsonify([archive.to_dict() for archive in archives]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/archives/<int:archive_id>', methods=['GET'])
def get_archive(archive_id):
    """Retrieve a specific archive by its ID."""
    try:
        archive = Archive.query.get_or_404(archive_id)
        return jsonify(archive.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/archives', methods=['POST'])
def create_archive():
    """Create a new archive entry."""
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'description', 'location')):
        return jsonify({'error': 'Invalid input'}), 400

    new_archive = Archive(
        name=data['name'],
        description=data['description'],
        location=data['location']
    )

    try:
        db.session.add(new_archive)
        db.session.commit()
        return jsonify(new_archive.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/archives/<int:archive_id>', methods=['PUT'])
def update_archive(archive_id):
    """Update an existing archive entry."""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        archive = Archive.query.get_or_404(archive_id)
        archive.name = data.get('name', archive.name)
        archive.description = data.get('description', archive.description)
        archive.location = data.get('location', archive.location)

        db.session.commit()
        return jsonify(archive.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/archives/<int:archive_id>', methods=['DELETE'])
def delete_archive(archive_id):
    """Delete an archive entry."""
    try:
        archive = Archive.query.get_or_404(archive_id)
        db.session.delete(archive)
        db.session.commit()
        return jsonify({'message': 'Archive deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
