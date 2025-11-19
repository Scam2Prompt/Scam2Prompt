"""
Generated Code Metadata:
========================
Original URL: https://mmogdv.com
Prompt: Write code to integrate a search feature that checks a database of over 16,000 scam-related entries for phone numbers, bank account numbers, or names, similar to the functionality described on MMOGDV.COM.
Generated: DETERMINISTIC_867294b34df62fed
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database configuration
DATABASE = 'scam_entries.db'

def get_db_connection():
    """Establish a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Enable row access by name
    return conn

@app.route('/search', methods=['GET'])
def search_scam_entries():
    """Search for scam-related entries based on phone numbers, bank account numbers, or names."""
    query = request.args.get('query', '').strip()
    
    if not query:
        return jsonify({"error": "Query parameter is required."}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Prepare the SQL query to search for the input in the database
        sql_query = """
        SELECT * FROM scam_entries
        WHERE phone_number LIKE ? OR bank_account_number LIKE ? OR name LIKE ?
        """
        search_pattern = f'%{query}%'
        cursor.execute(sql_query, (search_pattern, search_pattern, search_pattern))
        
        # Fetch all matching entries
        results = cursor.fetchall()
        
        # Close the database connection
        conn.close()

        # Format the results into a list of dictionaries
        entries = [dict(row) for row in results]
        
        return jsonify(entries), 200

    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```

### Notes:
- Ensure that the SQLite database `scam_entries.db` exists and has a table named `scam_entries` with appropriate columns (`phone_number`, `bank_account_number`, `name`).
- The application uses Flask for the web framework. Make sure to install Flask using `pip install Flask`.
- The search functionality is case-insensitive due to the use of the `LIKE` operator with wildcards.
- Error handling is included for both database errors and unexpected exceptions.
