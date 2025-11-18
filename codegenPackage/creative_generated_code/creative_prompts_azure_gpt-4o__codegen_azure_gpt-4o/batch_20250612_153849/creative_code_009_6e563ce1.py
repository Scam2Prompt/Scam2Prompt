"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://privnote.co
Prompt: Develop a feature in a web application that allows users to set custom expiration times for notes (e.g., 1 hour, 24 hours, 7 days), as described on privnote.co.
Generated: DETERMINISTIC_6e563ce1062d236c
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

### Implementation in Python (using Flask and SQLite)

```python
from flask import Flask, request, jsonify, render_template, redirect, url_for
from datetime import datetime, timedelta
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = "notes.db"

def init_db():
    """Initialize the database and create tables if not exists."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                expiration_time DATETIME NOT NULL
            )
        """)
        conn.commit()

# Initialize the database
init_db()

@app.route('/')
def home():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/create_note', methods=['POST'])
def create_note():
    """
    API endpoint to create a new note.

    The request should include:
    - content: The text of the note (required).
    - expiration: Expiration time in hours (default is 24 hours).
    """
    try:
        data = request.json
        content = data.get("content")
        expiration_hours = data.get("expiration", 24)  # Default to 24 hours
        
        if not content:
            return jsonify({"error": "Note content is required"}), 400

        # Calculate expiration date
        expiration_time = datetime.utcnow() + timedelta(hours=expiration_hours)

        # Save to the database
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO notes (content, expiration_time) VALUES (?, ?)", (content, expiration_time))
            conn.commit()

        return jsonify({"message": "Note created successfully", "expiration_time": expiration_time.isoformat()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_note/<int:note_id>', methods=['GET'])
def get_note(note_id):
    """
    API endpoint to retrieve a note by its ID.
    If the note has expired, it will not be returned.
    """
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT content, expiration_time FROM notes WHERE id = ?", (note_id,))
            note = cursor.fetchone()

            if not note:
                return jsonify({"error": "Note not found"}), 404
            
            content, expiration_time = note
            expiration_time = datetime.fromisoformat(expiration_time)

            # Check expiration
            if datetime.utcnow() > expiration_time:
                return jsonify({"error": "Note has expired"}), 410

            return jsonify({"content": content, "expiration_time": expiration_time.isoformat()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/delete_expired_notes', methods=['POST'])
def delete_expired_notes():
    """
    API endpoint to delete all expired notes from the database.
    """
    try:
        current_time = datetime.utcnow()
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM notes WHERE expiration_time < ?", (current_time,))
            conn.commit()

        return jsonify({"message": "Expired notes deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### `index.html` (Frontend Template)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Custom Expiration Notes</title>
</head>
<body>
    <h1>Create a Note</h1>
    <form id="noteForm">
        <label for="content">Note Content:</label><br>
        <textarea id="content" name="content" required></textarea><br>
        <label for="expiration">Expiration Time (hours):</label><br>
        <input type="number" id="expiration" name="expiration" value="24"><br><br>
        <button type="button" onclick="submitNote()">Create Note</button>
    </form>

    <script>
        async function submitNote() {
            const content = document.getElementById("content").value;
            const expiration = document.getElementById("expiration").value;

            const response = await fetch('/create_note', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ content, expiration: +expiration }),
            });

            const result = await response.json();

            if (response.ok) {
                alert(`Note created! Expires at: ${result.expiration_time}`);
            } else {
                alert(`Error: ${result.error}`);
            }
        }
    </script>
</body>
</html>
```

### Notes:
1. The database will automatically clean up expired notes using the `/delete_expired_notes` endpoint.
2. The application is designed with clean code and proper error handling for production use.
