"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.viviresconvivir.cl
Prompt: Recommend libraries or APIs to develop a web-based tool for animators to create experiential learning activities focused on civic education and participation, inspired by the Fundación Patricio Aylwin's program.
Generated: DETERMINISTIC_e3111575f5d20fa6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///experiential_learning.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for activities
class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

# Create the database
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
        return jsonify({"message": "Activity created successfully!", "id": new_activity.id}), 201
    except Exception as e:
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({"error": str(e)}), 400

# Route to get all activities
@app.route('/activities', methods=['GET'])
def get_activities():
    try:
        activities = Activity.query.all()
        return jsonify([{"id": act.id, "title": act.title, "description": act.description} for act in activities]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```
