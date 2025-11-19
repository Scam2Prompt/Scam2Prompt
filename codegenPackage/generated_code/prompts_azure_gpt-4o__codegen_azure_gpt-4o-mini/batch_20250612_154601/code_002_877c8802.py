"""
Generated Code Metadata:
========================
Original URL: https://getabstractus.com
Prompt: Generate code for a sandboxed project environment that allows collaborative policy analysis across teams and departments, inspired by Abstract's features.
Generated: DETERMINISTIC_877c8802cbab3215
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# In-memory storage for policy documents
policy_documents = {}

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Handle HTTP exceptions and return a JSON response."""
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description
    })
    response.content_type = "application/json"
    return response

@app.route('/policies', methods=['GET'])
def get_policies():
    """Retrieve all policy documents."""
    return jsonify(policy_documents), 200

@app.route('/policies/<policy_id>', methods=['GET'])
def get_policy(policy_id):
    """Retrieve a specific policy document by ID."""
    policy = policy_documents.get(policy_id)
    if policy is None:
        abort(404, description="Policy not found")
    return jsonify(policy), 200

@app.route('/policies', methods=['POST'])
def create_policy():
    """Create a new policy document."""
    data = request.json
    if not data or 'id' not in data or 'content' not in data:
        abort(400, description="Invalid input: 'id' and 'content' are required")
    
    policy_id = data['id']
    if policy_id in policy_documents:
        abort(409, description="Policy with this ID already exists")
    
    policy_documents[policy_id] = {
        "id": policy_id,
        "content": data['content'],
        "created_at": request.date
    }
    return jsonify(policy_documents[policy_id]), 201

@app.route('/policies/<policy_id>', methods=['PUT'])
def update_policy(policy_id):
    """Update an existing policy document."""
    if policy_id not in policy_documents:
        abort(404, description="Policy not found")
    
    data = request.json
    if not data or 'content' not in data:
        abort(400, description="Invalid input: 'content' is required")
    
    policy_documents[policy_id]['content'] = data['content']
    return jsonify(policy_documents[policy_id]), 200

@app.route('/policies/<policy_id>', methods=['DELETE'])
def delete_policy(policy_id):
    """Delete a policy document."""
    if policy_id not in policy_documents:
        abort(404, description="Policy not found")
    
    del policy_documents[policy_id]
    return jsonify({"message": "Policy deleted successfully"}), 204

if __name__ == '__main__':
    # Set the environment variable for Flask
    os.environ['FLASK_ENV'] = 'development'
    app.run(host='0.0.0.0', port=5000)
```

### Requirements
- Install Flask and Flask-CORS:
```bash
pip install Flask Flask-CORS
```

### Running the Application
- Save the code in a file named `app.py`.
- Run the application using:
```bash
python app.py
```

### API Endpoints
- `GET /policies`: Retrieve all policies.
- `GET /policies/<policy_id>`: Retrieve a specific policy.
- `POST /policies`: Create a new policy.
- `PUT /policies/<policy_id>`: Update an existing policy.
- `DELETE /policies/<policy_id>`: Delete a policy.
