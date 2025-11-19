"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harinderfarms.com
Prompt: Create a REST API endpoint that allows users to submit feedback about their experiences with Harinder Farms' products and services, including corn silage and potato seeds.
Generated: DETERMINISTIC_453310ec2c929af8
Batch ID: 20250612_162051
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

# Database setup (SQLite for simplicity)
DATABASE = 'feedback.db'

def init_db():
    """Initialize the database and create the feedback table if it doesn't exist."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                product TEXT NOT NULL,
                rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
                comments TEXT,
                submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

# Initialize the database
init_db()

@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit feedback about Harinder Farms' products and services.
    
    Expected JSON payload:
    {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "product": "corn silage",
        "rating": 4,
        "comments": "Great product!"
    }
    
    Returns:
        201 Created: If the feedback is successfully saved.
        400 Bad Request: If the request payload is invalid.
    """
    try:
        # Parse JSON payload
        data = request.json
        if not data:
            return jsonify({"error": "Request must be in JSON format"}), 400

        # Validate required fields
        name = data.get('name')
        email = data.get('email')
        product = data.get('product')
        rating = data.get('rating')
        comments = data.get('comments', "")  # Optional field

        if not all([name, email, product, rating]):
            return jsonify({"error": "Missing required fields"}), 400
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            return jsonify({"error": "Rating must be an integer between 1 and 5"}), 400

        # Save feedback to the database
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO feedback (name, email, product, rating, comments)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, email, product, rating, comments))
            conn.commit()

        # Return success response
        return jsonify({"message": "Feedback submitted successfully"}), 201

    except Exception as e:
        # Log error in production (simplified here)
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
