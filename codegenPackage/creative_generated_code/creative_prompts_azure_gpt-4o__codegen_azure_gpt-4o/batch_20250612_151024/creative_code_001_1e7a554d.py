"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happychex.com
Prompt: Recommend libraries or tools for managing domain-to-directory mappings on a server, with a focus on control panel integrations.
Generated: DETERMINISTIC_1e7a554d3993820c
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to manage domain-to-directory mappings on a server.
It uses Python with Flask for API endpoints and SQLite for mapping storage.
This can be extended to integrate with control panels like cPanel or Plesk.
"""

import os
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
DATABASE = 'domain_mappings.db'

# Initialize the SQLite database
def init_db():
    """Create the database and the mappings table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mappings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain TEXT NOT NULL UNIQUE,
            directory TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/add_mapping', methods=['POST'])
def add_mapping():
    """
    API endpoint to add a new domain-directory mapping.
    Expects JSON input: { "domain": "example.com", "directory": "/var/www/example" }
    """
    try:
        data = request.json
        domain = data.get('domain')
        directory = data.get('directory')

        if not domain or not directory:
            return jsonify({"error": "Both domain and directory are required"}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO mappings (domain, directory) VALUES (?, ?)', (domain, directory))
        conn.commit()
        conn.close()

        return jsonify({"message": "Mapping added successfully"}), 201

    except sqlite3.IntegrityError:
        return jsonify({"error": "Domain already exists"}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_mapping', methods=['GET'])
def get_mapping():
    """
    API endpoint to retrieve the directory for a specific domain.
    Expects query parameter: ?domain=example.com
    """
    try:
        domain = request.args.get('domain')
        if not domain:
            return jsonify({"error": "Domain parameter is required"}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT directory FROM mappings WHERE domain = ?', (domain,))
        result = cursor.fetchone()
        conn.close()

        if result:
            return jsonify({"domain": domain, "directory": result[0]}), 200
        else:
            return jsonify({"error": "Domain not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/delete_mapping', methods=['DELETE'])
def delete_mapping():
    """
    API endpoint to delete a domain-directory mapping.
    Expects JSON input: { "domain": "example.com" }
    """
    try:
        data = request.json
        domain = data.get('domain')

        if not domain:
            return jsonify({"error": "Domain is required"}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM mappings WHERE domain = ?', (domain,))
        changes = conn.total_changes
        conn.commit()
        conn.close()

        if changes > 0:
            return jsonify({"message": "Mapping deleted successfully"}), 200
        else:
            return jsonify({"error": "Domain not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/list_mappings', methods=['GET'])
def list_mappings():
    """
    API endpoint to list all domain-directory mappings.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT domain, directory FROM mappings')
        results = cursor.fetchall()
        conn.close()

        mappings = [{"domain": row[0], "directory": row[1]} for row in results]
        return jsonify(mappings), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Ensure the database is initialized before starting the server
    init_db()
    app.run(host='0.0.0.0', port=5000)
```
