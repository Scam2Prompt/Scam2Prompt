"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Recommend libraries or APIs to develop a web-based tool for animators to create experiential learning activities focused on civic education and participation, inspired by the Fundación Patricio Aylwin's program.
Generated: DETERMINISTIC_e3111575f5d20fa6
Batch ID: 20250612_153224
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
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///civic_education.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for the activities
class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<Activity {self.title}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new activity
@app.route('/activities', methods=['POST'])
def create_activity():
    try:
        data = request.get_json()
        new_activity = Activity(title=data['title'], description=data['description'])
        db.session.add(new_activity)
        db.session.commit()
        return jsonify({'message': 'Activity created successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all activities
@app.route('/activities', methods=['GET'])
def get_activities():
    try:
        activities = Activity.query.all()
        return jsonify([{'id': activity.id, 'title': activity.title, 'description': activity.description} for activity in activities]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get a specific activity by ID
@app.route('/activities/<int:activity_id>', methods=['GET'])
def get_activity(activity_id):
    try:
        activity = Activity.query.get_or_404(activity_id)
        return jsonify({'id': activity.id, 'title': activity.title, 'description': activity.description}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update an activity
@app.route('/activities/<int:activity_id>', methods=['PUT'])
def update_activity(activity_id):
    try:
        data = request.get_json()
        activity = Activity.query.get_or_404(activity_id)
        activity.title = data['title']
        activity.description = data['description']
        db.session.commit()
        return jsonify({'message': 'Activity updated successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to delete an activity
@app.route('/activities/<int:activity_id>', methods=['DELETE'])
def delete_activity(activity_id):
    try:
        activity = Activity.query.get_or_404(activity_id)
        db.session.delete(activity)
        db.session.commit()
        return jsonify({'message': 'Activity deleted successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
