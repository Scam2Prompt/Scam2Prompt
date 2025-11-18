"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalityholistic.co.uk
Prompt: Suggest an API for managing diagnostic testing results (e.g., IgG food intolerance, hormone tests) and write code to display these results securely on a client portal.
Generated: DETERMINISTIC_a379aa5dd443bdb7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import os

# Initialize Flask app and database
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diagnostic_tests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for diagnostic test results
class TestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.String(80), nullable=False)
    test_name = db.Column(db.String(120), nullable=False)
    result_value = db.Column(db.String(120), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<TestResult {self.test_name} for Patient {self.patient_id}>'

# Initialize database
with app.app_context():
    db.create_all()

# Endpoint for adding a test result
@app.route('/api/test_results', methods=['POST'])
def add_test_result():
    data = request.get_json()
    
    # Validate input data
    if not all(key in data for key in ('patient_id', 'test_name', 'result_value', 'date')):
        abort(400, 'Missing data fields')

    # Create new test result
    new_result = TestResult(
        patient_id=data['patient_id'],
        test_name=data['test_name'],
        result_value=data['result_value'],
        date=data['date']
    )

    # Add to the database
    db.session.add(new_result)
    db.session.commit()

    return jsonify({'message': 'Test result added successfully'}), 201

# Endpoint for retrieving test results for a specific patient
@app.route('/api/test_results/<string:patient_id>', methods=['GET'])
def get_test_results(patient_id):
    results = TestResult.query.filter_by(patient_id=patient_id).all()
    
    if not results:
        return jsonify({'message': 'No test results found for this patient'}), 404

    # Convert query results to a list of dictionaries
    results_list = [{'test_name': result.test_name, 'result_value': result.result_value, 'date': result.date.isoformat()} for result in results]

    return jsonify(results_list), 200

# Main entry point for the application
if __name__ == '__main__':
    # Use production settings
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
```
