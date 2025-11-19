"""
Generated Code Metadata:
========================
Original URL: https://chainback-en.web.app
Prompt: Design a system architecture for a decentralized cloud computing platform that allows individuals and data centers to contribute their unused GPU resources, similar to Chainback's GPU cloud computing model.
Generated: DETERMINISTIC_d51806407321d365
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import hashlib
import uuid
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gpu_resources.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for GPU Resource
class GPUResource(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    owner_id = db.Column(db.String(36), nullable=False)
    gpu_type = db.Column(db.String(50), nullable=False)
    memory_size = db.Column(db.Integer, nullable=False)  # in MB
    status = db.Column(db.String(20), default='available')  # available, in_use, offline

    def __repr__(self):
        return f"<GPUResource {self.gpu_type} owned by {self.owner_id}>"

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to register a new GPU resource
@app.route('/register_gpu', methods=['POST'])
def register_gpu():
    data = request.get_json()
    try:
        new_gpu = GPUResource(
            id=str(uuid.uuid4()),
            owner_id=data['owner_id'],
            gpu_type=data['gpu_type'],
            memory_size=data['memory_size']
        )
        db.session.add(new_gpu)
        db.session.commit()
        return jsonify({"message": "GPU resource registered successfully", "id": new_gpu.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Failed to register GPU resource"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to list available GPU resources
@app.route('/available_gpus', methods=['GET'])
def available_gpus():
    try:
        gpus = GPUResource.query.filter_by(status='available').all()
        return jsonify([{"id": gpu.id, "owner_id": gpu.owner_id, "gpu_type": gpu.gpu_type, "memory_size": gpu.memory_size} for gpu in gpus]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to request a GPU resource
@app.route('/request_gpu/<gpu_id>', methods=['POST'])
def request_gpu(gpu_id):
    try:
        gpu = GPUResource.query.get(gpu_id)
        if gpu is None or gpu.status != 'available':
            return jsonify({"error": "GPU resource not available"}), 404
        
        gpu.status = 'in_use'
        db.session.commit()
        return jsonify({"message": "GPU resource allocated successfully", "gpu_id": gpu.id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to release a GPU resource
@app.route('/release_gpu/<gpu_id>', methods=['POST'])
def release_gpu(gpu_id):
    try:
        gpu = GPUResource.query.get(gpu_id)
        if gpu is None or gpu.status != 'in_use':
            return jsonify({"error": "GPU resource not in use"}), 404
        
        gpu.status = 'available'
        db.session.commit()
        return jsonify({"message": "GPU resource released successfully", "gpu_id": gpu.id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
