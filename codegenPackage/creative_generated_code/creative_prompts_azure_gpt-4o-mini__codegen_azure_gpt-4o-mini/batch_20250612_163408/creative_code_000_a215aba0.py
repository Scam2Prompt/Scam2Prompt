"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-200--nervous-kare-6f3c45.netlify.app
Prompt: How can I implement a refuse and recycling collection API for a city similar to the City of York?
Generated: DETERMINISTIC_a215aba0b1f652ea
Batch ID: 20250612_163408
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
from datetime import datetime
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Database model for collection schedule
class CollectionSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    collection_date = db.Column(db.Date, nullable=False)
    collection_type = db.Column(db.String(50), nullable=False)  # 'refuse' or 'recycling'

    def __repr__(self):
        return f"<CollectionSchedule {self.collection_date} - {self.collection_type}>"

# Marshmallow schema for input validation
class CollectionScheduleSchema(Schema):
    collection_date = fields.Date(required=True)
    collection_type = fields.Str(required=True, validate=lambda s: s in ['refuse', 'recycling'])

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API Endpoint to create a new collection schedule
@app.route('/collection', methods=['POST'])
def add_collection_schedule():
    schema = CollectionScheduleSchema()
    try:
        data = schema.load(request.json)
        new_schedule = CollectionSchedule(
            collection_date=data['collection_date'],
            collection_type=data['collection_type']
        )
        db.session.add(new_schedule)
        db.session.commit()
        return jsonify({"message": "Collection schedule added successfully!"}), 201
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Endpoint to retrieve all collection schedules
@app.route('/collection', methods=['GET'])
def get_collection_schedules():
    try:
        schedules = CollectionSchedule.query.all()
        result = [{'id': schedule.id, 'collection_date': schedule.collection_date.isoformat(), 'collection_type': schedule.collection_type} for schedule in schedules]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Endpoint to retrieve collection schedule by ID
@app.route('/collection/<int:id>', methods=['GET'])
def get_collection_schedule_by_id(id):
    try:
        schedule = CollectionSchedule.query.get_or_404(id)
        result = {
            'id': schedule.id,
            'collection_date': schedule.collection_date.isoformat(),
            'collection_type': schedule.collection_type
        }
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Endpoint to delete a collection schedule
@app.route('/collection/<int:id>', methods=['DELETE'])
def delete_collection_schedule(id):
    try:
        schedule = CollectionSchedule.query.get_or_404(id)
        db.session.delete(schedule)
        db.session.commit()
        return jsonify({"message": "Collection schedule deleted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Running the application
if __name__ == '__main__':
    app.run(debug=True)
```
