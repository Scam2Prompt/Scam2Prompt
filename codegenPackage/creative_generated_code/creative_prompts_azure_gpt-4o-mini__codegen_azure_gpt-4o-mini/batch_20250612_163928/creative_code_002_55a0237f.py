"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debank.cz
Prompt: Create an API endpoint that returns the latest furniture collections and promotional offers from an online furniture store.
Generated: DETERMINISTIC_55a0237fcdf3e6dc
Batch ID: 20250612_163928
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
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure database connection (Change to your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///furniture_store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the FurnitureCollection model
class FurnitureCollection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    is_promotional = db.Column(db.Boolean, default=False)

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/api/latest-collections', methods=['GET'])
def get_latest_collections():
    """
    API endpoint to return the latest furniture collections and promotional offers.
    Returns:
        JSON response with a list of collections and promotional offers.
    """
    try:
        # Query for the latest furniture collections and promotional offers
        collections = FurnitureCollection.query.order_by(FurnitureCollection.id.desc()).all()
        
        # Prepare the response data
        response_data = [
            {
                'id': collection.id,
                'name': collection.name,
                'description': collection.description,
                'is_promotional': collection.is_promotional
            }
            for collection in collections
        ]
        return jsonify(response_data), 200

    except SQLAlchemyError as e:
        # Log the error and return an error response
        logging.error(f"Database error: {e}")
        return jsonify({'error': 'Database error occurred. Please try again later.'}), 500

    except Exception as e:
        # Log any other unexpected errors
        logging.error(f"Unexpected error: {e}")
        return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

Make sure to set up your database and install the required packages before running the code:
```bash
pip install Flask Flask-SQLAlchemy
```
