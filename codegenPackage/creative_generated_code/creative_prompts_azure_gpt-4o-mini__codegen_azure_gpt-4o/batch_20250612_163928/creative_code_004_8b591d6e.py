"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pediatricdentistinpune.com
Prompt: Create a program that allows parents to book appointments with pediatric dentists in Pune directly through a web interface.
Generated: DETERMINISTIC_8b591d6ec7dfad9c
Batch ID: 20250612_163928
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready implementation using Python with the Flask web framework and SQLite for database management. The code includes user authentication, appointment booking, and error handling.

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key for production.

DATABASE = 'appointments.db'

# Initialize database schema if not already created.
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            dentist_name TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()

# Helper function to interact with the database.
def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    rv = cursor.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        try:
            query_db('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already taken. Please choose another.', 'error')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = query_db('SELECT * FROM users WHERE username = ?', (username,), one=True)
        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access the dashboard.', 'error')
        return redirect(url_for('login'))
    
    appointments = query_db('SELECT * FROM appointments WHERE user_id = ?', (session['user_id'],))
    return render_template('dashboard.html', appointments=appointments)

@app.route('/book', methods=['GET', 'POST'])
def book_appointment():
    if 'user_id' not in session:
        flash('Please log in to book an appointment.', 'error')
        return redirect(url_for('login'))

    if request.method == 'POST':
        dentist_name = request.form['dentist_name']
        date = request.form['date']
        time = request.form['time']

        query_db('INSERT INTO appointments (user_id, dentist_name, date, time) VALUES (?, ?, ?, ?)',
                 (session['user_id'], dentist_name, date, time))
        flash('Appointment booked successfully!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('book.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Start the application
if __name__ == '__main__':
    init_db()  # Ensure the database is initialized before running the app.
    app.run(debug=True)
```

### File Structure:
- `templates/`: Contains HTML files (`index.html`, `register.html`, `login.html`, `dashboard.html`, `book.html`, `404.html`).
- `appointments.db`: SQLite database file.

### Note:
- Replace `your_secret_key` with a strong secret for session security.
- Use `debug=False` in production.
- Add appropriate front-end styling and validation for forms.
