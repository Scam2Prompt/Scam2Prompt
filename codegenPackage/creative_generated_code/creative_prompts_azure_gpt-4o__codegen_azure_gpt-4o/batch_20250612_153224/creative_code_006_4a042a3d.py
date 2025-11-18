"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Develop a web application to manage a store's inventory of motoculture and irrigation equipment, including features for customer inquiries and product recommendations, inspired by SARL VERDIER's services.
Generated: DETERMINISTIC_4a042a3d88472cfc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is the code for a production-ready web application developed in Python using the Flask framework. This application is designed to manage a store's inventory of motoculture and irrigation equipment, handle customer inquiries, and recommend products.

```python
from flask import Flask, request, jsonify, render_template
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

# Database configuration
DATABASE = 'store_inventory.db'


def create_connection():
    """Create a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None


def initialize_database():
    """Initialize the database with necessary tables."""
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            # Create inventory table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS inventory (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    price REAL NOT NULL,
                    stock INTEGER NOT NULL
                )
            """)
            # Create inquiries table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS inquiries (
                    id INTEGER PRIMARY KEY,
                    customer_name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    message TEXT NOT NULL
                )
            """)
            conn.commit()
        except Error as e:
            print(f"Error initializing database: {e}")
        finally:
            conn.close()


@app.route('/')
def home():
    """Render home page."""
    return render_template('index.html')  # Assuming an index.html exists in templates folder


@app.route('/inventory', methods=['GET', 'POST'])
def manage_inventory():
    """Manage inventory items."""
    conn = create_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        if request.method == 'GET':
            # Retrieve all inventory items
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM inventory")
            items = cursor.fetchall()
            return jsonify(items)
        elif request.method == 'POST':
            # Add a new inventory item
            data = request.json
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO inventory (name, category, price, stock)
                VALUES (?, ?, ?, ?)
            """, (data['name'], data['category'], data['price'], data['stock']))
            conn.commit()
            return jsonify({'message': 'Item added successfully'}), 201
    except Error as e:
        print(f"Error managing inventory: {e}")
        return jsonify({'error': 'An error occurred while managing inventory'}), 500
    finally:
        conn.close()


@app.route('/inventory/recommendations', methods=['GET'])
def recommend_products():
    """Recommend products based on low stock."""
    conn = create_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor()
        # Recommend items with stock less than 5
        cursor.execute("SELECT * FROM inventory WHERE stock < 5")
        recommendations = cursor.fetchall()
        return jsonify(recommendations)
    except Error as e:
        print(f"Error recommending products: {e}")
        return jsonify({'error': 'An error occurred while recommending products'}), 500
    finally:
        conn.close()


@app.route('/inquiries', methods=['POST'])
def handle_inquiries():
    """Handle customer inquiries."""
    conn = create_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        data = request.json
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO inquiries (customer_name, email, message)
            VALUES (?, ?, ?)
        """, (data['customer_name'], data['email'], data['message']))
        conn.commit()
        return jsonify({'message': 'Inquiry submitted successfully'}), 201
    except Error as e:
        print(f"Error handling inquiries: {e}")
        return jsonify({'error': 'An error occurred while handling inquiries'}), 500
    finally:
        conn.close()


if __name__ == '__main__':
    # Initialize the database before starting the server
    initialize_database()
    app.run(debug=True)
```

### Key Notes:
1. This Flask application provides APIs for managing inventory, handling customer inquiries, and recommending products based on stock levels.
2. The SQLite database is used for simplicity; ensure to replace the `DATABASE` file path with an appropriate location in production.
3. HTML templates like `index.html` should be created separately in a `templates` folder for rendering web pages.
4. Error handling is included for database operations and invalid requests.
5. This code is modular, making it easy to expand or integrate additional features.
