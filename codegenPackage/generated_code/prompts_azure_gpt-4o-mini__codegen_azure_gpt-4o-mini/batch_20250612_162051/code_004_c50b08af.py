"""
Generated Code Metadata:
========================
Original URL: https://samaneventos.com
Prompt: Design a RESTful API for managing customer feedback and reviews for a hospitality business like Saman Eventos, including features for rating food and service.
Generated: DETERMINISTIC_c50b08af66c43cab
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    food_rating = db.Column(db.Integer, nullable=False)
    service_rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String(500), nullable=True)

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for input validation
class FeedbackSchema(Schema):
    customer_name = fields.Str(required=True)
    food_rating = fields.Int(required=True, validate=lambda n: 1 <= n <= 5)
    service_rating = fields.Int(required=True, validate=lambda n: 1 <= n <= 5)
    comments = fields.Str(required=False)

feedback_schema = FeedbackSchema()
feedback_list_schema = FeedbackSchema(many=True)

# Route to create new feedback
@app.route('/feedback', methods=['POST'])
def create_feedback():
    """Create a new feedback entry."""
    json_data = request.get_json()
    try:
        data = feedback_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_feedback = Feedback(**data)
    db.session.add(new_feedback)
    db.session.commit()
    return feedback_schema.dump(new_feedback), 201

# Route to get all feedback
@app.route('/feedback', methods=['GET'])
def get_feedback():
    """Retrieve all feedback entries."""
    feedbacks = Feedback.query.all()
    return feedback_list_schema.dump(feedbacks), 200

# Route to get feedback by ID
@app.route('/feedback/<int:feedback_id>', methods=['GET'])
def get_feedback_by_id(feedback_id):
    """Retrieve feedback entry by ID."""
    feedback = Feedback.query.get(feedback_id)
    if feedback is None:
        abort(404, description="Feedback not found")
    return feedback_schema.dump(feedback), 200

# Route to update feedback by ID
@app.route('/feedback/<int:feedback_id>', methods=['PUT'])
def update_feedback(feedback_id):
    """Update an existing feedback entry."""
    feedback = Feedback.query.get(feedback_id)
    if feedback is None:
        abort(404, description="Feedback not found")

    json_data = request.get_json()
    try:
        data = feedback_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    for key, value in data.items():
        setattr(feedback, key, value)

    db.session.commit()
    return feedback_schema.dump(feedback), 200

# Route to delete feedback by ID
@app.route('/feedback/<int:feedback_id>', methods=['DELETE'])
def delete_feedback(feedback_id):
    """Delete a feedback entry by ID."""
    feedback = Feedback.query.get(feedback_id)
    if feedback is None:
        abort(404, description="Feedback not found")

    db.session.delete(feedback)
    db.session.commit()
    return jsonify({"message": "Feedback deleted successfully"}), 204

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
