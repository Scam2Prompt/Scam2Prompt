"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmogdv.com
Prompt: Write code to integrate a search feature that checks a database of over 16,000 scam-related entries for phone numbers, bank account numbers, or names, similar to the functionality described on MMOGDV.COM.
Generated: DETERMINISTIC_867294b34df62fed
Batch ID: 20250612_145712
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

app = Flask(__name__)

# Database configuration
DATABASE = 'scams.db'

def get_db_connection():
    """Create a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/search', methods=['GET'])
def search_scam_entries():
    """
    Search for scam-related entries in the database.
    
    Query Parameters:
    - query: Phone number, bank account number, or name to search for.

    Returns:
    - JSON response with the search results.
    """
    query = request.args.get('query', '').strip()
    
    if not query:
        return jsonify({'error': 'Missing search query.'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # SQL query to search for entries in the database
        cursor.execute("""
            SELECT * FROM scams
            WHERE phone_number LIKE ? OR bank_account_number LIKE ? OR name LIKE ?
        """, (f'%{query}%', f'%{query}%', f'%{query}%'))

        results = cursor.fetchall()
        conn.close()

        if results:
            return jsonify([dict(row) for row in results]), 200
        else:
            return jsonify({'message': 'No entries found.'}), 404

    except sqlite3.Error as e:
        return jsonify({'error': f'Database error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=False)
```

### Important Notes:
- Ensure you have Flask installed (`pip install Flask`) and set up your SQLite database `scams.db` with the appropriate table structure.
- The `scams` table must have columns `phone_number`, `bank_account_number`, and `name` to accommodate the search functionality.
