"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpastay.com
Prompt: Develop a REST API call in Python to fetch the amenities offered by City Prime Apartments, such as free Wi-Fi and smart TVs.
Generated: DETERMINISTIC_5d06b5fdfff90756
Batch ID: 20250612_161353
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

# Configuration for the database (replace with your database URL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///city_prime_apartments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Model representing the amenities offered by the City Prime Apartments
class Amenity(db.Model):
    __tablename__ = 'amenities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert the Amenity object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name
        }

# Route to fetch all amenities
@app.route('/api/amenities', methods=['GET'])
def get_amenities():
    try:
        amenities = Amenity.query.all()  # Query all amenities from the database
        return jsonify([amenity.to_dict() for amenity in amenities]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": str(e)}), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found."}), 404

# Error handler for other exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle generic exceptions."""
    return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Create the database and tables if they don't exist
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=True)  # Change to False in production
```
