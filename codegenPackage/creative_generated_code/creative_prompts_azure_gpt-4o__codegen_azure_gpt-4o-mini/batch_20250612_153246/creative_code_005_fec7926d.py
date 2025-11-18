"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://praiasdeminas.eng.br
Prompt: Write code to develop a customer feedback system that collects reviews about pool construction and renovation services, similar to the testimonials on the Praias de Minas website.
Generated: DETERMINISTIC_fec7926d87b0e238
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import re

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    review_text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Feedback {self.customer_name}, Rating: {self.rating}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to submit feedback
@app.route('/feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()

    # Validate input data
    if not all(key in data for key in ('customer_name', 'service_type', 'review_text', 'rating')):
        return jsonify({'error': 'Missing required fields'}), 400

    if not isinstance(data['rating'], int) or not (1 <= data['rating'] <= 5):
        return jsonify({'error': 'Rating must be an integer between 1 and 5'}), 400

    if not re.match("^[A-Za-z0-9 ]+$", data['customer_name']):
        return jsonify({'error': 'Invalid characters in customer name'}), 400

    # Create a new feedback entry
    new_feedback = Feedback(
        customer_name=data['customer_name'],
        service_type=data['service_type'],
        review_text=data['review_text'],
        rating=data['rating']
    )

    # Try to add the feedback to the database
    try:
        db.session.add(new_feedback)
        db.session.commit()
        return jsonify({'message': 'Feedback submitted successfully'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to submit feedback', 'details': str(e)}), 500

# Route to fetch all feedback
@app.route('/feedback', methods=['GET'])
def get_feedback():
    try:
        feedback_list = Feedback.query.all()
        feedback_data = [{'customer_name': feedback.customer_name, 'service_type': feedback.service_type,
                          'review_text': feedback.review_text, 'rating': feedback.rating} for feedback in feedback_list]
        return jsonify(feedback_data), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Failed to retrieve feedback', 'details': str(e)}), 500

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
