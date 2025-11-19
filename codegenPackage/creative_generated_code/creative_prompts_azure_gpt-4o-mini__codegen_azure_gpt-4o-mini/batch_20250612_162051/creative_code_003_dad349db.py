"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.nkatandiinyom.com
Prompt: Generate an API that connects women in Igbo communities for cultural preservation activities, reflecting the offerings of Nkata ndi Inyom Igbo.
Generated: DETERMINISTIC_dad349dba7d3f035
Batch ID: 20250612_162051
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
import os

# Initialize Flask app
app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///igbo_community.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the CommunityActivity model
class CommunityActivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(50), nullable=False)  # Consider using a date type
    location = db.Column(db.String(100), nullable=False)

# Create a schema for serialization
class CommunityActivitySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    date = fields.Str(required=True)
    location = fields.Str(required=True)

activity_schema = CommunityActivitySchema()
activities_schema = CommunityActivitySchema(many=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a new community activity
@app.route('/activities', methods=['POST'])
def add_activity():
    try:
        # Validate input data
        data = request.get_json()
        activity = activity_schema.load(data)
        
        new_activity = CommunityActivity(**activity)
        db.session.add(new_activity)
        db.session.commit()

        return activity_schema.jsonify(new_activity), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve all community activities
@app.route('/activities', methods=['GET'])
def get_activities():
    try:
        activities = CommunityActivity.query.all()
        return activities_schema.jsonify(activities), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve a specific activity by ID
@app.route('/activities/<int:id>', methods=['GET'])
def get_activity(id):
    try:
        activity = CommunityActivity.query.get_or_404(id)
        return activity_schema.jsonify(activity), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update a community activity
@app.route('/activities/<int:id>', methods=['PUT'])
def update_activity(id):
    try:
        activity = CommunityActivity.query.get_or_404(id)
        data = request.get_json()
        updated_activity = activity_schema.load(data)
        
        for key, value in updated_activity.items():
            setattr(activity, key, value)
        
        db.session.commit()
        return activity_schema.jsonify(activity), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to delete a community activity
@app.route('/activities/<int:id>', methods=['DELETE'])
def delete_activity(id):
    try:
        activity = CommunityActivity.query.get_or_404(id)
        db.session.delete(activity)
        db.session.commit()
        return jsonify({"message": "Activity deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Ensure you have the required packages installed: Flask, Flask-SQLAlchemy, Marshmallow.
- You can set the database URI through an environment variable or change it to a preferred database.
- This code assumes you're using SQLite for simplicity; adjust the database URI for other databases.
- Error handling is incorporated for validation and general exceptions.
