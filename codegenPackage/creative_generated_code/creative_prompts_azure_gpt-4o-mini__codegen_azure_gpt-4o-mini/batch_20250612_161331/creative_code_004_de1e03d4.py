"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://market-idex.com
Prompt: Outline a RESTful API design for a fitness center that includes endpoints for managing equipment inventory, class schedules, and member registrations.
Generated: DETERMINISTIC_de1e03d47b9d2beb
Batch ID: 20250612_161331
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

# Initialize the Flask application and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness_center.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class ClassSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Create the database (if it doesn't exist)
@app.before_first_request
def create_tables():
    db.create_all()

# Equipment endpoints
@app.route('/equipment', methods=['GET'])
def get_equipments():
    """Retrieve all equipment in the inventory."""
    equipments = Equipment.query.all()
    return jsonify([{'id': eq.id, 'name': eq.name, 'quantity': eq.quantity} for eq in equipments])

@app.route('/equipment', methods=['POST'])
def add_equipment():
    """Add new equipment to the inventory."""
    data = request.get_json()
    if not data or 'name' not in data or 'quantity' not in data:
        abort(400, description="Invalid input.")
    
    new_equipment = Equipment(name=data['name'], quantity=data['quantity'])
    db.session.add(new_equipment)
    db.session.commit()
    return jsonify({'id': new_equipment.id}), 201

@app.route('/equipment/<int:equipment_id>', methods=['PUT'])
def update_equipment(equipment_id):
    """Update an existing equipment's details."""
    equipment = Equipment.query.get_or_404(equipment_id)
    data = request.get_json()
    if 'name' in data:
        equipment.name = data['name']
    if 'quantity' in data:
        equipment.quantity = data['quantity']
    db.session.commit()
    return jsonify({'id': equipment.id}), 200

@app.route('/equipment/<int:equipment_id>', methods=['DELETE'])
def delete_equipment(equipment_id):
    """Delete an equipment from the inventory."""
    equipment = Equipment.query.get_or_404(equipment_id)
    db.session.delete(equipment)
    db.session.commit()
    return jsonify({'result': True}), 204

# Class schedule endpoints
@app.route('/classes', methods=['GET'])
def get_classes():
    """Retrieve all classes in the schedule."""
    classes = ClassSchedule.query.all()
    return jsonify([{'id': cls.id, 'name': cls.name, 'time': cls.time, 'capacity': cls.capacity} for cls in classes])

@app.route('/classes', methods=['POST'])
def add_class():
    """Add a new class to the schedule."""
    data = request.get_json()
    if not data or 'name' not in data or 'time' not in data or 'capacity' not in data:
        abort(400, description="Invalid input.")
    
    new_class = ClassSchedule(name=data['name'], time=data['time'], capacity=data['capacity'])
    db.session.add(new_class)
    db.session.commit()
    return jsonify({'id': new_class.id}), 201

@app.route('/classes/<int:class_id>', methods=['PUT'])
def update_class(class_id):
    """Update an existing class's details."""
    class_schedule = ClassSchedule.query.get_or_404(class_id)
    data = request.get_json()
    if 'name' in data:
        class_schedule.name = data['name']
    if 'time' in data:
        class_schedule.time = data['time']
    if 'capacity' in data:
        class_schedule.capacity = data['capacity']
    db.session.commit()
    return jsonify({'id': class_schedule.id}), 200

@app.route('/classes/<int:class_id>', methods=['DELETE'])
def delete_class(class_id):
    """Delete a class from the schedule."""
    class_schedule = ClassSchedule.query.get_or_404(class_id)
    db.session.delete(class_schedule)
    db.session.commit()
    return jsonify({'result': True}), 204

# Member registration endpoints
@app.route('/members', methods=['GET'])
def get_members():
    """Retrieve all registered members."""
    members = Member.query.all()
    return jsonify([{'id': m.id, 'name': m.name, 'email': m.email} for m in members])

@app.route('/members', methods=['POST'])
def add_member():
    """Register a new member."""
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        abort(400, description="Invalid input.")
    
    new_member = Member(name=data['name'], email=data['email'])
    db.session.add(new_member)
    db.session.commit()
    return jsonify({'id': new_member.id}), 201

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    """Update an existing member's details."""
    member = Member.query.get_or_404(member_id)
    data = request.get_json()
    if 'name' in data:
        member.name = data['name']
    if 'email' in data:
        member.email = data['email']
    db.session.commit()
    return jsonify({'id': member.id}), 200

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    """Delete a member's registration."""
    member = Member.query.get_or_404(member_id)
    db.session.delete(member)
    db.session.commit()
    return jsonify({'result': True}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
