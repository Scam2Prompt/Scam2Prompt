"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karnatakaaromas.com
Prompt: Suggest APIs or tools for managing long-term contracts and documentation for suppliers of aroma materials, referencing Karnataka Aromas' emphasis on transparency and efficiency.
Generated: DETERMINISTIC_b5168df47339c8ea
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Supplier Contract Management System
This script provides functionality to manage long-term contracts and supplier documentation 
with a focus on transparency and efficiency. It uses Flask (web framework) and SQLite database 
to create a simple API-based solution.

Dependencies:
- Flask: Lightweight web framework for creating APIs
- SQLite: Lightweight database for data storage
"""

from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Database configuration
DATABASE = 'supplier_contracts.db'

# Initialize database if not already set up
def init_db():
    """Creates the database and required tables."""
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE suppliers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact_info TEXT NOT NULL
        )
        """)
        cursor.execute("""
        CREATE TABLE contracts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            supplier_id INTEGER NOT NULL,
            contract_details TEXT NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            FOREIGN KEY (supplier_id) REFERENCES suppliers (id)
        )
        """)
        conn.commit()
        conn.close()

init_db()

# Error handler for database operations
def db_error_handler(func):
    """Decorator to catch database-related errors."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except sqlite3.Error as e:
            return jsonify({"error": str(e)}), 500
    return wrapper

@app.route('/suppliers', methods=['POST'])
@db_error_handler
def add_supplier():
    """
    Add a new supplier.
    Request body should contain:
    - name: Name of the supplier
    - contact_info: Contact details of the supplier
    """
    data = request.json
    name = data.get('name')
    contact_info = data.get('contact_info')
    if not name or not contact_info:
        return jsonify({"error": "Missing 'name' or 'contact_info'"}), 400
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO suppliers (name, contact_info) VALUES (?, ?)", (name, contact_info))
    conn.commit()
    conn.close()
    return jsonify({"message": "Supplier added successfully"}), 201

@app.route('/contracts', methods=['POST'])
@db_error_handler
def add_contract():
    """
    Add a new contract.
    Request body should contain:
    - supplier_id: ID of the supplier
    - contract_details: Details of the contract
    - start_date: Contract start date
    - end_date: Contract end date
    """
    data = request.json
    supplier_id = data.get('supplier_id')
    contract_details = data.get('contract_details')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    if not all([supplier_id, contract_details, start_date, end_date]):
        return jsonify({"error": "Missing one or more required fields"}), 400
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO contracts (supplier_id, contract_details, start_date, end_date) VALUES (?, ?, ?, ?)
    """, (supplier_id, contract_details, start_date, end_date))
    conn.commit()
    conn.close()
    return jsonify({"message": "Contract added successfully"}), 201

@app.route('/contracts/<int:supplier_id>', methods=['GET'])
@db_error_handler
def get_contracts_by_supplier(supplier_id):
    """
    Retrieve all contracts for a specific supplier.
    :param supplier_id: ID of the supplier
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT contracts.id, contract_details, start_date, end_date 
    FROM contracts 
    WHERE supplier_id = ?
    """, (supplier_id,))
    contracts = cursor.fetchall()
    conn.close()
    return jsonify({"contracts": contracts}), 200

@app.route('/suppliers', methods=['GET'])
@db_error_handler
def get_suppliers():
    """
    Retrieve a list of all suppliers.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, contact_info FROM suppliers")
    suppliers = cursor.fetchall()
    conn.close()
    return jsonify({"suppliers": suppliers}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Install dependencies with `pip install flask`.
- Run the script, and it will create the SQLite database (`supplier_contracts.db`) if it doesn't exist.
- Use tools like Postman or curl to test the endpoints for adding/retrieving suppliers/contracts.
