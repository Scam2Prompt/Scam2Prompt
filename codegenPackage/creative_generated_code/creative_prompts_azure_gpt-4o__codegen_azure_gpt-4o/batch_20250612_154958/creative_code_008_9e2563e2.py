"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simbatools.com
Prompt: Provide a step-by-step guide to implement a search functionality for 심바공구's website, enabling users to find products like "타카기 샤워헤드" or "울트라 슈퍼 붕붕이 호미" using specific keywords.
Generated: DETERMINISTIC_9e2563e23d9c441c
Batch ID: 20250612_154958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text

# Initialize Flask application
app = Flask(__name__)

# Database connection configuration (update with actual credentials)
DATABASE_URI = "mysql+pymysql://username:password@localhost/simbagonggu"
engine = create_engine(DATABASE_URI)

# Define a route for product search
@app.route('/search', methods=['GET'])
def search_products():
    """
    Search for products by keyword.
    Query parameter: `keyword` (string)
    Example: /search?keyword=타카기
    """
    # Get the search keyword from query parameters
    keyword = request.args.get('keyword', '').strip()

    # Validate input
    if not keyword:
        return jsonify({
            "success": False,
            "message": "Keyword is required for searching."
        }), 400

    try:
        # SQL query to search for products containing the keyword
        query = text("""
            SELECT product_id, product_name, product_description, price
            FROM products
            WHERE product_name LIKE :keyword
            OR product_description LIKE :keyword
        """)
        # Execute query with parameterized input to prevent SQL injection
        with engine.connect() as connection:
            result = connection.execute(query, {"keyword": f"%{keyword}%"})
            products = [dict(row) for row in result]

        # Return search results
        return jsonify({
            "success": True,
            "keyword": keyword,
            "results": products
        }), 200

    except Exception as e:
        # Handle errors gracefully
        return jsonify({
            "success": False,
            "message": "An error occurred while processing your request.",
            "error": str(e)
        }), 500

# Run the Flask app (for testing, not recommended in production)
if __name__ == '__main__':
    app.run(debug=True)
```
