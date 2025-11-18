"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suzuki-capital.com
Prompt: Create an API endpoint in Flask to retrieve customer reviews for Suzuki Capital Motors' sales and after-sales services, based on the testimonials provided on the website.
Generated: DETERMINISTIC_698597294a4d2fbd
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Define the Review model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    testimonial = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Review {self.customer_name}, {self.service_type}>'

# Create a schema for serializing / deserializing Review objects
class ReviewSchema(Schema):
    id = fields.Int()
    customer_name = fields.Str(required=True)
    service_type = fields.Str(required=True)
    testimonial = fields.Str(required=True)

# Initialize the review schema
review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)

# Error handler for HTTP exceptions
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": str(error)}), 400

# API endpoint to retrieve customer reviews
@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    """
    Get all customer reviews for Suzuki Capital Motors' services.
    
    Query parameters:
    - service_type (optional): Filter reviews by service type (sales or after-sales).
    
    Returns:
    - JSON containing a list of reviews.
    """
    try:
        service_type = request.args.get('service_type')
        
        if service_type:
            reviews = Review.query.filter_by(service_type=service_type).all()
        else:
            reviews = Review.query.all()

        return reviews_schema.dump(reviews), 200

    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving reviews.", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=False)  # Set debug to False for production
```
