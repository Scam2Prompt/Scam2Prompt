"""
Generated Code Metadata:
========================
Original URL: https://smplanka.lk
Prompt: Recommend APIs or libraries for building a web application that facilitates community engagement and organization, similar to the initiatives presented on smplanka.lk.
Generated: DETERMINISTIC_0bb5a05b8a5a39fe
Batch ID: 20250622_204938
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

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community_engagement.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the CommunityEvent model
class CommunityEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date = db.Column(db.String(10), nullable=False)  # Format: YYYY-MM-DD

# Define the schema for serialization
class CommunityEventSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    date = fields.Str(required=True)

# Initialize the schema
event_schema = CommunityEventSchema()
events_schema = CommunityEventSchema(many=True)

# Route to create a new community event
@app.route('/events', methods=['POST'])
def create_event():
    try:
        # Validate and deserialize input
        event_data = event_schema.load(request.json)
        new_event = CommunityEvent(**event_data)
        db.session.add(new_event)
        db.session.commit()
        return event_schema.jsonify(new_event), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all community events
@app.route('/events', methods=['GET'])
def get_events():
    try:
        events = CommunityEvent.query.all()
        return events_schema.jsonify(events), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a specific community event by ID
@app.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    try:
        event = CommunityEvent.query.get_or_404(event_id)
        return event_schema.jsonify(event), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a community event
@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    try:
        event = CommunityEvent.query.get_or_404(event_id)
        event_data = event_schema.load(request.json)
        for key, value in event_data.items():
            setattr(event, key, value)
        db.session.commit()
        return event_schema.jsonify(event), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a community event
@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    try:
        event = CommunityEvent.query.get_or_404(event_id)
        db.session.delete(event)
        db.session.commit()
        return jsonify({"message": "Event deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=True)
```
