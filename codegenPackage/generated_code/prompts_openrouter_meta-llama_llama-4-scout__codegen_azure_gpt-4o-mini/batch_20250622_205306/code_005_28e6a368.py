"""
Generated Code Metadata:
========================
Original URL: https://secondcitysummers.com
Prompt: Develop a chatbot that suggests comedy shows and classes at The Second City based on user input, such as location and interests.
Generated: DETERMINISTIC_28e6a368368e5171
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for comedy shows and classes at The Second City
comedy_data = {
    "Chicago": {
        "shows": [
            {"name": "The Best of Second City", "date": "2023-10-01", "time": "8:00 PM"},
            {"name": "Improvised Shakespeare", "date": "2023-10-02", "time": "7:00 PM"},
        ],
        "classes": [
            {"name": "Intro to Improv", "duration": "6 weeks", "level": "Beginner"},
            {"name": "Advanced Scene Study", "duration": "8 weeks", "level": "Advanced"},
        ],
    },
    "Toronto": {
        "shows": [
            {"name": "The Second City: Live", "date": "2023-10-05", "time": "9:00 PM"},
            {"name": "Comedy Lab", "date": "2023-10-06", "time": "8:00 PM"},
        ],
        "classes": [
            {"name": "Writing for Sketch Comedy", "duration": "4 weeks", "level": "Intermediate"},
            {"name": "Stand-Up Comedy Workshop", "duration": "5 weeks", "level": "Beginner"},
        ],
    },
}

@app.route('/suggest', methods=['POST'])
def suggest_comedy():
    """
    Suggest comedy shows and classes based on user input.
    Expects JSON input with 'location' and 'interests'.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        location = data.get('location')
        interests = data.get('interests', [])

        # Validate input
        if not location or location not in comedy_data:
            return jsonify({"error": "Invalid location provided."}), 400

        # Fetch shows and classes based on location
        shows = comedy_data[location]["shows"]
        classes = comedy_data[location]["classes"]

        # Filter suggestions based on interests
        suggested_shows = [show for show in shows if any(interest.lower() in show['name'].lower() for interest in interests)]
        suggested_classes = [cls for cls in classes if any(interest.lower() in cls['name'].lower() for interest in interests)]

        # If no specific interests match, suggest random options
        if not suggested_shows:
            suggested_shows = random.sample(shows, min(2, len(shows)))
        if not suggested_classes:
            suggested_classes = random.sample(classes, min(2, len(classes)))

        # Prepare the response
        response = {
            "suggested_shows": suggested_shows,
            "suggested_classes": suggested_classes,
        }

        return jsonify(response), 200

    except Exception as e:
        # Log the error (in production, use a logging framework)
        print(f"Error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
