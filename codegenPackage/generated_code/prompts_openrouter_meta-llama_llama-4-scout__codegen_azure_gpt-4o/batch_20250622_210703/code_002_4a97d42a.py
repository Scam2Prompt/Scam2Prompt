"""
Generated Code Metadata:
========================
Original URL: https://abiliatrading.co.za
Prompt: "Generate a code snippet for a simple online auction system with categories for engineering assets, office equipment, and vehicles, using a database like MySQL."
Generated: DETERMINISTIC_4a97d42ad0ea9964
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

# Initialize Flask app
app = Flask(__name__)

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',
    'database': 'auction_db'
}

# Establish database connection
def create_db_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Route: Add a new auction item
@app.route('/add_item', methods=['POST'])
def add_item():
    """
    Endpoint to add a new auction item.
    Expects JSON payload with 'name', 'category', 'starting_price', and 'description'.
    """
    data = request.json
    name = data.get('name')
    category = data.get('category')
    starting_price = data.get('starting_price')
    description = data.get('description')

    # Validate input
    if not name or not category or not starting_price:
        return jsonify({'error': 'Missing required fields'}), 400

    # Validate category
    valid_categories = ['Engineering Assets', 'Office Equipment', 'Vehicles']
    if category not in valid_categories:
        return jsonify({'error': f'Invalid category. Valid categories are: {valid_categories}'}), 400

    try:
        connection = create_db_connection()
        if connection:
            cursor = connection.cursor()
            query = """
                INSERT INTO auction_items (name, category, starting_price, description)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (name, category, starting_price, description))
            connection.commit()
            return jsonify({'message': 'Item added successfully'}), 201
    except Error as e:
        return jsonify({'error': f'Database error: {e}'}), 500
    finally:
        if connection and connection.is_connected():
            connection.close()

# Route: Get all auction items
@app.route('/items', methods=['GET'])
def get_items():
    """
    Endpoint to retrieve all auction items.
    """
    try:
        connection = create_db_connection()
        if connection:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM auction_items"
            cursor.execute(query)
            items = cursor.fetchall()
            return jsonify(items), 200
    except Error as e:
        return jsonify({'error': f'Database error: {e}'}), 500
    finally:
        if connection and connection.is_connected():
            connection.close()

# Route: Get items by category
@app.route('/items/<category>', methods=['GET'])
def get_items_by_category(category):
    """
    Endpoint to retrieve auction items by category.
    """
    valid_categories = ['Engineering Assets', 'Office Equipment', 'Vehicles']
    if category not in valid_categories:
        return jsonify({'error': f'Invalid category. Valid categories are: {valid_categories}'}), 400

    try:
        connection = create_db_connection()
        if connection:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM auction_items WHERE category = %s"
            cursor.execute(query, (category,))
            items = cursor.fetchall()
            return jsonify(items), 200
    except Error as e:
        return jsonify({'error': f'Database error: {e}'}), 500
    finally:
        if connection and connection.is_connected():
            connection.close()

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

### SQL Schema for MySQL Database
```sql
CREATE DATABASE auction_db;

USE auction_db;

CREATE TABLE auction_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category ENUM('Engineering Assets', 'Office Equipment', 'Vehicles') NOT NULL,
    starting_price DECIMAL(10, 2) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Notes:
- Replace `your_password` in the `DB_CONFIG` dictionary with your actual MySQL password.
- Ensure MySQL is running and the database/schema is created before running the Flask application.
