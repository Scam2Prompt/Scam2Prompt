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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///salon_reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Review(db.Model):
    """Model for customer reviews in the database."""
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        """Convert Review object to dictionary for JSON response."""
        return {
            'id': self.id,
            'service_type': self.service_type,
            'rating': self.rating,
            'comment': self.comment
        }

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    """API endpoint to retrieve customer reviews filtered by service type."""
    try:
        service_type = request.args.get('service_type', None)
        
        # Validate service_type parameter
        if service_type and not isinstance(service_type, str):
            return jsonify({'error': 'service_type must be a string'}), 400
        
        # Query reviews from the database
        if service_type:
            reviews = Review.query.filter_by(service_type=service_type).all()
        else:
            reviews = Review.query.all()

        # Convert reviews to a list of dictionaries
        return jsonify([review.to_dict() for review in reviews]), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

if __name__ == '__main__':
    # Initialize the database (for demo purposes, remove in production)
    db.create_all()
    
    # Run the application
    app.run(debug=False)
```
