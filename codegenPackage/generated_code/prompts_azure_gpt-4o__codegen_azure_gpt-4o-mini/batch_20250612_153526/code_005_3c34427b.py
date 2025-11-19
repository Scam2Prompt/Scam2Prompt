"""
Generated Code Metadata:
========================
Original URL: https://kiberahamlets.org
Prompt: Write code for a mobile app that tracks talent development activities such as spoken word, acrobatics, football, theatre, music, and dance, as described in the "Help me explore my talent" project.
Generated: DETERMINISTIC_3c34427bebd927c2
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///talent_development.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the TalentActivity model
class TalentActivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<TalentActivity {self.activity_type}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to add a new talent development activity
@app.route('/activities', methods=['POST'])
def add_activity():
    try:
        data = request.get_json()
        activity_type = data.get('activity_type')
        description = data.get('description')

        if not activity_type:
            return jsonify({"error": "Activity type is required"}), 400

        new_activity = TalentActivity(activity_type=activity_type, description=description)
        db.session.add(new_activity)
        db.session.commit()

        return jsonify({"message": "Activity added successfully", "activity": new_activity.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all talent development activities
@app.route('/activities', methods=['GET'])
def get_activities():
    try:
        activities = TalentActivity.query.all()
        return jsonify([{"id": activity.id, "activity_type": activity.activity_type, "description": activity.description, "date": activity.date} for activity in activities]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update an existing talent development activity
@app.route('/activities/<int:activity_id>', methods=['PUT'])
def update_activity(activity_id):
    try:
        data = request.get_json()
        activity = TalentActivity.query.get_or_404(activity_id)

        activity.activity_type = data.get('activity_type', activity.activity_type)
        activity.description = data.get('description', activity.description)

        db.session.commit()

        return jsonify({"message": "Activity updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a talent development activity
@app.route('/activities/<int:activity_id>', methods=['DELETE'])
def delete_activity(activity_id):
    try:
        activity = TalentActivity.query.get_or_404(activity_id)
        db.session.delete(activity)
        db.session.commit()

        return jsonify({"message": "Activity deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
