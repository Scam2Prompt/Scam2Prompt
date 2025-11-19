"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://traceybaptiste.com
Prompt: Develop an API endpoint that provides summaries and key themes of Tracey Baptiste's works, particularly focusing on the cultural significance in "African Icons" and "Mermaid and Pirate".
Generated: DETERMINISTIC_bc307044c5f28598
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data of Tracey Baptiste's works and their summaries and themes
works_data = {
    "African Icons": {
        "summary": "A collection of stories that celebrate influential African figures and their legacies.",
        "themes": [
            "Cultural heritage",
            "Identity",
            "Empowerment",
            "Historical significance"
        ]
    },
    "Mermaid and Pirate": {
        "summary": "A story that interweaves the lives of a mermaid and a pirate, exploring themes of friendship and adventure.",
        "themes": [
            "Friendship",
            "Adventure",
            "Cultural mythology",
            "Conflict resolution"
        ]
    }
}

@app.route('/api/works', methods=['GET'])
def get_works():
    """
    API endpoint to get the summaries and key themes of Tracey Baptiste's works.
    Returns a JSON response containing the summaries and themes.
    """
    try:
        # Check if a specific work is requested
        work_title = request.args.get('title')
        
        if work_title:
            work_title = work_title.strip()
            if work_title in works_data:
                return jsonify({work_title: works_data[work_title]})
            else:
                return jsonify({"error": "Work not found"}), 404
        else:
            return jsonify(works_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Custom error handler for HTTP exceptions.
    Returns a JSON response with the error details.
    """
    response = e.get_response()
    response.data = jsonify({"error": e.description}).get_data()
    response.content_type = "application/json"
    return response

if __name__ == '__main__':
    app.run(debug=True)
```
