"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qrubi.com
Prompt: Explain the process of how QRubi connects lost items with their owners through QR code scanning.
Generated: DETERMINISTIC_f153283d5d6cf1bd
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import sqlite3
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Database setup
DB_NAME = "qrubi.db"

def initialize_database():
    """
    Initialize the database and create necessary tables
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Create table for storing lost items and owners
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS LostItems (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_description TEXT NOT NULL,
            owner_name TEXT NOT NULL,
            owner_email TEXT NOT NULL,
            qr_code TEXT NOT NULL UNIQUE
        )
    """)
    conn.commit()
    conn.close()

# Initialize database
initialize_database()

# Helper function to generate QR code
def generate_qr_code(data):
    """
    Generates a QR code from the given data.
    
    Args:
        data (str): The data to encode in the QR code.

    Returns:
        str: Path to the saved QR code image.
    """
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save QR code with unique filename
    file_path = f"{data}.png"
    img.save(file_path)
    return file_path

# API endpoint: Register a lost item
@app.route('/register_item', methods=['POST'])
def register_item():
    """
    API endpoint to register a lost item.
    
    Request JSON:
    {
        "item_description": "Description of the lost item",
        "owner_name": "Owner's full name",
        "owner_email": "Owner's email address"
    }
    """
    try:
        # Parse input data
        data = request.json
        item_description = data['item_description']
        owner_name = data['owner_name']
        owner_email = data['owner_email']
        
        # Generate unique identifier for the item
        qr_data = f"{owner_email}-{item_description}"
        
        # Generate QR code
        qr_code_path = generate_qr_code(qr_data)
        
        # Save item details to database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO LostItems (item_description, owner_name, owner_email, qr_code)
            VALUES (?, ?, ?, ?)
        """, (item_description, owner_name, owner_email, qr_code_path))
        conn.commit()
        conn.close()
        
        return jsonify({"message": "Item registered successfully", "qr_code_path": qr_code_path}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint: Scan QR code and find owner details
@app.route('/scan_qr', methods=['POST'])
def scan_qr():
    """
    API endpoint to scan a QR code and retrieve owner details.
    
    Request JSON:
    {
        "qr_data": "Data encoded in QR code"
    }
    """
    try:
        # Parse input data
        data = request.json
        qr_data = data['qr_data']
        
        # Search for the item in the database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT item_description, owner_name, owner_email FROM LostItems
            WHERE qr_code LIKE ?
        """, (f"%{qr_data}%",))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            item_description, owner_name, owner_email = result
            return jsonify({
                "item_description": item_description,
                "owner_name": owner_name,
                "owner_email": owner_email
            }), 200
        else:
            return jsonify({"message": "No matching item found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
