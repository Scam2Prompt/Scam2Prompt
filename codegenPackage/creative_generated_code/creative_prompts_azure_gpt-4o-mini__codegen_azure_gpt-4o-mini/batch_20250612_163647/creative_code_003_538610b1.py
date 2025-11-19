"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://easydocgestao.com.br
Prompt: Suggest an API for integrating document management solutions that align with EasyDoc's approach to file security and consulting.
Generated: DETERMINISTIC_538610b103156db2
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest, NotFound

app = Flask(__name__)

# Mock database for documents
documents_db = {}

class Document:
    """Represents a document in the system."""
    
    def __init__(self, doc_id, title, content, owner):
        self.id = doc_id
        self.title = title
        self.content = content
        self.owner = owner
    
    def to_dict(self):
        """Convert the Document instance to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'owner': self.owner
        }

def validate_document(data):
    """Validate the incoming document data."""
    required_fields = ['title', 'content', 'owner']
    for field in required_fields:
        if field not in data:
            raise BadRequest(f"Missing required field: {field}")

@app.route('/documents', methods=['POST'])
def create_document():
    """Create a new document."""
    try:
        data = request.json
        validate_document(data)
        
        doc_id = len(documents_db) + 1  # Simple ID generation
        document = Document(doc_id, data['title'], data['content'], data['owner'])
        documents_db[doc_id] = document
        
        return jsonify(document.to_dict()), 201
    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred.'}), 500

@app.route('/documents/<int:doc_id>', methods=['GET'])
def get_document(doc_id):
    """Retrieve a document by ID."""
    document = documents_db.get(doc_id)
    if document is None:
        raise NotFound(f"Document with ID {doc_id} not found.")
    
    return jsonify(document.to_dict()), 200

@app.route('/documents/<int:doc_id>', methods=['PUT'])
def update_document(doc_id):
    """Update an existing document."""
    try:
        data = request.json
        validate_document(data)
        
        document = documents_db.get(doc_id)
        if document is None:
            raise NotFound(f"Document with ID {doc_id} not found.")

        document.title = data['title']
        document.content = data['content']
        document.owner = data['owner']
        
        return jsonify(document.to_dict()), 200
    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except NotFound as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred.'}), 500

@app.route('/documents/<int:doc_id>', methods=['DELETE'])
def delete_document(doc_id):
    """Delete a document by ID."""
    document = documents_db.pop(doc_id, None)
    if document is None:
        raise NotFound(f"Document with ID {doc_id} not found.")
    
    return jsonify({'message': 'Document deleted successfully.'}), 204

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```
