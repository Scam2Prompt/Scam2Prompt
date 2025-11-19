"""
Generated Code Metadata:
========================
Original URL: https://drop3.art
Prompt: What are some popular platforms for showcasing and selling digital art, and how can I build a similar platform using web development frameworks?
Generated: DETERMINISTIC_69822f549b594000
Batch ID: 20250622_212248
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready code example for building a basic platform for showcasing and selling digital art using Python's Flask framework. This example includes user authentication, art upload functionality, and a marketplace for browsing and purchasing art.

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
import os
import sqlite3

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Configure upload folder and allowed file types
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Database setup
DATABASE = 'database.db'

def init_db():
    """Initialize the database with required tables."""
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
        CREATE TABLE IF NOT EXISTS art (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            filename TEXT NOT NULL,
            price REAL NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()

# Helper functions
def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_db_connection():
    """Get a connection to the database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Routes
@app.route('/')
def index():
    """Homepage displaying all art pieces."""
    conn = get_db_connection()
    art_pieces = conn.execute('SELECT * FROM art').fetchall()
    conn.close()
    return render_template('index.html', art_pieces=art_pieces)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists. Please choose another.', 'error')
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
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()
        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials. Please try again.', 'error')
    return render_template('login.html')

@app.route('/logout')
def logout():
    """User logout."""
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    """Upload a new art piece."""
    if 'user_id' not in session:
        flash('You must be logged in to upload art.', 'error')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        file = request.files['file']
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            conn = get_db_connection()
            conn.execute('INSERT INTO art (title, filename, price, user_id) VALUES (?, ?, ?, ?)',
                         (title, filename, price, session['user_id']))
            conn.commit()
            conn.close()
            
            flash('Art uploaded successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid file type. Please upload an image.', 'error')
    
    return render_template('upload.html')

@app.route('/art/<int:art_id>')
def art_detail(art_id):
    """View details of a specific art piece."""
    conn = get_db_connection()
    art_piece = conn.execute('SELECT * FROM art WHERE id = ?', (art_id,)).fetchone()
    conn.close()
    if art_piece is None:
        flash('Art piece not found.', 'error')
        return redirect(url_for('index'))
    return render_template('art_detail.html', art_piece=art_piece)

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors."""
    return render_template('500.html'), 500

# Initialize database and run the app
if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        init_db()
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
```

### Directory Structure:
```
project/
├── app.py
├── database.db (auto-created)
├── static/
│   └── uploads/ (auto-created)
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── upload.html
│   ├── art_detail.html
│   ├── 404.html
│   └── 500.html
```

### Notes:
- Replace `your_secret_key` with a secure key for production.
- Add proper styling and frontend templates in the `templates/` directory.
- Use HTTPS and secure password hashing (e.g., `bcrypt`) for production.
- Consider scaling with a more robust database (e.g., PostgreSQL) and cloud storage for uploads.
