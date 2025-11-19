"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniair.id
Prompt: Develop a RESTful API endpoint that provides information on multimodal transportation options, inspired by the logistics solutions offered by Uniair Cargo.
Generated: DETERMINISTIC_d66f6be8f926c885
Batch ID: 20250612_161317
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
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transportation.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the Transportation model
class Transportation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mode = db.Column(db.String(50), nullable=False)
    details = db.Column(db.String(200), nullable=False)

# Create a schema for serialization
class TransportationSchema(Schema):
    id = fields.Int()
    mode = fields.Str(required=True)
    details = fields.Str(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to get all transportation options
@app.route('/api/transportation', methods=['GET'])
def get_transportation():
    try:
        options = Transportation.query.all()
        schema = TransportationSchema(many=True)
        return jsonify(schema.dump(options)), 200
    except Exception as e:
        logger.error(f"Error fetching transportation options: {e}")
        return jsonify({"error": "Failed to fetch transportation options."}), 500

# API endpoint to add a transportation option
@app.route('/api/transportation', methods=['POST'])
def add_transportation():
    try:
        data = request.get_json()
        schema = TransportationSchema()
        validated_data = schema.load(data)
        
        new_option = Transportation(
            mode=validated_data['mode'],
            details=validated_data['details']
        )
        db.session.add(new_option)
        db.session.commit()

        return jsonify(schema.dump(new_option)), 201

    except ValidationError as e:
        return jsonify({"error": "Invalid input", "messages": e.messages}), 400
    except Exception as e:
        logger.error(f"Error adding transportation option: {e}")
        return jsonify({"error": "Failed to add transportation option."}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=False)
```
