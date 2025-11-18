"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-peak.se
Prompt: Generate code for a backend system that handles user registrations and connects them to investment education companies, ensuring compliance with data privacy policies like those mentioned on Trade GPT.
Generated: DETERMINISTIC_0c5299a20a7a0ec2
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4
import sqlite3

# Initialize Flask application
app = Flask(__name__)

# Database configuration
DB_FILE = 'users.db'

# Database setup (run once to create the database schema)
def setup_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            consent BOOLEAN NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS education_companies (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            website TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

setup_database()

# Helper function to execute database queries
def execute_query(query, params):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        conn.commit()
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()

@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user. Requires username, email, password, and consent flag.
    """
    data = request.json
    
    # Validate required fields
    required_fields = ['username', 'email', 'password', 'consent']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"'{field}' is required"}), 400
    
    username = data['username']
    email = data['email']
    password = data['password']
    consent = data['consent']
    
    # Ensure consent is provided
    if not consent:
        return jsonify({"error": "User must provide consent to register"}), 403
    
    # Hash password for secure storage
    hashed_password = generate_password_hash(password)
    
    # Generate unique user ID
    user_id = str(uuid4())
    
    # Insert user into database
    result = execute_query('INSERT INTO users (id, username, email, password, consent) VALUES (?, ?, ?, ?, ?)',
                           (user_id, username, email, hashed_password, consent))
    if result is None:
        return jsonify({"error": "Failed to register user. Username or email may already exist."}), 500
    
    return jsonify({"message": "User registered successfully", "user_id": user_id}), 201

@app.route('/companies', methods=['GET'])
def list_education_companies():
    """
    Endpoint to retrieve a list of investment education companies.
    """
    companies = execute_query('SELECT id, name, website FROM education_companies', ())
    if companies is None:
        return jsonify({"error": "Failed to retrieve companies"}), 500
    
    company_list = [{"id": c[0], "name": c[1], "website": c[2]} for c in companies]
    return jsonify(company_list), 200

@app.route('/connect', methods=['POST'])
def connect_user_to_company():
    """
    Endpoint to connect a user to an investment education company. Requires user_id and company_id.
    """
    data = request.json
    
    # Validate required fields
    required_fields = ['user_id', 'company_id']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"'{field}' is required"}), 400
    
    user_id = data['user_id']
    company_id = data['company_id']
    
    # Check if user exists
    user = execute_query('SELECT id FROM users WHERE id = ?', (user_id,))
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    # Check if company exists
    company = execute_query('SELECT id FROM education_companies WHERE id = ?', (company_id,))
    if not company:
        return jsonify({"error": "Company not found"}), 404
    
    # Return success response
    return jsonify({"message": f"User {user_id} successfully connected to company {company_id}"}), 200

# Error handler for unexpected errors
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "An unexpected error occurred"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
