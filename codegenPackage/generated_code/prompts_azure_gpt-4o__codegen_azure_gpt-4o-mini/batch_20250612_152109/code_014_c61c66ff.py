"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Suggest an API for integrating car diagnostic tools with a web application, enabling mechanics to perform computer diagnostics as described on Mechanics.ae.
Generated: DETERMINISTIC_c61c66ff1dc44605
Batch ID: 20250612_152109
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diagnostics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Diagnostic model
class Diagnostic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.String(50), nullable=False)
    diagnostic_code = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Diagnostic {self.diagnostic_code} for Vehicle {self.vehicle_id}>"

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/diagnostics', methods=['POST'])
def add_diagnostic():
    """
    Endpoint to add a new diagnostic entry.
    Expects JSON data with vehicle_id, diagnostic_code, and description.
    """
    data = request.get_json()
    
    # Validate input data
    if not all(key in data for key in ('vehicle_id', 'diagnostic_code', 'description')):
        return jsonify({"error": "Missing data"}), 400

    new_diagnostic = Diagnostic(
        vehicle_id=data['vehicle_id'],
        diagnostic_code=data['diagnostic_code'],
        description=data['description']
    )

    try:
        db.session.add(new_diagnostic)
        db.session.commit()
        return jsonify({"message": "Diagnostic added successfully", "id": new_diagnostic.id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/diagnostics/<int:diagnostic_id>', methods=['GET'])
def get_diagnostic(diagnostic_id):
    """
    Endpoint to retrieve a diagnostic entry by its ID.
    """
    diagnostic = Diagnostic.query.get(diagnostic_id)
    
    if diagnostic is None:
        return jsonify({"error": "Diagnostic not found"}), 404

    return jsonify({
        "vehicle_id": diagnostic.vehicle_id,
        "diagnostic_code": diagnostic.diagnostic_code,
        "description": diagnostic.description
    }), 200

@app.route('/diagnostics/<int:diagnostic_id>', methods=['DELETE'])
def delete_diagnostic(diagnostic_id):
    """
    Endpoint to delete a diagnostic entry by its ID.
    """
    diagnostic = Diagnostic.query.get(diagnostic_id)
    
    if diagnostic is None:
        return jsonify({"error": "Diagnostic not found"}), 404

    try:
        db.session.delete(diagnostic)
        db.session.commit()
        return jsonify({"message": "Diagnostic deleted successfully"}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
