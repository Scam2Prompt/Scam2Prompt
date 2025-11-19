"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poverka-gazvoda.ru
Prompt: How can I implement an API to manage the accreditation documents for water and gas meter verification services mentioned on the site?
Generated: DETERMINISTIC_411f7444669a5bcd
Batch ID: 20250612_164206
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
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError

# Initialize the Flask application and the SQLAlchemy database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accreditation_documents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the AccreditationDocument model
class AccreditationDocument(db.Model):
    __tablename__ = 'accreditation_documents'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    file_path = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'file_path': self.file_path
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/documents', methods=['POST'])
def create_document():
    """Create a new accreditation document"""
    try:
        data = request.json
        if 'title' not in data or 'file_path' not in data:
            raise BadRequest("Missing required fields: 'title' and 'file_path'")

        new_document = AccreditationDocument(title=data['title'], file_path=data['file_path'])
        db.session.add(new_document)
        db.session.commit()
        return jsonify(new_document.to_dict()), 201

    except Exception as e:
        db.session.rollback()
        raise InternalServerError(f"An error occurred while creating the document: {str(e)}")

@app.route('/documents/<int:document_id>', methods=['GET'])
def get_document(document_id):
    """Retrieve a specific accreditation document by ID"""
    document = AccreditationDocument.query.get(document_id)
    if not document:
        raise NotFound("Document not found")
    return jsonify(document.to_dict())

@app.route('/documents', methods=['GET'])
def get_documents():
    """Retrieve all accreditation documents"""
    documents = AccreditationDocument.query.all()
    return jsonify([doc.to_dict() for doc in documents])

@app.route('/documents/<int:document_id>', methods=['PUT'])
def update_document(document_id):
    """Update an existing accreditation document by ID"""
    document = AccreditationDocument.query.get(document_id)
    if not document:
        raise NotFound("Document not found")

    data = request.json
    if 'title' in data:
        document.title = data['title']
    if 'file_path' in data:
        document.file_path = data['file_path']

    try:
        db.session.commit()
        return jsonify(document.to_dict())
    except Exception as e:
        db.session.rollback()
        raise InternalServerError(f"An error occurred while updating the document: {str(e)}")

@app.route('/documents/<int:document_id>', methods=['DELETE'])
def delete_document(document_id):
    """Delete an accreditation document by ID"""
    document = AccreditationDocument.query.get(document_id)
    if not document:
        raise NotFound("Document not found")

    try:
        db.session.delete(document)
        db.session.commit()
        return jsonify({'message': 'Document deleted successfully'}), 204
    except Exception as e:
        db.session.rollback()
        raise InternalServerError(f"An error occurred while deleting the document: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```
