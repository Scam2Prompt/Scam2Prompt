"""
Generated Code Metadata:
========================
Original URL: https://privnote.co
Prompt: Create a step-by-step guide for implementing password-protected self-destructing notes in a web application, including encryption and link generation, inspired by privnote.co.
Generated: DETERMINISTIC_cd3c97f550bc34b9
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, render_template, redirect, url_for, abort
from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet
import secrets
import string
import os
from datetime import datetime, timedelta
from models import db, Note
import uuid

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///notes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)
with app.app_context():
    db.create_all()

# Generate encryption key
def generate_encryption_key():
    return Fernet.generate_key()

# Encrypt note content
def encrypt_note(content, encryption_key):
    fernet = Fernet(encryption_key)
    return fernet.encrypt(content.encode())

# Decrypt note content
def decrypt_note(encrypted_content, encryption_key):
    fernet = Fernet(encryption_key)
    return fernet.decrypt(encrypted_content).decode()

# Generate unique URL
def generate_unique_url():
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(16))

# Create a new note
@app.route('/', methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        content = request.form.get('content')
        password = request.form.get('password')
        expiration_hours = int(request.form.get('expiration', 24))
        
        if not content:
            return render_template('create.html', error='Note content is required')
        
        # Generate encryption key and URL
        encryption_key = generate_encryption_key()
        note_url = generate_unique_url()
        
        # Encrypt content
        encrypted_content = encrypt_note(content, encryption_key)
        
        # Hash password if provided
        password_hash = generate_password_hash(password) if password else None
        
        # Calculate expiration time
        expiration_time = datetime.utcnow() + timedelta(hours=expiration_hours)
        
        # Save note to database
        note = Note(
            id=str(uuid.uuid4()),
            url=note_url,
            encrypted_content=encrypted_content,
            encryption_key=encryption_key,
            password_hash=password_hash,
            expiration_time=expiration_time,
            views_remaining=1
        )
        db.session.add(note)
        db.session.commit()
        
        return render_template('created.html', note_url=note_url)
    
    return render_template('create.html')

# View a note
@app.route('/<note_url>', methods=['GET', 'POST'])
def view_note(note_url):
    note = Note.query.filter_by(url=note_url).first()
    
    if not note:
        abort(404)
    
    if datetime.utcnow() > note.expiration_time:
        db.session.delete(note)
        db.session.commit()
        return render_template('expired.html')
    
    if note.views_remaining <= 0:
        db.session.delete(note)
        db.session.commit()
        return render_template('expired.html')
    
    if request.method == 'POST':
        password = request.form.get('password')
        
        if note.password_hash and not check_password_hash(note.password_hash, password):
            return render_template('view.html', note_url=note_url, error='Invalid password')
        
        # Decrypt content
        content = decrypt_note(note.encrypted_content, note.encryption_key)
        
        # Decrement views or delete note
        note.views_remaining -= 1
        if note.views_remaining <= 0:
            db.session.delete(note)
        db.session.commit()
        
        return render_template('display.html', content=content)
    
    if note.password_hash:
        return render_template('view.html', note_url=note_url)
    
    # If no password, show immediately
    content = decrypt_note(note.encrypted_content, note.encryption_key)
    note.views_remaining -= 1
    if note.views_remaining <= 0:
        db.session.delete(note)
    db.session.commit()
    
    return render_template('display.html', content=content)

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```python
# models.py
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Note(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    url = db.Column(db.String(16), unique=True, nullable=False)
    encrypted_content = db.Column(db.LargeBinary, nullable=False)
    encryption_key = db.Column(db.LargeBinary, nullable=False)
    password_hash = db.Column(db.String(128))
    expiration_time = db.Column(db.DateTime, nullable=False)
    views_remaining = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
```

```html
<!-- templates/create.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Create Self-Destructing Note</title>
</head>
<body>
    <h1>Create a New Note</h1>
    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}
    <form method="POST">
        <textarea name="content" rows="10" cols="50" required></textarea><br>
        <label>Password (optional):</label>
        <input type="password" name="password"><br>
        <label>Expires after:</label>
        <select name="expiration">
            <option value="1">1 hour</option>
            <option value="24" selected>24 hours</option>
            <option value="168">1 week</option>
        </select><br>
        <button type="submit">Create Note</button>
    </form>
</body>
</html>
```

```html
<!-- templates/created.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Note Created</title>
</head>
<body>
    <h1>Your Note Has Been Created</h1>
    <p>Share this link (it will self-destruct after being viewed):</p>
    <input type="text" value="{{ request.url_root }}{{ note_url }}" readonly size="50">
    <p>Warning: Anyone with this link can access the note.</p>
</body>
</html>
```

```html
<!-- templates/view.html -->
<!DOCTYPE html>
<html>
<head>
    <title>View Note</title>
</head>
<body>
    <h1>This Note is Password Protected</h1>
    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}
    <form method="POST">
        <label>Enter Password:</label>
        <input type="password" name="password" required>
        <button type="submit">View Note</button>
    </form>
</body>
</html>
```

```html
<!-- templates/display.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Note Content</title>
    <meta http-equiv="refresh" content="5;url=/">
</head>
<body>
    <h1>Your Note</h1>
    <pre>{{ content }}</pre>
    <p>This page will self-destruct in 5 seconds...</p>
</body>
</html>
```

```html
<!-- templates/expired.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Note Expired</title>
</head>
<body>
    <h1>This Note Has Expired</h1>
    <p>The note has been automatically deleted.</p>
</body>
</html>
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Not Found</title>
</head>
<body>
    <h1>404 - Note Not Found</h1>
    <p>The requested note does not exist or has been deleted.</p>
</body>
</html>
```

```html
<!-- templates/500.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Something went wrong on our end. Please try again later.</p>
</body>
</html>
```
