"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karmadolap.com
Prompt: Recommend an open-source tool to manage customer inquiries for products like "Karma 2MT 15 ÇEKMECELİ ÇALIŞMA TEZGAHI" and "Karma 3MT 25 ÇEKMECELİ ÇALIŞMA TEZGAHI," with features for tracking communication history.
Generated: DETERMINISTIC_7b7188673a1d779a
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Customer Inquiry Management System

This script provides a simple implementation of a customer inquiry management system
using Python and an SQLite database. It allows you to log customer inquiries, track
communication history, and view previous inquiries.

Note: This implementation is a basic prototype for managing inquiries and communication
history. For production use, consider using robust open-source tools like 
"Zammad" or "OSTicket" for enterprise-grade customer service management.

Dependencies:
- SQLite3 (Python's built-in library)
- Flask (For creating a web interface)

To install Flask, run: `pip install flask`
"""

import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
DATABASE = 'customer_inquiries.db'


# Database setup and initialization
def init_db():
    """
    Initialize the SQLite database and create tables if they do not exist.
    """
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS inquiries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                customer_name TEXT NOT NULL,
                inquiry_details TEXT NOT NULL,
                communication_history TEXT NOT NULL
            )
        """)
        conn.commit()


# Route: Add a new inquiry
@app.route('/add_inquiry', methods=['POST'])
def add_inquiry():
    """
    API endpoint to add a new customer inquiry.
    Expects a JSON payload with product_name, customer_name, inquiry_details, and communication_history.
    """
    try:
        data = request.json
        product_name = data.get('product_name')
        customer_name = data.get('customer_name')
        inquiry_details = data.get('inquiry_details')
        communication_history = data.get('communication_history')

        if not all([product_name, customer_name, inquiry_details, communication_history]):
            return jsonify({"error": "All fields are required"}), 400

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO inquiries (product_name, customer_name, inquiry_details, communication_history)
                VALUES (?, ?, ?, ?)
            """, (product_name, customer_name, inquiry_details, communication_history))
            conn.commit()

        return jsonify({"message": "Inquiry added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route: Get all inquiries
@app.route('/get_inquiries', methods=['GET'])
def get_inquiries():
    """
    API endpoint to retrieve all customer inquiries.
    Returns a JSON list of inquiries.
    """
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM inquiries")
            inquiries = cursor.fetchall()
        
        inquiry_list = [
            {
                "id": inquiry[0],
                "product_name": inquiry[1],
                "customer_name": inquiry[2],
                "inquiry_details": inquiry[3],
                "communication_history": inquiry[4]
            }
            for inquiry in inquiries
        ]
        
        return jsonify(inquiry_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route: Update communication history
@app.route('/update_communication/<int:inquiry_id>', methods=['PUT'])
def update_communication(inquiry_id):
    """
    API endpoint to update communication history for a specific inquiry.
    Expects a JSON payload with updated communication_history.
    """
    try:
        data = request.json
        communication_history = data.get('communication_history')

        if not communication_history:
            return jsonify({"error": "Communication history is required"}), 400

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE inquiries
                SET communication_history = ?
                WHERE id = ?
            """, (communication_history, inquiry_id))
            conn.commit()

            if cursor.rowcount == 0:
                return jsonify({"error": "Inquiry not found"}), 404

        return jsonify({"message": "Communication history updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route: Delete an inquiry
@app.route('/delete_inquiry/<int:inquiry_id>', methods=['DELETE'])
def delete_inquiry(inquiry_id):
    """
    API endpoint to delete a specific inquiry.
    """
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM inquiries WHERE id = ?", (inquiry_id,))
            conn.commit()

            if cursor.rowcount == 0:
                return jsonify({"error": "Inquiry not found"}), 404

        return jsonify({"message": "Inquiry deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Main entry point
if __name__ == '__main__':
    # Initialize database
    init_db()
    # Run the Flask app
    app.run(debug=True)
```

This script provides a simple implementation of a customer inquiry management system using Python and SQLite. For production use cases, consider evaluating open-source tools like "Zammad" or "OSTicket," which provide enterprise-grade features for customer service management.
