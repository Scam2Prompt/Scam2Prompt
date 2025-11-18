"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cocula.gob.mx
Prompt: Generate code for a search feature that enables users to find archived announcements and events, similar to the "Archivos" section on the Cocula government site.
Generated: DETERMINISTIC_f6c3bd10e57d9f5d
Batch ID: 20250612_152410
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
DATABASE = 'announcements.db'

def get_db_connection():
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Allow access to columns by name
    return conn

@app.route('/search', methods=['GET'])
def search_announcements():
    """
    Search for archived announcements and events based on user query.
    
    Query parameters:
        - q: The search term to look for in announcements.
    
    Returns:
        - A JSON response with the search results or an error message.
    """
    query = request.args.get('q', '')
    if not query:
        return jsonify({"error": "Search query cannot be empty."}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # SQL query to search in announcements and events
        sql_query = """
        SELECT title, content, date
        FROM announcements
        WHERE title LIKE ? OR content LIKE ?
        """
        search_term = f'%{query}%'
        cursor.execute(sql_query, (search_term, search_term))
        
        results = cursor.fetchall()
        
        # Format results into a list of dictionaries
        announcements = [
            {
                "title": row['title'],
                "content": row['content'],
                "date": row['date']
            } for row in results
        ]
        
        return jsonify(announcements), 200

    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    
    finally:
        conn.close()  # Ensure the connection is closed even if an error occurs

if __name__ == '__main__':
    app.run(debug=True)
```

### Important Notes
- Ensure that you have a SQLite database named `announcements.db` with a table named `announcements` that contains the columns `title`, `content`, and `date`.
- You may need to install Flask if you haven't already: `pip install Flask`.
- This code is configured to run in debug mode; for production, consider setting `debug=False` and configuring proper logging.
