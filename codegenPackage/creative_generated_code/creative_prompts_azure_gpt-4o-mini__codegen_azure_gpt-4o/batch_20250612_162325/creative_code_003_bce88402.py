"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plus.endeavorschools.com
Prompt: Develop an API endpoint that allows users to search for Endeavor Schools by state and program type, such as STEM or Active Athletes.
Generated: DETERMINISTIC_bce884021e596448
Batch ID: 20250612_162325
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

# Function to establish database connection
def get_db_connection():
    """Establishes and returns a connection to the SQLite database."""
    conn = sqlite3.connect('endeavor_schools.db')
    conn.row_factory = sqlite3.Row  # Ensures rows are returned as dictionaries
    return conn

# API Endpoint: Search for Endeavor Schools by state and program type
@app.route('/search-schools', methods=['GET'])
def search_schools():
    """
    API endpoint to search for schools by state and program type.
    Query Parameters:
        - state: str (required)
        - program_type: str (optional)
    Returns:
        - List of schools matching the criteria or an error message.
    """
    try:
        # Get query parameters
        state = request.args.get('state')
        program_type = request.args.get('program_type')

        # Validate required parameters
        if not state:
            return jsonify({"error": "State parameter is required."}), 400

        # Establish database connection
        conn = get_db_connection()
        cursor = conn.cursor()

        # Construct SQL query dynamically based on provided parameters
        query = "SELECT * FROM schools WHERE state = ?"
        params = [state]

        if program_type:
            query += " AND program_type = ?"
            params.append(program_type)

        # Execute query
        cursor.execute(query, params)
        schools = cursor.fetchall()

        # Close connection
        conn.close()

        # Format results
        school_list = [dict(school) for school in schools]

        return jsonify({"schools": school_list, "count": len(school_list)}), 200

    except sqlite3.Error as e:
        # Handle database errors
        return jsonify({"error": "Database error: " + str(e)}), 500

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** 
- Ensure you have a SQLite database (`endeavor_schools.db`) with a table named `schools` that contains columns such as `id`, `name`, `state`, and `program_type`.
- Install Flask (`pip install flask`) and set up the database with relevant data to test this API.
