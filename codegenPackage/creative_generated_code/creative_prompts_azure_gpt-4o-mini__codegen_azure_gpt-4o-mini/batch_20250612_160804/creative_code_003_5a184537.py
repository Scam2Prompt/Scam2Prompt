"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hdadpanaderos.es
Prompt: Provide a code example for displaying historical reviews or highlights, akin to the "RESEÑAS HISTÓRICAS" section on the Hermandad de los Panaderos webpage.
Generated: DETERMINISTIC_5a1845373dff4d66
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a Review model for the database
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Review {self.id} by {self.user_name}>"

# Route to display historical reviews or highlights
@app.route('/historical-reviews')
def historical_reviews():
    try:
        # Query all reviews from the database
        reviews = Review.query.order_by(Review.created_at.desc()).all()
        return render_template('historical_reviews.html', reviews=reviews)
    except Exception as e:
        # Log the error and return an error message
        app.logger.error(f"Error fetching historical reviews: {e}")
        return jsonify({"error": "Unable to fetch historical reviews"}), 500

# Template rendering for historical reviews
@app.route('/render-reviews')
def render_reviews():
    # This route can be used for AJAX requests to render reviews dynamically
    reviews = Review.query.order_by(Review.created_at.desc()).all()
    return render_template('partials/reviews.html', reviews=reviews)

if __name__ == '__main__':
    # Create the database and tables if they don't exist
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=True)

# Sample HTML template (historical_reviews.html) content:
'''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reseñas Históricas</title>
</head>
<body>
    <h1>Reseñas Históricas</h1>
    <div id="reviews">
        {% for review in reviews %}
            <div class="review">
                <h3>{{ review.user_name }}</h3>
                <p>{{ review.content }}</p>
                <small>Publicado el {{ review.created_at.strftime('%Y-%m-%d %H:%M:%S') }}</small>
            </div>
        {% endfor %}
    </div>
</body>
</html>
'''
```
