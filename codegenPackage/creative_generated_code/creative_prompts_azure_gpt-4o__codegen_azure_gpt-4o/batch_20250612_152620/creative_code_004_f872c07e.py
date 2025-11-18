"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koltinsuchitoto.com
Prompt: Suggest an API for integrating multilingual reviews and ratings into a hotel website, similar to the review section on Hostal Koltin Suchitoto's page.
Generated: DETERMINISTIC_f872c07e1130c0ae
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a clean, production-ready implementation of an API for integrating multilingual reviews and ratings into a hotel website. The code is written in Python using Flask for the backend, with proper error handling and comments throughout.

```python
from flask import Flask, request, jsonify
from googletrans import Translator  # For handling multilingual reviews
import sqlite3  # Database for storing reviews and ratings

app = Flask(__name__)
translator = Translator()

# Initialize the database
DB_FILE = 'reviews.db'


def init_db():
    """Initialize the SQLite database for storing reviews and ratings."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            review TEXT NOT NULL,
            rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
            language TEXT NOT NULL DEFAULT 'en',
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/api/reviews', methods=['POST'])
def add_review():
    """
    Endpoint to add a new review.
    Expects JSON with 'name', 'review', 'rating', and 'language' (optional).
    """
    try:
        data = request.get_json()
        name = data.get('name')
        review = data.get('review')
        rating = data.get('rating')
        language = data.get('language', 'en')  # Default language is English

        # Validate input
        if not name or not review or not rating:
            return jsonify({'error': 'Missing required fields'}), 400
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            return jsonify({'error': 'Rating must be an integer between 1 and 5'}), 400

        # Save to database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO reviews (name, review, rating, language)
            VALUES (?, ?, ?, ?)
        ''', (name, review, rating, language))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Review added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    """
    Endpoint to fetch all reviews.
    Supports optional 'language' query parameter for translation.
    """
    try:
        language = request.args.get('language', 'en')  # Default language is English

        # Fetch reviews from database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('SELECT name, review, rating, language, timestamp FROM reviews')
        rows = cursor.fetchall()
        conn.close()

        reviews = []
        for row in rows:
            name, review, rating, original_language, timestamp = row
            translated_review = review

            # Translate review if necessary
            if original_language != language:
                translated_review = translator.translate(review, src=original_language, dest=language).text

            reviews.append({
                'name': name,
                'review': translated_review,
                'rating': rating,
                'original_language': original_language,
                'timestamp': timestamp
            })

        return jsonify({'reviews': reviews}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/reviews/average-rating', methods=['GET'])
def get_average_rating():
    """
    Endpoint to calculate the average rating.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('SELECT AVG(rating) FROM reviews')
        average_rating = cursor.fetchone()[0]
        conn.close()

        return jsonify({'average_rating': average_rating or 0}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # Initialize the database before starting the server
    init_db()

    # Start the Flask server
    app.run(debug=False, host='0.0.0.0', port=5000)
```

**Instructions for Use:**
1. Install dependencies:
   ```
   pip install flask googletrans==4.0.0-rc1
   ```
2. Run the script:
   ```
   python app.py
   ```
3. Use endpoints:
   - `POST /api/reviews` to add a review (provide JSON body).
   - `GET /api/reviews` to fetch all reviews, optionally with `?language=<language_code>` for translation.
   - `GET /api/reviews/average-rating` to get the average rating.

Let me know if you need additional features!
