"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plenamintairdrop.vercel.app
Prompt: Suggest tools or frameworks to implement a whitelist system for $PLENA token distribution, as described in the Plena Finance airdrop campaign.
Generated: DETERMINISTIC_79eb19c4927937ff
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation for a whitelist system for $PLENA token distribution using Flask as the web framework and SQLite as the database for simplicity. It meets your requirements for clean, well-commented, production-ready code.

```python
from flask import Flask, request, jsonify
import sqlite3
from sqlite3 import Error

# Initialize Flask app
app = Flask(__name__)

# Database setup
DB_PATH = "whitelist.db"

def create_connection(db_file):
    """Create a database connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def initialize_database():
    """Initialize the database and create necessary tables if not exist."""
    conn = create_connection(DB_PATH)
    if conn:
        try:
            with conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS whitelist (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        wallet_address TEXT UNIQUE NOT NULL,
                        amount INTEGER NOT NULL
                    );
                """)
        except Error as e:
            print(f"Error initializing database: {e}")
        finally:
            conn.close()

# Initialize database on application start
initialize_database()

# Helper function to check if wallet address is valid format
def is_valid_wallet_address(wallet_address):
    """Validate wallet address format."""
    # Example validation rule: address should be alphanumeric and 42 characters long
    return isinstance(wallet_address, str) and len(wallet_address) == 42 and wallet_address.isalnum()

# Route to add a wallet address to the whitelist
@app.route('/api/whitelist', methods=['POST'])
def add_to_whitelist():
    """
    Add a wallet address to the whitelist.

    Request JSON format:
    {
        "wallet_address": "0x1234567890abcdef1234567890abcdef12345678",
        "amount": 100
    }
    """
    data = request.get_json()
    wallet_address = data.get("wallet_address")
    amount = data.get("amount")

    # Validate input
    if not wallet_address or not is_valid_wallet_address(wallet_address):
        return jsonify({"error": "Invalid wallet address"}), 400
    if not amount or not isinstance(amount, int) or amount <= 0:
        return jsonify({"error": "Invalid amount"}), 400

    conn = create_connection(DB_PATH)
    if conn:
        try:
            with conn:
                conn.execute(
                    "INSERT INTO whitelist (wallet_address, amount) VALUES (?, ?)",
                    (wallet_address, amount)
                )
            return jsonify({"message": "Wallet address successfully added to whitelist"}), 201
        except sqlite3.IntegrityError:
            return jsonify({"error": "Wallet address already exists in whitelist"}), 409
        except Error as e:
            return jsonify({"error": f"Database error: {e}"}), 500
        finally:
            conn.close()
    return jsonify({"error": "Unable to connect to database"}), 500

# Route to retrieve the whitelist
@app.route('/api/whitelist', methods=['GET'])
def get_whitelist():
    """
    Retrieve the whitelist.

    Response JSON format:
    [
        {
            "wallet_address": "0x1234567890abcdef1234567890abcdef12345678",
            "amount": 100
        },
        ...
    ]
    """
    conn = create_connection(DB_PATH)
    if conn:
        try:
            with conn:
                cursor = conn.execute("SELECT wallet_address, amount FROM whitelist")
                whitelist = [{"wallet_address": row[0], "amount": row[1]} for row in cursor.fetchall()]
            return jsonify(whitelist), 200
        except Error as e:
            return jsonify({"error": f"Database error: {e}"}), 500
        finally:
            conn.close()
    return jsonify({"error": "Unable to connect to database"}), 500

# Route to delete a wallet address from the whitelist
@app.route('/api/whitelist/<wallet_address>', methods=['DELETE'])
def delete_from_whitelist(wallet_address):
    """
    Delete a wallet address from the whitelist.

    URL Parameter:
    wallet_address: wallet address to be removed.

    Response JSON format:
    {
        "message": "Wallet address successfully removed from whitelist"
    }
    """
    if not is_valid_wallet_address(wallet_address):
        return jsonify({"error": "Invalid wallet address"}), 400

    conn = create_connection(DB_PATH)
    if conn:
        try:
            with conn:
                cursor = conn.execute(
                    "DELETE FROM whitelist WHERE wallet_address = ?",
                    (wallet_address,)
                )
                if cursor.rowcount == 0:
                    return jsonify({"error": "Wallet address not found"}), 404
            return jsonify({"message": "Wallet address successfully removed from whitelist"}), 200
        except Error as e:
            return jsonify({"error": f"Database error: {e}"}), 500
        finally:
            conn.close()
    return jsonify({"error": "Unable to connect to database"}), 500

# Start Flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Notes:
- Run the script to start a Flask server.
- Use `/api/whitelist` POST route to add wallet addresses.
- Use `/api/whitelist` GET route to retrieve all whitelisted addresses.
- Use `/api/whitelist/<wallet_address>` DELETE route to remove a wallet address.
- Replace the wallet address validation logic with actual blockchain-specific validation if required.
