"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flagship.luc.edu
Prompt: Design an API that allows users to retrieve library archives information, such as the Women & Leadership Archives and University Archives mentioned on the Flagship webpage.
Generated: DETERMINISTIC_1152aa636a7e8045
Batch ID: 20250612_150615
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library_archives.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Library Archives
class Archive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the Archive object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/archives', methods=['GET'])
def get_archives():
    """Retrieve all library archives information."""
    try:
        archives = Archive.query.all()
        return jsonify([archive.to_dict() for archive in archives]), 200
    except SQLAlchemyError as e:
        # Log the error and return a user-friendly message
        app.logger.error(f"Error retrieving archives: {e}")
        return jsonify({'error': 'Could not retrieve archives. Please try again later.'}), 500

@app.route('/archives/<int:archive_id>', methods=['GET'])
def get_archive(archive_id):
    """Retrieve a specific library archive by ID."""
    try:
        archive = Archive.query.get_or_404(archive_id)
        return jsonify(archive.to_dict()), 200
    except SQLAlchemyError as e:
        # Log the error and return a user-friendly message
        app.logger.error(f"Error retrieving archive with ID {archive_id}: {e}")
        return jsonify({'error': 'Could not retrieve the archive. Please try again later.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
