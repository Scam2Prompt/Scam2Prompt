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
import uuid
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for self-destructing notes
notes_storage = {}

class Note:
    def __init__(self, content, max_views):
        self.id = str(uuid.uuid4())
        self.content = content
        self.max_views = max_views
        self.views = 0
        self.created_at = time.time()

    def view(self):
        if self.views < self.max_views:
            self.views += 1
            return self.content
        else:
            raise Exception("This note has reached its maximum number of views and cannot be accessed anymore.")

@app.route('/create_note', methods=['POST'])
def create_note():
    """Create a new self-destructing note."""
    data = request.json
    content = data.get('content')
    max_views = data.get('max_views')

    if not content or not isinstance(max_views, int) or max_views <= 0:
        return jsonify({"error": "Invalid input. 'content' is required and 'max_views' must be a positive integer."}), 400

    note = Note(content, max_views)
    notes_storage[note.id] = note
    return jsonify({"note_id": note.id}), 201

@app.route('/view_note/<note_id>', methods=['GET'])
def view_note(note_id):
    """View a self-destructing note."""
    note = notes_storage.get(note_id)

    if note is None:
        return jsonify({"error": "Note not found."}), 404

    try:
        content = note.view()
        return jsonify({"content": content, "remaining_views": note.max_views - note.views}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 410

@app.route('/delete_note/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    """Delete a self-destructing note."""
    if note_id in notes_storage:
        del notes_storage[note_id]
        return jsonify({"message": "Note deleted successfully."}), 200
    else:
        return jsonify({"error": "Note not found."}), 404

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False in production
```

### Note
To run the code, install Flask with the following command:
```bash
pip install Flask
```

Then, execute the script using Python. Use tools like Postman or Curl to interact with the API. Make sure to handle any necessary CORS configurations based on your deployment environment.
