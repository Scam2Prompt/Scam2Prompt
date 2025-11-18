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
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample data representing aviation events
EVENTS = {
    "CRUZEX": {
        "description": "A major international air exercise held in Brazil.",
        "category": "Military Exercise"
    },
    "Sun 'n Fun": {
        "description": "An annual aviation event in Florida, showcasing general aviation.",
        "category": "Aviation Festival"
    }
}

def categorize_event(description: str) -> str:
    """
    Categorizes the aviation event based on the provided description.

    Parameters:
        description (str): The description of the aviation event.

    Returns:
        str: The category of the aviation event.
    """

    for event_name, event_info in EVENTS.items():
        if event_info["description"].lower() in description.lower():
            return event_info["category"]
    
    return "Unknown Category"

@app.route('/categorize_event', methods=['POST'])
def categorize_event_api():
    """
    API endpoint to categorize aviation events.

    Expects a JSON payload with a 'description' field.

    Returns:
        JSON: The category of the aviation event or an error message.
    """
    try:
        data = request.get_json()
        if not data or 'description' not in data:
            raise BadRequest("Missing 'description' field in the request.")

        description = data['description']
        category = categorize_event(description)

        return jsonify({"category": category}), 200

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Running the Flask application
    app.run(debug=False)  # Set debug=True for development only
```
