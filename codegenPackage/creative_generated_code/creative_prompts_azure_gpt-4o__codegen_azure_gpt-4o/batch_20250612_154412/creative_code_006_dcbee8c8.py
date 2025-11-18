"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cloud-telephonie.net
Prompt: Create a backend script to handle form submissions for a telephony quote request system, including storing user details and project urgency in a database.
Generated: DETERMINISTIC_dcbee8c8366d255e
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify
import sqlite3
import datetime

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
DB_NAME = 'telephony_quotes.db'

# Function to initialize the database
def initialize_database():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        # Create a table for storing quote requests if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS quote_requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                urgency TEXT NOT NULL,
                timestamp DATETIME NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

# Call the function to initialize the database
initialize_database()

# Route to handle form submissions
@app.route('/submit-quote', methods=['POST'])
def submit_quote():
    try:
        # Parse form data from the request
        form_data = request.get_json()
        name = form_data.get('name')
        email = form_data.get('email')
        phone = form_data.get('phone')
        urgency = form_data.get('urgency')

        # Validate form data
        if not name or not email or not phone or not urgency:
            return jsonify({'error': 'All fields are required.'}), 400

        # Store data in the database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO quote_requests (name, email, phone, urgency, timestamp)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, email, phone, urgency, datetime.datetime.now()))
        conn.commit()

        return jsonify({'message': 'Quote request submitted successfully.'}), 200

    except sqlite3.Error as e:
        return jsonify({'error': f'Database error: {e}'}), 500

    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {e}'}), 500

    finally:
        # Ensure the database connection is closed
        conn.close()

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
