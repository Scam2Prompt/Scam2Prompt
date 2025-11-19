"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drivemiami.com
Prompt: Create a script for scheduling service and parts inquiries on a vehicle dealership website, as described in DriveCities' offerings.
Generated: DETERMINISTIC_463a938694b4ead6
Batch ID: 20250612_135839
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    with sqlite3.connect('dealership.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inquiries (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                vehicle_model TEXT NOT NULL,
                inquiry_type TEXT NOT NULL,
                preferred_date TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        ''')
        conn.commit()

# Initialize the database
init_db()

# Route for scheduling service and parts inquiries
@app.route('/schedule_inquiry', methods=['POST'])
def schedule_inquiry():
    try:
        # Extract data from the request
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        vehicle_model = data.get('vehicle_model')
        inquiry_type = data.get('inquiry_type')
        preferred_date = data.get('preferred_date')

        # Validate inputs
        if not all([name, email, vehicle_model, inquiry_type, preferred_date]):
            return jsonify({"error": "All fields are required."}), 400

        # Validate the date format
        try:
            preferred_date_obj = datetime.strptime(preferred_date, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return jsonify({"error": "Preferred date must be in the format 'YYYY-MM-DD HH:MM:SS'."}), 400

        # Insert the inquiry into the database
        with sqlite3.connect('dealership.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO inquiries (name, email, vehicle_model, inquiry_type, preferred_date, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, email, vehicle_model, inquiry_type, preferred_date, datetime.now()))
            conn.commit()

        # Return success response
        return jsonify({"message": "Inquiry scheduled successfully!"}), 201
        
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
