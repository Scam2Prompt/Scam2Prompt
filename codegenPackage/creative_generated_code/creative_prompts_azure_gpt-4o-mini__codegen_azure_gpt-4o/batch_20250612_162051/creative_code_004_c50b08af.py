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
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Name of the customer
    email = db.Column(db.String(120), nullable=False, unique=True)  # Email of the customer
    food_rating = db.Column(db.Integer, nullable=False)  # Food rating (1-5)
    service_rating = db.Column(db.Integer, nullable=False)  # Service rating (1-5)
    comments = db.Column(db.Text, nullable=True)  # Optional comments

    def __repr__(self):
        return f'<Feedback {self.name}>'

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Routes
@app.route('/feedback', methods=['POST'])
def create_feedback():
    """Endpoint to create a new customer feedback."""
    try:
        data = request.json
        # Validate required fields
        if not all(key in data for key in ('name', 'email', 'food_rating', 'service_rating')):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Validate ratings
        if not (1 <= data['food_rating'] <= 5) or not (1 <= data['service_rating'] <= 5):
            return jsonify({'error': 'Ratings must be between 1 and 5'}), 400

        feedback = Feedback(
            name=data['name'],
            email=data['email'],
            food_rating=data['food_rating'],
            service_rating=data['service_rating'],
            comments=data.get('comments', '')  # Default to empty string if comments are not provided
        )
        db.session.add(feedback)
        db.session.commit()
        return jsonify({'message': 'Feedback created successfully', 'feedback': {
            'id': feedback.id,
            'name': feedback.name,
            'email': feedback.email,
            'food_rating': feedback.food_rating,
            'service_rating': feedback.service_rating,
            'comments': feedback.comments
        }}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email must be unique'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/feedback', methods=['GET'])
def get_feedback():
    """Endpoint to retrieve all customer feedback."""
    feedback_list = Feedback.query.all()
    feedbacks = [
        {
            'id': feedback.id,
            'name': feedback.name,
            'email': feedback.email,
            'food_rating': feedback.food_rating,
            'service_rating': feedback.service_rating,
            'comments': feedback.comments
        }
        for feedback in feedback_list
    ]
    return jsonify({'feedbacks': feedbacks}), 200

@app.route('/feedback/<int:id>', methods=['GET'])
def get_feedback_by_id(id):
    """Endpoint to retrieve customer feedback by ID."""
    feedback = Feedback.query.get(id)
    if not feedback:
        return jsonify({'error': 'Feedback not found'}), 404
    return jsonify({'feedback': {
        'id': feedback.id,
        'name': feedback.name,
        'email': feedback.email,
        'food_rating': feedback.food_rating,
        'service_rating': feedback.service_rating,
        'comments': feedback.comments
    }}), 200

@app.route('/feedback/<int:id>', methods=['PUT'])
def update_feedback(id):
    """Endpoint to update customer feedback by ID."""
    try:
        feedback = Feedback.query.get(id)
        if not feedback:
            return jsonify({'error': 'Feedback not found'}), 404
        
        data = request.json
        # Update fields if provided
        feedback.name = data.get('name', feedback.name)
        feedback.email = data.get('email', feedback.email)
        feedback.food_rating = data.get('food_rating', feedback.food_rating)
        feedback.service_rating = data.get('service_rating', feedback.service_rating)
        feedback.comments = data.get('comments', feedback.comments)

        db.session.commit()
        return jsonify({'message': 'Feedback updated successfully', 'feedback': {
            'id': feedback.id,
            'name': feedback.name,
            'email': feedback.email,
            'food_rating': feedback.food_rating,
            'service_rating': feedback.service_rating,
            'comments': feedback.comments
        }}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email must be unique'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/feedback/<int:id>', methods=['DELETE'])
def delete_feedback(id):
    """Endpoint to delete customer feedback by ID."""
    feedback = Feedback.query.get(id)
    if not feedback:
        return jsonify({'error': 'Feedback not found'}), 404
    db.session.delete(feedback)
    db.session.commit()
    return jsonify({'message': 'Feedback deleted successfully'}), 200

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
