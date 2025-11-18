"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trentino.edu.pe
Prompt: Develop a web application for managing workshops and events, inspired by the "Cursos - Talleres" and "Eventos" sections of the Trentino website.
Generated: DETERMINISTIC_4015e7c00f1c3794
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready implementation for a web application for managing workshops and events using Python's Flask framework:

```python
from flask import Flask, request, jsonify, render_template
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = 'event_manager.db'


def init_db():
    """Initialize the SQLite database with required tables."""
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS workshops (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            date TEXT NOT NULL,
            location TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            date TEXT NOT NULL,
            location TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()


# Initialize database
init_db()


# Routes
@app.route('/')
def home():
    """Render the homepage."""
    return render_template('index.html')


@app.route('/workshops', methods=['GET', 'POST'])
def manage_workshops():
    """
    Handle workshop management:
    - GET: Fetch all workshops
    - POST: Add a new workshop
    """
    if request.method == 'GET':
        try:
            connection = sqlite3.connect(DATABASE)
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM workshops')
            workshops = cursor.fetchall()
            connection.close()
            return jsonify(workshops)
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    elif request.method == 'POST':
        try:
            data = request.json
            title = data.get('title')
            description = data.get('description', '')
            date = data.get('date')
            location = data.get('location')

            if not title or not date or not location:
                return jsonify({'error': 'Missing required fields'}), 400

            # Validate date format
            try:
                datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                return jsonify({'error': 'Invalid date format, expected YYYY-MM-DD'}), 400

            connection = sqlite3.connect(DATABASE)
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO workshops (title, description, date, location) VALUES (?, ?, ?, ?)',
                (title, description, date, location)
            )
            connection.commit()
            connection.close()
            return jsonify({'message': 'Workshop added successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500


@app.route('/events', methods=['GET', 'POST'])
def manage_events():
    """
    Handle event management:
    - GET: Fetch all events
    - POST: Add a new event
    """
    if request.method == 'GET':
        try:
            connection = sqlite3.connect(DATABASE)
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM events')
            events = cursor.fetchall()
            connection.close()
            return jsonify(events)
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    elif request.method == 'POST':
        try:
            data = request.json
            name = data.get('name')
            description = data.get('description', '')
            date = data.get('date')
            location = data.get('location')

            if not name or not date or not location:
                return jsonify({'error': 'Missing required fields'}), 400

            # Validate date format
            try:
                datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                return jsonify({'error': 'Invalid date format, expected YYYY-MM-DD'}), 400

            connection = sqlite3.connect(DATABASE)
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO events (name, description, date, location) VALUES (?, ?, ?, ?)',
                (name, description, date, location)
            )
            connection.commit()
            connection.close()
            return jsonify({'message': 'Event added successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500


@app.route('/workshops/<int:workshop_id>', methods=['DELETE'])
def delete_workshop(workshop_id):
    """Delete a workshop by its ID."""
    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute('DELETE FROM workshops WHERE id = ?', (workshop_id,))
        connection.commit()
        connection.close()

        if cursor.rowcount == 0:
            return jsonify({'error': 'Workshop not found'}), 404

        return jsonify({'message': 'Workshop deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    """Delete an event by its ID."""
    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute('DELETE FROM events WHERE id = ?', (event_id,))
        connection.commit()
        connection.close()

        if cursor.rowcount == 0:
            return jsonify({'error': 'Event not found'}), 404

        return jsonify({'message': 'Event deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Accompanying HTML Template (index.html)
Create a file named `templates/index.html` for the homepage:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Workshop & Event Manager</title>
</head>
<body>
    <h1>Welcome to the Workshop & Event Manager</h1>
    <p>Use the API endpoints to manage workshops and events.</p>
</body>
</html>
```

### Notes:
1. Install required dependencies: `pip install flask`
2. The SQLite database file (`event_manager.db`) will be created automatically when the application runs.
3. Error handling and input validation are implemented.
4. APIs are designed to follow REST principles.
