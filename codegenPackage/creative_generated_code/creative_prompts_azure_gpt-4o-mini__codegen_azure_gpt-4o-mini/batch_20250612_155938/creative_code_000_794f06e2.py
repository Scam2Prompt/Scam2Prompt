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
from flask import Flask, jsonify, request, send_file, abort
import os

app = Flask(__name__)

# Directory where movie files are stored
MOVIE_DIRECTORY = "movies"

# Check if the movie directory exists
if not os.path.exists(MOVIE_DIRECTORY):
    os.makedirs(MOVIE_DIRECTORY)

@app.route('/movies', methods=['GET'])
def list_movies():
    """
    Endpoint to list all available movies.
    Returns a JSON object with the movie titles.
    """
    try:
        movies = os.listdir(MOVIE_DIRECTORY)
        # Filter out files that are not videos
        movie_list = [movie for movie in movies if movie.endswith(('.mp4', '.avi', '.mov'))]
        return jsonify(movie_list), 200
    except Exception as e:
        # Log the error and return an internal server error
        app.logger.error(f"Error listing movies: {str(e)}")
        return jsonify({"error": "Unable to list movies"}), 500

@app.route('/movies/<movie_name>', methods=['GET'])
def stream_movie(movie_name):
    """
    Endpoint to stream a specific movie by name.
    Arguments:
    - movie_name: The name of the movie to stream.
    Returns the movie file if it exists, or a 404 error if not found.
    """
    try:
        file_path = os.path.join(MOVIE_DIRECTORY, movie_name)
        if os.path.exists(file_path):
            return send_file(file_path), 200
        else:
            # Return a 404 error if the movie file does not exist
            abort(404, description=f"Movie '{movie_name}' not found")
    except Exception as e:
        # Log any unexpected errors and return a generic error
        app.logger.error(f"Error streaming movie '{movie_name}': {str(e)}")
        return jsonify({"error": "Unable to stream movie"}), 500

@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 errors.
    Returns a JSON response for a not found error.
    """
    return jsonify({"error": str(error)}), 404

if __name__ == '__main__':
    # Run the app with debug mode off for production
    app.run(host='0.0.0.0', port=5000, debug=False)
```
