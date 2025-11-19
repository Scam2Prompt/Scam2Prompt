"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://japkasai.net
Prompt: Create an API endpoint that retrieves customer reviews for a men's grooming salon, ensuring it filters by service type (e.g., massage, hair removal) and includes ratings and comments.
Generated: DETERMINISTIC_ee27225b26a9b42a
Batch ID: 20250612_164151
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

app = Flask(__name__)

# Configure the database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Review model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(50), nullable=False)  # Type of service (e.g., massage, hair removal)
    rating = db.Column(db.Integer, nullable=False)          # Rating out of 5
    comment = db.Column(db.String(200), nullable=True)      # User comment

# Create the database tables (run once to initialize the database)
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to retrieve filtered customer reviews
@app.route('/reviews', methods=['GET'])
def get_reviews():
    """
    Endpoint to retrieve customer reviews filtered by service type.
    Parameters (query string):
    - service_type: Type of service to filter by (e.g., massage, hair removal).
    Returns:
        JSON: List of reviews with their ratings and comments.
    """
    try:
        # Get the service_type from query parameters
        service_type = request.args.get('service_type')
        
        # If no service_type is provided, return a bad request error
        if not service_type:
            return jsonify({"error": "Missing 'service_type' query parameter"}), 400

        # Query the database for reviews matching the service_type
        reviews = Review.query.filter_by(service_type=service_type).all()

        # Convert the reviews to a list of dictionaries for JSON serialization
        reviews_list = [
            {"id": review.id, "service_type": review.service_type, "rating": review.rating, "comment": review.comment}
            for review in reviews
        ]

        # Return the filtered reviews
        return jsonify({"reviews": reviews_list}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
