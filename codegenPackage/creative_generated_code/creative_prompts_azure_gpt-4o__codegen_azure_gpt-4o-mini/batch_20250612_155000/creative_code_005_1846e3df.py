"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linktre.me
Prompt: Suggest tools or libraries to create a personalized URL for a user’s link page, as described in the "Bio.links" functionality.
Generated: DETERMINISTIC_1846e3df6bf49005
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
from flask import Flask, request, jsonify
import shortuuid
import sqlite3

# Initialize Flask application
app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('link_page.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_links (
            id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            url TEXT NOT NULL,
            title TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Generate a personalized short URL
def generate_short_url(user_id):
    return shortuuid.uuid()  # Generates a unique short URL identifier

# Endpoint to create a new link for a user
@app.route('/create_link', methods=['POST'])
def create_link():
    try:
        data = request.json
        user_id = data.get('user_id')
        url = data.get('url')
        title = data.get('title')

        if not user_id or not url or not title:
            return jsonify({'error': 'Invalid input. user_id, url, and title are required.'}), 400

        link_id = generate_short_url(user_id)

        # Save the link to the database
        conn = sqlite3.connect('link_page.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO user_links (id, user_id, url, title) VALUES (?, ?, ?, ?)', 
                       (link_id, user_id, url, title))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Link created successfully', 'link_id': link_id}), 201

    except sqlite3.Error as e:
        return jsonify({'error': f'Database error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

# Endpoint to retrieve links for a specific user
@app.route('/get_links/<user_id>', methods=['GET'])
def get_links(user_id):
    try:
        # Fetch links associated with the user_id
        conn = sqlite3.connect('link_page.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, url, title FROM user_links WHERE user_id = ?', (user_id,))
        links = cursor.fetchall()
        conn.close()

        # Format the response
        response = [{'link_id': link[0], 'url': link[1], 'title': link[2]} for link in links]
        return jsonify(response), 200

    except sqlite3.Error as e:
        return jsonify({'error': f'Database error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    init_db()  # Initialize the database upon starting the application
    app.run(debug=True)  # Start the Flask application
```
