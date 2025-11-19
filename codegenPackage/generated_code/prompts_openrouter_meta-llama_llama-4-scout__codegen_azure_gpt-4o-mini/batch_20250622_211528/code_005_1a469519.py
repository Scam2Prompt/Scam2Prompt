"""
Generated Code Metadata:
========================
Original URL: https://bplservicescenter.com
Prompt: Design a RESTful API for managing BPL service center operations, including technician assignments, repair status updates, and customer feedback collection.
Generated: DETERMINISTIC_1a4695193aa8cc52
Batch ID: 20250622_211528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bpl_service_center.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Technician model
class Technician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    assigned_repairs = db.relationship('Repair', backref='technician', lazy=True)

# Define the Repair model
class Repair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    technician_id = db.Column(db.Integer, db.ForeignKey('technician.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    feedback = db.relationship('Feedback', backref='repair', lazy=True)

# Define the Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    repair_id = db.Column(db.Integer, db.ForeignKey('repair.id'), nullable=False)
    comments = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# API endpoint to create a technician
@app.route('/technicians', methods=['POST'])
def create_technician():
    data = request.get_json()
    if not data or 'name' not in data:
        abort(400, description="Invalid input: 'name' is required.")
    
    technician = Technician(name=data['name'])
    db.session.add(technician)
    db.session.commit()
    return jsonify({'id': technician.id, 'name': technician.name}), 201

# API endpoint to assign a technician to a repair
@app.route('/repairs/<int:repair_id>/assign', methods=['POST'])
def assign_technician(repair_id):
    data = request.get_json()
    technician_id = data.get('technician_id')
    
    repair = Repair.query.get(repair_id)
    if repair is None:
        abort(404)
    
    technician = Technician.query.get(technician_id)
    if technician is None:
        abort(404)
    
    repair.technician_id = technician.id
    db.session.commit()
    return jsonify({'message': 'Technician assigned successfully.'}), 200

# API endpoint to update repair status
@app.route('/repairs/<int:repair_id>/status', methods=['PUT'])
def update_repair_status(repair_id):
    data = request.get_json()
    new_status = data.get('status')
    
    repair = Repair.query.get(repair_id)
    if repair is None:
        abort(404)
    
    repair.status = new_status
    db.session.commit()
    return jsonify({'message': 'Repair status updated successfully.'}), 200

# API endpoint to collect customer feedback
@app.route('/repairs/<int:repair_id>/feedback', methods=['POST'])
def collect_feedback(repair_id):
    data = request.get_json()
    if not data or 'comments' not in data or 'rating' not in data:
        abort(400, description="Invalid input: 'comments' and 'rating' are required.")
    
    feedback = Feedback(repair_id=repair_id, comments=data['comments'], rating=data['rating'])
    db.session.add(feedback)
    db.session.commit()
    return jsonify({'message': 'Feedback submitted successfully.'}), 201

# API endpoint to get all repairs
@app.route('/repairs', methods=['GET'])
def get_repairs():
    repairs = Repair.query.all()
    return jsonify([{'id': r.id, 'description': r.description, 'status': r.status} for r in repairs]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
