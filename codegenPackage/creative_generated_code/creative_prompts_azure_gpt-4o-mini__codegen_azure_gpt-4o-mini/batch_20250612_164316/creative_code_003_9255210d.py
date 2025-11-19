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
from flask_cors import CORS
from werkzeug.exceptions import NotFound

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for all routes

# Sample data representing music mixes and shows
music_data = {
    'Chill': [
        {'title': 'Chill Vibes Mix', 'duration': '60min', 'date': '2023-10-01'},
        {'title': 'Evening Chill Sessions', 'duration': '45min', 'date': '2023-10-05'}
    ],
    'Gym': [
        {'title': 'High Energy Workout Mix', 'duration': '30min', 'date': '2023-09-28'},
        {'title': 'Pump Up Beats', 'duration': '50min', 'date': '2023-10-02'}
    ],
    'Folk': [
        {'title': 'Folk Tales', 'duration': '70min', 'date': '2023-09-30'},
        {'title': 'Acoustic Evening', 'duration': '55min', 'date': '2023-10-04'}
    ]
}

@app.route('/api/music-mixes', methods=['GET'])
def get_music_mixes():
    """
    API endpoint to retrieve the latest music mixes and shows from Radio S.
    
    Returns:
        JSON response containing the latest music mixes categorized by type.
    """
    category = request.args.get('category')  # Get category from query parameters

    if category and category in music_data:
        return jsonify({category: music_data[category]}), 200
    elif category:
        raise NotFound(f'Category "{category}" not found.')
    
    return jsonify(music_data), 200  # Return all mixes if no specific category is requested

@app.errorhandler(NotFound)
def handle_not_found(error):
    """
    Handle NotFound errors and return a JSON response with the error message.
    """
    return jsonify({'error': str(error)}), 404

if __name__ == '__main__':
    app.run(debug=False)  # Run the Flask app in production mode
```
