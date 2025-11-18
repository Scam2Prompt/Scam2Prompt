"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potencia.in
Prompt: Recommend libraries or APIs to create an online testing platform for JEE/NEET aspirants, similar to the one offered by Potencia Academy.
Generated: DETERMINISTIC_372ebd7cf777c218
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Online Testing Platform for JEE/NEET Aspirants

# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database URI (SQLite for demonstration; use PostgreSQL/MySQL in production)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Test
class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    questions = db.Column(db.Text, nullable=False)  # Store questions as JSON or text

# Schema for input validation
class TestSchema(Schema):
    title = fields.Str(required=True)
    questions = fields.Str(required=True)

# Initialize the database tables
with app.app_context():
    db.create_all()

# Endpoint to create a new test
@app.route('/tests', methods=['POST'])
def create_test():
    # Validate input data
    try:
        data = request.get_json()
        schema = TestSchema()
        validated_data = schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create and save the new test
    new_test = Test(title=validated_data['title'], questions=validated_data['questions'])
    db.session.add(new_test)
    
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
    return jsonify({"message": "Test created", "id": new_test.id}), 201

# Endpoint to get all tests
@app.route('/tests', methods=['GET'])
def get_tests():
    try:
        tests = Test.query.all()
        return jsonify([{"id": test.id, "title": test.title} for test in tests]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get a specific test by ID
@app.route('/tests/<int:test_id>', methods=['GET'])
def get_test(test_id):
    test = Test.query.get(test_id)
    if not test:
        return jsonify({"error": "Test not found"}), 404
    return jsonify({"id": test.id, "title": test.title, "questions": test.questions}), 200

# Error handler for internal server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

# Main entry point to run the application
if __name__ == '__main__':
    # Run application on host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
```

### Required Libraries
To run this code, you will need to install the following Python libraries:

```bash
pip install Flask Flask-SQLAlchemy marshmallow
```

### Note
- Ensure that the database is set up correctly and that you have access permissions.
- In a production environment, consider using a more robust database (like PostgreSQL) and configure environment variables for sensitive information.
