"""
Generated Code Metadata:
========================
Original URL: https://enlconsortium.com
Prompt: "Develop a Python API to manage warehouse space and container stacking for a logistics company like ENL Consortium."
Generated: DETERMINISTIC_875d80c2d0790d61
Batch ID: 20250622_204704
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///warehouse.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Container model
class Container(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    weight = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    width = db.Column(db.Float, nullable=False)
    depth = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Container {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to add a new container
@app.route('/containers', methods=['POST'])
def add_container():
    data = request.get_json()
    try:
        new_container = Container(
            name=data['name'],
            weight=data['weight'],
            height=data['height'],
            width=data['width'],
            depth=data['depth']
        )
        db.session.add(new_container)
        db.session.commit()
        return jsonify({'message': 'Container added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Container with this name already exists.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to get all containers
@app.route('/containers', methods=['GET'])
def get_containers():
    containers = Container.query.all()
    return jsonify([{
        'id': container.id,
        'name': container.name,
        'weight': container.weight,
        'height': container.height,
        'width': container.width,
        'depth': container.depth
    } for container in containers]), 200

# API endpoint to get a specific container by ID
@app.route('/containers/<int:container_id>', methods=['GET'])
def get_container(container_id):
    container = Container.query.get(container_id)
    if container:
        return jsonify({
            'id': container.id,
            'name': container.name,
            'weight': container.weight,
            'height': container.height,
            'width': container.width,
            'depth': container.depth
        }), 200
    return jsonify({'error': 'Container not found.'}), 404

# API endpoint to update a container
@app.route('/containers/<int:container_id>', methods=['PUT'])
def update_container(container_id):
    data = request.get_json()
    container = Container.query.get(container_id)
    if not container:
        return jsonify({'error': 'Container not found.'}), 404

    try:
        container.name = data.get('name', container.name)
        container.weight = data.get('weight', container.weight)
        container.height = data.get('height', container.height)
        container.width = data.get('width', container.width)
        container.depth = data.get('depth', container.depth)
        db.session.commit()
        return jsonify({'message': 'Container updated successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to delete a container
@app.route('/containers/<int:container_id>', methods=['DELETE'])
def delete_container(container_id):
    container = Container.query.get(container_id)
    if not container:
        return jsonify({'error': 'Container not found.'}), 404

    try:
        db.session.delete(container)
        db.session.commit()
        return jsonify({'message': 'Container deleted successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
