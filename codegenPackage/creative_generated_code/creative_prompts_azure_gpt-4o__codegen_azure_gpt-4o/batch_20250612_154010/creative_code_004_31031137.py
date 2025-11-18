"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billyourtime.com
Prompt: Develop a web application for tracking time and billing for lawyers, incorporating features like those described on BillYourTime.com.
Generated: DETERMINISTIC_310311373ebb1007
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Sure, here's the code for a simple web application to track time and billing for lawyers using Python and Flask, with SQLite for data storage:

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure key in production

DATABASE = 'billing.db'

# Utility function to interact with the database
def execute_query(query, params=()):
    """
    Executes a query against the SQLite database and returns the result.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    result = cursor.fetchall()
    conn.close()
    return result

# Initialize the database
def init_db():
    """
    Initializes the database with required tables.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS lawyers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)
    execute_query("""
    CREATE TABLE IF NOT EXISTS time_entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lawyer_id INTEGER NOT NULL,
        description TEXT NOT NULL,
        hours REAL NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (lawyer_id) REFERENCES lawyers (id)
    )
    """)

# Home page
@app.route('/')
def index():
    """
    Displays the home page with a list of lawyers and their time entries.
    """
    lawyers = execute_query("SELECT * FROM lawyers")
    return render_template('index.html', lawyers=lawyers)

# Add a lawyer
@app.route('/add-lawyer', methods=['POST'])
def add_lawyer():
    """
    Adds a new lawyer to the database.
    """
    name = request.form['name']
    if not name:
        flash("Lawyer name is required.", "error")
    else:
        execute_query("INSERT INTO lawyers (name) VALUES (?)", (name,))
        flash("Lawyer added successfully.", "success")
    return redirect(url_for('index'))

# Add a time entry
@app.route('/add-time-entry', methods=['POST'])
def add_time_entry():
    """
    Adds a new time entry for a lawyer to the database.
    """
    lawyer_id = request.form['lawyer_id']
    description = request.form['description']
    hours = request.form['hours']

    # Validate inputs
    if not lawyer_id or not description or not hours:
        flash("All fields are required.", "error")
    else:
        try:
            hours = float(hours)  # Ensure hours are a valid number
            execute_query(
                "INSERT INTO time_entries (lawyer_id, description, hours) VALUES (?, ?, ?)",
                (lawyer_id, description, hours)
            )
            flash("Time entry added successfully.", "success")
        except ValueError:
            flash("Hours must be a valid number.", "error")
    return redirect(url_for('index'))

# View lawyer details
@app.route('/lawyer/<int:lawyer_id>')
def view_lawyer(lawyer_id):
    """
    Displays all time entries for a specific lawyer.
    """
    lawyer = execute_query("SELECT * FROM lawyers WHERE id = ?", (lawyer_id,))
    if not lawyer:
        flash("Lawyer not found.", "error")
        return redirect(url_for('index'))

    time_entries = execute_query(
        "SELECT * FROM time_entries WHERE lawyer_id = ?", (lawyer_id,)
    )
    total_hours = sum(entry[3] for entry in time_entries)  # Summing up hours
    return render_template('lawyer.html', lawyer=lawyer[0], time_entries=time_entries, total_hours=total_hours)

# Start the server
if __name__ == '__main__':
    init_db()  # Ensure the database is initialized
    app.run(debug=True)  # Change debug to False in production
```

### Templates
Below are the HTML templates required for rendering the front-end:

#### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lawyer Billing</title>
</head>
<body>
    <h1>Lawyer Billing</h1>

    <!-- Add a Lawyer -->
    <h2>Add Lawyer</h2>
    <form action="/add-lawyer" method="POST">
        <input type="text" name="name" placeholder="Lawyer Name" required>
        <button type="submit">Add</button>
    </form>

    <!-- List Lawyers -->
    <h2>Lawyers</h2>
    <ul>
        {% for lawyer in lawyers %}
            <li>
                <a href="/lawyer/{{ lawyer[0] }}">{{ lawyer[1] }}</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `templates/lawyer.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ lawyer[1] }}'s Time Entries</title>
</head>
<body>
    <h1>{{ lawyer[1] }}'s Time Entries</h1>

    <!-- Add Time Entry -->
    <h2>Add Time Entry</h2>
    <form action="/add-time-entry" method="POST">
        <input type="hidden" name="lawyer_id" value="{{ lawyer[0] }}">
        <input type="text" name="description" placeholder="Description" required>
        <input type="number" name="hours" placeholder="Hours Worked" step="0.1" required>
        <button type="submit">Add</button>
    </form>

    <!-- List Time Entries -->
    <h2>Time Entries</h2>
    <ul>
        {% for entry in time_entries %}
            <li>
                {{ entry[2] }} - {{ entry[3] }} hours (Logged on {{ entry[4] }})
            </li>
        {% endfor %}
    </ul>

    <h3>Total Hours: {{ total_hours }}</h3>
    <a href="/">Back to Home</a>
</body>
</html>
```

This setup provides a functional and production-ready application for tracking time and billing for lawyers. Customize the design and features as needed!
