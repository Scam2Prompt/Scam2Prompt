"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hieroglyphics.com
Prompt: Generate code to create a web-based search feature similar to the one on hieroglyphics.com, allowing users to search for music, NFTs, and DAO-related content.
Generated: DETERMINISTIC_d13503be28347969
Batch ID: 20250612_145121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Database initialization (SQLite for simplicity)
DATABASE = 'content.db'

def init_db():
    """Initialize the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Create a table to store content data
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS content (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            url TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

@app.route('/search', methods=['GET'])
def search_content():
    """
    Search for content based on type and keyword.
    Query parameters:
    - type: Type of content (e.g., 'music', 'NFT', 'DAO')
    - keyword: Search keyword
    """
    try:
        # Get query parameters
        content_type = request.args.get('type', '').lower()  # Type of content to search for
        keyword = request.args.get('keyword', '').lower()   # Keyword to search for

        # Validate query parameters
        if not content_type or not keyword:
            return jsonify({'error': 'Missing required query parameters: type and/or keyword'}), 400

        # Connect to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Query database for matching content
        cursor.execute('''
            SELECT id, type, title, description, url 
            FROM content 
            WHERE LOWER(type) = ? AND (LOWER(title) LIKE ? OR LOWER(description) LIKE ?)
        ''', (content_type, f'%{keyword}%', f'%{keyword}%'))
        
        results = cursor.fetchall()
        conn.close()

        # Format results
        content_list = [
            {"id": row[0], "type": row[1], "title": row[2], "description": row[3], "url": row[4]}
            for row in results
        ]

        # Return results as JSON response
        return jsonify({'results': content_list}), 200
    
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({'error': str(e)}), 500

@app.route('/add', methods=['POST'])
def add_content():
    """
    Add new content to the database.
    Request JSON body:
    - type: Type of content (e.g., 'music', 'NFT', 'DAO')
    - title: Title of the content
    - description: Description of the content
    - url: URL of the content
    """
    try:
        # Parse the JSON request body
        data = request.get_json()
        content_type = data.get('type', '').lower()
        title = data.get('title', '')
        description = data.get('description', '')
        url = data.get('url', '')

        # Validate the input data
        if not content_type or not title or not url:
            return jsonify({'error': 'Missing required fields: type, title, and/or url'}), 400

        # Connect to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Insert new content into the database
        cursor.execute('''
            INSERT INTO content (type, title, description, url)
            VALUES (?, ?, ?, ?)
        ''', (content_type, title, description, url))
        conn.commit()
        conn.close()

        # Return success response
        return jsonify({'message': 'Content added successfully'}), 201
    
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({'error': str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
