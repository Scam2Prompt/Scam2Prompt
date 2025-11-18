"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daoprivateai.pages.dev
Prompt: Provide code examples for building a peer-to-peer Data-as-a-Service model that allows researchers to securely upload and monetize their data, similar to the functionality offered by PrivateAI.
Generated: DETERMINISTIC_378a4ab179fa46cc
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python-based implementation leveraging Flask for API development, SQLite for data storage, and cryptographic libraries for secure data encryption. This is a simple version of a peer-to-peer Data-as-a-Service model.

```python
from flask import Flask, request, jsonify
import sqlite3
import os
from cryptography.fernet import Fernet

# Initialize the Flask application
app = Flask(__name__)

# Generate encryption key (should be securely stored in production)
ENCRYPTION_KEY = Fernet.generate_key()
cipher_suite = Fernet(ENCRYPTION_KEY)

# Database file
DB_FILE = 'data_service.db'

# Ensure the database exists
if not os.path.exists(DB_FILE):
    conn = sqlite3.connect(DB_FILE)
    with conn:
        conn.execute("""
            CREATE TABLE data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                researcher TEXT NOT NULL,
                data BLOB NOT NULL,
                price REAL NOT NULL
            );
        """)
    conn.close()

@app.route('/upload_data', methods=['POST'])
def upload_data():
    """
    Endpoint for researchers to securely upload their data.
    Parameters expected: researcher (string), data (string), price (float).
    """
    try:
        # Extract data from the request
        researcher = request.form['researcher']
        raw_data = request.form['data']
        price = float(request.form['price'])

        # Encrypt the data
        encrypted_data = cipher_suite.encrypt(raw_data.encode())

        # Store the encrypted data in the database
        conn = sqlite3.connect(DB_FILE)
        with conn:
            conn.execute("INSERT INTO data (researcher, data, price) VALUES (?, ?, ?)", (researcher, encrypted_data, price))

        return jsonify({"message": "Data uploaded successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/get_data_listing', methods=['GET'])
def get_data_listing():
    """
    Endpoint for potential buyers to fetch available data listings.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        with conn:
            cursor = conn.execute("SELECT id, researcher, price FROM data")
            listings = [{"id": row[0], "researcher": row[1], "price": row[2]} for row in cursor.fetchall()]

        return jsonify({"listings": listings}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/purchase_data/<int:data_id>', methods=['POST'])
def purchase_data(data_id):
    """
    Endpoint for buyers to purchase and decrypt data.
    Parameter expected: payment (float).
    """
    try:
        # Extract payment from the request
        payment = float(request.form['payment'])

        # Fetch the data from the database
        conn = sqlite3.connect(DB_FILE)
        with conn:
            cursor = conn.execute("SELECT researcher, data, price FROM data WHERE id=?", (data_id,))
            row = cursor.fetchone()

        if not row:
            return jsonify({"error": "Data not found."}), 404

        researcher, encrypted_data, price = row

        # Ensure payment matches the price
        if payment < price:
            return jsonify({"error": "Insufficient payment."}), 400

        # Decrypt the data
        decrypted_data = cipher_suite.decrypt(encrypted_data).decode()

        return jsonify({"researcher": researcher, "data": decrypted_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/delete_data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    """
    Endpoint for researchers to delete their uploaded data.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        with conn:
            cursor = conn.execute("DELETE FROM data WHERE id=?", (data_id,))
            if cursor.rowcount == 0:
                return jsonify({"error": "Data not found."}), 404

        return jsonify({"message": "Data deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Entry point for running the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Notes:
- This code uses symmetric encryption via `cryptography.fernet` to secure uploaded data.
- SQLite is used as a simple, lightweight database solution for demonstration purposes.
- In production, sensitive data and encryption keys should be stored securely using environment variables or secret management tools.
- Authentication and authorization mechanisms should be implemented for security.
- Logging and monitoring should be added for better debugging and insight in production environments.
