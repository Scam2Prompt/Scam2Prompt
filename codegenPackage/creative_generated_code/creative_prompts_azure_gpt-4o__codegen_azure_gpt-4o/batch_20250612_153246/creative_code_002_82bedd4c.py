"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spottersbrasil.com.br
Prompt: Develop an API that categorizes aviation events like CRUZEX and Sun 'n Fun, based on the descriptions provided by Spotters Brasil.
Generated: DETERMINISTIC_82bedd4cfc4e7fa3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample categories for aviation events
EVENT_CATEGORIES = {
    "Air Show": ["CRUZEX", "Sun 'n Fun", "Red Flag"],
    "Military Exercise": ["CRUZEX", "Red Flag"],
    "General Aviation Gathering": ["Sun 'n Fun", "EAA AirVenture"],
}

# Error message template
ERROR_MESSAGE = {
    "error": "Invalid input. Please provide a valid event description."
}


def categorize_event(description):
    """
    Categorize an aviation event based on its description.

    Args:
        description (str): Description of the event.

    Returns:
        list: Categories the event belongs to.
    """
    categories = []
    for category, events in EVENT_CATEGORIES.items():
        if any(event.lower() in description.lower() for event in events):
            categories.append(category)
    return categories


@app.route('/api/categorize', methods=['POST'])
def categorize():
    """
    API endpoint to categorize an aviation event based on its description.

    Expected JSON format:
    {
        "description": "Event description here"
    }

    Returns:
        JSON: Categories the event belongs to.
    """
    try:
        data = request.get_json()
        if not data or 'description' not in data:
            return jsonify(ERROR_MESSAGE), 400

        description = data['description']
        categories = categorize_event(description)
        
        if not categories:
            return jsonify({"message": "No matching categories found.", "categories": []}), 200

        return jsonify({"message": "Categories identified successfully.", "categories": categories}), 200

    except Exception as e:
        # Log exception (could be extended to use logging libraries)
        print(f"Error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500


if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
