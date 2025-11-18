"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meyerseim.com
Prompt: Write code to upload and organize photos and media files in a genealogy database, referencing the media attachment system described on the Meyer/Seim family website.
Generated: DETERMINISTIC_fce6826baa2e8be2
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sqlite3
from flask import Flask, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure key in production
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov', 'mp3'}

# Configure upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Database setup
DATABASE = 'genealogy.db'

def get_db():
    """Establish a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with the required table."""
    with get_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS media (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_name TEXT NOT NULL,
                file_path TEXT NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

def allowed_file(filename):
    """Check if the uploaded file is allowed based on its extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and store it in the database."""
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Save the file to the upload folder
        file.save(file_path)

        # Insert the file information into the database
        try:
            with get_db() as conn:
                conn.execute('INSERT INTO media (file_name, file_path, description) VALUES (?, ?, ?)',
                             (filename, file_path, request.form.get('description', '')))
                conn.commit()
        except sqlite3.Error as e:
            flash(f'Error saving to database: {e}')
            return redirect(request.url)

        flash('File successfully uploaded')
        return redirect(url_for('upload_file'))
    
    flash('File type not allowed')
    return redirect(request.url)

@app.route('/uploads')
def list_media():
    """List all uploaded media files from the database."""
    try:
        with get_db() as conn:
            media_items = conn.execute('SELECT * FROM media').fetchall()
            return {
                "media": [dict(item) for item in media_items]
            }
    except sqlite3.Error as e:
        return {"error": str(e)}

if __name__ == '__main__':
    init_db()  # Initialize the database when the application starts
    app.run(debug=True)
```
