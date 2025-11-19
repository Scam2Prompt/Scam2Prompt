"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amarhospital.com
Prompt: Create a REST API endpoint for a hospital management system that allows for the retrieval of patient records, reflecting the fully computerized health records system at Amar Hospital.
Generated: DETERMINISTIC_c7c86fb38f544230
Batch ID: 20250612_155840
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

# Initialize the Flask application
app = Flask(__name__)

# Configuring the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'  # Use your preferred database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model definition for Patient
class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    record = db.Column(db.Text, nullable=True)

    def to_dict(self):
        """Convert Patient object to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'record': self.record
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/api/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    """Retrieve a patient record by ID."""
    patient = Patient.query.get(patient_id)
    
    if patient is None:
        # If patient not found, return a 404 error
        abort(404, description='Patient not found')
    
    return jsonify(patient.to_dict()), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": str(error)}), 404

@app.errorhandler(Exception)
def handle_exception(e):
    """Handle unexpected errors."""
    return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install the required libraries before running the application:
```bash
pip install Flask Flask-SQLAlchemy
```

You can run this Flask application and access patient records via the following endpoint:
```
GET /api/patients/<patient_id>
```
