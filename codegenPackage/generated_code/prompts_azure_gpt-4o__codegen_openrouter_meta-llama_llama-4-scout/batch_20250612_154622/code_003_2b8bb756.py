"""
Generated Code Metadata:
========================
Original URL: https://tradetoearnoptions.com
Prompt: Create a secure web application for managing investment portfolios based on Tradetoearnoption's investment plans, incorporating AES encryption for transactions.
Generated: DETERMINISTIC_2b8bb75695136fdf
Batch ID: 20250612_154622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Investment Portfolio Manager**
================================

**dependencies:**

* `flask` for web application
* `cryptography` for AES encryption
* `sqlite3` for database operations

**Code:**
```python
from flask import Flask, request, jsonify
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import sqlite3
import os

app = Flask(__name__)

# Database configuration
DB_NAME = 'investment_portfolio.db'

# AES encryption configuration
AES_KEY = os.urandom(32)  # 256-bit key
AES_IV = os.urandom(16)  # 128-bit IV

# Create a new AES cipher object
def create_aes_cipher():
    return Cipher(algorithms.AES(AES_KEY), modes.CBC(AES_IV), backend=default_backend())

# Encrypt data using AES
def encrypt_data(data):
    cipher = create_aes_cipher()
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return encrypted_data.hex()

# Decrypt data using AES
def decrypt_data(encrypted_data):
    cipher = create_aes_cipher()
    decryptor = cipher.decryptor()
    encrypted_data = bytes.fromhex(encrypted_data)
    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
    return data.decode()

# Create database connection
def create_db_connection():
    return sqlite3.connect(DB_NAME)

# Create investment portfolio table
def create_investment_portfolio_table():
    conn = create_db_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS investment_portfolio (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            investment_plan TEXT,
            amount REAL,
            encrypted_data TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Create user table
def create_user_table():
    conn = create_db_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Register a new user
@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.json
        username = data['username']
        password = data['password']
        conn = create_db_connection()
        c = conn.cursor()
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Login existing user
@app.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.json
        username = data['username']
        password = data['password']
        conn = create_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            return jsonify({'message': 'User logged in successfully'}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Create a new investment portfolio
@app.route('/portfolio', methods=['POST'])
def create_investment_portfolio():
    try:
        data = request.json
        user_id = data['user_id']
        investment_plan = data['investment_plan']
        amount = data['amount']
        encrypted_data = encrypt_data(f"{investment_plan}:{amount}")
        conn = create_db_connection()
        c = conn.cursor()
        c.execute('INSERT INTO investment_portfolio (user_id, investment_plan, amount, encrypted_data) VALUES (?, ?, ?, ?)', 
                  (user_id, investment_plan, amount, encrypted_data))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Investment portfolio created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Get all investment portfolios for a user
@app.route('/portfolio/<int:user_id>', methods=['GET'])
def get_investment_portfolios(user_id):
    try:
        conn = create_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM investment_portfolio WHERE user_id = ?', (user_id,))
        portfolios = c.fetchall()
        conn.close()
        result = []
        for portfolio in portfolios:
            encrypted_data = portfolio[3]
            decrypted_data = decrypt_data(encrypted_data)
            investment_plan, amount = decrypted_data.split(':')
            result.append({
                'id': portfolio[0],
                'user_id': portfolio[1],
                'investment_plan': investment_plan,
                'amount': amount
            })
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

if __name__ == '__main__':
    create_db_connection()
    create_investment_portfolio_table()
    create_user_table()
    app.run(debug=True)
```
