"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demirsoft.com
Prompt: Write code to integrate DemirSoft's "Caller ID Cihazı" with a customer database for identifying incoming calls and retrieving customer information.
Generated: DETERMINISTIC_67ee28741c06a227
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import requests
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Database configuration
DATABASE = 'customer_database.db'

def init_db():
    """Initialize the SQLite database and create the customers table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone_number TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            email TEXT,
            address TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/incoming_call', methods=['POST'])
def incoming_call():
    """Endpoint to handle incoming calls and retrieve customer information based on the phone number."""
    try:
        # Extract incoming call data from the request
        data = request.json
        phone_number = data.get('phone_number')

        if not phone_number:
            return jsonify({'error': 'Phone number is required'}), 400

        # Retrieve customer information from the database
        customer_info = get_customer_info(phone_number)
        
        if customer_info:
            return jsonify(customer_info), 200
        else:
            return jsonify({'message': 'Customer not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_customer_info(phone_number):
    """Fetch customer information from the database based on the phone number."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM customers WHERE phone_number = ?', (phone_number,))
    customer = cursor.fetchone()

    conn.close()

    # Convert the customer data into a dictionary
    if customer:
        return {
            'id': customer[0],
            'phone_number': customer[1],
            'name': customer[2],
            'email': customer[3],
            'address': customer[4]
        }
    return None

def add_customer(phone_number, name, email, address):
    """Add a new customer to the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO customers (phone_number, name, email, address) VALUES (?, ?, ?, ?)',
                       (phone_number, name, email, address))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Customer with this phone number already exists.")
    finally:
        conn.close()

if __name__ == "__main__":
    # Initialize the database
    init_db()
    
    # Run the Flask application
    app.run(debug=True)
```
