"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: Suggest an API for integrating a multi-step quality control system in automotive manufacturing, ensuring precision and durability, as emphasized in the "کنترل کیفی چند مرحله‌ای" section of the website.
Generated: DETERMINISTIC_0c653fa1f644e612
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quality_control.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the QualityControl model
class QualityControl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    step_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    comments = db.Column(db.String(255), nullable=True)

# Create a schema for input validation
class QualityControlSchema(Schema):
    step_name = fields.Str(required=True)
    status = fields.Str(required=True)
    comments = fields.Str()

# Initialize the database
with app.app_context():
    db.create_all()

# API endpoint to create a new quality control step
@app.route('/api/quality-control', methods=['POST'])
def create_quality_control():
    try:
        # Validate and deserialize input
        schema = QualityControlSchema()
        quality_control_data = schema.load(request.json)

        # Create a new QualityControl instance
        new_quality_control = QualityControl(
            step_name=quality_control_data['step_name'],
            status=quality_control_data['status'],
            comments=quality_control_data.get('comments')
        )

        # Add to the session and commit to the database
        db.session.add(new_quality_control)
        db.session.commit()

        return jsonify({"message": "Quality control step created successfully", "id": new_quality_control.id}), 201

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve all quality control steps
@app.route('/api/quality-control', methods=['GET'])
def get_quality_controls():
    try:
        quality_controls = QualityControl.query.all()
        result = [{"id": qc.id, "step_name": qc.step_name, "status": qc.status, "comments": qc.comments} for qc in quality_controls]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update a quality control step
@app.route('/api/quality-control/<int:id>', methods=['PUT'])
def update_quality_control(id):
    try:
        quality_control = QualityControl.query.get_or_404(id)
        schema = QualityControlSchema()
        quality_control_data = schema.load(request.json)

        # Update the quality control step
        quality_control.step_name = quality_control_data['step_name']
        quality_control.status = quality_control_data['status']
        quality_control.comments = quality_control_data.get('comments')

        db.session.commit()
        return jsonify({"message": "Quality control step updated successfully"}), 200

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to delete a quality control step
@app.route('/api/quality-control/<int:id>', methods=['DELETE'])
def delete_quality_control(id):
    try:
        quality_control = QualityControl.query.get_or_404(id)
        db.session.delete(quality_control)
        db.session.commit()
        return jsonify({"message": "Quality control step deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
