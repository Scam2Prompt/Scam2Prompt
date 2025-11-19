"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clientfuel.digital
Prompt: How can I implement a lead generation system for my grooming business using the Click, Capture, Close model described on Client Fuel's website?
Generated: DETERMINISTIC_4d5079744f2a83b6
Batch ID: 20250612_140403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready implementation of a lead generation system for a grooming business using the "Click, Capture, Close" model. We'll use Python with Flask for the backend and SQLite for lead storage.

```python
# app.py

from flask import Flask, request, jsonify, render_template
import sqlite3
import os

# Initialize Flask app
app = Flask(__name__)
DB_FILE = 'leads.db'

# Ensure database exists and initialize schema
def init_db():
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                message TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

init_db()

# Home route with HTML form for lead capture
@app.route('/')
def home():
    return render_template('index.html')  # Render a form for lead capture

# Capture route to collect leads from the form submission
@app.route('/capture', methods=['POST'])
def capture_lead():
    try:
        # Extract form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        # Validate input (basic validation)
        if not name or not email or not phone or not message:
            return jsonify({'error': 'All fields are required'}), 400

        # Save lead to database
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute('INSERT INTO leads (name, email, phone, message) VALUES (?, ?, ?, ?)',
                  (name, email, phone, message))
        conn.commit()
        conn.close()

        # Response to acknowledge successful capture
        return jsonify({'message': 'Lead captured successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Close route for retrieving leads to follow up (admin use case)
@app.route('/close', methods=['GET'])
def get_leads():
    try:
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute('SELECT id, name, email, phone, message FROM leads')
        leads = c.fetchall()  # Fetch all leads
        conn.close()

        # Return leads in JSON format
        return jsonify({'leads': [
            {'id': lead[0], 'name': lead[1], 'email': lead[2], 'phone': lead[3], 'message': lead[4]}
            for lead in leads
        ]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

# templates/index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lead Capture Form</title>
</head>
<body>
    <h1>Grooming Business Lead Capture</h1>
    <form action="/capture" method="post">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        <label for="phone">Phone:</label><br>
        <input type="text" id="phone" name="phone" required><br><br>
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" required></textarea><br><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

### Notes:
- Install Flask via `pip install flask` before running the project.
- SQLite is used as the database for simplicity, but you can replace it with a more robust database like PostgreSQL for production.
- Save the HTML file (`index.html`) in a folder named `templates` in the same directory as the Python file (`app.py`).
- Error handling is included to ensure the code gracefully handles issues like missing fields or database errors.
