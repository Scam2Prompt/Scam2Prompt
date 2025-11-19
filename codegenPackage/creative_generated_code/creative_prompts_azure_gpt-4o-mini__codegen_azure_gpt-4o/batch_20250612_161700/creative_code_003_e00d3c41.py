"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karlakarita.com.br
Prompt: Create an API endpoint in Python that retrieves special sales items from an e-commerce database, similar to the deals highlighted on karlakarita.com.br.
Generated: DETERMINISTIC_e00d3c4143b15eb2
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text
import os

app = Flask(__name__)

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///ecommerce.db")  # Replace with your actual database URL
engine = create_engine(DATABASE_URL)

@app.route('/api/special-sales', methods=['GET'])
def get_special_sales():
    """
    API endpoint to retrieve special sales items from the database.
    Returns a JSON response with the list of items.
    """
    try:
        # Define the SQL query to fetch special sales items
        query = text("""
            SELECT id, name, description, price, discount_percentage, image_url 
            FROM products 
            WHERE is_on_sale = 1
            ORDER BY discount_percentage DESC
        """)

        # Execute the query
        with engine.connect() as connection:
            result = connection.execute(query)
            items = [
                {
                    "id": row["id"],
                    "name": row["name"],
                    "description": row["description"],
                    "price": float(row["price"]),
                    "discount_percentage": float(row["discount_percentage"]),
                    "image_url": row["image_url"]
                }
                for row in result
            ]

        # Return the items as a JSON response
        return jsonify({"success": True, "special_sales": items}), 200

    except Exception as e:
        # Catch any errors and return a failure response
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
1. Replace the `DATABASE_URL` environment variable with your actual database URL or connection string.
2. Ensure you have `Flask` and `SQLAlchemy` installed (`pip install flask sqlalchemy`).
3. This code assumes your database has a `products` table with columns matching the query (`id`, `name`, `description`, `price`, `discount_percentage`, `image_url`, `is_on_sale`).
4. Run this script in an environment where the database is accessible and configured correctly.
