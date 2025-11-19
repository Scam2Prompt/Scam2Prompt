"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amarparasanar.com.mx
Prompt: Generate a code snippet for a web application that allows users to book online therapy sessions with licensed therapists specializing in EMDR and Bioneuroemoción.
Generated: DETERMINISTIC_060906383fc3895b
Batch ID: 20250612_155829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize Flask application and configure database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///therapy_sessions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database model for Therapy Session
class TherapySession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    therapist_name = db.Column(db.String(100), nullable=False)
    session_date = db.Column(db.DateTime, nullable=False)
    session_type = db.Column(db.String(50), nullable=False)  # EMDR or Bioneuroemoción

    def __repr__(self):
        return f"<TherapySession {self.client_name} - {self.session_type} on {self.session_date}>"

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to render booking form
@app.route('/')
def index():
    return render_template('booking_form.html')

# Route to handle booking requests
@app.route('/book', methods=['POST'])
def book_session():
    try:
        data = request.get_json()
        
        # Validate input data
        if not data or 'client_name' not in data or 'therapist_name' not in data or 'session_date' not in data or 'session_type' not in data:
            return jsonify({"error": "Missing required fields"}), 400
        
        # Create a new therapy session
        new_session = TherapySession(
            client_name=data['client_name'],
            therapist_name=data['therapist_name'],
            session_date=datetime.strptime(data['session_date'], '%Y-%m-%d %H:%M:%S'),
            session_type=data['session_type']
        )

        # Add session to the database
        db.session.add(new_session)
        db.session.commit()

        logging.info(f"Session booked: {new_session}")
        return jsonify({"message": "Session successfully booked", "session_id": new_session.id}), 201

    except Exception as e:
        logging.error(f"Error while booking session: {e}")
        return jsonify({"error": "An error occurred while booking the session"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/booking_form.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Therapy Session</title>
</head>
<body>
    <h1>Book Your Therapy Session</h1>
    <form id="bookingForm">
        <label for="client_name">Your Name:</label>
        <input type="text" id="client_name" name="client_name" required><br><br>

        <label for="therapist_name">Therapist Name:</label>
        <input type="text" id="therapist_name" name="therapist_name" required><br><br>

        <label for="session_date">Session Date (YYYY-MM-DD HH:MM:SS):</label>
        <input type="text" id="session_date" name="session_date" required><br><br>

        <label for="session_type">Session Type:</label>
        <select id="session_type" name="session_type" required>
            <option value="EMDR">EMDR</option>
            <option value="Bioneuroemoción">Bioneuroemoción</option>
        </select><br><br>

        <button type="submit">Book Session</button>
    </form>
    
    <script>
        document.getElementById('bookingForm').onsubmit = async function (e) {
            e.preventDefault();

            const formData = {
                client_name: document.getElementById('client_name').value,
                therapist_name: document.getElementById('therapist_name').value,
                session_date: document.getElementById('session_date').value,
                session_type: document.getElementById('session_type').value
            };

            const response = await fetch('/book', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            const result = await response.json();
            alert(result.message || result.error);
        };
    </script>
</body>
</html>
```

### Note:
Ensure that you have the required libraries installed before running the application. You can install Flask and SQLAlchemy via pip:

```bash
pip install Flask SQLAlchemy
```
