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
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'feedback.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Feedback Model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    event_type = db.Column(db.String(100), nullable=False)
    food_rating = db.Column(db.Integer, nullable=False)
    service_rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text)
    date_submitted = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, customer_name, email, event_type, food_rating, service_rating, comments):
        self.customer_name = customer_name
        self.email = email
        self.event_type = event_type
        self.food_rating = food_rating
        self.service_rating = service_rating
        self.comments = comments

# Feedback Schema
class FeedbackSchema(ma.Schema):
    class Meta:
        fields = ('id', 'customer_name', 'email', 'event_type', 'food_rating', 'service_rating', 'comments', 'date_submitted')

# Initialize schema
feedback_schema = FeedbackSchema()
feedbacks_schema = FeedbackSchema(many=True)

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Routes
@app.route('/feedback', methods=['POST'])
def add_feedback():
    try:
        customer_name = request.json['customer_name']
        email = request.json['email']
        event_type = request.json['event_type']
        food_rating = request.json['food_rating']
        service_rating = request.json['service_rating']
        comments = request.json.get('comments', '')

        # Validate ratings
        if not (1 <= food_rating <= 5) or not (1 <= service_rating <= 5):
            return jsonify({'error': 'Ratings must be between 1 and 5'}), 400

        new_feedback = Feedback(customer_name, email, event_type, food_rating, service_rating, comments)

        db.session.add(new_feedback)
        db.session.commit()

        return feedback_schema.jsonify(new_feedback), 201
    except KeyError as e:
        return jsonify({'error': f'Missing required field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/feedback', methods=['GET'])
def get_feedbacks():
    try:
        all_feedbacks = Feedback.query.all()
        result = feedbacks_schema.dump(all_feedbacks)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/feedback/<id>', methods=['GET'])
def get_feedback(id):
    try:
        feedback = Feedback.query.get(id)
        if not feedback:
            return jsonify({'error': 'Feedback not found'}), 404
        return feedback_schema.jsonify(feedback), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/feedback/<id>', methods=['PUT'])
def update_feedback(id):
    try:
        feedback = Feedback.query.get(id)
        if not feedback:
            return jsonify({'error': 'Feedback not found'}), 404

        if 'customer_name' in request.json:
            feedback.customer_name = request.json['customer_name']
        if 'email' in request.json:
            feedback.email = request.json['email']
        if 'event_type' in request.json:
            feedback.event_type = request.json['event_type']
        if 'food_rating' in request.json:
            food_rating = request.json['food_rating']
            if not (1 <= food_rating <= 5):
                return jsonify({'error': 'Food rating must be between 1 and 5'}), 400
            feedback.food_rating = food_rating
        if 'service_rating' in request.json:
            service_rating = request.json['service_rating']
            if not (1 <= service_rating <= 5):
                return jsonify({'error': 'Service rating must be between 1 and 5'}), 400
            feedback.service_rating = service_rating
        if 'comments' in request.json:
            feedback.comments = request.json['comments']

        db.session.commit()
        return feedback_schema.jsonify(feedback), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/feedback/<id>', methods=['DELETE'])
def delete_feedback(id):
    try:
        feedback = Feedback.query.get(id)
        if not feedback:
            return jsonify({'error': 'Feedback not found'}), 404

        db.session.delete(feedback)
        db.session.commit()
        return jsonify({'message': 'Feedback deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/feedback/average-ratings', methods=['GET'])
def get_average_ratings():
    try:
        # Calculate average food rating
        avg_food = db.session.query(db.func.avg(Feedback.food_rating)).scalar()
        # Calculate average service rating
        avg_service = db.session.query(db.func.avg(Feedback.service_rating)).scalar()

        return jsonify({
            'average_food_rating': round(float(avg_food or 0), 2),
            'average_service_rating': round(float(avg_service or 0), 2)
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({'error': 'Method not allowed'}), 405

# Run server
if __name__ == '__main__':
    app.run(debug=True)
```
