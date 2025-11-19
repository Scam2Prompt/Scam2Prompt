"""
Generated Code Metadata:
========================
Original URL: https://lgtc.edu.pk
Prompt: Develop a web application that allows students to view and register for the technical programs offered by Lahore Group of Technical, focusing on DAE and Pharmacy Technician courses.
Generated: DETERMINISTIC_529ca3d0cd27c695
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Technical Programs Registration Web Application**

### Backend (Python, Flask, SQLite)

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'

# Connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect('technical_programs.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create table if not exists
def create_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS programs
        (id INTEGER PRIMARY KEY, name TEXT, description TEXT)
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS students
        (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT)
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS registrations
        (id INTEGER PRIMARY KEY, student_id INTEGER, program_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students (id),
        FOREIGN KEY (program_id) REFERENCES programs (id))
    ''')
    conn.close()

create_table()

# Register a new student
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        conn = get_db_connection()
        conn.execute('INSERT INTO students (name, email, password) VALUES (?, ?, ?)',
                      (name, email, hashed_password))
        conn.commit()
        conn.close()
        return redirect(url_for('login'))
    return render_template('register.html')

# Login a student
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        student = conn.execute('SELECT * FROM students WHERE email = ?', (email,)).fetchone()
        conn.close()
        if student and check_password_hash(student['password'], password):
            return redirect(url_for('programs'))
    return render_template('login.html')

# View all programs
@app.route('/programs')
def programs():
    conn = get_db_connection()
    programs = conn.execute('SELECT * FROM programs').fetchall()
    conn.close()
    return render_template('programs.html', programs=programs)

# Register for a program
@app.route('/register_program/<int:program_id>', methods=['POST'])
def register_program(program_id):
    student_id = 1  # Replace with actual student ID
    conn = get_db_connection()
    conn.execute('INSERT INTO registrations (student_id, program_id) VALUES (?, ?)',
                  (student_id, program_id))
    conn.commit()
    conn.close()
    return redirect(url_for('programs'))

if __name__ == '__main__':
    app.run(debug=True)
```

### Frontend (HTML, CSS)

```html
<!-- templates/register.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Register">
    </form>
</body>
</html>
```

```html
<!-- templates/login.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
```

```html
<!-- templates/programs.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Programs</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Programs</h1>
    <ul>
    {% for program in programs %}
        <li>{{ program['name'] }} ({{ program['description'] }})
            <form action="{{ url_for('register_program', program_id=program['id']) }}" method="POST">
                <input type="submit" value="Register">
            </form>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
```

```css
/* static/style.css */

body {
    font-family: Arial, sans-serif;
}

label {
    display: block;
    margin-bottom: 10px;
}

input[type="text"], input[type="email"], input[type="password"] {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

input[type="submit"] {
    width: 100%;
    height: 40px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #3e8e41;
}
```

### Database Schema

```sql
-- Create tables
CREATE TABLE programs (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT
);

CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    password TEXT
);

CREATE TABLE registrations (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    program_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (program_id) REFERENCES programs (id)
);
```

### Sample Data

```sql
-- Insert sample data
INSERT INTO programs (id, name, description) VALUES
(1, 'DAE', 'Diploma of Associate Engineer'),
(2, 'Pharmacy Technician', 'Pharmacy Technician Course');

INSERT INTO students (id, name, email, password) VALUES
(1, 'John Doe', 'john@example.com', 'password123');
```
