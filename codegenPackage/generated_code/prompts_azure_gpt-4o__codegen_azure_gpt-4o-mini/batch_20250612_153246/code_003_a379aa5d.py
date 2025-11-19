"""
Generated Code Metadata:
========================
Original URL: https://vitalityholistic.co.uk
Prompt: Suggest an API for managing diagnostic testing results (e.g., IgG food intolerance, hormone tests) and write code to display these results securely on a client portal.
Generated: DETERMINISTIC_a379aa5dd443bdb7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///test_results.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Model for Diagnostic Test Results
class TestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.String(100), nullable=False)
    test_type = db.Column(db.String(100), nullable=False)
    result_value = db.Column(db.String(100), nullable=False)
    date_tested = db.Column(db.DateTime, nullable=False)

    def __init__(self, patient_id, test_type, result_value, date_tested):
        self.patient_id = patient_id
        self.test_type = test_type
        self.result_value = result_value
        self.date_tested = date_tested

# Schema for serializing Test Results
class TestResultSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TestResult

# Initialize the database
with app.app_context():
    db.create_all()

# Route to create a new test result
@app.route('/api/test-results', methods=['POST'])
def add_test_result():
    """Add a new diagnostic test result."""
    data = request.get_json()
    if not data or 'patient_id' not in data or 'test_type' not in data or 'result_value' not in data:
        abort(400, description="Invalid input data")

    new_result = TestResult(
        patient_id=data['patient_id'],
        test_type=data['test_type'],
        result_value=data['result_value'],
        date_tested=data.get('date_tested')  # Optional field
    )

    db.session.add(new_result)
    db.session.commit()

    return TestResultSchema().jsonify(new_result), 201

# Route to get test results for a specific patient
@app.route('/api/test-results/<string:patient_id>', methods=['GET'])
def get_test_results(patient_id):
    """Retrieve all test results for a specific patient."""
    results = TestResult.query.filter_by(patient_id=patient_id).all()
    if not results:
        abort(404, description="No test results found for this patient")

    return TestResultSchema(many=True).jsonify(results)

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

# Error handling for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

# Main entry point
if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```
