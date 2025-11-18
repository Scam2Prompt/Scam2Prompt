"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedigitalage.co.nz
Prompt: Recommend a library or API for managing client reviews on a business website, and provide example code for displaying and filtering reviews dynamically.
Generated: DETERMINISTIC_0bcf5c7ad7d31406
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Example Code for Managing and Displaying Client Reviews on a Business Website
# Using Flask as the web framework and SQLite as the database.

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize SQLite database
DATABASE = 'reviews.db'


def get_db_connection():
    """Establish a connection to the SQLite database."""
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row  # Access results as dictionaries
    return connection


# Create the database schema
@app.before_first_request
def init_db():
    """Create the reviews table if it doesn't already exist."""
    conn = get_db_connection()
    with conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_name TEXT NOT NULL,
            review_text TEXT NOT NULL,
            rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
    conn.close()


@app.route('/reviews', methods=['GET'])
def get_reviews():
    """
    Endpoint to fetch all reviews.
    Optional query parameters:
        - min_rating: Filter reviews by minimum rating.
    """
    min_rating = request.args.get('min_rating', type=int)  # Optional filter

    conn = get_db_connection()
    cursor = conn.cursor()

    if min_rating:
        # Fetch reviews filtered by minimum rating
        cursor.execute("SELECT * FROM reviews WHERE rating >= ?", (min_rating,))
    else:
        # Fetch all reviews
        cursor.execute("SELECT * FROM reviews")

    reviews = cursor.fetchall()
    conn.close()

    # Return reviews as JSON
    return jsonify([dict(review) for review in reviews])


@app.route('/reviews', methods=['POST'])
def add_review():
    """
    Endpoint to add a new client review.
    Request JSON body should include:
        - client_name: Name of the client.
        - review_text: Text of the review.
        - rating: Rating (1-5).
    """
    data = request.json

    # Input validation
    if 'client_name' not in data or 'review_text' not in data or 'rating' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    if not (1 <= data['rating'] <= 5):
        return jsonify({'error': 'Rating must be between 1 and 5'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Insert the new review into the database
        cursor.execute(
            "INSERT INTO reviews (client_name, review_text, rating) VALUES (?, ?, ?)",
            (data['client_name'], data['review_text'], data['rating'])
        )
        conn.commit()
        return jsonify({'message': 'Review added successfully'}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({'error': 'Failed to add review', 'details': str(e)}), 500
    finally:
        conn.close()


@app.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    """
    Endpoint to delete a review by its ID.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Delete the review with the specified ID
        cursor.execute("DELETE FROM reviews WHERE id = ?", (review_id,))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({'error': 'Review not found'}), 404

        return jsonify({'message': 'Review deleted successfully'}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({'error': 'Failed to delete review', 'details': str(e)}), 500
    finally:
        conn.close()


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
1. Install dependencies: `pip install flask`.
2. Execute the script to create the SQLite database (`reviews.db`) and run the server.
3. Use tools like Postman or cURL to interact with the endpoints (`GET /reviews`, `POST /reviews`, `DELETE /reviews/<id>`).
