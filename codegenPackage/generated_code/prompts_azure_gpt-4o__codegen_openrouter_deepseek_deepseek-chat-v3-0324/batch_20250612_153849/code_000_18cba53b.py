"""
Generated Code Metadata:
========================
Original URL: https://privnote.co
Prompt: Write a Python script that uses an API or library to create a self-destructing note similar to the functionality described on privnote.co, including encryption and a custom expiration time.
Generated: DETERMINISTIC_18cba53b44209aa0
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import secrets
import string
from datetime import datetime, timedelta
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', secrets.token_hex(32))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Generate encryption key
ENCRYPTION_KEY = Fernet.generate_key()
cipher_suite = Fernet(ENCRYPTION_KEY)

class Note(db.Model):
    id = db.Column(db.String(16), primary_key=True)
    encrypted_content = db.Column(db.LargeBinary, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime)
    views_remaining = db.Column(db.Integer, default=1)

    def is_expired(self):
        return datetime.utcnow() > self.expires_at if self.expires_at else False

    def decrypt_content(self):
        return cipher_suite.decrypt(self.encrypted_content).decode('utf-8')

@app.before_first_request
def create_tables():
    db.create_all()

def generate_note_id(length=16):
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form.get('content')
        expiration = request.form.get('expiration')
        views = int(request.form.get('views', 1))

        if not content:
            flash('Note content cannot be empty', 'error')
            return redirect(url_for('index'))

        # Set expiration time
        if expiration == '1h':
            expires_at = datetime.utcnow() + timedelta(hours=1)
        elif expiration == '1d':
            expires_at = datetime.utcnow() + timedelta(days=1)
        elif expiration == '1w':
            expires_at = datetime.utcnow() + timedelta(weeks=1)
        else:
            expires_at = None

        # Encrypt content
        encrypted_content = cipher_suite.encrypt(content.encode('utf-8'))

        # Create note
        note_id = generate_note_id()
        note = Note(
            id=note_id,
            encrypted_content=encrypted_content,
            expires_at=expires_at,
            views_remaining=views
        )
        db.session.add(note)
        db.session.commit()

        return redirect(url_for('show_note', note_id=note_id))

    return render_template('index.html')

@app.route('/note/<note_id>', methods=['GET'])
def show_note(note_id):
    note = Note.query.get_or_404(note_id)

    if note.is_expired() or note.views_remaining <= 0:
        db.session.delete(note)
        db.session.commit()
        return render_template('expired.html')

    content = note.decrypt_content()
    note.views_remaining -= 1

    if note.views_remaining <= 0:
        db.session.delete(note)
    db.session.commit()

    return render_template('note.html', content=content)

if __name__ == '__main__':
    app.run(debug=False)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Self-Destructing Note</title>
</head>
<body>
    <h1>Create a Self-Destructing Note</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="alert alert-{{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
    {% endwith %}
    <form method="POST">
        <textarea name="content" rows="10" cols="50" required></textarea><br>
        <label for="expiration">Expiration:</label>
        <select name="expiration" id="expiration">
            <option value="none">No expiration</option>
            <option value="1h">1 Hour</option>
            <option value="1d">1 Day</option>
            <option value="1w">1 Week</option>
        </select><br>
        <label for="views">Views Allowed:</label>
        <input type="number" name="views" id="views" min="1" value="1"><br>
        <button type="submit">Create Note</button>
    </form>
</body>
</html>
```

```html
<!-- templates/note.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Your Note</title>
</head>
<body>
    <h1>Your Note</h1>
    <div class="note-content">{{ content }}</div>
    <p>This note will self-destruct after being viewed.</p>
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
    <h1>Note Expired or Already Viewed</h1>
    <p>This note has expired or has already been viewed and has been deleted.</p>
</body>
</html>
```
