"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perez-3-jennifer-89.pages.dev
Prompt: How can I create an API endpoint that retrieves promotional offers specifically for best friends?
Generated: DETERMINISTIC_a521b57d5dff54d3
Batch ID: 20250612_155140
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy part of the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///promotions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for promotional offers
class PromotionalOffer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    is_best_friend_offer = db.Column(db.Boolean, default=False)

    def to_dict(self):
        """Convert the PromotionalOffer object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'is_best_friend_offer': self.is_best_friend_offer
        }

# Create the database
@app.before_first_request
def create_tables():
    """Create database tables if they don't exist."""
    db.create_all()

@app.route('/api/promotions/best-friends', methods=['GET'])
def get_best_friend_promotions():
    """
    API endpoint to retrieve promotional offers specifically for best friends.
    
    Returns:
        JSON response containing a list of promotional offers for best friends.
    """
    try:
        # Query the database for best friend promotions
        best_friend_offers = PromotionalOffer.query.filter_by(is_best_friend_offer=True).all()
        
        # Convert the offers to a list of dictionaries
        offers_list = [offer.to_dict() for offer in best_friend_offers]
        
        # Return the offers as a JSON response
        return jsonify(offers_list), 200
    
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': 'An error occurred while retrieving promotions.', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
