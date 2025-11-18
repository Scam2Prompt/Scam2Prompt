"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnwinternational.com
Prompt: Develop a web application that allows users to book trial IELTS or PTE classes, inspired by the flexible batch booking system mentioned on RNW International's site.
Generated: DETERMINISTIC_2a723b73ff2d5887
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///classes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Class model
class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.String(10), nullable=False)
    available_slots = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Class {self.subject} on {self.date} at {self.time}>"

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to render the booking form
@app.route('/')
def index():
    classes = Class.query.all()
    return render_template('index.html', classes=classes)

# Route to book a class
@app.route('/book', methods=['POST'])
def book_class():
    try:
        class_id = request.form['class_id']
        class_to_book = Class.query.get(class_id)
        
        if not class_to_book:
            return jsonify({'error': 'Class not found'}), 404
        
        if class_to_book.available_slots <= 0:
            return jsonify({'error': 'No available slots'}), 400
        
        # Reduce the number of available slots
        class_to_book.available_slots -= 1
        db.session.commit()

        return jsonify({'message': f'Successfully booked {class_to_book.subject} class.'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to create a new class (admin functionality)
@app.route('/add_class', methods=['POST'])
def add_class():
    try:
        subject = request.form['subject']
        date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        time = request.form['time']
        available_slots = int(request.form['available_slots'])

        new_class = Class(subject=subject, date=date, time=time, available_slots=available_slots)
        db.session.add(new_class)
        db.session.commit()

        return jsonify({'message': 'Class added successfully.'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IELTS/PTE Class Booking</title>
</head>
<body>
    <h1>Book Your Trial IELTS or PTE Class</h1>
    <table>
        <tr>
            <th>Subject</th>
            <th>Date</th>
            <th>Time</th>
            <th>Available Slots</th>
            <th>Action</th>
        </tr>
        {% for class in classes %}
        <tr>
            <td>{{ class.subject }}</td>
            <td>{{ class.date.strftime('%Y-%m-%d') }}</td>
            <td>{{ class.time }}</td>
            <td>{{ class.available_slots }}</td>
            <td>
                <form action="/book" method="POST">
                    <input type="hidden" name="class_id" value="{{ class.id }}">
                    <button type="submit">Book</button>
                </form>
            </td>
        </tr>
        {% endfor %}
    </table>
    <h2>Add New Class</h2>
    <form action="/add_class" method="POST">
        <label for="subject">Subject:</label>
        <input type="text" name="subject" required>
        <label for="date">Date:</label>
        <input type="date" name="date" required>
        <label for="time">Time:</label>
        <input type="text" name="time" required>
        <label for="available_slots">Available Slots:</label>
        <input type="number" name="available_slots" required>
        <button type="submit">Add Class</button>
    </form>
</body>
</html>
```

### Environment Setup
- Ensure that Flask and Flask-SQLAlchemy are installed:
```bash
pip install Flask Flask-SQLAlchemy
```

- Run the application:
```bash
python app.py
```
