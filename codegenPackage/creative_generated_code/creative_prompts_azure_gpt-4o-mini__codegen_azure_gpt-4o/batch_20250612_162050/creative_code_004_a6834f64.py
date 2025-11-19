"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coiplusa.com.py
Prompt: Illustrate how to implement a search feature in a web app that queries the COIPLUSA database for household products like Limpaki and Life Clean.
Generated: DETERMINISTIC_a6834f64fe82bc00
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web app implementation for a search feature querying COIPLUSA database
# Ensure you have Flask and SQLAlchemy installed before running this code
# pip install flask sqlalchemy

from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Database connection configuration - replace with your actual database URI
DATABASE_URI = 'mysql+pymysql://username:password@localhost/coiplusa'
engine = create_engine(DATABASE_URI)

@app.route('/search', methods=['GET'])
def search_products():
    """
    Endpoint to search for household products in the COIPLUSA database.
    Query parameters:
    - query: The search term to look for in the product name.
    Example: GET /search?query=Limpaki
    """
    query_term = request.args.get('query', '').strip()  # Get search term from query parameter
    if not query_term:
        return jsonify({'error': 'Query parameter "query" is required.'}), 400

    try:
        # SQL query with parameterized input to prevent SQL injection
        sql_query = text("SELECT id, name, description, price FROM products WHERE name LIKE :query_term")
        # Execute query with wildcard for partial match
        with engine.connect() as connection:
            results = connection.execute(sql_query, {"query_term": f"%{query_term}%"}).fetchall()

        # Convert results to a JSON-response friendly format
        products = [
            {
                "id": row['id'],
                "name": row['name'],
                "description": row['description'],
                "price": row['price']
            }
            for row in results
        ]

        return jsonify({'products': products}), 200
    except SQLAlchemyError as e:
        # Handle database errors and return an error response
        return jsonify({'error': 'Database error occurred.', 'details': str(e)}), 500

# Run the web server
if __name__ == '__main__':
    app.run(debug=True)
```
