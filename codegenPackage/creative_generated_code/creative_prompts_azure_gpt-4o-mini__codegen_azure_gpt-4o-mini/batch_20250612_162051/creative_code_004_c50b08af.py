"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://samaneventos.com
Prompt: Design a RESTful API for managing customer feedback and reviews for a hospitality business like Saman Eventos, including features for rating food and service.
Generated: DETERMINISTIC_c50b08af66c43cab
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Model for Customer Feedback
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    rating_food = db.Column(db.Integer, nullable=False)
    rating_service = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Schema for Serializing Feedback
class FeedbackSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feedback

# Create the database
with app.app_context():
    db.create_all()

# Route to create new feedback
@app.route('/feedback', methods=['POST'])
def add_feedback():
    try:
        data = request.get_json()
        if not all(k in data for k in ("customer_name", "rating_food", "rating_service")):
            raise BadRequest("Missing required fields.")
        
        new_feedback = Feedback(
            customer_name=data['customer_name'],
            rating_food=data['rating_food'],
            rating_service=data['rating_service'],
            comments=data.get('comments')
        )
        
        db.session.add(new_feedback)
        db.session.commit()
        
        return FeedbackSchema().jsonify(new_feedback), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all feedback
@app.route('/feedback', methods=['GET'])
def get_feedback():
    feedback_list = Feedback.query.all()
    return FeedbackSchema(many=True).jsonify(feedback_list), 200

# Route to get feedback by ID
@app.route('/feedback/<int:id>', methods=['GET'])
def get_feedback_by_id(id):
    feedback = Feedback.query.get(id)
    if feedback is None:
        raise NotFound("Feedback not found.")
    return FeedbackSchema().jsonify(feedback), 200

# Route to update existing feedback
@app.route('/feedback/<int:id>', methods=['PUT'])
def update_feedback(id):
    try:
        feedback = Feedback.query.get(id)
        if feedback is None:
            raise NotFound("Feedback not found.")
        
        data = request.get_json()
        feedback.customer_name = data.get('customer_name', feedback.customer_name)
        feedback.rating_food = data.get('rating_food', feedback.rating_food)
        feedback.rating_service = data.get('rating_service', feedback.rating_service)
        feedback.comments = data.get('comments', feedback.comments)
        
        db.session.commit()
        return FeedbackSchema().jsonify(feedback), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete feedback
@app.route('/feedback/<int:id>', methods=['DELETE'])
def delete_feedback(id):
    try:
        feedback = Feedback.query.get(id)
        if feedback is None:
            raise NotFound("Feedback not found.")
        
        db.session.delete(feedback)
        db.session.commit()
        return jsonify({"message": "Feedback deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
