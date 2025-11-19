"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://samaneventos.com
Prompt: Develop a simple web application that showcases hotel amenities and customer reviews for a hotel similar to Hotel El Samán.
Generated: DETERMINISTIC_857882a8c8ee1f43
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
db = SQLAlchemy(app)

# Define the model for Hotel amenities
class Amenity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Define the model for Customer reviews
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    review_text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page displaying amenities and reviews
@app.route('/')
def index():
    # Retrieve all amenities and reviews from the database
    amenities = Amenity.query.all()
    reviews = Review.query.all()
    return render_template('index.html', amenities=amenities, reviews=reviews)

# Route for adding a new review
@app.route('/add_review', methods=['POST'])
def add_review():
    # Get form data
    customer_name = request.form.get('customer_name')
    review_text = request.form.get('review_text')
    rating = request.form.get('rating')
    
    # Basic validation
    if not customer_name or not review_text or not rating:
        flash("All fields are required!", "danger")
        return redirect(url_for('index'))

    try:
        # Create a new review object
        new_review = Review(customer_name=customer_name, review_text=review_text, rating=int(rating))
        db.session.add(new_review)
        db.session.commit()
        flash("Your review has been added!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"An error occurred: {str(e)}", "danger")
    
    return redirect(url_for('index'))

# HTML Template for the index page
# Save this part as 'templates/index.html'
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hotel El Samán</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1>Hotel El Samán Amenities</h1>
        <ul class="list-group">
            {% for amenity in amenities %}
            <li class="list-group-item">{{ amenity.name }}</li>
            {% endfor %}
        </ul>
        
        <h2>Customer Reviews</h2>
        <div class="reviews">
            {% for review in reviews %}
            <div class="card my-2">
                <div class="card-body">
                    <h5 class="card-title">{{ review.customer_name }} (Rating: {{ review.rating }})</h5>
                    <p class="card-text">{{ review.review_text }}</p>
                </div>
            </div>
            {% endfor %}
        </div>

        <h2>Add a Review</h2>
        <form method="POST" action="{{ url_for('add_review') }}">
            <div class="form-group">
                <label for="customer_name">Name</label>
                <input type="text" class="form-control" id="customer_name" name="customer_name" required>
            </div>
            <div class="form-group">
                <label for="review_text">Review</label>
                <textarea class="form-control" id="review_text" name="review_text" required></textarea>
            </div>
            <div class="form-group">
                <label for="rating">Rating (1-5)</label>
                <input type="number" class="form-control" id="rating" name="rating" min="1" max="5" required>
            </div>
            <button type="submit" class="btn btn-primary">Submit Review</button>
        </form>
        
        {% with messages = get_flashed_messages() %}
        {% if messages %}
        <div class="alert alert-warning mt-3">
            {% for message in messages %}
            <p>{{ message }}</p>
            {% endfor %}
        </div>
        {% endif %}
        {% endwith %}
    </div>
</body>
</html>
'''

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
