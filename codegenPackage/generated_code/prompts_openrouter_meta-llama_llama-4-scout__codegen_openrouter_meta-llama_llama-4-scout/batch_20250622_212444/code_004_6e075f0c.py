"""
Generated Code Metadata:
========================
Original URL: https://privnote.icu
Prompt: How can I build a web application similar to Privnote using Flask or Django, with features like note encryption, self-destruction, and password protection?
Generated: DETERMINISTIC_6e075f0c217beef2
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Privnote-like Web Application using Flask**
====================================================

**Requirements**
---------------

* Python 3.8+
* Flask 2.0+
* cryptography 4.0+
* Flask-SQLAlchemy 2.5+

**Code**
------

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet
from werkzeug.security import generate_password_hash, check_password_hash
import os
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///privnote.db'
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    encrypted_content = db.Column(db.Text, nullable=False)
    password_hash = db.Column(db.String(128), nullable=True)
    destruction_time = db.Column(db.DateTime, nullable=True)

    def __init__(self, encrypted_content, password_hash=None, destruction_time=None):
        self.encrypted_content = encrypted_content
        self.password_hash = password_hash
        self.destruction_time = destruction_time

def generate_key():
    return Fernet.generate_key()

def encrypt_note(content, key):
    f = Fernet(key)
    return f.encrypt(content.encode())

def decrypt_note(encrypted_content, key):
    f = Fernet(key)
    return f.decrypt(encrypted_content).decode()

@app.route('/create', methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        content = request.form['content']
        password = request.form.get('password')
        destruction_time = request.form.get('destruction_time')

        key = generate_key()
        encrypted_content = encrypt_note(content, key)

        note = Note(encrypted_content)

        if password:
            note.password_hash = generate_password_hash(password)

        if destruction_time:
            note.destruction_time = datetime.strptime(destruction_time, '%Y-%m-%d %H:%M:%S')

        db.session.add(note)
        db.session.commit()

        return jsonify({'note_id': note.id, 'key': key.decode()})

    return render_template('create.html')

@app.route('/note/<int:note_id>', methods=['GET', 'POST'])
def view_note(note_id):
    note = Note.query.get(note_id)

    if not note:
        return jsonify({'error': 'Note not found'}), 404

    if note.destruction_time and note.destruction_time < datetime.now():
        db.session.delete(note)
        db.session.commit()
        return jsonify({'error': 'Note has been destroyed'}), 410

    if request.method == 'POST':
        password = request.form.get('password')

        if note.password_hash and not check_password_hash(note.password_hash, password):
            return jsonify({'error': 'Invalid password'}), 401

        key = request.form.get('key')

        try:
            content = decrypt_note(note.encrypted_content, key.encode())
            return jsonify({'content': content})
        except Exception as e:
            return jsonify({'error': 'Invalid key'}), 400

    return render_template('view.html', note_id=note_id)

if __name__ == '__main__':
    app.run(debug=True)
```

**templates/create.html**
```html
<form method="post">
    <textarea name="content"></textarea>
    <input type="password" name="password" placeholder="Password (optional)">
    <input type="datetime-local" name="destruction_time" placeholder="Destruction time (optional)">
    <button type="submit">Create Note</button>
</form>
```

**templates/view.html**
```html
<form method="post">
    <input type="password" name="password" placeholder="Password">
    <input type="text" name="key" placeholder="Key">
    <button type="submit">View Note</button>
</form>
```

**requirements.txt**
```
Flask==2.0.2
Flask-SQLAlchemy==2.5.1
cryptography==4.0.2
```

**Run**
-----

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
