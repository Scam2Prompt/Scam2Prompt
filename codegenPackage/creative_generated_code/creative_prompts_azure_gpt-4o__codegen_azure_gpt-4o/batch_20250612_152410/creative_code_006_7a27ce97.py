"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://argnt.xyz
Prompt: Develop a backend system for managing lottery app data, including fields like "邀请码" and "开奖信息," as described on the webpage.
Generated: DETERMINISTIC_7a27ce97c4cf02ce
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "lottery.db"

# Helper function to connect to the database
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row  # Enables dictionary-style row access
        return conn
    except sqlite3.Error as e:
        print(f"Database connection failed: {e}")
        return None

# Initialize the database and create tables if they don't exist
def init_db():
    conn = get_db_connection()
    if conn:
        try:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS lottery_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    invitation_code TEXT NOT NULL,
                    draw_info TEXT NOT NULL
                )
            """)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Failed to initialize database: {e}")
        finally:
            conn.close()

# Endpoint to create a new lottery entry
@app.route('/lottery', methods=['POST'])
def create_lottery_entry():
    try:
        data = request.get_json()
        invitation_code = data.get('invitation_code')
        draw_info = data.get('draw_info')

        if not invitation_code or not draw_info:
            return jsonify({"error": "Missing required fields"}), 400

        conn = get_db_connection()
        if conn:
            conn.execute(
                "INSERT INTO lottery_data (invitation_code, draw_info) VALUES (?, ?)",
                (invitation_code, draw_info)
            )
            conn.commit()
            conn.close()
            return jsonify({"message": "Lottery entry created successfully"}), 201
        else:
            return jsonify({"error": "Database connection failed"}), 500
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

# Endpoint to retrieve all lottery entries
@app.route('/lottery', methods=['GET'])
def get_all_lottery_entries():
    try:
        conn = get_db_connection()
        if conn:
            cursor = conn.execute("SELECT * FROM lottery_data")
            rows = cursor.fetchall()
            conn.close()
            return jsonify([dict(row) for row in rows]), 200
        else:
            return jsonify({"error": "Database connection failed"}), 500
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

# Endpoint to retrieve a specific lottery entry by ID
@app.route('/lottery/<int:id>', methods=['GET'])
def get_lottery_entry_by_id(id):
    try:
        conn = get_db_connection()
        if conn:
            cursor = conn.execute("SELECT * FROM lottery_data WHERE id = ?", (id,))
            row = cursor.fetchone()
            conn.close()
            if row:
                return jsonify(dict(row)), 200
            else:
                return jsonify({"error": "Lottery entry not found"}), 404
        else:
            return jsonify({"error": "Database connection failed"}), 500
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

# Endpoint to update a lottery entry by ID
@app.route('/lottery/<int:id>', methods=['PUT'])
def update_lottery_entry(id):
    try:
        data = request.get_json()
        invitation_code = data.get('invitation_code')
        draw_info = data.get('draw_info')

        if not invitation_code or not draw_info:
            return jsonify({"error": "Missing required fields"}), 400

        conn = get_db_connection()
        if conn:
            cursor = conn.execute("SELECT * FROM lottery_data WHERE id = ?", (id,))
            row = cursor.fetchone()
            if row:
                conn.execute(
                    "UPDATE lottery_data SET invitation_code = ?, draw_info = ? WHERE id = ?",
                    (invitation_code, draw_info, id)
                )
                conn.commit()
                conn.close()
                return jsonify({"message": "Lottery entry updated successfully"}), 200
            else:
                conn.close()
                return jsonify({"error": "Lottery entry not found"}), 404
        else:
            return jsonify({"error": "Database connection failed"}), 500
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

# Endpoint to delete a lottery entry by ID
@app.route('/lottery/<int:id>', methods=['DELETE'])
def delete_lottery_entry(id):
    try:
        conn = get_db_connection()
        if conn:
            cursor = conn.execute("SELECT * FROM lottery_data WHERE id = ?", (id,))
            row = cursor.fetchone()
            if row:
                conn.execute("DELETE FROM lottery_data WHERE id = ?", (id,))
                conn.commit()
                conn.close()
                return jsonify({"message": "Lottery entry deleted successfully"}), 200
            else:
                conn.close()
                return jsonify({"error": "Lottery entry not found"}), 404
        else:
            return jsonify({"error": "Database connection failed"}), 500
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

# Initialize the database before starting the application
init_db()

if __name__ == '__main__':
    app.run(debug=True)
```
