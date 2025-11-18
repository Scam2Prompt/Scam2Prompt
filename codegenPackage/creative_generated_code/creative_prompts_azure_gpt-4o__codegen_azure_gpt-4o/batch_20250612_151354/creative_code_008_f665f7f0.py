"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1minutedog.com
Prompt: Recommend a library for creating a rating system for training videos, like the 5-star ratings displayed for the free videos on the "1 Minute Dog Training" site.
Generated: DETERMINISTIC_f665f7f0fa15711f
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready implementation in Python using Flask and SQLite for a 5-star rating system for training videos:

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = 'ratings.db'

def init_db():
    """
    Initialize the SQLite database with a table for storing video ratings.
    """
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS video_ratings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            video_id TEXT NOT NULL,
            rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5)
        )
    ''')
    connection.commit()
    connection.close()

# Initialize the database when the application starts
init_db()

@app.route('/rate', methods=['POST'])
def rate_video():
    """
    Endpoint for submitting a rating for a video.

    Expected JSON input:
    {
        "video_id": "example_video_id",
        "rating": 5
    }

    Returns:
        JSON response with success or error message.
    """
    data = request.json
    video_id = data.get('video_id')
    rating = data.get('rating')

    # Validate input
    if not video_id or not isinstance(video_id, str):
        return jsonify({"error": "Invalid or missing 'video_id'"}), 400
    if not rating or not isinstance(rating, int) or rating < 1 or rating > 5:
        return jsonify({"error": "Invalid or missing 'rating'. Must be an integer between 1 and 5."}), 400

    try:
        # Insert the rating into the database
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO video_ratings (video_id, rating) VALUES (?, ?)', (video_id, rating))
        connection.commit()
        connection.close()

        return jsonify({"success": f"Rating of {rating} submitted for video ID {video_id}"}), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/average_rating/<video_id>', methods=['GET'])
def get_average_rating(video_id):
    """
    Endpoint for retrieving the average rating of a specific video.

    URL Parameter:
        video_id: The ID of the video to retrieve the average rating for.

    Returns:
        JSON response with the average rating or an error message.
    """
    try:
        # Query the database for the average rating of the video
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute('SELECT AVG(rating) FROM video_ratings WHERE video_id = ?', (video_id,))
        result = cursor.fetchone()
        connection.close()

        # Check if the video has any ratings
        if result[0] is None:
            return jsonify({"error": f"No ratings found for video ID {video_id}"}), 404

        # Return the average rating
        return jsonify({"video_id": video_id, "average_rating": round(result[0], 2)}), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/ratings/<video_id>', methods=['GET'])
def get_all_ratings(video_id):
    """
    Endpoint for retrieving all ratings for a specific video.

    URL Parameter:
        video_id: The ID of the video to retrieve ratings for.

    Returns:
        JSON response with a list of ratings or an error message.
    """
    try:
        # Query the database for all ratings of the video
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute('SELECT rating FROM video_ratings WHERE video_id = ?', (video_id,))
        ratings = cursor.fetchall()
        connection.close()

        # Check if the video has any ratings
        if not ratings:
            return jsonify({"error": f"No ratings found for video ID {video_id}"}), 404

        # Return the list of ratings
        return jsonify({"video_id": video_id, "ratings": [rating[0] for rating in ratings]}), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)
```

### Key Features of the Code:
1. **Endpoints**:
   - `/rate`: Submit a rating for a video.
   - `/average_rating/<video_id>`: Retrieve the average rating for a specific video.
   - `/ratings/<video_id>`: Retrieve all ratings for a specific video.
   
2. **Error Handling**:
   - Validates input data.
   - Handles unexpected errors gracefully and returns meaningful error messages.

3. **Database**:
   - SQLite is used for storing ratings data.
   - The database is initialized automatically when the app starts.

4. **Best Practices**:
   - Input validation and proper HTTP status codes.
   - Separation of concerns for database handling and request processing.

This code is designed to be production-ready and adheres to best practices. You can extend it further based on specific requirements, such as user authentication or additional data fields.
