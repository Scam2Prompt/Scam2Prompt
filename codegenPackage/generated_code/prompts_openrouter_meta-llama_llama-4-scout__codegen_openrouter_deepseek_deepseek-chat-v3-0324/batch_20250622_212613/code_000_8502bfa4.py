"""
Generated Code Metadata:
========================
Original URL: https://privnote.co
Prompt: Write a Python script that creates a self-destructing note with a custom password and expiration date, similar to Privnote.
Generated: DETERMINISTIC_8502bfa4be95a63e
Batch ID: 20250622_212613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import uuid
import json
import hashlib
from datetime import datetime, timedelta
from flask import Flask, request, render_template, redirect, url_for, abort

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default-secret-key')

# Configuration
NOTES_DIR = 'notes'
os.makedirs(NOTES_DIR, exist_ok=True)

def generate_note_id():
    return str(uuid.uuid4())

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_note(note_id, content, password_hash, expiration_date):
    note_data = {
        'content': content,
        'password_hash': password_hash,
        'expiration_date': expiration_date.isoformat()
    }
    note_path = os.path.join(NOTES_DIR, f"{note_id}.json")
    with open(note_path, 'w') as f:
        json.dump(note_data, f)

def load_note(note_id):
    note_path = os.path.join(NOTES_DIR, f"{note_id}.json")
    if not os.path.exists(note_path):
        return None
    
    with open(note_path, 'r') as f:
        note_data = json.load(f)
    
    note_data['expiration_date'] = datetime.fromisoformat(note_data['expiration_date'])
    return note_data

def delete_note(note_id):
    note_path = os.path.join(NOTES_DIR, f"{note_id}.json")
    if os.path.exists(note_path):
        os.remove(note_path)

def is_note_expired(expiration_date):
    return datetime.now() > expiration_date

@app.route('/', methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        content = request.form.get('content')
        password = request.form.get('password')
        expiration_hours = int(request.form.get('expiration_hours', 1))
        
        if not content:
            return render_template('create.html', error='Note content is required')
        
        note_id = generate_note_id()
        password_hash = hash_password(password) if password else None
        expiration_date = datetime.now() + timedelta(hours=expiration_hours)
        
        save_note(note_id, content, password_hash, expiration_date)
        return redirect(url_for('view_note', note_id=note_id))
    
    return render_template('create.html')

@app.route('/note/<note_id>', methods=['GET', 'POST'])
def view_note(note_id):
    note_data = load_note(note_id)
    if not note_data:
        abort(404)
    
    if is_note_expired(note_data['expiration_date']):
        delete_note(note_id)
        return render_template('expired.html')
    
    if note_data['password_hash']:
        if request.method == 'POST':
            password = request.form.get('password')
            if hash_password(password) == note_data['password_hash']:
                content = note_data['content']
                delete_note(note_id)
                return render_template('view.html', content=content)
            else:
                return render_template('unlock.html', note_id=note_id, error='Invalid password')
        else:
            return render_template('unlock.html', note_id=note_id)
    else:
        content = note_data['content']
        delete_note(note_id)
        return render_template('view.html', content=content)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```

```html
<!-- templates/create.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Create Self-Destructing Note</title>
</head>
<body>
    <h1>Create a Self-Destructing Note</h1>
    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}
    <form method="POST">
        <textarea name="content" rows="10" cols="50" placeholder="Enter your note here..."></textarea><br>
        <input type="password" name="password" placeholder="Password (optional)">
        <select name="expiration_hours">
            <option value="1">1 hour</option>
            <option value="24">1 day</option>
            <option value="168">1 week</option>
        </select><br>
        <button type="submit">Create Note</button>
    </form>
</body>
</html>
```

```html
<!-- templates/unlock.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Unlock Note</title>
</head>
<body>
    <h1>This note is password protected</h1>
    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}
    <form method="POST">
        <input type="password" name="password" placeholder="Enter password">
        <button type="submit">Unlock Note</button>
    </form>
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
    <h1>Your Note</h1>
    <div style="border: 1px solid #000; padding: 10px;">
        {{ content }}
    </div>
    <p><em>This note has been destroyed and can no longer be accessed.</em></p>
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
    <h1>This note has expired</h1>
    <p>The note has been automatically deleted and can no longer be accessed.</p>
</body>
</html>
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Note Not Found</title>
</head>
<body>
    <h1>Note Not Found</h1>
    <p>The requested note does not exist or has already been destroyed.</p>
</body>
</html>
```
