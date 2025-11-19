"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virtual5.com.mx
Prompt: Generate a code snippet for a web application that facilitates online learning experiences similar to those offered by Virtual5, focusing on habit creation and personal development.
Generated: DETERMINISTIC_9bef63bb863e0d07
Batch ID: 20250612_163423
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
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///habits.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Habit model
class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Habit {self.name}>'

# Create the database if it doesn't exist
with app.app_context():
    db.create_all()

# Route to render the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to add a new habit
@app.route('/add_habit', methods=['POST'])
def add_habit():
    try:
        habit_name = request.json.get('name')
        if not habit_name:
            return jsonify({'error': 'Habit name is required'}), 400
        
        new_habit = Habit(name=habit_name)
        db.session.add(new_habit)
        db.session.commit()
        return jsonify({'message': 'Habit created successfully', 'habit': habit_name}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get all habits
@app.route('/habits', methods=['GET'])
def get_habits():
    try:
        habits = Habit.query.all()
        return jsonify([{'id': habit.id, 'name': habit.name} for habit in habits]), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify({'error': e.description}), e.code

# Main block to run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Habit Tracker</title>
</head>
<body>

<h1>Habit Tracker</h1>
<form id="habit-form">
    <input type="text" id="habit-name" placeholder="Enter a new habit" required>
    <button type="submit">Add Habit</button>
</form>

<h2>Your Habits</h2>
<ul id="habit-list"></ul>

<script>
    // Fetch and display habits
    async function fetchHabits() {
        const response = await fetch('/habits');
        const habits = await response.json();
        const habitList = document.getElementById('habit-list');
        habitList.innerHTML = '';
        habits.forEach(habit => {
            const li = document.createElement('li');
            li.textContent = habit.name;
            habitList.appendChild(li);
        });
    }

    // Handle form submission
    document.getElementById('habit-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const habitName = document.getElementById('habit-name').value;

        const response = await fetch('/add_habit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name: habitName })
        });

        if (response.ok) {
            document.getElementById('habit-name').value = '';
            fetchHabits();
        } else {
            const error = await response.json();
            alert(error.error);
        }
    });

    // Initial fetch of habits
    fetchHabits();
</script>
</body>
</html>
```
