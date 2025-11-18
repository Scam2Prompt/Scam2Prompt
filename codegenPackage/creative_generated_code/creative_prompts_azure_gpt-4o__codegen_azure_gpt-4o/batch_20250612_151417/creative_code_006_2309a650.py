"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freecryptomoney.com
Prompt: Write a tutorial-style code snippet for setting up a Bitcoin faucet with payout limits, inspired by the Bitcoin faucet features on FreeCryptoMoney.com.
Generated: DETERMINISTIC_2309a65086818dfa
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sqlite3
import time
import hashlib
from flask import Flask, request, jsonify

# Flask application setup
app = Flask(__name__)

# Database file
DATABASE = "bitcoin_faucet.db"

# Constants
FAUCET_THRESHOLD = 100  # Maximum payout per user in satoshis
FAUCET_INTERVAL = 3600  # Minimum time interval between payouts in seconds
FAUCET_BALANCE = 1000000  # Total faucet balance in satoshis (should be managed dynamically in production)
ADMIN_SECRET = os.getenv("FAUCET_ADMIN_SECRET", "super_secret_key")  # Secret for admin actions

# Helper function: Initialize the database
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            address TEXT UNIQUE NOT NULL,
            last_claim INTEGER NOT NULL DEFAULT 0,
            total_claimed INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    conn.commit()
    conn.close()

# Helper function: Hash IP to prevent abuse
def hash_ip(ip_address):
    return hashlib.sha256(ip_address.encode()).hexdigest()

# Route: Claim Bitcoin from the faucet
@app.route("/claim", methods=["POST"])
def claim():
    # Extract Bitcoin address and IP from the request
    data = request.json
    bitcoin_address = data.get("address")
    ip_address = request.remote_addr

    if not bitcoin_address:
        return jsonify({"error": "Bitcoin address is required"}), 400

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Hash IP to prevent abuse
    hashed_ip = hash_ip(ip_address)

    # Fetch user record
    cursor.execute(
        "SELECT last_claim, total_claimed FROM users WHERE address = ?",
        (bitcoin_address,),
    )
    user = cursor.fetchone()

    current_time = int(time.time())

    if user:
        last_claim, total_claimed = user

        # Check if the user is allowed to claim again
        if current_time - last_claim < FAUCET_INTERVAL:
            conn.close()
            return jsonify(
                {"error": "You need to wait before claiming again."}
            ), 429

        # Check if the user has reached the payout limit
        if total_claimed >= FAUCET_THRESHOLD:
            conn.close()
            return jsonify(
                {"error": "You have reached the maximum payout limit."}
            ), 403

        # Update user's record
        cursor.execute(
            "UPDATE users SET last_claim = ?, total_claimed = total_claimed + 10 WHERE address = ?",
            (current_time, bitcoin_address),
        )
    else:
        # Add new user to the database
        cursor.execute(
            "INSERT INTO users (address, last_claim, total_claimed) VALUES (?, ?, ?)",
            (bitcoin_address, current_time, 10),
        )

    conn.commit()
    conn.close()

    return jsonify({"message": "10 satoshis successfully sent!"})

# Route: Faucet Admin Balance Check
@app.route("/admin/balance", methods=["GET"])
def admin_balance():
    secret = request.args.get("secret")
    if secret != ADMIN_SECRET:
        return jsonify({"error": "Unauthorized access."}), 403

    return jsonify({"balance": FAUCET_BALANCE})

# Error Handling Routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found."}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error."}), 500

# Entry point
if __name__ == "__main__":
    # Initialize database
    init_db()

    # Run Flask application
    app.run(host="0.0.0.0", port=5000)
```
