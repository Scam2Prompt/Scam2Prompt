"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://energiakert.com
Prompt: Develop a RESTful API endpoint that allows users to retrieve exclusive offers and promotions similar to those found on EnergiaKert.
Generated: DETERMINISTIC_119cea2c8bc564a2
Batch ID: 20250612_155446
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

# Initialize Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///offers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Offer model
class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    discount_percentage = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert Offer model to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'discount_percentage': self.discount_percentage
        }

# Create the database and tables
with app.app_context():
    db.create_all()

# API Endpoint to retrieve exclusive offers
@app.route('/api/offers', methods=['GET'])
def get_offers():
    """Retrieve all exclusive offers."""
    try:
        # Query all offers from the database
        offers = Offer.query.all()
        return jsonify([offer.to_dict() for offer in offers]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

# Error handling for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    """Return a custom 404 error message."""
    return jsonify({'error': 'Resource not found'}), 404

# Error handling for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """Return a custom 500 error message."""
    return jsonify({'error': 'Internal server error'}), 500

# Main entry point
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```
