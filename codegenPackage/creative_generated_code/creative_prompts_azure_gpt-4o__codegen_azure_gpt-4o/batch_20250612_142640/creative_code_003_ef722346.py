"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoassetfinance.com
Prompt: Generate code for a web application that allows businesses to compare bespoke asset finance options for light aircraft, agricultural equipment, and other assets, inspired by Rhino Asset Finance's services.
Generated: DETERMINISTIC_ef72234627ab9b97
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
import sqlite3

# Initialize Flask application
app = Flask(__name__)

# Database configuration
DATABASE = 'finance_options.db'

# Helper function: Connect to the database
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row  # Enable dictionary-like row access
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# Helper function: Close the database connection
def close_db_connection(conn):
    if conn:
        conn.close()

# Initialize database and create tables (run once, ideally not part of production code)
def init_db():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS finance_options (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                asset_type TEXT NOT NULL,
                finance_provider TEXT NOT NULL,
                interest_rate REAL NOT NULL,
                term_months INTEGER NOT NULL,
                conditions TEXT
            )
        ''')
        conn.commit()
        close_db_connection(conn)

# Route: Get finance options based on asset type
@app.route('/finance-options', methods=['GET'])
def get_finance_options():
    asset_type = request.args.get('asset_type', '').lower()
    if not asset_type:
        return jsonify({'error': 'Asset type is required'}), 400
    
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Failed to connect to the database'}), 500
    
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM finance_options WHERE asset_type = ?', (asset_type,))
        rows = cursor.fetchall()
        finance_options = [dict(row) for row in rows]
        return jsonify({'finance_options': finance_options})
    except sqlite3.Error as e:
        print(f"Database query error: {e}")
        return jsonify({'error': 'Failed to retrieve finance options'}), 500
    finally:
        close_db_connection(conn)

# Route: Add a new finance option (Admin functionality)
@app.route('/finance-options', methods=['POST'])
def add_finance_option():
    try:
        data = request.get_json()
        asset_type = data.get('asset_type', '').lower()
        finance_provider = data.get('finance_provider', '')
        interest_rate = data.get('interest_rate')
        term_months = data.get('term_months')
        conditions = data.get('conditions', '')

        if not (asset_type and finance_provider and interest_rate and term_months):
            return jsonify({'error': 'All fields are required'}), 400
        
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Failed to connect to the database'}), 500

        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO finance_options (asset_type, finance_provider, interest_rate, term_months, conditions)
            VALUES (?, ?, ?, ?, ?)
        ''', (asset_type, finance_provider, interest_rate, term_months, conditions))
        conn.commit()  # Save changes to the database
        return jsonify({'message': 'Finance option added successfully'}), 201
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return jsonify({'error': 'Failed to add finance option'}), 500
    except Exception as e:
        print(f"Unexpected error: {e}")
        return jsonify({'error': 'An error occurred'}), 500
    finally:
        if 'conn' in locals():
            close_db_connection(conn)

# Route: Health check
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

# Run the application
if __name__ == '__main__':
    # Initialize database if running for the first time
    init_db()
    # Start the Flask development server
    app.run(debug=True)
```
