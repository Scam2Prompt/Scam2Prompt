"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matter.com.uy
Prompt: Create an API that facilitates the collection and visualization of organizational data to support decision-making processes, inspired by Matter's data analytics strategies.
Generated: DETERMINISTIC_06244c9ed9dafa7c
Batch ID: 20250612_162050
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
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///organizational_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define a model for organizational data
class OrganizationalData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(80), nullable=False)
    metric = db.Column(db.String(120), nullable=False)
    value = db.Column(db.Float, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define a schema for input validation
class OrganizationalDataSchema(Schema):
    department = fields.Str(required=True)
    metric = fields.Str(required=True)
    value = fields.Float(required=True)

# Initialize the schema
data_schema = OrganizationalDataSchema()

# API endpoint to collect organizational data
@app.route('/data', methods=['POST'])
def collect_data():
    try:
        # Validate and deserialize input data
        data = data_schema.load(request.json)
        
        # Create a new record
        new_data = OrganizationalData(**data)
        db.session.add(new_data)
        db.session.commit()
        
        return jsonify({"message": "Data collected successfully", "id": new_data.id}), 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        logging.error(f"Error collecting data: {e}")
        return jsonify({"message": "Internal server error"}), 500

# API endpoint to visualize organizational data
@app.route('/data', methods=['GET'])
def visualize_data():
    try:
        # Fetch all records
        results = OrganizationalData.query.all()
        data = [{"id": d.id, "department": d.department, "metric": d.metric, "value": d.value} for d in results]
        
        return jsonify(data), 200
    except Exception as e:
        logging.error(f"Error retrieving data: {e}")
        return jsonify({"message": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```
