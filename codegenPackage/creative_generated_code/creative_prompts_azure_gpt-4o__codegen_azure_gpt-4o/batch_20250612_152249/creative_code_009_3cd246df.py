"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patenteimpresa.it
Prompt: Create a script to integrate the "Patente d'Impresa" registration form with a database, ensuring secure storage of participant information like name, email, and phone number.
Generated: DETERMINISTIC_3cd246dfb756eccc
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, request, jsonify
import re

# Initialize Flask application
app = Flask(__name__)

# Setup SQLite database connection
DB_NAME = 'registration.db'

# Function to initialize the database schema
def initialize_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS registrations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

initialize_database()

# Regular expression for validating email format
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

# Endpoint to register participant information
@app.route('/register', methods=['POST'])
def register():
    try:
        # Parse data from the request
        data = request.json
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        # Input validation
        if not name or not email or not phone:
            return jsonify({'error': 'Name, email, and phone are required.'}), 400
        
        if not EMAIL_REGEX.match(email):
            return jsonify({'error': 'Invalid email format.'}), 400
        
        if not phone.isdigit() or len(phone) < 7:
            return jsonify({'error': 'Phone number must be numeric and at least 7 digits.'}), 400

        # Securely insert data into the database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO registrations (name, email, phone)
        VALUES (?, ?, ?)
        """, (name, email, phone))
        conn.commit()
        conn.close()

        # Return success response
        return jsonify({'message': 'Registration successful!'}), 201

    except sqlite3.IntegrityError as e:
        # Handle duplicate email registration
        return jsonify({'error': 'Email already registered.'}), 409
    except Exception as e:
        # Handle general errors
        return jsonify({'error': 'An error occurred during registration.'}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
