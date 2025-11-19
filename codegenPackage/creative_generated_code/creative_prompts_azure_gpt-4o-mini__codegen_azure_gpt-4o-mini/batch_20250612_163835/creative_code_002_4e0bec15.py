"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Create an API endpoint that retrieves Engel Coolers product details, including specifications for hard and soft coolers.
Generated: DETERMINISTIC_4e0bec15fb933231
Batch ID: 20250612_163835
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

# Configure database URI (replace with your actual database configuration)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///engel_coolers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define a model for Cooler products
class Cooler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(10), nullable=False)  # 'hard' or 'soft'
    capacity = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert Cooler object to dictionary format."""
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'capacity': self.capacity,
            'color': self.color,
            'price': self.price
        }

# API endpoint to retrieve Cooler product details
@app.route('/api/coolers', methods=['GET'])
def get_coolers():
    """Fetch all coolers from the database."""
    try:
        # Query the database for all coolers
        coolers = Cooler.query.all()
        # Convert query results to a list of dictionaries
        coolers_list = [cooler.to_dict() for cooler in coolers]
        return jsonify(coolers_list), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

# Error handling for not found
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Resource not found'}), 404

# Error handling for internal server errors
@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'An internal error occurred'}), 500

if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Run the application
    app.run(debug=True)  # Set to False in production
```
