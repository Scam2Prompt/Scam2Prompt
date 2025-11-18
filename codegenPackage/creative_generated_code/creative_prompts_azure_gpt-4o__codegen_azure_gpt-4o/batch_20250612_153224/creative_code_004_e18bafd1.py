"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sharawatch.org
Prompt: Suggest APIs or tools for organizing international contests, such as the caricature contest "Full batteries – empty land" mentioned on the sharawatch.org website.
Generated: DETERMINISTIC_e18bafd17defc77d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python code example for organizing an international contest system using Flask (a lightweight web framework) and SQLite for database management. It provides basic endpoints for contest creation, participant registration, and submission management.

```python
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database file path
DATABASE = 'contest.db'

def init_db():
    """
    Initialize the SQLite database with necessary tables.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS participants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contest_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            FOREIGN KEY (contest_id) REFERENCES contests (id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            participant_id INTEGER NOT NULL,
            file_url TEXT NOT NULL,
            submission_date TEXT NOT NULL,
            FOREIGN KEY (participant_id) REFERENCES participants (id)
        )
    ''')
    conn.commit()
    conn.close()

@app.before_first_request
def setup():
    """
    Perform setup tasks before the Flask app starts handling requests.
    """
    init_db()

@app.route('/contests', methods=['POST'])
def create_contest():
    """
    Endpoint to create a new contest.
    """
    data = request.json
    try:
        name = data['name']
        description = data.get('description', '')
        start_date = data['start_date']
        end_date = data['end_date']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO contests (name, description, start_date, end_date)
            VALUES (?, ?, ?, ?)
        ''', (name, description, start_date, end_date))
        conn.commit()
        conn.close()

        return jsonify({"message": "Contest created successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/participants', methods=['POST'])
def register_participant():
    """
    Endpoint to register a new participant for a contest.
    """
    data = request.json
    try:
        contest_id = data['contest_id']
        name = data['name']
        email = data['email']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO participants (contest_id, name, email)
            VALUES (?, ?, ?)
        ''', (contest_id, name, email))
        conn.commit()
        conn.close()

        return jsonify({"message": "Participant registered successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/submissions', methods=['POST'])
def submit_entry():
    """
    Endpoint to submit a contest entry.
    """
    data = request.json
    try:
        participant_id = data['participant_id']
        file_url = data['file_url']
        submission_date = data['submission_date']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO submissions (participant_id, file_url, submission_date)
            VALUES (?, ?, ?)
        ''', (participant_id, file_url, submission_date))
        conn.commit()
        conn.close()

        return jsonify({"message": "Submission uploaded successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/contests', methods=['GET'])
def list_contests():
    """
    Endpoint to list all contests.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM contests')
        contests = cursor.fetchall()
        conn.close()

        return jsonify({"contests": contests}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

### Instructions
1. Install dependencies: `pip install flask`.
2. Run the application: `python app.py`.
3. Use a tool like Postman or curl to interact with the endpoints.
