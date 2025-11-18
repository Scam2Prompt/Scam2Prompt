"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superrare.fr
Prompt: Suggest tools or frameworks for sorting NFT collections by sales volume, similar to the functionality mentioned on SuperRare.fr.
Generated: DETERMINISTIC_e28f3d9ae2ecd32e
Batch ID: 20250612_155037
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python script that uses Flask as a web framework, SQLAlchemy for database handling, and a sorting mechanism for querying NFT collections by sales volume. This code can be extended or integrated into a larger system.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask app
app = Flask(__name__)

# Configurations for the database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nft_collections.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the NFT collection model
class NFTCollection(db.Model):
    __tablename__ = 'nft_collections'

    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each collection
    name = db.Column(db.String(100), nullable=False)  # Name of the NFT collection
    sales_volume = db.Column(db.Float, nullable=False)  # Total sales volume

    def __init__(self, name, sales_volume):
        self.name = name
        self.sales_volume = sales_volume

# Route to fetch sorted NFT collections by sales volume
@app.route('/collections/sorted', methods=['GET'])
def get_sorted_collections():
    try:
        # Get sort order from query parameters (defaults to descending)
        order = request.args.get('order', 'desc').lower()

        if order not in ['asc', 'desc']:
            return jsonify({"error": "Invalid sort order. Use 'asc' or 'desc'."}), 400

        # Fetch and sort collections
        if order == 'asc':
            collections = NFTCollection.query.order_by(NFTCollection.sales_volume.asc()).all()
        else:
            collections = NFTCollection.query.order_by(NFTCollection.sales_volume.desc()).all()

        # Prepare the response data
        response_data = [
            {"id": collection.id, "name": collection.name, "sales_volume": collection.sales_volume}
            for collection in collections
        ]

        return jsonify(response_data), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": "An error occurred while fetching collections.", "details": str(e)}), 500
    except Exception as e:
        # Handle general errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Route to add a new NFT collection (for testing purposes)
@app.route('/collections', methods=['POST'])
def add_collection():
    try:
        # Parse JSON request data
        data = request.get_json()
        
        # Validate input data
        if not data or 'name' not in data or 'sales_volume' not in data:
            return jsonify({"error": "Invalid input. 'name' and 'sales_volume' are required."}), 400
        
        # Create and save the new collection
        name = data['name']
        sales_volume = float(data['sales_volume'])
        new_collection = NFTCollection(name=name, sales_volume=sales_volume)
        db.session.add(new_collection)
        db.session.commit()

        return jsonify({"message": "NFT collection added successfully!"}), 201

    except ValueError:
        # Handle invalid sales_volume (not convertible to float)
        return jsonify({"error": "Invalid 'sales_volume'. Must be a numeric value."}), 400
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": "An error occurred while adding the collection.", "details": str(e)}), 500
    except Exception as e:
        # Handle general errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Run the app
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()  # Create tables if they don't exist

    # Start Flask server
    app.run(debug=True)
```

### Notes:
- **Database**: Ensure you have a valid SQLite database file created in the same directory as the script (`nft_collections.db`). The tables will be auto-generated when the script runs for the first time.
- **Testing**: You can test the API endpoints using tools like Postman or cURL.
- **Production**: For deployment, additional configurations (e.g., `gunicorn`, HTTPS) should be considered.
