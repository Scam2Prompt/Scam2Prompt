"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morevacare.com
Prompt: Recommend a library or API for implementing a "pre-order with discount" feature, similar to the one offered on MorevaCare, for an e-commerce site.
Generated: DETERMINISTIC_4fb2b650c2e83954
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script implements a "pre-order with discount" feature for an e-commerce site.
It uses the Flask framework for the web server and integrates SQLite as the database
to manage pre-orders and apply discounts. This code is production-ready and can be
easily adapted or scaled for larger systems with more sophisticated databases like PostgreSQL.
"""

from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Database setup
DATABASE = 'ecommerce.db'


def create_tables():
    """Create necessary tables in the database if they don't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pre_orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            product_id INTEGER NOT NULL,
            original_price REAL NOT NULL,
            discounted_price REAL NOT NULL,
            pre_order_date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


create_tables()  # Ensure tables are created on application start


def calculate_discount(price, discount_percentage):
    """
    Calculate the discounted price based on the given discount percentage.
    :param price: Original price of the product.
    :param discount_percentage: Discount percentage to apply.
    :return: Discounted price.
    """
    try:
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")
        return round(price - (price * (discount_percentage / 100)), 2)
    except Exception as e:
        raise ValueError(f"Error calculating discount: {e}")


@app.route('/pre_order', methods=['POST'])
def pre_order():
    """
    Endpoint for creating a pre-order.
    Expects JSON payload with 'customer_name', 'product_id', 'original_price', and 'discount_percentage'.
    """
    try:
        data = request.json

        # Validate incoming data
        if not all(key in data for key in ['customer_name', 'product_id', 'original_price', 'discount_percentage']):
            return jsonify({'error': 'Missing required fields'}), 400

        customer_name = data['customer_name']
        product_id = data['product_id']
        original_price = float(data['original_price'])
        discount_percentage = float(data['discount_percentage'])

        if original_price <= 0:
            return jsonify({'error': 'Original price must be greater than 0'}), 400

        discounted_price = calculate_discount(original_price, discount_percentage)
        pre_order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Save pre-order to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO pre_orders (customer_name, product_id, original_price, discounted_price, pre_order_date)
            VALUES (?, ?, ?, ?, ?)
        """, (customer_name, product_id, original_price, discounted_price, pre_order_date))
        conn.commit()
        conn.close()

        return jsonify({
            'message': 'Pre-order created successfully',
            'pre_order': {
                'customer_name': customer_name,
                'product_id': product_id,
                'original_price': original_price,
                'discounted_price': discounted_price,
                'pre_order_date': pre_order_date
            }
        }), 201

    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': f"An unexpected error occurred: {e}"}), 500


@app.route('/pre_orders', methods=['GET'])
def list_pre_orders():
    """
    Endpoint for retrieving all pre-orders.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pre_orders")
        pre_orders = cursor.fetchall()
        conn.close()

        # Format pre-orders data as a list of dictionaries
        pre_orders_list = [
            {
                "id": row[0],
                "customer_name": row[1],
                "product_id": row[2],
                "original_price": row[3],
                "discounted_price": row[4],
                "pre_order_date": row[5]
            } for row in pre_orders
        ]

        return jsonify(pre_orders_list), 200

    except Exception as e:
        return jsonify({'error': f"An unexpected error occurred: {e}"}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
