"""
Generated Code Metadata:
========================
Original URL: https://dbcop.org
Prompt: Provide an example of a web application that could facilitate online admission processes similar to those at DBCOP, including necessary features.
Generated: DETERMINISTIC_6fa441670f2b635a
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
# A simple web application for online admission processes using Flask

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for session management and flash messages

DATABASE = 'admissions.db'

# Helper function to connect to the database
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# Route: Home page
@app.route('/')
def index():
    return render_template('index.html')

# Route: Admission form
@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':
        # Collect form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        course = request.form.get('course')

        # Validate form data
        if not name or not email or not phone or not course:
            flash('All fields are required!', 'error')
            return redirect(url_for('apply'))

        # Save data to the database
        conn = get_db_connection()
        if conn:
            try:
                conn.execute(
                    'INSERT INTO applications (name, email, phone, course) VALUES (?, ?, ?, ?)',
                    (name, email, phone, course)
                )
                conn.commit()
                flash('Application submitted successfully!', 'success')
            except sqlite3.Error as e:
                flash(f'Error saving application: {e}', 'error')
            finally:
                conn.close()
        else:
            flash('Database connection error!', 'error')

        return redirect(url_for('index'))

    return render_template('apply.html')

# Route: View applications (Admin view)
@app.route('/applications')
def applications():
    conn = get_db_connection()
    if conn:
        try:
            applications = conn.execute('SELECT * FROM applications').fetchall()
            return render_template('applications.html', applications=applications)
        except sqlite3.Error as e:
            flash(f'Error fetching applications: {e}', 'error')
        finally:
            conn.close()
    else:
        flash('Database connection error!', 'error')

    return redirect(url_for('index'))

# Initialize the database
def init_db():
    conn = get_db_connection()
    if conn:
        try:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS applications (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    course TEXT NOT NULL
                )
            ''')
            conn.commit()
        except sqlite3.Error as e:
            print(f'Error initializing database: {e}')
        finally:
            conn.close()

# Main entry point
if __name__ == '__main__':
    init_db()  # Ensure the database is initialized
    app.run(debug=True)

```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Online Admission Portal</title>
</head>
<body>
    <h1>Welcome to the Online Admission Portal</h1>
    <a href="/apply">Apply for Admission</a>
    <a href="/applications">View Applications (Admin)</a>
</body>
</html>
```

```html
<!-- templates/apply.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apply for Admission</title>
</head>
<body>
    <h1>Admission Form</h1>
    <form method="POST" action="/apply">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" required><br>
        <label for="course">Course:</label>
        <input type="text" id="course" name="course" required><br>
        <button type="submit">Submit</button>
    </form>
    <a href="/">Back to Home</a>
</body>
</html>
```

```html
<!-- templates/applications.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Applications</title>
</head>
<body>
    <h1>Submitted Applications</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Course</th>
        </tr>
        {% for application in applications %}
        <tr>
            <td>{{ application['id'] }}</td>
            <td>{{ application['name'] }}</td>
            <td>{{ application['email'] }}</td>
            <td>{{ application['phone'] }}</td>
            <td>{{ application['course'] }}</td>
        </tr>
        {% endfor %}
    </table>
    <a href="/">Back to Home</a>
</body>
</html>
```
