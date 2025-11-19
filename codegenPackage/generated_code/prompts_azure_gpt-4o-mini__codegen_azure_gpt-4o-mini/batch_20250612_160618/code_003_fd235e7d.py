"""
Generated Code Metadata:
========================
Original URL: https://sautikenya.com
Prompt: Create an API that collects data on women's participation in clean energy initiatives, reflecting the outcomes of Sauti Kenya's Cohort 2 project.
Generated: DETERMINISTIC_fd235e7de072ee73
Batch ID: 20250612_160618
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

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///sauti_kenya.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the data model for women's participation in clean energy initiatives
class Participation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    initiative = db.Column(db.String(100), nullable=False)
    outcome = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Participation {self.name} - {self.initiative}>'

# Define a schema for input validation and serialization
class ParticipationSchema(Schema):
    name = fields.Str(required=True)
    initiative = fields.Str(required=True)
    outcome = fields.Str(required=True)

# Initialize the schema
participation_schema = ParticipationSchema()
participations_schema = ParticipationSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to collect data on women's participation
@app.route('/api/participation', methods=['POST'])
def add_participation():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        participation_data = participation_schema.load(data)

        # Create a new Participation instance
        new_participation = Participation(**participation_data)

        # Add to the session and commit to the database
        db.session.add(new_participation)
        db.session.commit()

        return jsonify(participation_schema.dump(new_participation)), 201

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve all participations
@app.route('/api/participation', methods=['GET'])
def get_participations():
    try:
        participations = Participation.query.all()
        return jsonify(participations_schema.dump(participations)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
