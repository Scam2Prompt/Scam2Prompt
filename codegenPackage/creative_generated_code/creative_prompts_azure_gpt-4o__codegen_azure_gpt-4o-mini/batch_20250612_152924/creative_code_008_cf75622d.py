"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://provincialwatersolutions.com
Prompt: Create an API that integrates customer testimonials and feedback to recommend water treatment systems, inspired by the testimonial section of Provincial Water Solutions.
Generated: DETERMINISTIC_cf75622d33344b68
Batch ID: 20250612_152924
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
import logging

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testimonials.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define the Testimonial model
class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    feedback = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'feedback': self.feedback,
            'rating': self.rating
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/testimonials', methods=['POST'])
def add_testimonial():
    """
    Endpoint to add a new customer testimonial.
    Expects JSON payload with 'customer_name', 'feedback', and 'rating'.
    """
    data = request.get_json()
    
    # Validate input data
    if not all(key in data for key in ('customer_name', 'feedback', 'rating')):
        return jsonify({'error': 'Missing fields'}), 400

    if not isinstance(data['rating'], int) or not (1 <= data['rating'] <= 5):
        return jsonify({'error': 'Rating must be an integer between 1 and 5'}), 400

    # Create a new testimonial
    testimonial = Testimonial(
        customer_name=data['customer_name'],
        feedback=data['feedback'],
        rating=data['rating']
    )
    
    try:
        db.session.add(testimonial)
        db.session.commit()
        return jsonify(testimonial.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Could not save testimonial'}), 500

@app.route('/testimonials', methods=['GET'])
def get_testimonials():
    """
    Endpoint to fetch all customer testimonials.
    Returns a list of testimonials in JSON format.
    """
    testimonials = Testimonial.query.all()
    return jsonify([testimonial.to_dict() for testimonial in testimonials]), 200

@app.route('/recommendations', methods=['GET'])
def recommend_systems():
    """
    Endpoint to recommend water treatment systems based on testimonials' ratings.
    Returns recommended systems based on average rating.
    """
    testimonials = Testimonial.query.all()
    
    if not testimonials:
        return jsonify({'recommendations': []}), 200

    average_rating = sum(t.rating for t in testimonials) / len(testimonials)

    # Simple recommendation logic based on average rating
    if average_rating >= 4.5:
        recommendation = "High-End Water Treatment Systems"
    elif average_rating >= 3:
        recommendation = "Mid-Range Water Treatment Systems"
    else:
        recommendation = "Basic Water Treatment Systems"

    return jsonify({'average_rating': average_rating, 'recommendation': recommendation}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
