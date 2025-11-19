"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magiceden-ww.blogspot.com
Prompt: Create an API endpoint that retrieves the latest nail polish collections and their prices, similar to the "Lançamentos" section on the aquarelaesmalte blog.
Generated: DETERMINISTIC_b921561cf85f749d
Batch ID: 20250612_164310
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
from datetime import datetime

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nail_polish_collections.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Nail Polish Collection
class NailPolishCollection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    release_date = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'release_date': self.release_date.isoformat()  # Convert date to ISO format
        }

# Create the database and table if they don't exist
with app.app_context():
    db.create_all()

@app.route('/api/nail_polish_collections', methods=['GET'])
def get_latest_collections():
    """
    Retrieve the latest nail polish collections sorted by release date.
    Returns a JSON response with the collection details.
    """
    try:
        # Fetch collections sorted by release date in descending order
        collections = NailPolishCollection.query.order_by(NailPolishCollection.release_date.desc()).all()

        # Convert collections to a list of dictionaries
        collections_list = [collection.to_dict() for collection in collections]

        return jsonify(collections_list), 200  # Return status 200 for successful request

    except Exception as e:
        # Log error and return an internal server error
        app.logger.error(f"Error fetching collections: {str(e)}")
        return jsonify({"error": "An error occurred while fetching collections."}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for development, should be False in production
```
