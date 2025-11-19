"""
Generated Code Metadata:
========================
Original URL: https://jasmynetwork.org
Prompt: Create a code snippet that demonstrates how to integrate user ratings for web content within the Stumble! application framework.
Generated: DETERMINISTIC_b5bfb787c47f84cc
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
import sqlite3
from typing import Dict, Any, Optional

# Initialize Flask application
app = Flask(__name__)

# Database configuration
DATABASE = 'stumble.db'

def get_db_connection():
    """Create and return a database connection."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    """Initialize the database with required tables."""
    conn = get_db_connection()
    try:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS content_ratings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(content_id, user_id)
            )
        ''')
        conn.commit()
    finally:
        conn.close()

@app.route('/api/ratings', methods=['POST'])
def submit_rating():
    """Handle submission of a new rating for web content."""
    data: Optional[Dict[str, Any]] = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    required_fields = ['content_id', 'user_id', 'rating']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        rating = int(data['rating'])
        if rating < 1 or rating > 5:
            return jsonify({'error': 'Rating must be between 1 and 5'}), 400
        
        conn = get_db_connection()
        try:
            conn.execute('''
                INSERT OR REPLACE INTO content_ratings (content_id, user_id, rating)
                VALUES (?, ?, ?)
            ''', (data['content_id'], data['user_id'], rating))
            conn.commit()
            return jsonify({'message': 'Rating submitted successfully'}), 201
        finally:
            conn.close()
    except ValueError:
        return jsonify({'error': 'Invalid rating value'}), 400
    except sqlite3.IntegrityError as e:
        return jsonify({'error': 'Database integrity error', 'details': str(e)}), 400

@app.route('/api/ratings/<int:content_id>', methods=['GET'])
def get_content_ratings(content_id: int):
    """Retrieve all ratings for a specific content item."""
    conn = get_db_connection()
    try:
        cursor = conn.execute('''
            SELECT rating FROM content_ratings
            WHERE content_id = ?
        ''', (content_id,))
        ratings = [row['rating'] for row in cursor.fetchall()]
        
        if not ratings:
            return jsonify({'message': 'No ratings found for this content'}), 404
        
        average_rating = sum(ratings) / len(ratings)
        return jsonify({
            'content_id': content_id,
            'average_rating': round(average_rating, 2),
            'total_ratings': len(ratings),
            'ratings': ratings
        }), 200
    finally:
        conn.close()

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions and return JSON responses."""
    return jsonify({
        'error': e.name,
        'message': e.description
    }), e.code

@app.errorhandler(Exception)
def handle_exception(e):
    """Handle unexpected exceptions."""
    return jsonify({
        'error': 'Internal Server Error',
        'message': 'An unexpected error occurred'
    }), 500

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)
```
