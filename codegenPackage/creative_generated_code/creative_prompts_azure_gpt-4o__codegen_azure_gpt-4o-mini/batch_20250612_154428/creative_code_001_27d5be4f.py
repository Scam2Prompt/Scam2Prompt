"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momspg.com
Prompt: Develop a REST API using Flask that allows users to search for PG accommodations by location, room type (single, double, triple), and price range, similar to the features offered by Moms PG.
Generated: DETERMINISTIC_27d5be4fddeacccf
Batch ID: 20250612_154428
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

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pg_accommodations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the PG Accommodation model
class PGAccommodation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    room_type = db.Column(db.String(10), nullable=False)  # e.g., 'single', 'double', 'triple'
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the PGAccommodation object to a dictionary."""
        return {
            'id': self.id,
            'location': self.location,
            'room_type': self.room_type,
            'price': self.price
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/search', methods=['GET'])
def search_pg_accommodations():
    """
    Search for PG accommodations by location, room type, and price range.
    
    Query Parameters:
    - location: str, the location to search
    - room_type: str, the type of room (single, double, triple)
    - min_price: float, optional minimum price
    - max_price: float, optional maximum price
    
    Returns:
    - JSON list of matching PG accommodations
    """
    try:
        # Get query parameters
        location = request.args.get('location')
        room_type = request.args.get('room_type')
        min_price = request.args.get('min_price', type=float)
        max_price = request.args.get('max_price', type=float)

        # Build the query
        query = PGAccommodation.query

        # Filter by location
        if location:
            query = query.filter(PGAccommodation.location.ilike(f'%{location}%'))

        # Filter by room type
        if room_type in ['single', 'double', 'triple']:
            query = query.filter(PGAccommodation.room_type == room_type)

        # Filter by price range
        if min_price is not None:
            query = query.filter(PGAccommodation.price >= min_price)
        if max_price is not None:
            query = query.filter(PGAccommodation.price <= max_price)

        # Execute the query and get results
        results = query.all()

        # Convert results to dictionary format
        accommodations = [accommodation.to_dict() for accommodation in results]

        return jsonify(accommodations), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
