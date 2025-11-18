"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: Provide an API recommendation for managing energy performance certificates (ΠΕΑ) in Greece, including features for categorizing buildings into energy classes from A+ to H.
Generated: DETERMINISTIC_ab2e271239987c3e
Batch ID: 20250612_152249
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///energy_certificates.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the EnergyPerformanceCertificate model
class EnergyPerformanceCertificate(db.Model):
    __tablename__ = 'certificates'
    
    id = db.Column(db.Integer, primary_key=True)
    building_name = db.Column(db.String(100), nullable=False)
    energy_class = db.Column(db.String(2), nullable=False)  # A+ to H
    issued_date = db.Column(db.String(10), nullable=False)  # Format: YYYY-MM-DD

    def __repr__(self):
        return f"<Certificate {self.building_name} - Class {self.energy_class}>"

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/certificates', methods=['POST'])
def create_certificate():
    """Create a new energy performance certificate."""
    data = request.get_json()

    # Validate input data
    if not all(key in data for key in ('building_name', 'energy_class', 'issued_date')):
        return jsonify({"error": "Missing fields"}), 400
    
    if data['energy_class'] not in [f"{class_}" for class_ in ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'E', 'F', 'G', 'H']]:
        return jsonify({"error": "Invalid energy class"}), 400

    new_certificate = EnergyPerformanceCertificate(
        building_name=data['building_name'],
        energy_class=data['energy_class'],
        issued_date=data['issued_date']
    )

    try:
        db.session.add(new_certificate)
        db.session.commit()
        return jsonify({"message": "Certificate created", "id": new_certificate.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database integrity error"}), 500

@app.route('/certificates', methods=['GET'])
def get_certificates():
    """Retrieve all energy performance certificates."""
    certificates = EnergyPerformanceCertificate.query.all()
    return jsonify([{
        "id": cert.id,
        "building_name": cert.building_name,
        "energy_class": cert.energy_class,
        "issued_date": cert.issued_date
    } for cert in certificates]), 200

@app.route('/certificates/<int:cert_id>', methods=['GET'])
def get_certificate(cert_id):
    """Retrieve a specific energy performance certificate by ID."""
    certificate = EnergyPerformanceCertificate.query.get(cert_id)
    if certificate is None:
        return jsonify({"error": "Certificate not found"}), 404

    return jsonify({
        "id": certificate.id,
        "building_name": certificate.building_name,
        "energy_class": certificate.energy_class,
        "issued_date": certificate.issued_date
    }), 200

@app.route('/certificates/<int:cert_id>', methods=['DELETE'])
def delete_certificate(cert_id):
    """Delete a specific energy performance certificate by ID."""
    certificate = EnergyPerformanceCertificate.query.get(cert_id)
    if certificate is None:
        return jsonify({"error": "Certificate not found"}), 404

    db.session.delete(certificate)
    db.session.commit()
    return jsonify({"message": "Certificate deleted"}), 204

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```
