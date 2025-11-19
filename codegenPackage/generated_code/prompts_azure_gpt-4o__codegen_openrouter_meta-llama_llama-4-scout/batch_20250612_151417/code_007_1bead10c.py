"""
Generated Code Metadata:
========================
Original URL: https://excelwithsmart.com
Prompt: Create a dashboard for tracking the progress of placement training programs across multiple colleges, inspired by SMART Training Resources' widespread operations.
Generated: DETERMINISTIC_1bead10cf0868502
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Placement Training Program Dashboard**
=====================================

### Dependencies

This code uses Python 3.8+, Flask 2.0+, and SQLite 3.

### Code

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

# Database connection settings
DATABASE_NAME = 'placement_training.db'

# Create database connection
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        return conn
    except Error as e:
        print(e)

# Create table for colleges
def create_college_table(conn):
    sql = """
        CREATE TABLE IF NOT EXISTS colleges (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            location TEXT NOT NULL
        )
    """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

# Create table for training programs
def create_program_table(conn):
    sql = """
        CREATE TABLE IF NOT EXISTS programs (
            id INTEGER PRIMARY KEY,
            college_id INTEGER NOT NULL,
            program_name TEXT NOT NULL,
            start_date DATE NOT NULL,
            end_date DATE NOT NULL,
            FOREIGN KEY (college_id) REFERENCES colleges (id)
        )
    """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

# Create table for program progress
def create_progress_table(conn):
    sql = """
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY,
            program_id INTEGER NOT NULL,
            student_count INTEGER NOT NULL,
            completion_rate REAL NOT NULL,
            FOREIGN KEY (program_id) REFERENCES programs (id)
        )
    """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

# Initialize database
def init_db():
    conn = create_connection()
    with conn:
        create_college_table(conn)
        create_program_table(conn)
        create_progress_table(conn)
    conn.close()

# Initialize database
init_db()

# Route for dashboard
@app.route('/')
def dashboard():
    conn = create_connection()
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM colleges")
        colleges = c.fetchall()
        c.execute("SELECT * FROM programs")
        programs = c.fetchall()
        c.execute("SELECT * FROM progress")
        progress = c.fetchall()
    conn.close()
    return render_template('dashboard.html', colleges=colleges, programs=programs, progress=progress)

# Route for adding college
@app.route('/add_college', methods=['POST'])
def add_college():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        conn = create_connection()
        with conn:
            c = conn.cursor()
            c.execute("INSERT INTO colleges (name, location) VALUES (?, ?)", (name, location))
        conn.close()
        return redirect(url_for('dashboard'))

# Route for adding program
@app.route('/add_program', methods=['POST'])
def add_program():
    if request.method == 'POST':
        college_id = request.form['college_id']
        program_name = request.form['program_name']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        conn = create_connection()
        with conn:
            c = conn.cursor()
            c.execute("INSERT INTO programs (college_id, program_name, start_date, end_date) VALUES (?, ?, ?, ?)", 
                      (college_id, program_name, start_date, end_date))
        conn.close()
        return redirect(url_for('dashboard'))

# Route for adding progress
@app.route('/add_progress', methods=['POST'])
def add_progress():
    if request.method == 'POST':
        program_id = request.form['program_id']
        student_count = request.form['student_count']
        completion_rate = request.form['completion_rate']
        conn = create_connection()
        with conn:
            c = conn.cursor()
            c.execute("INSERT INTO progress (program_id, student_count, completion_rate) VALUES (?, ?, ?)", 
                      (program_id, student_count, completion_rate))
        conn.close()
        return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/dashboard.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Placement Training Program Dashboard</title>
</head>
<body>
    <h1>Placement Training Program Dashboard</h1>
    <h2>Colleges</h2>
    <ul>
    {% for college in colleges %}
        <li>{{ college[1] }} ({{ college[2] }})</li>
    {% endfor %}
    </ul>

    <h2>Programs</h2>
    <ul>
    {% for program in programs %}
        <li>{{ program[2] }} ({{ program[3] }} - {{ program[4] }})</li>
    {% endfor %}
    </ul>

    <h2>Progress</h2>
    <ul>
    {% for prog in progress %}
        <li>Program {{ prog[1] }}: {{ prog[2] }} students, {{ prog[3] }}% completion rate</li>
    {% endfor %}
    </ul>

    <form action="{{ url_for('add_college') }}" method="post">
        <label for="name">College Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="location">Location:</label>
        <input type="text" id="location" name="location"><br><br>
        <input type="submit" value="Add College">
    </form>

    <form action="{{ url_for('add_program') }}" method="post">
        <label for="college_id">College ID:</label>
        <input type="text" id="college_id" name="college_id"><br><br>
        <label for="program_name">Program Name:</label>
        <input type="text" id="program_name" name="program_name"><br><br>
        <label for="start_date">Start Date:</label>
        <input type="date" id="start_date" name="start_date"><br><br>
        <label for="end_date">End Date:</label>
        <input type="date" id="end_date" name="end_date"><br><br>
        <input type="submit" value="Add Program">
    </form>

    <form action="{{ url_for('add_progress') }}" method="post">
        <label for="program_id">Program ID:</label>
        <input type="text" id="program_id" name="program_id"><br><br>
        <label for="student_count">Student Count:</label>
        <input type="text" id="student_count" name="student_count"><br><br>
        <label for="completion_rate">Completion Rate:</label>
        <input type="text" id="completion_rate" name="completion_rate"><br><br>
        <input type="submit" value="Add Progress">
    </form>
</body>
</html>
```
