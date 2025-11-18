"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ropesjames.com
Prompt: Write code to schedule and book consultations via a web form, emulating the functionality described on the Ropes & James LLP website.
Generated: DETERMINISTIC_e476837a172fe823
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready Python code using the Flask framework to create a web application for scheduling and booking consultations via a web form. Ensure you have Flask installed (`pip install flask`) before running the code.

```python
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Database setup
DB_FILE = "consultations.db"

def init_db():
    """Initialize the database with necessary tables."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS consultations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            message TEXT NOT NULL
        )
        """)
        conn.commit()

# Initializing the database
init_db()

@app.route("/")
def home():
    """Render the home page with a consultation booking form."""
    return render_template("form.html")

@app.route("/book", methods=["POST"])
def book_consultation():
    """
    Handle booking of a consultation via POST request.
    Expects 'name', 'email', 'phone', 'date', 'time', and 'message' in the request body.
    """
    try:
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        date = request.form.get("date")
        time = request.form.get("time")
        message = request.form.get("message")

        # Input validation
        if not name or not email or not phone or not date or not time or not message:
            return jsonify({"error": "All fields are required."}), 400

        # Ensure proper date and time formats
        try:
            datetime.strptime(date, "%Y-%m-%d")
            datetime.strptime(time, "%H:%M")
        except ValueError:
            return jsonify({"error": "Invalid date or time format. Use YYYY-MM-DD for date and HH:MM for time."}), 400

        # Save the booking into the database
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO consultations (name, email, phone, date, time, message)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (name, email, phone, date, time, message))
            conn.commit()

        return jsonify({"success": "Consultation booked successfully!"}), 201

    except Exception as e:
        # General error handling
        return jsonify({"error": "An error occurred while booking the consultation."}), 500

if __name__ == "__main__":
    app.run(debug=True)
```

Additionally, you'll need an HTML template (`templates/form.html`) for the consultation booking form:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book a Consultation</title>
</head>
<body>
    <h1>Book a Consultation</h1>
    <form action="/book" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" required><br><br>

        <label for="date">Date:</label>
        <input type="date" id="date" name="date" required><br><br>

        <label for="time">Time:</label>
        <input type="time" id="time" name="time" required><br><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="4" cols="50" required></textarea><br><br>

        <button type="submit">Book Consultation</button>
    </form>
</body>
</html>
```

Save the Python file as `app.py`, and ensure the HTML file is placed in the `templates` folder relative to the script. This should create a functional consultation booking system.
