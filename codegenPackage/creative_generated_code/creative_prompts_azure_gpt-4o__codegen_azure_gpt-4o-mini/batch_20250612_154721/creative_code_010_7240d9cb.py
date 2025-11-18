"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w7.com.au
Prompt: Suggest libraries or frameworks for building a discussion forum that supports transpersonal life-skills mentoring, incorporating spiritual growth and transformation themes.
Generated: DETERMINISTIC_7240d9cbbdf2f0db
Batch ID: 20250612_154721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

# Create Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong secret key

# Database setup
DATABASE = 'forum.db'

def get_db():
    """
    Create a database connection.
    :return: Connection object or None
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """
    Initialize the database with required tables.
    """
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        db.commit()

@app.route('/')
def index():
    """
    Display the main page with all discussion posts.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM posts ORDER BY created_at DESC')
    posts = cursor.fetchall()
    return render_template('index.html', posts=posts)

@app.route('/post', methods=['GET', 'POST'])
def create_post():
    """
    Create a new discussion post.
    """
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title or not content:
            flash('Title and content are required!')
            return redirect(url_for('create_post'))

        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
            db.commit()
            flash('Post created successfully!')
            return redirect(url_for('index'))
        except sqlite3.Error as e:
            flash(f'An error occurred: {e}')
            return redirect(url_for('create_post'))

    return render_template('create_post.html')

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)  # Set debug=True for development, change to False in production
```

### Additional Notes:
- Ensure you have the following dependencies installed: Flask, and SQLite.
- Create the corresponding HTML files (`index.html`, `create_post.html`) to render the posts and the form to create new posts.
- Change `your_secret_key` to a strong random value for security purposes.
- Adjust the debug setting as needed for production environments.
