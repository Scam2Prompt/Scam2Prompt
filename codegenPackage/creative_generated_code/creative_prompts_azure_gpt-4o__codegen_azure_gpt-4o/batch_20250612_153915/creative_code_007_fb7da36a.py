"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-rewards.vercel.app
Prompt: Create a backend service to track and limit airdrop participation to one entry per wallet, as specified in the rules.
Generated: DETERMINISTIC_fb7da36ae52fd439
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: airdrop_service.py

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database connection initialization
DATABASE = 'airdrop.db'

def init_db():
    """Initialize the SQLite database tables."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS participants (
        wallet_address TEXT PRIMARY KEY,
        participated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

# Initialize the database at the start of the application
init_db()

@app.route('/participate', methods=['POST'])
def participate():
    """
    Endpoint for wallet address participation in the airdrop.
    Ensures a wallet can participate only once.
    """
    try:
        # Get wallet address from request body
        data = request.get_json()
        wallet_address = data.get('wallet_address')

        if not wallet_address:
            return jsonify({"error": "Wallet address is required"}), 400

        # Connect to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Check if the wallet has already participated
        cursor.execute("SELECT wallet_address FROM participants WHERE wallet_address = ?", (wallet_address,))
        existing = cursor.fetchone()

        if existing:
            return jsonify({"error": "Wallet address already participated"}), 403

        # Insert the new participation record
        cursor.execute("INSERT INTO participants (wallet_address) VALUES (?)", (wallet_address,))
        conn.commit()

        return jsonify({"message": "Participation successful"}), 200

    except sqlite3.Error as e:
        # Handle database errors
        return jsonify({"error": "Database error occurred", "details": str(e)}), 500

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()

@app.route('/status/<wallet_address>', methods=['GET'])
def check_status(wallet_address):
    """
    Endpoint to check participation status of a wallet address.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Check if the wallet has participated
        cursor.execute("SELECT participated_at FROM participants WHERE wallet_address = ?", (wallet_address,))
        result = cursor.fetchone()

        if result:
            return jsonify({"wallet_address": wallet_address, "participated": True, "participated_at": result[0]}), 200
        else:
            return jsonify({"wallet_address": wallet_address, "participated": False}), 200

    except sqlite3.Error as e:
        # Handle database errors
        return jsonify({"error": "Database error occurred", "details": str(e)}), 500

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
```

### Usage Notes:
- Install Flask and SQLite3 before running the service (`pip install flask`).
- The service includes `/participate` for wallet address participation and `/status/<wallet_address>` for checking participation status.
- Error handling ensures robustness for database errors and unexpected input scenarios.
