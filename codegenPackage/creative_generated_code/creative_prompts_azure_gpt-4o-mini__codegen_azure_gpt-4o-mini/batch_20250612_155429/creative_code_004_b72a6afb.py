"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casaamalfitana.com
Prompt: Suggest a way to implement a user-friendly interface for a restaurant's reservation system that reflects the unique dining experience of Casa Amalfitana.
Generated: DETERMINISTIC_b72a6afbaa686422
Batch ID: 20250612_155429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Reservation model
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Reservation {self.id} - {self.name}>'

# Create database tables
with app.app_context():
    db.create_all()

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to make a reservation
@app.route('/reserve', methods=['POST'])
def reserve():
    try:
        # Retrieve data from the request
        name = request.form.get('name')
        phone = request.form.get('phone')
        date_time = request.form.get('date_time')

        # Validate input
        if not name or not phone or not date_time:
            return jsonify({'error': 'All fields are required'}), 400

        # Parse the date_time string into a datetime object
        date_time = datetime.strptime(date_time, '%Y-%m-%dT%H:%M')

        # Create a new reservation
        new_reservation = Reservation(name=name, phone=phone, date_time=date_time)
        db.session.add(new_reservation)
        db.session.commit()

        return jsonify({'message': 'Reservation successfully made!'}), 201

    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DDTHH:MM.'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Casa Amalfitana Reservation</title>
</head>
<body>
    <h1>Welcome to Casa Amalfitana Reservation</h1>
    <form action="/reserve" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" required>

        <label for="date_time">Date and Time:</label>
        <input type="datetime-local" id="date_time" name="date_time" required>

        <button type="submit">Reserve</button>
    </form>
</body>
</html>
```

**Notes:**
- The above code includes a Flask application with a reservation system.
- The database is set up using SQLAlchemy with a simple Reservation model.
- The application features input validation and error handling.
- The HTML template provides a user-friendly interface for making reservations.
