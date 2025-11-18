"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drivemiami.com
Prompt: Develop a feature for a dealership website to offer coupons and sales incentives to customers, as outlined in DriveCities Membership benefits.
Generated: DETERMINISTIC_b84a2a903dd0ed8a
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a Python implementation for the requested feature using Flask as the web framework and SQLite for the database.

```python
# dealership_coupons.py
from flask import Flask, jsonify, request
import sqlite3
import os

# Initialize the Flask application
app = Flask(__name__)

# Database file name
DB_FILE = 'dealership.db'

# Ensure the database exists
if not os.path.exists(DB_FILE):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE coupons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            discount_percentage INTEGER NOT NULL,
            expiration_date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Helper function to connect to the database
def get_db_connection():
    return sqlite3.connect(DB_FILE)

# Route to get all available coupons
@app.route('/api/coupons', methods=['GET'])
def get_coupons():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coupons WHERE expiration_date >= DATE('now')")
        coupons = cursor.fetchall()
        conn.close()
        
        # Return the coupons list as JSON
        return jsonify({'coupons': [
            {'id': coupon[0], 'name': coupon[1], 'description': coupon[2],
             'discount_percentage': coupon[3], 'expiration_date': coupon[4]}
            for coupon in coupons
        ]}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to fetch coupons', 'details': str(e)}), 500

# Route to add a new coupon (Admin feature)
@app.route('/api/coupons', methods=['POST'])
def create_coupon():
    try:
        data = request.json
        name = data.get('name')
        description = data.get('description')
        discount_percentage = data.get('discount_percentage')
        expiration_date = data.get('expiration_date')
        
        # Validate inputs
        if not all([name, description, discount_percentage, expiration_date]):
            return jsonify({'error': 'Missing required fields'}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO coupons (name, description, discount_percentage, expiration_date)
            VALUES (?, ?, ?, ?)
        """, (name, description, discount_percentage, expiration_date))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Coupon added successfully'}), 201
    except Exception as e:
        return jsonify({'error': 'Failed to create coupon', 'details': str(e)}), 500

# Route to delete an expired coupon (Admin feature)
@app.route('/api/coupons/<int:coupon_id>', methods=['DELETE'])
def delete_coupon(coupon_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM coupons WHERE id = ?", (coupon_id,))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Coupon deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to delete coupon', 'details': str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Usage:
1. **Get Coupons**:
   - Endpoint: `GET /api/coupons`
   - Response: A list of active coupons.

2. **Create Coupon**:
   - Endpoint: `POST /api/coupons`
   - Body: `{"name": "Discount Coupon", "description": "10% off", "discount_percentage": 10, "expiration_date": "YYYY-MM-DD"}`
   - Response: Confirmation of creation.

3. **Delete Coupon**:
   - Endpoint: `DELETE /api/coupons/<coupon_id>`
   - Response: Confirmation of deletion.

### Setup Instructions:
1. Save the code to a file, e.g., `dealership_coupons.py`.
2. Install Flask:
   ```bash
   pip install flask
   ```
3. Run the application:
   ```bash
   python dealership_coupons.py
   ```
4. Use a tool like Postman to interact with the API.
