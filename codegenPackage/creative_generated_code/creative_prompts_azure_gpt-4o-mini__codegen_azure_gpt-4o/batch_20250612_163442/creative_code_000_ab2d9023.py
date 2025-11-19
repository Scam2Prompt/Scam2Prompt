"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elon.vip
Prompt: How can I implement a secure buying process for domain sales similar to the one described on elon.vip?
Generated: DETERMINISTIC_ab2d90239ec3c646
Batch ID: 20250612_163442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import hashlib
from datetime import datetime, timedelta
import sqlite3
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Database Setup
DB_NAME = 'domain_sales.db'

# Create and initialize the database
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS domains (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain_name TEXT NOT NULL,
            price REAL NOT NULL,
            buyer_email TEXT,
            sold BOOLEAN DEFAULT 0,
            transaction_id TEXT,
            expiration_time TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Utility function to generate a unique transaction ID
def generate_transaction_id():
    return str(uuid.uuid4())

# Utility function to hash sensitive data (e.g., email)
def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Endpoint: List available domains
@app.route('/domains', methods=['GET'])
def list_domains():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id, domain_name, price FROM domains WHERE sold = 0")
        domains = cursor.fetchall()
        conn.close()
        return jsonify(domains), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch domains", "details": str(e)}), 500

# Endpoint: Initiate purchase
@app.route('/purchase', methods=['POST'])
def initiate_purchase():
    try:
        data = request.json
        domain_id = data.get('domain_id')
        buyer_email = data.get('buyer_email')

        if not domain_id or not buyer_email:
            return jsonify({"error": "Missing domain_id or buyer_email"}), 400

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Check if the domain exists and is available
        cursor.execute("SELECT * FROM domains WHERE id = ? AND sold = 0", (domain_id,))
        domain = cursor.fetchone()
        if not domain:
            conn.close()
            return jsonify({"error": "Domain not available"}), 404

        # Generate transaction ID and expiration time
        transaction_id = generate_transaction_id()
        expiration_time = datetime.now() + timedelta(minutes=15)  # Transaction expires in 15 minutes

        # Update domain record with transaction details
        cursor.execute("""
            UPDATE domains SET buyer_email = ?, transaction_id = ?, expiration_time = ?
            WHERE id = ?
        """, (hash_data(buyer_email), transaction_id, expiration_time, domain_id))
        conn.commit()
        conn.close()

        return jsonify({"transaction_id": transaction_id, "message": "Transaction initiated successfully"}), 200
    except Exception as e:
        return jsonify({"error": "Failed to initiate purchase", "details": str(e)}), 500

# Endpoint: Complete purchase
@app.route('/complete_purchase', methods=['POST'])
def complete_purchase():
    try:
        data = request.json
        transaction_id = data.get('transaction_id')

        if not transaction_id:
            return jsonify({"error": "Missing transaction_id"}), 400

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Verify the transaction
        cursor.execute("""
            SELECT id, domain_name, price, expiration_time FROM domains
            WHERE transaction_id = ? AND sold = 0
        """, (transaction_id,))
        domain = cursor.fetchone()
        if not domain:
            conn.close()
            return jsonify({"error": "Invalid or expired transaction"}), 404

        domain_id, domain_name, price, expiration_time = domain
        if datetime.now() > datetime.strptime(expiration_time, '%Y-%m-%d %H:%M:%S'):
            conn.close()
            return jsonify({"error": "Transaction expired"}), 410

        # Mark domain as sold
        cursor.execute("""
            UPDATE domains SET sold = 1 WHERE id = ?
        """, (domain_id,))
        conn.commit()
        conn.close()

        return jsonify({"message": f"Domain '{domain_name}' purchased successfully for ${price}"}), 200
    except Exception as e:
        return jsonify({"error": "Failed to complete purchase", "details": str(e)}), 500

# Run Flask application
if __name__ == '__main__':
    app.run(debug=False)
```
