"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingroofing.com
Prompt: Suggest an API for integrating customer reviews into a roofing service website, similar to the testimonials displayed on King Roofing's webpage.
Generated: DETERMINISTIC_13d48f67db2031a1
Batch ID: 20250612_145114
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

# Database setup: Initialize database and create table if it doesn't exist
def initialize_database():
    conn = sqlite3.connect('reviews.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            rating INTEGER NOT NULL CHECK(rating >= 1 AND rating <= 5),
            review TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
initialize_database()

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    """
    Endpoint to fetch all customer reviews.
    Returns:
        JSON response with list of all reviews.
    """
    try:
        conn = sqlite3.connect('reviews.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, rating, review, timestamp FROM reviews ORDER BY timestamp DESC')
        reviews = cursor.fetchall()
        conn.close()

        # Format response
        response = [
            {"id": row[0], "name": row[1], "rating": row[2], "review": row[3], "timestamp": row[4]}
            for row in reviews
        ]
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch reviews", "details": str(e)}), 500


@app.route('/api/reviews', methods=['POST'])
def add_review():
    """
    Endpoint to add a new customer review.
    Request JSON should include 'name', 'rating', and 'review'.
    Returns:
        Success message or error response.
    """
    try:
        data = request.get_json()
        
        # Validate the input
        if not data or 'name' not in data or 'rating' not in data or 'review' not in data:
            return jsonify({"error": "Invalid input. 'name', 'rating', and 'review' are required."}), 400
        
        name = data['name']
        rating = data['rating']
        review = data['review']
        
        # Ensure rating is within valid range
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            return jsonify({"error": "Invalid rating. It must be an integer between 1 and 5."}), 400
        
        conn = sqlite3.connect('reviews.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO reviews (name, rating, review) VALUES (?, ?, ?)', (name, rating, review))
        conn.commit()
        conn.close()
        
        return jsonify({"message": "Review added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": "Failed to add review", "details": str(e)}), 500


@app.route('/api/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    """
    Endpoint to delete a customer review by ID.
    Args:
        review_id (int): ID of the review to delete.
    Returns:
        Success message or error response.
    """
    try:
        conn = sqlite3.connect('reviews.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM reviews WHERE id = ?', (review_id,))
        conn.commit()
        conn.close()
        
        if cursor.rowcount == 0:
            return jsonify({"error": "Review not found"}), 404
        
        return jsonify({"message": "Review deleted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": "Failed to delete review", "details": str(e)}), 500


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
1. To test this API, you can use tools like Postman or Curl.
2. Ensure you have `Flask` installed (`pip install flask`) and SQLite available.
3. The database file `reviews.db` will be created automatically in the working directory upon the first run.
4. Disable `debug=True` in production for enhanced security.
