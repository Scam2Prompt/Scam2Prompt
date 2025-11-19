"""
Generated Code Metadata:
========================
Original URL: https://www.gmpinvestments.co.uk
Prompt: Create a RESTful API endpoint that accepts user input (e.g., property type, location) and returns a list of properties that match the criteria, using a database that is familiar with local and regional planning policies.
Generated: DETERMINISTIC_3232ab8df15d3842
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text
import os

app = Flask(__name__)

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///properties.db")  # Replace with your database URL
engine = create_engine(DATABASE_URL)

# Error messages
ERROR_INVALID_INPUT = "Invalid input. Please provide valid property type and location."
ERROR_DATABASE_CONNECTION = "Unable to connect to the database. Please try again later."

@app.route('/api/properties', methods=['GET'])
def get_properties():
    """
    RESTful API endpoint to fetch properties based on user input.
    Query parameters:
        - property_type: Type of property (e.g., 'residential', 'commercial')
        - location: Location of the property (e.g., 'New York', 'Los Angeles')
    Returns:
        - JSON response containing a list of matching properties.
    """
    try:
        # Get query parameters
        property_type = request.args.get('property_type')
        location = request.args.get('location')

        # Validate input
        if not property_type or not location:
            return jsonify({"error": ERROR_INVALID_INPUT}), 400

        # Query the database
        query = text("""
            SELECT id, name, property_type, location, price, description
            FROM properties
            WHERE property_type = :property_type AND location = :location
        """)
        with engine.connect() as connection:
            result = connection.execute(query, {"property_type": property_type, "location": location})
            properties = [dict(row) for row in result]

        # Return the results
        return jsonify({"properties": properties}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": ERROR_DATABASE_CONNECTION, "details": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
- Replace `sqlite:///properties.db` with your actual database connection string.
- Ensure the `properties` table exists in your database with appropriate columns (`id`, `name`, `property_type`, `location`, `price`, `description`).
- Install required dependencies (`Flask`, `SQLAlchemy`) using `pip install flask sqlalchemy`.
- Set the `DATABASE_URL` environment variable for production use.
