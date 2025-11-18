"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Recommend a library or API for managing customer inquiries and free quote requests, similar to the contact form used on Perfect Melbourne Carpet's website.
Generated: DETERMINISTIC_f32e5c714786be02
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script uses Flask (a lightweight web framework for Python) and SQLite database 
to implement a simple API for managing customer inquiries and free quote requests.
It is production-ready, follows best practices, and includes error handling.

To use this code, ensure Flask is installed: `pip install flask`
"""

from flask import Flask, request, jsonify
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Database file
DB_FILE = 'customer_inquiries.db'


# Function to initialize the SQLite database
def init_db():
    """
    Creates the database table if it doesn't exist.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Create a table for inquiries
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS inquiries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.commit()
    except sqlite3.Error as e:
        print(f"Database Initialization Error: {e}")
    finally:
        conn.close()


@app.route('/api/inquiries', methods=['POST'])
def submit_inquiry():
    """
    API endpoint to submit a new inquiry.
    Expects JSON payload with 'name', 'email', and 'message'.
    """
    try:
        # Parse JSON request data
        data = request.get_json()

        # Validate payload
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        if not name or not email or not message:
            return jsonify({"error": "Missing required fields"}), 400

        # Insert inquiry into the database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO inquiries (name, email, message)
            VALUES (?, ?, ?)
        """, (name, email, message))

        conn.commit()
        return jsonify({"message": "Inquiry submitted successfully"}), 201
    except sqlite3.Error as e:
        return jsonify({"error": f"Database Error: {e}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected Error: {e}"}), 500
    finally:
        conn.close()


@app.route('/api/inquiries', methods=['GET'])
def list_inquiries():
    """
    API endpoint to list all customer inquiries.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Retrieve all inquiries from the database
        cursor.execute("SELECT id, name, email, message, created_at FROM inquiries")
        inquiries = cursor.fetchall()

        # Convert DB rows into a list of dictionaries
        result = [
            {"id": row[0], "name": row[1], "email": row[2], "message": row[3], "created_at": row[4]}
            for row in inquiries
        ]

        return jsonify(result), 200
    except sqlite3.Error as e:
        return jsonify({"error": f"Database Error: {e}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected Error: {e}"}), 500
    finally:
        conn.close()


@app.route('/api/inquiries/<int:id>', methods=['GET'])
def get_inquiry(id):
    """
    API endpoint to retrieve a specific inquiry by ID.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Retrieve inquiry by ID
        cursor.execute("SELECT id, name, email, message, created_at FROM inquiries WHERE id = ?", (id,))
        row = cursor.fetchone()

        if row:
            inquiry = {"id": row[0], "name": row[1], "email": row[2], "message": row[3], "created_at": row[4]}
            return jsonify(inquiry), 200
        else:
            return jsonify({"error": "Inquiry not found"}), 404
    except sqlite3.Error as e:
        return jsonify({"error": f"Database Error: {e}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected Error: {e}"}), 500
    finally:
        conn.close()


# Entry point for the Flask application
if __name__ == '__main__':
    # Initialize the database
    init_db()

    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=False)
```
