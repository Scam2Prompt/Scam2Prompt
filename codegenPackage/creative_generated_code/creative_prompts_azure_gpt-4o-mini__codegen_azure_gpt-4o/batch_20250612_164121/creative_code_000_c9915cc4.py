"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.noterip.com
Prompt: How can I create a self-destructing note using NoteRIP and set a maximum number of views for it?
Generated: DETERMINISTIC_c9915cc402f09eee
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for notes
notes = {}

class Note:
    def __init__(self, content, max_views):
        """
        Initialize a note with content and maximum allowed views.
        """
        self.content = content
        self.max_views = max_views
        self.views = 0

    def view(self):
        """
        Increment the view count for the note and check if it should self-destruct.
        """
        self.views += 1
        if self.views >= self.max_views:
            return self.content, True  # Return content and self-destruct flag
        return self.content, False

@app.route('/create_note', methods=['POST'])
def create_note():
    """
    Endpoint to create a self-destructing note.
    Expected JSON payload: {"content": "<text>", "max_views": <integer>}
    """
    try:
        data = request.json
        content = data.get('content')
        max_views = data.get('max_views')

        if not content or not isinstance(max_views, int) or max_views <= 0:
            return jsonify({"error": "Invalid input. Ensure 'content' is a string and 'max_views' is a positive integer."}), 400

        note_id = str(int(time.time() * 1000))  # Generate a unique note ID based on timestamp
        notes[note_id] = Note(content, max_views)

        return jsonify({"note_id": note_id}), 201
    except Exception as e:
        return jsonify({"error": "Failed to create note", "details": str(e)}), 500

@app.route('/view_note/<note_id>', methods=['GET'])
def view_note(note_id):
    """
    Endpoint to view a note. 
    If the maximum number of views is reached, the note self-destructs.
    """
    try:
        note = notes.get(note_id)
        if not note:
            return jsonify({"error": "Note not found"}), 404

        content, should_delete = note.view()
        if should_delete:
            del notes[note_id]  # Self-destruct the note

        return jsonify({"content": content, "remaining_views": max(0, note.max_views - note.views)}), 200
    except Exception as e:
        return jsonify({"error": "Failed to view note", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
