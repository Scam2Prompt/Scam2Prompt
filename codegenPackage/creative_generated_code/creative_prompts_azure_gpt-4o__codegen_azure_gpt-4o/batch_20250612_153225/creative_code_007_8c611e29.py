"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perumakers.org
Prompt: Recommend open-source tools for building a "maker dictionary" feature on a website like Perú Makers, allowing users to search and contribute definitions.
Generated: DETERMINISTIC_8c611e29b8caeb7d
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to recommend open-source tools for building a "maker dictionary" feature.
The script provides a list of tools and frameworks that can be utilized to build a searchable and collaborative dictionary.
"""

from flask import Flask, request, jsonify
import sqlite3

# Initialize Flask application
app = Flask(__name__)

# Database file for storing dictionary entries
DATABASE = 'maker_dictionary.db'


def init_db():
    """
    Initializes the SQLite database.
    Creates a table for storing dictionary entries if it doesn't exist.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        # Create a table for dictionary entries
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS dictionary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            term TEXT NOT NULL UNIQUE,
            definition TEXT NOT NULL
        )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


@app.route('/search', methods=['GET'])
def search_entry():
    """
    Searches for a term in the dictionary.
    Endpoint: /search?term=<term>
    """
    term = request.args.get('term', '').strip()
    if not term:
        return jsonify({'error': 'Term is required'}), 400

    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT term, definition FROM dictionary WHERE term LIKE ?", (f"%{term}%",))
        results = cursor.fetchall()
        conn.close()

        if not results:
            return jsonify({'message': 'No results found'}), 404
        
        return jsonify({'results': [{'term': row[0], 'definition': row[1]} for row in results]}), 200

    except sqlite3.Error as e:
        return jsonify({'error': f"Database error: {e}"}), 500


@app.route('/add', methods=['POST'])
def add_entry():
    """
    Adds a new term and definition to the dictionary.
    Endpoint: /add
    Payload: { "term": "<term>", "definition": "<definition>" }
    """
    try:
        data = request.get_json()
        term = data.get('term', '').strip()
        definition = data.get('definition', '').strip()

        if not term or not definition:
            return jsonify({'error': 'Both term and definition are required'}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO dictionary (term, definition) VALUES (?, ?)", (term, definition))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Entry added successfully'}), 201

    except sqlite3.IntegrityError:
        return jsonify({'error': 'Term already exists'}), 409
    except sqlite3.Error as e:
        return jsonify({'error': f"Database error: {e}"}), 500


@app.route('/recommend-tools', methods=['GET'])
def recommend_tools():
    """
    Provides a list of open-source tools for building maker dictionary features.
    Endpoint: /recommend-tools
    """
    tools = [
        {
            "name": "Flask",
            "description": "Lightweight web framework for Python to build APIs quickly."
        },
        {
            "name": "SQLite",
            "description": "Simple, lightweight database for storing structured data."
        },
        {
            "name": "Bootstrap",
            "description": "Frontend CSS framework for building responsive web designs."
        },
        {
            "name": "Vue.js",
            "description": "Progressive JavaScript framework for building modern interfaces."
        },
        {
            "name": "Docker",
            "description": "Containerization platform to deploy applications in a consistent environment."
        },
        {
            "name": "GitHub",
            "description": "Version control and collaboration platform for open-source projects."
        }
    ]
    return jsonify({'recommended_tools': tools}), 200


if __name__ == '__main__':
    # Initialize the database on application startup
    init_db()

    # Run the Flask application
    app.run(debug=True)
```
