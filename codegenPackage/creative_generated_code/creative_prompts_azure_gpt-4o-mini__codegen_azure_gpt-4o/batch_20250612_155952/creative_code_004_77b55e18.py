"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lzero.us
Prompt: Design a simple web application that displays the schedule and details of the basketball training camps offered by L-Zero, allowing users to register directly through the app.
Generated: DETERMINISTIC_77b55e187a673888
Batch ID: 20250612_155952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required libraries for the web application
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.exceptions import HTTPException
import sqlite3

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = "your_secret_key"

# Database file for storing camp information and registrations
DATABASE = 'training_camps.db'


# Function to initialize the database
def initialize_db():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    
    # Create table for camps
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS camps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT NOT NULL,
            location TEXT NOT NULL,
            description TEXT
        )
    ''')

    # Create table for registrations
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            camp_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            FOREIGN KEY (camp_id) REFERENCES camps(id)
        )
    ''')

    connection.commit()
    connection.close()


# Route: Home page, displaying all available camps
@app.route('/')
def index():
    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM camps')
        camps = cursor.fetchall()
        connection.close()
        return render_template('index.html', camps=camps)
    except Exception as e:
        flash(f"An error occurred while fetching the camps: {e}")
        return render_template('error.html')


# Route: Registration page for a specific camp
@app.route('/register/<int:camp_id>', methods=['GET', 'POST'])
def register(camp_id):
    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        # Fetch camp details
        cursor.execute('SELECT * FROM camps WHERE id = ?', (camp_id,))
        camp = cursor.fetchone()

        if not camp:
            flash("Camp not found.")
            return redirect(url_for('index'))

        if request.method == 'POST':
            # Collect user registration details
            name = request.form['name']
            email = request.form['email']
            phone = request.form.get('phone', '')

            if not name or not email:
                flash("Name and Email are required!")
                return render_template('register.html', camp=camp)

            # Insert registration data into database
            cursor.execute('''
                INSERT INTO registrations (camp_id, name, email, phone)
                VALUES (?, ?, ?, ?)
            ''', (camp_id, name, email, phone))
            
            connection.commit()
            connection.close()
            flash("Registration successful!")
            return redirect(url_for('index'))

        connection.close()
        return render_template('register.html', camp=camp)
    except Exception as e:
        flash(f"An error occurred during registration: {e}")
        return render_template('error.html')


# Route: Admin page to add training camps (for demonstration purposes)
@app.route('/admin/add_camp', methods=['GET', 'POST'])
def add_camp():
    if request.method == 'POST':
        try:
            name = request.form['name']
            date = request.form['date']
            location = request.form['location']
            description = request.form.get('description', '')

            if not name or not date or not location:
                flash("Name, Date, and Location are required!")
                return render_template('add_camp.html')

            connection = sqlite3.connect(DATABASE)
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO camps (name, date, location, description)
                VALUES (?, ?, ?, ?)
            ''', (name, date, location, description))
            
            connection.commit()
            connection.close()
            flash("Camp added successfully!")
            return redirect(url_for('index'))
        except Exception as e:
            flash(f"An error occurred while adding the camp: {e}")
            return render_template('error.html')

    return render_template('add_camp.html')


# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return render_template('error.html', error=str(e)), e.code


# Error handling for generic exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return render_template('error.html', error=str(e)), 500


# Initialize the database before starting the app
initialize_db()


# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates:
Place the following HTML files in a `templates` directory.

#### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Training Camps</title>
</head>
<body>
    <h1>Basketball Training Camps</h1>
    <ul>
        {% for camp in camps %}
        <li>
            <strong>{{ camp[1] }}</strong> - {{ camp[2] }} at {{ camp[3] }}
            <br>
            {{ camp[4] }}
            <br>
            <a href="{{ url_for('register', camp_id=camp[0]) }}">Register</a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `register.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Register</title>
</head>
<body>
    <h1>Register for {{ camp[1] }}</h1>
    <form method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone">
        <br>
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

#### `add_camp.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add Training Camp</title>
</head>
<body>
    <h1>Add a Basketball Training Camp</h1>
    <form method="post">
        <label for="name">Camp Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="date">Date:</label>
        <input type="date" id="date" name="date" required>
        <br>
        <label for="location">Location:</label>
        <input type="text" id="location" name="location" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea>
        <br>
        <button type="submit">Add Camp</button>
    </form>
</body>
</html>
```

#### `error.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Error</title>
</head>
<body>
    <h1>An error occurred</h1>
    <p>{{ error }}</p>
</body>
</html>
```
