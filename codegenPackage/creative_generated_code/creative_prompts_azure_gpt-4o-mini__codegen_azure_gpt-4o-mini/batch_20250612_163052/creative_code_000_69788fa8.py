"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatevortex.co
Prompt: Generate a Python script that connects users with investment education companies, similar to the Immediate Renova platform.
Generated: DETERMINISTIC_69788fa896faa1c4
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Connect to SQLite database (or create it if it doesn't exist)
DATABASE = 'investment_education.db'

def init_db():
    """Initialize the database and create the necessary table."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS companies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                website TEXT NOT NULL,
                description TEXT
            )
        ''')
        conn.commit()

@app.route('/companies', methods=['POST'])
def add_company():
    """Endpoint to add a new investment education company."""
    try:
        data = request.json
        name = data.get('name')
        website = data.get('website')
        description = data.get('description', '')

        # Validate input
        if not name or not website:
            return jsonify({'error': 'Name and website are required.'}), 400

        # Insert new company into the database
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO companies (name, website, description) VALUES (?, ?, ?)',
                           (name, website, description))
            conn.commit()

        return jsonify({'message': 'Company added successfully.'}), 201

    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

@app.route('/companies', methods=['GET'])
def get_companies():
    """Endpoint to retrieve a list of investment education companies."""
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM companies')
            companies = cursor.fetchall()

        # Format the response
        company_list = [{'id': row[0], 'name': row[1], 'website': row[2], 'description': row[3]} for row in companies]
        return jsonify(company_list), 200

    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

if __name__ == '__main__':
    # Initialize the database on startup
    init_db()
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)
```
