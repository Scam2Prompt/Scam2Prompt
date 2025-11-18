"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://leprettystellar.com
Prompt: Suggest an API for managing product reviews and ratings on an e-commerce platform, ensuring compatibility with categories like "Health & Beauty" and "Automotive."
Generated: DETERMINISTIC_507af7d40d49f7a7
Batch ID: 20250612_155102
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
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the ProductReview model
class ProductReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review_text = db.Column(db.String(500), nullable=True)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Review {self.id}>'

# Define the schema for validation using Marshmallow
class ProductReviewSchema(Schema):
    product_id = fields.Int(required=True)
    rating = fields.Float(required=True)
    review_text = fields.Str(required=False)
    category = fields.Str(required=True)

# Initialize the schema
review_schema = ProductReviewSchema()
reviews_schema = ProductReviewSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to add a new review
@app.route('/reviews', methods=['POST'])
def add_review():
    try:
        # Validate incoming data
        data = request.get_json()
        review = review_schema.load(data)

        # Check if category is valid
        if review['category'] not in ["Health & Beauty", "Automotive"]:
            return jsonify({"error": "Invalid category. Must be either 'Health & Beauty' or 'Automotive'."}), 400
        
        # Create a new review
        new_review = ProductReview(**review)
        db.session.add(new_review)
        db.session.commit()
        
        return jsonify(review_schema.dump(new_review)), 201
    
    except ValidationError as ve:
        return jsonify(ve.messages), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# API endpoint to get all reviews
@app.route('/reviews', methods=['GET'])
def get_reviews():
    try:
        reviews = ProductReview.query.all()
        return jsonify(reviews_schema.dump(reviews)), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get reviews by category
@app.route('/reviews/category/<string:category>', methods=['GET'])
def get_reviews_by_category(category):
    try:
        if category not in ["Health & Beauty", "Automotive"]:
            return jsonify({"error": "Invalid category. Must be either 'Health & Beauty' or 'Automotive'."}), 400
        
        reviews = ProductReview.query.filter_by(category=category).all()
        return jsonify(reviews_schema.dump(reviews)), 200
    
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
