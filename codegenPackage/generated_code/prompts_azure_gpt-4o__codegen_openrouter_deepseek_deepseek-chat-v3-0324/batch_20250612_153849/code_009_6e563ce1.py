"""
Generated Code Metadata:
========================
Original URL: https://privnote.co
Prompt: Develop a feature in a web application that allows users to set custom expiration times for notes (e.g., 1 hour, 24 hours, 7 days), as described on privnote.co.
Generated: DETERMINISTIC_6e563ce1062d236c
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
from datetime import datetime, timedelta
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import uuid
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///notes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Note model
class Note(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime)
    is_encrypted = db.Column(db.Boolean, default=False)

    def is_expired(self):
        return datetime.utcnow() > self.expires_at if self.expires_at else False

# Create database tables
with app.app_context():
    db.create_all()

# Helper function to calculate expiration time
def get_expiration_time(expiration_option):
    now = datetime.utcnow()
    if expiration_option == '1h':
        return now + timedelta(hours=1)
    elif expiration_option == '24h':
        return now + timedelta(days=1)
    elif expiration_option == '7d':
        return now + timedelta(days=7)
    else:
        return None

# Route to create a new note
@app.route('/api/notes', methods=['POST'])
def create_note():
    try:
        data = request.get_json()
        content = data.get('content')
        expiration_option = data.get('expiration_option', '24h')
        
        if not content:
            return jsonify({'error': 'Content is required'}), 400
        
        expires_at = get_expiration_time(expiration_option)
        if not expires_at:
            return jsonify({'error': 'Invalid expiration option'}), 400
        
        note_id = str(uuid.uuid4())
        new_note = Note(
            id=note_id,
            content=content,
            expires_at=expires_at
        )
        
        db.session.add(new_note)
        db.session.commit()
        
        return jsonify({
            'id': note_id,
            'expires_at': expires_at.isoformat()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to view a note
@app.route('/api/notes/<note_id>', methods=['GET'])
def get_note(note_id):
    try:
        note = Note.query.get(note_id)
        
        if not note:
            return jsonify({'error': 'Note not found'}), 404
            
        if note.is_expired():
            db.session.delete(note)
            db.session.commit()
            return jsonify({'error': 'Note has expired'}), 410
            
        return jsonify({
            'content': note.content,
            'created_at': note.created_at.isoformat(),
            'expires_at': note.expires_at.isoformat() if note.expires_at else None
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to delete a note (after viewing)
@app.route('/api/notes/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    try:
        note = Note.query.get(note_id)
        
        if not note:
            return jsonify({'error': 'Note not found'}), 404
            
        db.session.delete(note)
        db.session.commit()
        
        return jsonify({'message': 'Note deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Frontend route to create note
@app.route('/')
def index():
    return render_template('index.html')

# Frontend route to view note
@app.route('/n/<note_id>')
def view_note(note_id):
    return render_template('view_note.html', note_id=note_id)

# Cleanup expired notes
def cleanup_expired_notes():
    with app.app_context():
        expired_notes = Note.query.filter(Note.expires_at < datetime.utcnow()).all()
        for note in expired_notes:
            db.session.delete(note)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Secure Note</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
        textarea { width: 100%; height: 200px; margin-bottom: 15px; }
        button { padding: 10px 15px; background: #4CAF50; color: white; border: none; cursor: pointer; }
        button:hover { background: #45a049; }
        .expiration-options { margin: 15px 0; }
        .result { margin-top: 20px; padding: 10px; background: #f8f8f8; }
    </style>
</head>
<body>
    <h1>Create a Secure Note</h1>
    <form id="noteForm">
        <textarea id="noteContent" placeholder="Enter your note here..." required></textarea>
        <div class="expiration-options">
            <label>Expiration:</label>
            <select id="expirationOption">
                <option value="1h">1 Hour</option>
                <option value="24h" selected>24 Hours</option>
                <option value="7d">7 Days</option>
            </select>
        </div>
        <button type="submit">Create Note</button>
    </form>
    <div id="result" class="result" style="display: none;">
        <p>Your note has been created. Share this link:</p>
        <a id="noteLink" target="_blank"></a>
        <p>Note will be automatically deleted after expiration.</p>
    </div>

    <script>
        document.getElementById('noteForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const content = document.getElementById('noteContent').value;
            const expirationOption = document.getElementById('expirationOption').value;
            
            try {
                const response = await fetch('/api/notes', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        content,
                        expiration_option: expirationOption
                    })
                });
                
                if (!response.ok) {
                    throw new Error('Failed to create note');
                }
                
                const data = await response.json();
                const noteUrl = `${window.location.origin}/n/${data.id}`;
                
                document.getElementById('noteLink').href = noteUrl;
                document.getElementById('noteLink').textContent = noteUrl;
                document.getElementById('result').style.display = 'block';
                
            } catch (error) {
                alert('Error creating note: ' + error.message);
            }
        });
    </script>
</body>
</html>
```

```html
<!-- templates/view_note.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>View Secure Note</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
        .note-content { background: #f8f8f8; padding: 20px; margin: 20px 0; white-space: pre-wrap; }
        .error { color: red; }
    </style>
</head>
<body>
    <h1>Secure Note</h1>
    <div id="noteContainer">
        <p>Loading note...</p>
    </div>

    <script>
        const noteId = '{{ note_id }}';
        
        async function fetchNote() {
            try {
                const response = await fetch(`/api/notes/${noteId}`);
                
                if (!response.ok) {
                    throw new Error(await response.text());
                }
                
                const data = await response.json();
                
                const noteContainer = document.getElementById('noteContainer');
                noteContainer.innerHTML = `
                    <div class="note-content">${data.content}</div>
                    <p>Created: ${new Date(data.created_at).toLocaleString()}</p>
                    <p>Expires: ${new Date(data.expires_at).toLocaleString()}</p>
                `;
                
                // Delete note after viewing
                await fetch(`/api/notes/${noteId}`, { method: 'DELETE' });
                
            } catch (error) {
                document.getElementById('noteContainer').
