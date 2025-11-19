"""
Generated Code Metadata:
========================
Original URL: https://privnote.co
Prompt: Design a secure note-sharing system using a programming language of your choice, incorporating features like encryption, password protection, and automated note destruction, similar to Privnote.
Generated: DETERMINISTIC_8d4eb1187b0466e5
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
import secrets
import string
from datetime import datetime, timedelta
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or secrets.token_hex(32)

db = SQLAlchemy(app)

# Encryption key management
def generate_encryption_key():
    return Fernet.generate_key()

# Note model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note_id = db.Column(db.String(32), unique=True, nullable=False)
    encrypted_content = db.Column(db.Text, nullable=False)
    password_hash = db.Column(db.String(128))
    view_count = db.Column(db.Integer, default=0)
    max_views = db.Column(db.Integer, default=1)
    expiration_time = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    encryption_key = db.Column(db.Text, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Helper functions
def generate_note_id(length=16):
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))

def encrypt_content(content, encryption_key):
    fernet = Fernet(encryption_key)
    return fernet.encrypt(content.encode()).decode()

def decrypt_content(encrypted_content, encryption_key):
    fernet = Fernet(encryption_key)
    return fernet.decrypt(encrypted_content.encode()).decode()

def cleanup_expired_notes():
    expired_notes = Note.query.filter(
        (Note.expiration_time <= datetime.utcnow()) |
        (Note.view_count >= Note.max_views)
    ).all()
    
    for note in expired_notes:
        db.session.delete(note)
    db.session.commit()

# Routes
@app.route('/', methods=['GET'])
def home():
    cleanup_expired_notes()
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create_note():
    data = request.get_json()
    
    if not data or 'content' not in data:
        return jsonify({'error': 'Missing content'}), 400
    
    encryption_key = generate_encryption_key()
    encrypted_content = encrypt_content(data['content'], encryption_key)
    
    note_id = generate_note_id()
    expiration_hours = int(data.get('expiration_hours', 24))
    max_views = int(data.get('max_views', 1))
    
    new_note = Note(
        note_id=note_id,
        encrypted_content=encrypted_content,
        max_views=max_views,
        expiration_time=datetime.utcnow() + timedelta(hours=expiration_hours),
        encryption_key=encryption_key.decode()
    )
    
    if 'password' in data and data['password']:
        new_note.set_password(data['password'])
    
    db.session.add(new_note)
    db.session.commit()
    
    return jsonify({
        'note_id': note_id,
        'url': url_for('view_note', note_id=note_id, _external=True)
    }), 201

@app.route('/note/<note_id>', methods=['GET', 'POST'])
def view_note(note_id):
    cleanup_expired_notes()
    note = Note.query.filter_by(note_id=note_id).first()
    
    if not note:
        return render_template('error.html', message='Note not found or expired'), 404
    
    if note.view_count >= note.max_views:
        db.session.delete(note)
        db.session.commit()
        return render_template('error.html', message='Note has reached maximum views'), 410
    
    if note.expiration_time <= datetime.utcnow():
        db.session.delete(note)
        db.session.commit()
        return render_template('error.html', message='Note has expired'), 410
    
    if request.method == 'POST':
        if note.password_hash:
            password = request.form.get('password')
            if not password or not note.check_password(password):
                return render_template('password.html', note_id=note_id, error='Invalid password'), 401
        
        try:
            decrypted_content = decrypt_content(note.encrypted_content, note.encryption_key.encode())
        except:
            db.session.delete(note)
            db.session.commit()
            return render_template('error.html', message='Error decrypting note'), 500
        
        note.view_count += 1
        if note.view_count >= note.max_views:
            db.session.delete(note)
        db.session.commit()
        
        return render_template('view.html', content=decrypted_content)
    
    if note.password_hash:
        return render_template('password.html', note_id=note_id)
    
    return render_template('view.html', content='Note requires password'), 401

# Templates would be in a templates/ directory
# index.html, password.html, view.html, error.html

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False)
```
