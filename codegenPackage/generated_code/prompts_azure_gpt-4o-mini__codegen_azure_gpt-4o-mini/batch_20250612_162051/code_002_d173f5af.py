"""
Generated Code Metadata:
========================
Original URL: https://jusoor.ch
Prompt: Create a REST API that allows users to report human rights abuses, incorporating features discussed in Jusoor International's programs and goals.
Generated: DETERMINISTIC_d173f5aff61605c1
Batch ID: 20250612_162051
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///abuses.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Abuse model
class Abuse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    reported_by = db.Column(db.String(100), nullable=False)

# Create a schema for input validation
class AbuseSchema(Schema):
    description = fields.Str(required=True)
    location = fields.Str(required=True)
    reported_by = fields.Str(required=True)

# Initialize the schema
abuse_schema = AbuseSchema()
abuses_schema = AbuseSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to report a human rights abuse
@app.route('/report', methods=['POST'])
def report_abuse():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = abuse_schema.load(data)

        # Create a new Abuse record
        new_abuse = Abuse(**validated_data)
        db.session.add(new_abuse)
        db.session.commit()

        return jsonify({"message": "Abuse reported successfully", "id": new_abuse.id}), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all reported abuses
@app.route('/abuses', methods=['GET'])
def get_abuses():
    try:
        abuses = Abuse.query.all()
        return jsonify(abuses_schema.dump(abuses)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
```

### Requirements
To run this code, ensure you have the following Python packages installed:
```bash
pip install Flask Flask-SQLAlchemy marshmallow
```

### Environment Variables
- `DATABASE_URL`: URL for the database (default is SQLite).
- `FLASK_DEBUG`: Set to 'True' for debug mode, 'False' otherwise.
