"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jusoor.ch
Prompt: Generate code for a web application that tracks humanitarian interventions and medical aid distribution, aligning with Jusoor International's programs.
Generated: DETERMINISTIC_333d55984762f9a4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# humanitarian_tracker.py

from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Database initialization
DATABASE = 'aid_tracker.db'

def init_db():
    """Initializes the database with the required schema."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS interventions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            program_name TEXT NOT NULL,
            region TEXT NOT NULL,
            aid_type TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            date_distributed DATE NOT NULL,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Error handler for database operations
@app.errorhandler(500)
def handle_internal_error(error):
    """Returns a generic error message for server errors."""
    return jsonify({"error": "An internal error occurred. Please try again later."}), 500

@app.route('/interventions', methods=['POST'])
def add_intervention():
    """
    Endpoint to add a new intervention record.
    Expected JSON payload:
    {
        "program_name": "Program Name",
        "region": "Region Name",
        "aid_type": "Type of Aid",
        "quantity": 100,
        "date_distributed": "YYYY-MM-DD",
        "notes": "Additional notes"
    }
    """
    try:
        data = request.get_json()
        
        # Validate input
        required_fields = ["program_name", "region", "aid_type", "quantity", "date_distributed"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO interventions (program_name, region, aid_type, quantity, date_distributed, notes)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (data['program_name'], data['region'], data['aid_type'], data['quantity'], data['date_distributed'], data.get('notes', None)))
        conn.commit()
        conn.close()

        return jsonify({"message": "Intervention record added successfully."}), 201

    except Exception as e:
        return jsonify({"error": "Failed to add intervention record.", "details": str(e)}), 500

@app.route('/interventions', methods=['GET'])
def list_interventions():
    """
    Endpoint to list all intervention records.
    Query parameters can be used for filtering, e.g., /interventions?region=Syria
    """
    try:
        filters = request.args
        query = 'SELECT * FROM interventions WHERE 1=1'
        params = []

        for key, value in filters.items():
            query += f' AND {key}=?'
            params.append(value)
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()

        interventions = []
        for row in results:
            interventions.append({
                "id": row[0],
                "program_name": row[1],
                "region": row[2],
                "aid_type": row[3],
                "quantity": row[4],
                "date_distributed": row[5],
                "notes": row[6]
            })

        return jsonify(interventions), 200

    except Exception as e:
        return jsonify({"error": "Failed to retrieve intervention records.", "details": str(e)}), 500

@app.route('/interventions/<int:id>', methods=['PUT'])
def update_intervention(id):
    """
    Endpoint to update an existing intervention record by ID.
    Expected JSON payload (similar to POST):
    {
        "program_name": "Program Name",
        "region": "Region Name",
        "aid_type": "Type of Aid",
        "quantity": 120,
        "date_distributed": "YYYY-MM-DD",
        "notes": "Updated notes"
    }
    """
    try:
        data = request.get_json()
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE interventions
            SET program_name=?, region=?, aid_type=?, quantity=?, date_distributed=?, notes=?
            WHERE id=?
        ''', (data['program_name'], data['region'], data['aid_type'], data['quantity'], data['date_distributed'], data.get('notes', None), id))
        conn.commit()
        conn.close()

        return jsonify({"message": "Intervention record updated successfully."}), 200

    except Exception as e:
        return jsonify({"error": "Failed to update intervention record.", "details": str(e)}), 500

@app.route('/interventions/<int:id>', methods=['DELETE'])
def delete_intervention(id):
    """
    Endpoint to delete an intervention record by ID.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM interventions WHERE id=?', (id,))
        conn.commit()
        conn.close()

        return jsonify({"message": "Intervention record deleted successfully."}), 200

    except Exception as e:
        return jsonify({"error": "Failed to delete intervention record.", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
