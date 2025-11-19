"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sautikenya.com
Prompt: Create an API that collects data on women's participation in clean energy initiatives, reflecting the outcomes of Sauti Kenya's Cohort 2 project.
Generated: DETERMINISTIC_fd235e7de072ee73
Batch ID: 20250612_160618
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

# Configure the database URI and initialize SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sauti_kenya.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Create a model for the data
class Participation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    project = db.Column(db.String(100), nullable=False)
    outcome = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Participation {self.name}>'

# Create a schema for data validation
class ParticipationSchema(Schema):
    name = fields.Str(required=True)
    project = fields.Str(required=True)
    outcome = fields.Str(required=True)

participation_schema = ParticipationSchema()
participation_list_schema = ParticipationSchema(many=True)

# Endpoint to add participation data
@app.route('/api/participation', methods=['POST'])
def add_participation():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        participation = participation_schema.load(data)
        
        # Create a new Participation object
        new_participation = Participation(**participation)
        
        # Add to the session and commit
        db.session.add(new_participation)
        db.session.commit()
        
        return jsonify(participation_schema.dump(new_participation)), 201
    except ValidationError as err:
        logging.error(f"Validation error: {err.messages}")
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

# Endpoint to retrieve all participation data
@app.route('/api/participation', methods=['GET'])
def get_participation():
    try:
        # Query all participation data
        all_participation = Participation.query.all()
        result = participation_list_schema.dump(all_participation)
        return jsonify(result), 200
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

# Initialize the database and create the tables
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```
