"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://provincialwatersolutions.com
Prompt: Suggest an API for integrating water testing solutions that align with the offerings of Provincial Water Solutions, particularly for well water issues.
Generated: DETERMINISTIC_c4130167ba087e01
Batch ID: 20250612_161700
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
from flask_marshmallow import Marshmallow

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///water_testing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Database model for water tests
class WaterTest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_type = db.Column(db.String(80), nullable=False)
    result = db.Column(db.String(120), nullable=False)
    notes = db.Column(db.String(255), nullable=True)

    def __init__(self, test_type, result, notes):
        self.test_type = test_type
        self.result = result
        self.notes = notes


# Schema for serializing WaterTest data
class WaterTestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WaterTest


# Initialize the schema
water_test_schema = WaterTestSchema()
water_tests_schema = WaterTestSchema(many=True)


# Endpoint to create a new water test
@app.route('/api/water_tests', methods=['POST'])
def add_water_test():
    try:
        test_type = request.json['test_type']
        result = request.json['result']
        notes = request.json.get('notes', '')

        new_test = WaterTest(test_type, result, notes)
        db.session.add(new_test)
        db.session.commit()

        return water_test_schema.jsonify(new_test), 201
    except KeyError as e:
        return jsonify({"error": f"Missing key: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Endpoint to retrieve all water tests
@app.route('/api/water_tests', methods=['GET'])
def get_water_tests():
    try:
        tests = WaterTest.query.all()
        return water_tests_schema.jsonify(tests), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Endpoint to retrieve a specific water test by ID
@app.route('/api/water_tests/<int:test_id>', methods=['GET'])
def get_water_test(test_id):
    try:
        test = WaterTest.query.get_or_404(test_id)
        return water_test_schema.jsonify(test), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Endpoint to update a water test
@app.route('/api/water_tests/<int:test_id>', methods=['PUT'])
def update_water_test(test_id):
    try:
        test = WaterTest.query.get_or_404(test_id)

        test.test_type = request.json.get('test_type', test.test_type)
        test.result = request.json.get('result', test.result)
        test.notes = request.json.get('notes', test.notes)

        db.session.commit()
        return water_test_schema.jsonify(test), 200
    except KeyError as e:
        return jsonify({"error": f"Missing key: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Endpoint to delete a water test
@app.route('/api/water_tests/<int:test_id>', methods=['DELETE'])
def delete_water_test(test_id):
    try:
        test = WaterTest.query.get_or_404(test_id)
        db.session.delete(test)
        db.session.commit()
        return jsonify({"message": "Water test deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run the application
if __name__ == '__main__':
    # Create the database and tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
