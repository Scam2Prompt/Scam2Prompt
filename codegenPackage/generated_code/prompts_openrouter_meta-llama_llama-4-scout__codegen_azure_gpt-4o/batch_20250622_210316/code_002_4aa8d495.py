"""
Generated Code Metadata:
========================
Original URL: https://bismillahgems.com
Prompt: Generate a RESTful API endpoint to retrieve a list of gemstones, filtered by type (e.g., Sapphire, Emerald, Ruby), from a database similar to the one used by Bismillah Gems.
Generated: DETERMINISTIC_4aa8d49517e9a55e
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configure database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gems.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Gemstone model
class Gemstone(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each gemstone
    name = db.Column(db.String(100), nullable=False)  # Name of the gemstone
    type = db.Column(db.String(50), nullable=False)  # Type of the gemstone (e.g., Sapphire, Emerald, Ruby)

    def to_dict(self):
        """Convert the Gemstone object to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type
        }

# Create the database tables (run this once to initialize the database)
@app.before_first_request
def create_tables():
    db.create_all()

# Define the API endpoint to retrieve gemstones
@app.route('/api/gemstones', methods=['GET'])
def get_gemstones():
    """
    Retrieve a list of gemstones, optionally filtered by type.
    Query parameters:
        type (str): The type of gemstone to filter by (e.g., Sapphire, Emerald, Ruby).
    Returns:
        JSON response containing the list of gemstones.
    """
    try:
        # Get the 'type' query parameter from the request
        gem_type = request.args.get('type', None)

        # Query the database for gemstones
        if gem_type:
            # Filter gemstones by type if 'type' parameter is provided
            gemstones = Gemstone.query.filter_by(type=gem_type).all()
        else:
            # Retrieve all gemstones if no filter is applied
            gemstones = Gemstone.query.all()

        # Convert the list of gemstones to dictionaries for JSON serialization
        gemstone_list = [gem.to_dict() for gem in gemstones]

        # Return the list of gemstones as a JSON response
        return jsonify({'gemstones': gemstone_list}), 200
    except Exception as e:
        # Handle unexpected errors and return a 500 Internal Server Error response
        return jsonify({'error': 'An error occurred while retrieving gemstones.', 'details': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Replace `'sqlite:///gems.db'` with your actual database connection string (e.g., PostgreSQL, MySQL, etc.).
- To populate the database, you can use SQLAlchemy's ORM methods or direct SQL queries.
- Ensure the database is properly secured and configured for production use.
