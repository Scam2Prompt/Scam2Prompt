"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch.danngol.com
Prompt: Create a REST API endpoint for a platform like "단골가게" that handles user registration, business selection, prepayment processing, and discount redemption.
Generated: DETERMINISTIC_8590303786c790ef
Batch ID: 20250612_150848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
import sqlite3
import uuid

app = Flask(__name__)

# Database setup
DB_FILE = 'dangol_store.db'

def init_db():
    """Initialize the database with necessary tables."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS businesses (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            discounts TEXT NOT NULL -- JSON format to store available discounts
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prepayments (
            id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            business_id TEXT NOT NULL,
            amount REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(business_id) REFERENCES businesses(id)
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Helper functions
def create_response(message, status_code=200, data=None):
    """Utility function to create a consistent API response."""
    response = {
        "message": message,
        "status": status_code,
        "data": data or {}
    }
    return jsonify(response), status_code

def connect_db():
    """Utility function to connect to the database."""
    return sqlite3.connect(DB_FILE)

# Route: User Registration
@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint for user registration.
    Expects JSON payload with 'name' and 'email'.
    """
    try:
        user_data = request.json
        name = user_data.get('name')
        email = user_data.get('email')

        if not name or not email:
            return create_response("Name and email are required.", status_code=400)

        user_id = str(uuid.uuid4())
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute('INSERT INTO users (id, name, email) VALUES (?, ?, ?)', (user_id, name, email))
        conn.commit()
        conn.close()

        return create_response("User registered successfully.", data={"user_id": user_id})
    except sqlite3.IntegrityError:
        return create_response("Email already exists.", status_code=400)
    except Exception as e:
        return create_response(f"An error occurred: {str(e)}", status_code=500)

# Route: Business Selection
@app.route('/businesses', methods=['GET'])
def list_businesses():
    """
    Endpoint to list available businesses.
    """
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, discounts FROM businesses')
        businesses = cursor.fetchall()
        conn.close()

        business_list = [{"id": b[0], "name": b[1], "discounts": b[2]} for b in businesses]
        return create_response("Businesses fetched successfully.", data={"businesses": business_list})
    except Exception as e:
        return create_response(f"An error occurred: {str(e)}", status_code=500)

# Route: Prepayment Processing
@app.route('/prepay', methods=['POST'])
def prepay():
    """
    Endpoint for prepayment processing.
    Expects JSON payload with 'user_id', 'business_id', and 'amount'.
    """
    try:
        payload = request.json
        user_id = payload.get('user_id')
        business_id = payload.get('business_id')
        amount = payload.get('amount')

        if not user_id or not business_id or not amount:
            return create_response("User ID, business ID, and amount are required.", status_code=400)
        
        prepayment_id = str(uuid.uuid4())
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO prepayments (id, user_id, business_id, amount) VALUES (?, ?, ?, ?)', 
                       (prepayment_id, user_id, business_id, amount))
        conn.commit()
        conn.close()

        return create_response("Prepayment processed successfully.", data={"prepayment_id": prepayment_id})
    except Exception as e:
        return create_response(f"An error occurred: {str(e)}", status_code=500)

# Route: Discount Redemption
@app.route('/redeem', methods=['POST'])
def redeem_discount():
    """
    Endpoint for discount redemption.
    Expects JSON payload with 'user_id' and 'business_id'.
    """
    try:
        payload = request.json
        user_id = payload.get('user_id')
        business_id = payload.get('business_id')

        if not user_id or not business_id:
            return create_response("User ID and business ID are required.", status_code=400)
        
        # Simulate discount redemption logic (e.g., fetching discounts from the database)
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT discounts FROM businesses WHERE id = ?', (business_id,))
        business = cursor.fetchone()
        conn.close()

        if not business:
            return create_response("Business not found.", status_code=404)
        
        discounts = business[0]  # Assuming discounts are stored as JSON string

        return create_response("Discount redeemed successfully.", data={"discounts": discounts})
    except Exception as e:
        return create_response(f"An error occurred: {str(e)}", status_code=500)

# Global error handler
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions with a consistent response format."""
    return create_response(e.description, status_code=e.code)

@app.errorhandler(Exception)
def handle_exception(e):
    """Handle generic exceptions with a consistent response format."""
    return create_response(f"An unexpected error occurred: {str(e)}", status_code=500)

# Main application entry point
if __name__ == '__main__':
    app.run(debug=True)
```
