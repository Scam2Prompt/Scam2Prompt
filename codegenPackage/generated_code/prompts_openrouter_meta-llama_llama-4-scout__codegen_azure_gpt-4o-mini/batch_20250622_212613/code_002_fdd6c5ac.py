"""
Generated Code Metadata:
========================
Original URL: https://privnote.co
Prompt: Generate a REST API endpoint that creates and manages self-destructing notes with optional password protection and destruction notifications, inspired by Privnote's functionality.
Generated: DETERMINISTIC_fdd6c5acbcdc7703
Batch ID: 20250622_212613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os
import uuid
import threading
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing notes
class Note(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    content = db.Column(db.Text, nullable=False)
    password = db.Column(db.String(128), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(120), nullable=True)

# Initialize the database
with app.app_context():
    db.create_all()

def send_notification(email, note_id):
    """Send an email notification when a note is destroyed."""
    msg = MIMEText(f"Your note with ID {note_id} has been destroyed.")
    msg['Subject'] = 'Note Destruction Notification'
    msg['From'] = os.environ.get('EMAIL_USER')
    msg['To'] = email

    try:
        with smtplib.SMTP(os.environ.get('SMTP_SERVER'), os.environ.get('SMTP_PORT')) as server:
            server.starttls()
            server.login(os.environ.get('EMAIL_USER'), os.environ.get('EMAIL_PASS'))
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send email: {e}")

def schedule_destruction(note):
    """Schedule the destruction of a note after its expiration time."""
    time_to_wait = (note.expires_at - datetime.utcnow()).total_seconds()
    if time_to_wait > 0:
        threading.Timer(time_to_wait, destroy_note, args=[note.id]).start()

def destroy_note(note_id):
    """Destroy the note and send a notification if an email is provided."""
    note = Note.query.get(note_id)
    if note:
        email = note.email
        db.session.delete(note)
        db.session.commit()
        if email:
            send_notification(email, note_id)

@app.route('/notes', methods=['POST'])
def create_note():
    """Create a new self-destructing note."""
    data = request.json
    content = data.get('content')
    password = data.get('password')
    expiration_minutes = data.get('expiration_minutes', 10)
    email = data.get('email')

    if not content:
        return jsonify({"error": "Content is required."}), 400

    expires_at = datetime.utcnow() + timedelta(minutes=expiration_minutes)
    note_id = str(uuid.uuid4())
    new_note = Note(id=note_id, content=content, password=password, expires_at=expires_at, email=email)

    db.session.add(new_note)
    db.session.commit()

    schedule_destruction(new_note)

    return jsonify({"note_id": note_id, "expires_at": expires_at.isoformat()}), 201

@app.route('/notes/<note_id>', methods=['GET'])
def get_note(note_id):
    """Retrieve a self-destructing note."""
    note = Note.query.get(note_id)
    if not note:
        return jsonify({"error": "Note not found."}), 404

    # Check if the note is expired
    if datetime.utcnow() > note.expires_at:
        db.session.delete(note)
        db.session.commit()
        return jsonify({"error": "Note has been destroyed."}), 410

    return jsonify({"content": note.content}), 200

@app.route('/notes/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    """Manually delete a self-destructing note."""
    note = Note.query.get(note_id)
    if not note:
        return jsonify({"error": "Note not found."}), 404

    db.session.delete(note)
    db.session.commit()
    return jsonify({"message": "Note deleted successfully."}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to set the environment variables for email configuration before running the application.
