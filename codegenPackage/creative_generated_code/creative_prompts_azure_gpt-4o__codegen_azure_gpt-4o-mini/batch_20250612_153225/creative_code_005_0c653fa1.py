"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tdkco.ir
Prompt: Suggest an API for integrating a multi-step quality control system in automotive manufacturing, ensuring precision and durability, as emphasized in the "کنترل کیفی چند مرحله‌ای" section of the website.
Generated: DETERMINISTIC_0c653fa1f644e612
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configuring the database URI for SQLite for simplicity in this example
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quality_control.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Quality Check
class QualityCheck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    step_name = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(10), nullable=False)  # e.g., 'passed', 'failed'
    notes = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<QualityCheck {self.step_name}: {self.status}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/quality-check', methods=['POST'])
def create_quality_check():
    """
    Endpoint to create a new quality check.
    Expects JSON with `step_name`, `status`, and optional `notes`.
    """
    try:
        data = request.get_json()
        new_check = QualityCheck(
            step_name=data['step_name'],
            status=data['status'],
            notes=data.get('notes', None)
        )
        db.session.add(new_check)
        db.session.commit()
        return jsonify({'message': 'Quality check created', 'id': new_check.id}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/quality-check/<int:id>', methods=['GET'])
def get_quality_check(id):
    """
    Endpoint to retrieve a quality check by its ID.
    """
    quality_check = QualityCheck.query.get(id)
    if quality_check is None:
        return jsonify({'error': 'Quality check not found'}), 404
    return jsonify({
        'id': quality_check.id,
        'step_name': quality_check.step_name,
        'status': quality_check.status,
        'notes': quality_check.notes
    }), 200

@app.route('/quality-check/<int:id>', methods=['PUT'])
def update_quality_check(id):
    """
    Endpoint to update a quality check.
    Expects JSON with optional `step_name`, `status`, and `notes`.
    """
    quality_check = QualityCheck.query.get(id)
    if quality_check is None:
        return jsonify({'error': 'Quality check not found'}), 404

    data = request.get_json()
    quality_check.step_name = data.get('step_name', quality_check.step_name)
    quality_check.status = data.get('status', quality_check.status)
    quality_check.notes = data.get('notes', quality_check.notes)

    try:
        db.session.commit()
        return jsonify({'message': 'Quality check updated'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/quality-check/<int:id>', methods=['DELETE'])
def delete_quality_check(id):
    """
    Endpoint to delete a quality check by its ID.
    """
    quality_check = QualityCheck.query.get(id)
    if quality_check is None:
        return jsonify({'error': 'Quality check not found'}), 404

    try:
        db.session.delete(quality_check)
        db.session.commit()
        return jsonify({'message': 'Quality check deleted'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install Flask and Flask-SQLAlchemy before running the code:

```bash
pip install Flask Flask-SQLAlchemy
```
