"""
Generated Code Metadata:
========================
Original URL: https://www.nkatandiinyom.com
Prompt: Generate an API that connects women in Igbo communities for cultural preservation activities, reflecting the offerings of Nkata ndi Inyom Igbo.
Generated: DETERMINISTIC_dad349dba7d3f035
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///igbo_community.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Model for cultural activities
class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    location = db.Column(db.String(100), nullable=False)

    def __init__(self, title, description, location):
        self.title = title
        self.description = description
        self.location = location

# Schema for serializing Activity objects
class ActivitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Activity

# Initialize the schema
activity_schema = ActivitySchema()
activities_schema = ActivitySchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new cultural activity
@app.route('/activities', methods=['POST'])
def add_activity():
    try:
        title = request.json['title']
        description = request.json['description']
        location = request.json['location']

        new_activity = Activity(title, description, location)
        db.session.add(new_activity)
        db.session.commit()

        return activity_schema.jsonify(new_activity), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get all cultural activities
@app.route('/activities', methods=['GET'])
def get_activities():
    try:
        all_activities = Activity.query.all()
        return activities_schema.jsonify(all_activities), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a specific activity by ID
@app.route('/activities/<int:id>', methods=['GET'])
def get_activity(id):
    try:
        activity = Activity.query.get_or_404(id)
        return activity_schema.jsonify(activity), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

# Route to update an existing activity
@app.route('/activities/<int:id>', methods=['PUT'])
def update_activity(id):
    try:
        activity = Activity.query.get_or_404(id)
        title = request.json.get('title', activity.title)
        description = request.json.get('description', activity.description)
        location = request.json.get('location', activity.location)

        activity.title = title
        activity.description = description
        activity.location = location

        db.session.commit()
        return activity_schema.jsonify(activity), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to delete an activity
@app.route('/activities/<int:id>', methods=['DELETE'])
def delete_activity(id):
    try:
        activity = Activity.query.get_or_404(id)
        db.session.delete(activity)
        db.session.commit()
        return jsonify({"message": "Activity deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
