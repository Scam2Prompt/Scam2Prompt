"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://biamtechintl.com
Prompt: Illustrate how to implement a search feature in a web app that queries BIAM Tech's database for specific surgical kits and displays the results.
Generated: DETERMINISTIC_53a41ad2cdd966b0
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text
import os

app = Flask(__name__)

# Database configuration (update according to your environment)
DB_CONNECTION_STRING = os.getenv('DB_CONNECTION_STRING', 'mysql+pymysql://username:password@hostname/dbname')

# Initialize database connection
engine = create_engine(DB_CONNECTION_STRING)

@app.route('/search', methods=['GET'])
def search_surgical_kits():
    """
    Endpoint to search for surgical kits in BIAM Tech's database.
    Query parameters:
    - query: The search keyword for surgical kits.
    Returns:
    - A JSON response containing the search results.
    """
    try:
        # Retrieve the search keyword from query parameters
        search_query = request.args.get('query', '').strip()
        
        if not search_query:
            # Return a bad request response if no query is provided
            return jsonify({"error": "Search query is required"}), 400

        # Prepare the SQL query with parameterized input to prevent SQL injection
        sql = text("""
            SELECT kit_id, kit_name, description, price 
            FROM surgical_kits 
            WHERE kit_name LIKE :search OR description LIKE :search
        """)
        # Execute the query, safely injecting the search term
        with engine.connect() as connection:
            result = connection.execute(sql, search=f"%{search_query}%").fetchall()

        # Format the database results into a JSON-friendly structure
        kits = [
            {
                "kit_id": row["kit_id"],
                "kit_name": row["kit_name"],
                "description": row["description"],
                "price": row["price"]
            }
            for row in result
        ]

        # Return the results
        return jsonify({"results": kits}), 200

    except Exception as e:
        # Log the error (production-ready applications should use logging frameworks)
        print(f"Error occurred: {e}")
        # Return a server error response
        return jsonify({"error": "An error occurred while processing your request"}), 500


if __name__ == '__main__':
    # Start the Flask application in debug mode (use production mode for production deployment)
    app.run(debug=True)
```

### Notes:
- Replace `DB_CONNECTION_STRING` with your actual database connection details.
- Ensure proper database permissions and configurations for production use.
- Use environment variables for sensitive information such as database credentials.
- Consider using a logging library for detailed error logging in production systems.
