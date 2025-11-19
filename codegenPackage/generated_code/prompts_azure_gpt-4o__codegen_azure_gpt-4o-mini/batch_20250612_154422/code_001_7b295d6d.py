"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Recommend libraries or APIs to build a web-based test series platform for IAS Prelims and Mains, inspired by Shield IAS's thematic tests and rapid revision modules.
Generated: DETERMINISTIC_7b295d6d5b2e35ee
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_series.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Test model
class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    category = db.Column(db.String(50), nullable=False)

# Define the schema for serialization
class TestSchema(Schema):
    id = fields.Int()
    title = fields.Str(required=True)
    description = fields.Str()
    category = fields.Str(required=True)

# Initialize the schema
test_schema = TestSchema()
tests_schema = TestSchema(many=True)

# Route to create a new test
@app.route('/tests', methods=['POST'])
def create_test():
    try:
        # Validate and deserialize input
        test_data = test_schema.load(request.json)
        new_test = Test(**test_data)
        db.session.add(new_test)
        db.session.commit()
        return test_schema.jsonify(new_test), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all tests
@app.route('/tests', methods=['GET'])
def get_tests():
    try:
        tests = Test.query.all()
        return tests_schema.jsonify(tests), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a specific test by ID
@app.route('/tests/<int:test_id>', methods=['GET'])
def get_test(test_id):
    try:
        test = Test.query.get_or_404(test_id)
        return test_schema.jsonify(test), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a test
@app.route('/tests/<int:test_id>', methods=['PUT'])
def update_test(test_id):
    try:
        test = Test.query.get_or_404(test_id)
        test_data = test_schema.load(request.json)
        for key, value in test_data.items():
            setattr(test, key, value)
        db.session.commit()
        return test_schema.jsonify(test), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a test
@app.route('/tests/<int:test_id>', methods=['DELETE'])
def delete_test(test_id):
    try:
        test = Test.query.get_or_404(test_id)
        db.session.delete(test)
        db.session.commit()
        return jsonify({"message": "Test deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Requirements
To run this code, you will need to install the following Python packages:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate marshmallow
```

### Database Initialization
Before running the application, initialize the database:
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```
