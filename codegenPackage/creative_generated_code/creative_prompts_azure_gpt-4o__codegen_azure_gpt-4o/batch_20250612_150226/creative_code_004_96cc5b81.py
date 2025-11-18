"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kid-69m.pages.dev
Prompt: Write code to create a "Yearbook" feature for AKCB, where NFT holders can voluntarily add and update their ownership history and personal details in a gallery format.
Generated: DETERMINISTIC_96cc5b81e37a5d2f
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code for the requested "Yearbook" feature, assuming the use of Flask for backend development and SQLite for the database. This code includes functionality to add and update ownership history and personal details, along with a gallery view.

```python
from flask import Flask, request, jsonify, render_template
import sqlite3
import os

app = Flask(__name__)

# Database file
DATABASE_FILE = "yearbook.db"

# Initialize the database if it doesn't exist
def init_db():
    if not os.path.exists(DATABASE_FILE):
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS yearbook (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nft_holder TEXT NOT NULL,
                nft_id TEXT NOT NULL,
                ownership_history TEXT,
                personal_details TEXT
            )
        ''')
        conn.commit()
        conn.close()

# Initialize the database
init_db()

@app.route('/add_entry', methods=['POST'])
def add_entry():
    """
    Add a new entry to the yearbook.
    Request JSON format:
    {
        "nft_holder": "Holder Name",
        "nft_id": "NFT Unique ID",
        "ownership_history": "Ownership details",
        "personal_details": "Personal details"
    }
    """
    try:
        data = request.json
        nft_holder = data.get('nft_holder')
        nft_id = data.get('nft_id')
        ownership_history = data.get('ownership_history', '')
        personal_details = data.get('personal_details', '')

        if not nft_holder or not nft_id:
            return jsonify({"error": "NFT holder and NFT ID are required."}), 400

        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO yearbook (nft_holder, nft_id, ownership_history, personal_details)
            VALUES (?, ?, ?, ?)
        ''', (nft_holder, nft_id, ownership_history, personal_details))
        conn.commit()
        conn.close()

        return jsonify({"message": "Entry successfully added."}), 201

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/update_entry/<int:entry_id>', methods=['PUT'])
def update_entry(entry_id):
    """
    Update an existing entry in the yearbook.
    Request JSON format:
    {
        "nft_holder": "Updated Holder Name",
        "ownership_history": "Updated Ownership details",
        "personal_details": "Updated Personal details"
    }
    """
    try:
        data = request.json
        nft_holder = data.get('nft_holder')
        ownership_history = data.get('ownership_history')
        personal_details = data.get('personal_details')

        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        
        # Check if the entry exists
        cursor.execute('SELECT * FROM yearbook WHERE id = ?', (entry_id,))
        entry = cursor.fetchone()
        if not entry:
            return jsonify({"error": "Entry not found."}), 404

        # Update the entry
        cursor.execute('''
            UPDATE yearbook
            SET nft_holder = COALESCE(?, nft_holder),
                ownership_history = COALESCE(?, ownership_history),
                personal_details = COALESCE(?, personal_details)
            WHERE id = ?
        ''', (nft_holder, ownership_history, personal_details, entry_id))
        conn.commit()
        conn.close()

        return jsonify({"message": "Entry successfully updated."}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/gallery', methods=['GET'])
def gallery():
    """
    Display all entries in the yearbook in a gallery format.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM yearbook')
        entries = cursor.fetchall()
        conn.close()

        # Render as an HTML gallery
        return render_template('gallery.html', entries=entries)

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (`templates/gallery.html`)
Below is an example of the gallery HTML template:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yearbook Gallery</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        .entry {
            border: 1px solid #ddd;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>Yearbook Gallery</h1>
    {% for entry in entries %}
        <div class="entry">
            <p><strong>NFT Holder:</strong> {{ entry[1] }}</p>
            <p><strong>NFT ID:</strong> {{ entry[2] }}</p>
            <p><strong>Ownership History:</strong> {{ entry[3] or 'N/A' }}</p>
            <p><strong>Personal Details:</strong> {{ entry[4] or 'N/A' }}</p>
        </div>
    {% endfor %}
</body>
</html>
```

This code covers the requested functionality and adheres to the specifications provided. It handles errors gracefully and includes comments for clarity. Let me know if further adjustments are needed!
