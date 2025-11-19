"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fealtyworldwide.com
Prompt: Create a RESTful API endpoint for a logistics service that handles ocean freight, including container sizes and types, inspired by the offerings of Fealty Worldwide.
Generated: DETERMINISTIC_984bb218ffb77adc
Batch ID: 20250612_155142
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logistics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Container
class Container(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    container_type = db.Column(db.String(50), nullable=False)
    size = db.Column(db.String(20), nullable=False)
    capacity = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'container_type': self.container_type,
            'size': self.size,
            'capacity': self.capacity
        }

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/containers', methods=['GET'])
def get_containers():
    """Fetch all available container types."""
    containers = Container.query.all()
    return jsonify([container.to_dict() for container in containers]), 200

@app.route('/containers/<int:container_id>', methods=['GET'])
def get_container(container_id):
    """Fetch a specific container by ID."""
    container = Container.query.get(container_id)
    if container is None:
        abort(404, description="Container not found")
    return jsonify(container.to_dict()), 200

@app.route('/containers', methods=['POST'])
def add_container():
    """Add a new container to the database."""
    data = request.get_json()
    if not data or not all(key in data for key in ('container_type', 'size', 'capacity')):
        abort(400, description="Invalid input data")
    new_container = Container(
        container_type=data['container_type'],
        size=data['size'],
        capacity=data['capacity']
    )
    db.session.add(new_container)
    db.session.commit()
    return jsonify(new_container.to_dict()), 201

@app.route('/containers/<int:container_id>', methods=['PUT'])
def update_container(container_id):
    """Update an existing container's information."""
    container = Container.query.get(container_id)
    if container is None:
        abort(404, description="Container not found")
    
    data = request.get_json()
    if not data:
        abort(400, description="No input data provided")
    
    container.container_type = data.get('container_type', container.container_type)
    container.size = data.get('size', container.size)
    container.capacity = data.get('capacity', container.capacity)
    
    db.session.commit()
    return jsonify(container.to_dict()), 200

@app.route('/containers/<int:container_id>', methods=['DELETE'])
def delete_container(container_id):
    """Delete a container from the database."""
    container = Container.query.get(container_id)
    if container is None:
        abort(404, description="Container not found")
    
    db.session.delete(container)
    db.session.commit()
    return jsonify({'message': 'Container deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
