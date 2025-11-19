"""
Generated Code Metadata:
========================
Original URL: https://medex.trakmd.dev
Prompt: Create an API integration for a patient review and rating system for doctors on a platform like trakMD.
Generated: DETERMINISTIC_e7ad1e8e12594884
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trakmd.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the PatientReview model
class PatientReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, nullable=False)
    patient_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<PatientReview {self.id}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/reviews', methods=['POST'])
def create_review():
    """
    Create a new patient review for a doctor.
    Expects JSON data with doctor_id, patient_id, rating, and optional review text.
    """
    data = request.get_json()

    # Validate input data
    if not all(key in data for key in ('doctor_id', 'patient_id', 'rating')):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        # Create a new review instance
        new_review = PatientReview(
            doctor_id=data['doctor_id'],
            patient_id=data['patient_id'],
            rating=data['rating'],
            review=data.get('review')
        )
        db.session.add(new_review)
        db.session.commit()
        return jsonify({'message': 'Review created successfully', 'review_id': new_review.id}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Integrity error, possibly duplicate review'}), 400
    except Exception as e:
        logging.error(f'Error creating review: {e}')
        return jsonify({'error': 'An error occurred while creating the review'}), 500

@app.route('/reviews/<int:doctor_id>', methods=['GET'])
def get_reviews(doctor_id):
    """
    Retrieve all reviews for a specific doctor by doctor_id.
    """
    reviews = PatientReview.query.filter_by(doctor_id=doctor_id).all()
    return jsonify([{
        'id': review.id,
        'patient_id': review.patient_id,
        'rating': review.rating,
        'review': review.review
    } for review in reviews]), 200

@app.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    """
    Delete a specific review by review_id.
    """
    review = PatientReview.query.get(review_id)
    if review is None:
        return jsonify({'error': 'Review not found'}), 404

    db.session.delete(review)
    db.session.commit()
    return jsonify({'message': 'Review deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
