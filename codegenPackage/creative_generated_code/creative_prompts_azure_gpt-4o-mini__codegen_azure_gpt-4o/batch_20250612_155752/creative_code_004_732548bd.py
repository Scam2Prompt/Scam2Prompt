"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonanzavc.com
Prompt: How do I create a secure login system for a membership-based website like BonanzaVC that includes both username and password authentication?
Generated: DETERMINISTIC_732548bd627ee49e
Batch ID: 20250612_155752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python implementation using Flask for building a secure login system. It uses hashed passwords for security and includes error handling. You can expand this for a production-ready membership-based website like BonanzaVC.  

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'YourSuperSecretKey'  # Replace with a strong secret key for production

# Database setup
DATABASE = 'users.db'

def init_db():
    """Initializes the SQLite database with a users table."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

def get_db_connection():
    """Returns a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except sqlite3.Error as e:
        print(f"Database connection failed: {e}")
        return None

@app.route('/')
def home():
    """Home page route."""
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handles user registration."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash("Username and password are required!", "error")
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='sha256')

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("Username already exists. Please choose another.", "error")
        finally:
            conn.close()

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles user login."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash("Username and password are required!", "error")
            return redirect(url_for('login'))

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            flash("Login successful!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid username or password.", "error")

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """Protected route for logged-in users."""
    if 'user_id' not in session:
        flash("Please log in to access the dashboard.", "error")
        return redirect(url_for('login'))

    return render_template('dashboard.html', username=session.get('username'))

@app.route('/logout')
def logout():
    """Handles user logout."""
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

# ** HTML Templates (Brief Overview) **
# 1. `index.html`: A simple landing page with links to login and register.
# 2. `register.html`: A form for username and password registration.
# 3. `login.html`: A form for username and password authentication.
# 4. `dashboard.html`: A restricted page shown after successful login.
#
# Note: Store the templates in a `templates` folder.
```

### Key Points:
- Use HTTPS for secure communication in production.
- Replace `YourSuperSecretKey` with a randomly generated, strong secret key.
- Consider additional measures like account lockout after repeated failed login attempts to prevent brute force attacks.
- For production, use a more robust database like PostgreSQL or MySQL instead of SQLite.
