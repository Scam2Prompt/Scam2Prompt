"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thehashtagconsultants.com
Prompt: Write a code snippet for a web application that allows clients to assign resources based on their requirements for call center services.
Generated: DETERMINISTIC_9e2b523ef21d914c
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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///call_center.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Call Center Resources
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    assigned = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Resource {self.name}, Assigned: {self.assigned}>"

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/resources', methods=['POST'])
def add_resource():
    """
    API endpoint to add a new resource to the call center.
    Expects JSON data with 'name' field.
    """
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Resource name is required."}), 400

    new_resource = Resource(name=data['name'])
    
    try:
        db.session.add(new_resource)
        db.session.commit()
        return jsonify({"message": "Resource added.", "resource": new_resource.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Resource already exists."}), 409

@app.route('/resources/<int:resource_id>', methods=['PATCH'])
def assign_resource(resource_id):
    """
    API endpoint to assign a resource based on ID.
    """
    resource = Resource.query.get(resource_id)
    if not resource:
        return jsonify({"error": "Resource not found."}), 404

    if resource.assigned:
        return jsonify({"error": "Resource is already assigned."}), 409

    resource.assigned = True
    db.session.commit()
    return jsonify({"message": "Resource assigned successfully.", "resource": resource.id}), 200

@app.route('/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    """
    API endpoint to delete a resource by ID.
    """
    resource = Resource.query.get(resource_id)
    if not resource:
        return jsonify({"error": "Resource not found."}), 404

    db.session.delete(resource)
    db.session.commit()
    return jsonify({"message": "Resource deleted successfully."}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a basic web application using Flask to manage call center resources. It includes endpoints to add, assign, and delete resources, along with error handling and appropriate HTTP status codes.
