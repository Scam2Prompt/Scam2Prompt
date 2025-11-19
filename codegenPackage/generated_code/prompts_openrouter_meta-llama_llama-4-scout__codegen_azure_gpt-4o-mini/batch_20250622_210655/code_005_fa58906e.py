"""
Generated Code Metadata:
========================
Original URL: https://cemnazmakine.com
Prompt: Write an API documentation for a patates işleme tesisi (potato processing plant) management system, including endpoints for machine monitoring, production tracking, and quality control.
Generated: DETERMINISTIC_fa58906ef1fe90e7
Batch ID: 20250622_210655
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
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///potato_processing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Machine
class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    last_checked = db.Column(db.DateTime, default=datetime.utcnow)

# Database model for Production
class Production(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

# Database model for Quality Control
class QualityControl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inspection_date = db.Column(db.DateTime, default=datetime.utcnow)
    quality_score = db.Column(db.Float, nullable=False)

# Endpoint to monitor machines
@app.route('/api/machines', methods=['GET'])
def get_machines():
    """Retrieve the list of machines and their statuses."""
    machines = Machine.query.all()
    return jsonify([{'id': m.id, 'name': m.name, 'status': m.status, 'last_checked': m.last_checked} for m in machines])

# Endpoint to update machine status
@app.route('/api/machines/<int:machine_id>', methods=['PUT'])
def update_machine(machine_id):
    """Update the status of a specific machine."""
    data = request.json
    machine = Machine.query.get(machine_id)
    if not machine:
        return jsonify({'error': 'Machine not found'}), 404
    machine.status = data.get('status', machine.status)
    machine.last_checked = datetime.utcnow()
    db.session.commit()
    return jsonify({'message': 'Machine status updated successfully'})

# Endpoint to track production
@app.route('/api/production', methods=['POST'])
def add_production():
    """Add a new production record."""
    data = request.json
    new_production = Production(quantity=data['quantity'])
    db.session.add(new_production)
    db.session.commit()
    return jsonify({'message': 'Production record added successfully'}), 201

# Endpoint to get production records
@app.route('/api/production', methods=['GET'])
def get_production():
    """Retrieve all production records."""
    productions = Production.query.all()
    return jsonify([{'id': p.id, 'quantity': p.quantity, 'date': p.date} for p in productions])

# Endpoint for quality control
@app.route('/api/quality-control', methods=['POST'])
def add_quality_control():
    """Add a new quality control record."""
    data = request.json
    new_quality_control = QualityControl(quality_score=data['quality_score'])
    db.session.add(new_quality_control)
    db.session.commit()
    return jsonify({'message': 'Quality control record added successfully'}), 201

# Endpoint to get quality control records
@app.route('/api/quality-control', methods=['GET'])
def get_quality_control():
    """Retrieve all quality control records."""
    quality_records = QualityControl.query.all()
    return jsonify([{'id': qc.id, 'inspection_date': qc.inspection_date, 'quality_score': qc.quality_score} for qc in quality_records])

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    """Return a 404 error for invalid routes."""
    return jsonify({'error': 'Not found'}), 404

# Error handling for internal server errors
@app.errorhandler(500)
def internal_error(error):
    """Return a 500 error for internal server issues."""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
