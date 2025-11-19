"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Develop a simple web application that allows users to browse and request repairs for agricultural machinery, inspired by the repair services offered by SARL VERDIER.
Generated: DETERMINISTIC_d905adacb8dfeac3
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is a simple web application written in Python using the Flask framework. This application allows users to browse available agricultural machinery and request repairs for them. 

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# SQLite database configuration
DATABASE = 'repair_service.db'

def get_db_connection():
    """Establishes and returns a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    """Homepage route that lists available agricultural machinery."""
    conn = get_db_connection()
    machines = conn.execute('SELECT * FROM machinery').fetchall()
    conn.close()
    return render_template('index.html', machines=machines)

@app.route('/request_repair/<int:machine_id>', methods=['GET', 'POST'])
def request_repair(machine_id):
    """
    Repair request route.
    Handles GET requests to display the repair form and POST requests to submit a repair request.
    """
    conn = get_db_connection()
    machine = conn.execute('SELECT * FROM machinery WHERE id = ?', (machine_id,)).fetchone()
    conn.close()

    if machine is None:
        flash("Machine not found!", 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        issue_description = request.form['issue_description']

        # Basic input validation
        if not name or not email or not issue_description:
            flash("All fields are required!", 'error')
            return render_template('request_repair.html', machine=machine)

        # Insert repair request into the database
        conn = get_db_connection()
        conn.execute('INSERT INTO repair_requests (machine_id, name, email, issue_description) VALUES (?, ?, ?, ?)',
                     (machine_id, name, email, issue_description))
        conn.commit()
        conn.close()

        flash("Repair request submitted successfully!", 'success')
        return redirect(url_for('index'))

    return render_template('request_repair.html', machine=machine)


@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page."""
    return render_template('404.html'), 404


# Initialize the database and create tables
def init_db():
    """Initializes the SQLite database with the necessary tables."""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS machinery (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS repair_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            machine_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            issue_description TEXT NOT NULL,
            FOREIGN KEY (machine_id) REFERENCES machinery (id)
        )
    ''')
    conn.close()


if __name__ == '__main__':
    # Initialize database on first run
    init_db()
    app.run(debug=True)
```

### Templates

#### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Repair Services</title>
</head>
<body>
    <h1>Agricultural Machinery</h1>
    <ul>
        {% for machine in machines %}
        <li>
            <strong>{{ machine['name'] }}</strong>: {{ machine['description'] }}
            <a href="{{ url_for('request_repair', machine_id=machine['id']) }}">Request Repair</a>
        </li>
        {% endfor %}
    </ul>
    {% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        <ul>
            {% for category, message in messages %}
            <li><strong>{{ category }}</strong>: {{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}
    {% endwith %}
</body>
</html>
```

#### `templates/request_repair.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Request Repair</title>
</head>
<body>
    <h1>Request Repair for {{ machine['name'] }}</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>
        <label for="issue_description">Issue Description:</label><br>
        <textarea id="issue_description" name="issue_description" required></textarea><br>
        <button type="submit">Submit Repair Request</button>
    </form>
</body>
</html>
```

#### `templates/404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you're looking for doesn't exist.</p>
    <a href="{{ url_for('index') }}">Go back to homepage</a>
</body>
</html>
```

### Instructions:
1. Save the Python code to a file named `app.py`.
2. Create a `templates` folder and save the HTML code in corresponding files (`index.html`, `request_repair.html`, `404.html`).
3. Run the application with `python app.py`.
4. Visit `http://127.0.0.1:5000` in your browser.

This is a basic implementation that can be extended with more functionality, such as user authentication, image uploads for machinery, and email notifications for repair requests.
