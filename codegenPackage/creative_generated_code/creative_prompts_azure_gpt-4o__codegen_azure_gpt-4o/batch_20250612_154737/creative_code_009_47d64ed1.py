"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grants-archive-cf.webflow.io
Prompt: Develop a REST API endpoint to fetch Gitcoin Grants round data, including funding and grantee details, from a database populated using the Gitcoin Grants Archive.
Generated: DETERMINISTIC_47d64ed15e5cbcd7
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask app
app = Flask(__name__)

# Database configuration
DATABASE_URI = "sqlite:///gitcoin_grants.db"  # Replace with your actual database URI
engine = create_engine(DATABASE_URI)

# Utility function to execute database queries safely
def execute_query(query, params=None):
    """
    Executes a database query and handles errors.
    :param query: SQL query string
    :param params: Parameters for the query (optional)
    :return: Query results or None in case of failure
    """
    try:
        with engine.connect() as connection:
            result = connection.execute(text(query), params or {})
            return result.fetchall()
    except SQLAlchemyError as e:
        app.logger.error(f"Database error: {e}")
        return None

# Endpoint to fetch Gitcoin Grants round data
@app.route('/gitcoin-grants/round/<round_id>', methods=['GET'])
def get_gitcoin_grants_round(round_id):
    """
    Fetch details of a specific Gitcoin Grants round, including 
    funding and grantee information.
    :param round_id: ID of the grants round
    :return: JSON response with the grants round data
    """
    try:
        # Validate input
        if not round_id.isdigit():
            abort(400, description="Round ID must be a numeric value")
        
        # Fetch grants round data from the database
        grants_round_query = """
        SELECT 
            gr.id AS grant_id,
            gr.name AS grant_name,
            gr.funding AS grant_funding,
            g.name AS grantee_name
        FROM 
            grants_rounds gr
        JOIN 
            grantees g 
        ON 
            gr.grantee_id = g.id
        WHERE 
            gr.round_id = :round_id
        """
        grants_round_data = execute_query(grants_round_query, {"round_id": round_id})
        
        # Handle case where no data is found
        if not grants_round_data:
            abort(404, description="No data found for the specified round ID")
        
        # Format response data
        response_data = [
            {
                "grant_id": row["grant_id"],
                "grant_name": row["grant_name"],
                "grant_funding": row["grant_funding"],
                "grantee_name": row["grantee_name"]
            }
            for row in grants_round_data
        ]
        
        return jsonify({"round_id": round_id, "grants": response_data})

    except Exception as e:
        app.logger.error(f"Unexpected error: {e}")
        abort(500, description="Internal server error")

# Error handlers
@app.errorhandler(400)
def bad_request(error):
    """Handles 400 Bad Request errors."""
    return jsonify({"error": "Bad Request", "message": error.description}), 400

@app.errorhandler(404)
def not_found(error):
    """Handles 404 Not Found errors."""
    return jsonify({"error": "Not Found", "message": error.description}), 404

@app.errorhandler(500)
def internal_server_error(error):
    """Handles 500 Internal Server errors."""
    return jsonify({"error": "Internal Server Error", "message": error.description}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)  # Set debug=False in production
```
