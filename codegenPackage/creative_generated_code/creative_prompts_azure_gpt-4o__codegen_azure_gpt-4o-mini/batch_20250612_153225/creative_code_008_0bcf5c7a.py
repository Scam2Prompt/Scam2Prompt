"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedigitalage.co.nz
Prompt: Recommend a library or API for managing client reviews on a business website, and provide example code for displaying and filtering reviews dynamically.
Generated: DETERMINISTIC_0bcf5c7ad7d31406
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy part of the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Review model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Review {self.client_name}, Rating: {self.rating}>'

# Route to display all reviews
@app.route('/reviews', methods=['GET'])
def get_reviews():
    try:
        reviews = Review.query.all()
        return jsonify([{'client_name': r.client_name, 'rating': r.rating, 'comment': r.comment} for r in reviews])
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Route to filter reviews by rating
@app.route('/reviews/filter', methods=['GET'])
def filter_reviews():
    rating = request.args.get('rating', type=int)
    if rating is None:
        return jsonify({'error': 'Rating parameter is required'}), 400

    try:
        filtered_reviews = Review.query.filter_by(rating=rating).all()
        return jsonify([{'client_name': r.client_name, 'rating': r.rating, 'comment': r.comment} for r in filtered_reviews])
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Route to add a new review
@app.route('/reviews', methods=['POST'])
def add_review():
    data = request.get_json()

    if not data or 'client_name' not in data or 'rating' not in data:
        return jsonify({'error': 'Invalid input, client name and rating are required'}), 400

    new_review = Review(client_name=data['client_name'], rating=data['rating'], comment=data.get('comment'))

    try:
        db.session.add(new_review)
        db.session.commit()
        return jsonify({'message': 'Review added successfully!'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Initialize the database (only needed once)
@app.before_first_request
def create_tables():
    db.create_all()

# Main function to run the app
if __name__ == '__main__':
    app.run(debug=True)
```

### Usage
1. Install the required packages:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Use the endpoints `/reviews`, `/reviews/filter?rating=<rating>` to manage and retrieve reviews.
