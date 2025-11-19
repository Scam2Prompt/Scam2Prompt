"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://as-media.rs
Prompt: Develop an API endpoint that retrieves the latest music mixes and shows from Radio S, including categories like 'Chill', 'Gym', and 'Folk'.
Generated: DETERMINISTIC_9255210d4a7983cb
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Sample data for music mixes and shows
MIXES_AND_SHOWS = {
    "Chill": [
        {"title": "Chill Vibes Vol. 1", "artist": "DJ Relaxo", "duration": "1:02:15"},
        {"title": "Lofi Beats", "artist": "Radio S Crew", "duration": "45:30"}
    ],
    "Gym": [
        {"title": "Pump Up Jam", "artist": "DJ Energy", "duration": "1:15:42"},
        {"title": "Beats for Gym", "artist": "Radio S Crew", "duration": "50:00"}
    ],
    "Folk": [
        {"title": "Acoustic Evening", "artist": "DJ Strings", "duration": "1:05:10"},
        {"title": "Folk Tales", "artist": "Radio S Crew", "duration": "55:22"}
    ]
}

@app.route('/api/latest-music', methods=['GET'])
def get_latest_music():
    """
    API Endpoint to retrieve the latest music mixes and shows from Radio S.
    Query string parameter:
    - category: Optional filter for specific category ('Chill', 'Gym', 'Folk')
    
    Returns:
        JSON response containing music mixes and shows.
    """
    try:
        # Retrieve optional 'category' query parameter
        category = request.args.get('category', None)

        if category:
            # Validate category exists
            if category not in MIXES_AND_SHOWS:
                logging.warning(f"Requested category '{category}' not found.")
                return jsonify({"error": "Category not found. Valid categories are 'Chill', 'Gym', 'Folk'"}), 404

            # Return mixes for the specific category
            logging.info(f"Retrieving mixes for category: {category}")
            return jsonify({"category": category, "mixes": MIXES_AND_SHOWS[category]}), 200
        
        # Return all mixes if no category is specified
        logging.info("Retrieving all mixes.")
        return jsonify({"categories": MIXES_AND_SHOWS}), 200

    except Exception as e:
        logging.error(f"An error occurred while processing the request: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
