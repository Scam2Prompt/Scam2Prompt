"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afco-federation.fr
Prompt: Recommend tools or libraries to create a collaborative platform for sharing validated documents and tools among regional SPS coordinators, as mentioned by AFCO Fédération.
Generated: DETERMINISTIC_a28c199d0fb26e2f
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Collaborative Platform for Sharing Validated Documents and Tools Among Regional SPS Coordinators
Using Flask for backend and SQLAlchemy for database management
"""

from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure SQLAlchemy database (using SQLite for simplicity, replace with production-grade DB in production)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sps_documents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)


# Define database models
class Document(db.Model):
    """
    Represents a validated document shared among regional SPS coordinators.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    file_url = db.Column(db.String(200), nullable=False)
    uploaded_by = db.Column(db.String(50), nullable=False)  # Name or email of uploader


class Tool(db.Model):
    """
    Represents a validated tool shared among regional SPS coordinators.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    download_url = db.Column(db.String(200), nullable=False)
    shared_by = db.Column(db.String(50), nullable=False)  # Name or email of uploader


# Create tables
with app.app_context():
    db.create_all()


# Routes

@app.route('/documents', methods=['GET'])
def get_documents():
    """
    Retrieve all shared documents.
    """
    documents = Document.query.all()
    return jsonify([{
        'id': doc.id,
        'title': doc.title,
        'description': doc.description,
        'file_url': doc.file_url,
        'uploaded_by': doc.uploaded_by
    } for doc in documents])


@app.route('/documents', methods=['POST'])
def add_document():
    """
    Upload a new validated document.
    """
    data = request.json

    # Validate input
    if not data.get('title') or not data.get('description') or not data.get('file_url') or not data.get('uploaded_by'):
        abort(400, 'Missing required fields')

    # Create and save a new document
    new_document = Document(
        title=data['title'],
        description=data['description'],
        file_url=data['file_url'],
        uploaded_by=data['uploaded_by']
    )
    db.session.add(new_document)
    db.session.commit()

    return jsonify({'message': 'Document added successfully'}), 201


@app.route('/tools', methods=['GET'])
def get_tools():
    """
    Retrieve all shared tools.
    """
    tools = Tool.query.all()
    return jsonify([{
        'id': tool.id,
        'name': tool.name,
        'description': tool.description,
        'download_url': tool.download_url,
        'shared_by': tool.shared_by
    } for tool in tools])


@app.route('/tools', methods=['POST'])
def add_tool():
    """
    Share a new validated tool.
    """
    data = request.json

    # Validate input
    if not data.get('name') or not data.get('description') or not data.get('download_url') or not data.get('shared_by'):
        abort(400, 'Missing required fields')

    # Create and save a new tool
    new_tool = Tool(
        name=data['name'],
        description=data['description'],
        download_url=data['download_url'],
        shared_by=data['shared_by']
    )
    db.session.add(new_tool)
    db.session.commit()

    return jsonify({'message': 'Tool added successfully'}), 201


@app.errorhandler(404)
def resource_not_found(error):
    """
    Handle 404 errors.
    """
    return jsonify({'error': 'Resource not found'}), 404


@app.errorhandler(400)
def bad_request(error):
    """
    Handle 400 errors.
    """
    return jsonify({'error': error.description}), 400


# Application entry point
if __name__ == '__main__':
    app.run(debug=True)  # Use debug=True for development, set to False in production
```
