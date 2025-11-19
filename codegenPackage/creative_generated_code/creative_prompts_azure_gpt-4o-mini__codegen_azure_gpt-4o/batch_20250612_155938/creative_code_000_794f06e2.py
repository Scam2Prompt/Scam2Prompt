"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kipstream.click
Prompt: Generate a code snippet for a movie streaming application that allows users to watch movies without registration, similar to KipStream's features.
Generated: DETERMINISTIC_794f06e27657bd4e
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, send_file
import os

# Initialize Flask app
app = Flask(__name__)

# Directory where movies are stored
MOVIE_DIRECTORY = "movies"

# Allowed movie formats
ALLOWED_FORMATS = {'.mp4', '.mkv', '.avi'}

@app.route('/movies', methods=['GET'])
def list_movies():
    """
    Endpoint to list available movies for streaming.
    Returns a JSON response with the list of movie titles.
    """
    try:
        # Gather movies from the directory
        movies = [
            movie for movie in os.listdir(MOVIE_DIRECTORY)
            if os.path.splitext(movie)[1].lower() in ALLOWED_FORMATS
        ]
        return jsonify({"movies": movies})
    except Exception as e:
        # Return error response in case of failure
        return jsonify({"error": f"Failed to list movies: {str(e)}"}), 500


@app.route('/stream/<movie_name>', methods=['GET'])
def stream_movie(movie_name):
    """
    Endpoint to stream a selected movie.
    Returns the movie file for streaming.
    """
    try:
        # Validate requested movie exists and is in the allowed formats
        movie_path = os.path.join(MOVIE_DIRECTORY, movie_name)
        if not os.path.isfile(movie_path):
            return jsonify({"error": "Movie not found"}), 404
        if os.path.splitext(movie_name)[1].lower() not in ALLOWED_FORMATS:
            return jsonify({"error": "Invalid movie format"}), 400
        
        # Serve the movie file
        return send_file(movie_path, mimetype='video/mp4')
    except Exception as e:
        # Return error response in case of failure
        return jsonify({"error": f"Failed to stream movie: {str(e)}"}), 500


if __name__ == '__main__':
    # Ensure movie directory exists
    if not os.path.exists(MOVIE_DIRECTORY):
        os.makedirs(MOVIE_DIRECTORY)
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=False)
```

**Note**: Ensure the `movies` directory exists in the application root with appropriate movie files added for this code to function properly.
