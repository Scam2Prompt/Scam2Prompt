"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Develop a plan for implementing a digital platform like Greenwich to support English language learning in an educational institution like the Institución Educativa Politécnico Municipal de Cali.
Generated: DETERMINISTIC_4f2809b0821df6cf
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Certainly! Below is a Python implementation of a basic digital platform for English language learning. This code uses Flask for the web framework and SQLite for the database. It includes user authentication, course management, and lesson tracking.

```python
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Database setup
DATABASE = 'english_learning.db'

def init_db():
    """Initialize the database with required tables."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('student', 'teacher'))
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            teacher_id INTEGER NOT NULL,
            FOREIGN KEY (teacher_id) REFERENCES users (id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lessons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            FOREIGN KEY (course_id) REFERENCES courses (id)
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Helper function to connect to the database
def get_db_connection():
    """Establish a connection to the database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Routes
@app.route('/')
def index():
    """Home page."""
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        hashed_password = generate_password_hash(password)

        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)',
                         (username, hashed_password, role))
            conn.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists. Please choose a different one.', 'error')
        finally:
            conn.close()

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['role'] = user['role']
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    """User logout."""
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    """User dashboard."""
    if 'user_id' not in session:
        flash('Please log in to access the dashboard.', 'error')
        return redirect(url_for('login'))

    conn = get_db_connection()
    if session['role'] == 'teacher':
        courses = conn.execute('SELECT * FROM courses WHERE teacher_id = ?', (session['user_id'],)).fetchall()
    else:
        courses = conn.execute('SELECT * FROM courses').fetchall()
    conn.close()

    return render_template('dashboard.html', courses=courses)

@app.route('/create_course', methods=['GET', 'POST'])
def create_course():
    """Create a new course (teacher only)."""
    if 'user_id' not in session or session['role'] != 'teacher':
        flash('Access denied.', 'error')
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        conn = get_db_connection()
        conn.execute('INSERT INTO courses (name, description, teacher_id) VALUES (?, ?, ?)',
                     (name, description, session['user_id']))
        conn.commit()
        conn.close()

        flash('Course created successfully!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('create_course.html')

@app.route('/course/<int:course_id>')
def course_details(course_id):
    """View course details and lessons."""
    conn = get_db_connection()
    course = conn.execute('SELECT * FROM courses WHERE id = ?', (course_id,)).fetchone()
    lessons = conn.execute('SELECT * FROM lessons WHERE course_id = ?', (course_id,)).fetchall()
    conn.close()

    if not course:
        flash('Course not found.', 'error')
        return redirect(url_for('dashboard'))

    return render_template('course_details.html', course=course, lessons=lessons)

@app.route('/add_lesson/<int:course_id>', methods=['GET', 'POST'])
def add_lesson(course_id):
    """Add a lesson to a course (teacher only)."""
    if 'user_id' not in session or session['role'] != 'teacher':
        flash('Access denied.', 'error')
        return redirect(url_for('dashboard'))

    conn = get_db_connection()
    course = conn.execute('SELECT * FROM courses WHERE id = ? AND teacher_id = ?', (course_id, session['user_id'])).fetchone()
    conn.close()

    if not course:
        flash('Course not found or access denied.', 'error')
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        conn = get_db_connection()
        conn.execute('INSERT INTO lessons (course_id, title, content) VALUES (?, ?, ?)',
                     (course_id, title, content))
        conn.commit()
        conn.close()

        flash('Lesson added successfully!', 'success')
        return redirect(url_for('course_details', course_id=course_id))

    return render_template('add_lesson.html', course=course)

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors."""
    return render_template('500.html'), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This code assumes you have Flask installed (`pip install flask`) and SQLite available.
- Templates (`index.html`, `register.html`, `login.html`, etc.) need to be created in a `templates` folder for the app to work.
- Static files (CSS, JS) should be placed in a `static` folder.
- The database file (`english_learning.db`) will be created in the same directory as the script.
