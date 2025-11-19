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
import logging

app = Flask(__name__)

# Setup basic logging
logging.basicConfig(level=logging.INFO)

# Data source: Summaries and key themes of Tracey Baptiste's works
WORKS_SUMMARY = {
    "African Icons": {
        "summary": (
            "African Icons: Ten People Who Shaped History is a book that highlights "
            "the unsung heroes of African history. It explores cultural significance, "
            "innovation, and leadership while celebrating African heritage."
        ),
        "key_themes": [
            "Leadership in African history",
            "Cultural and historical legacy",
            "Empowerment through storytelling",
            "Pre-colonial African achievements",
        ],
    },
    "Mermaid and Pirate": {
        "summary": (
            "Mermaid and Pirate is a beautifully illustrated children's book that tells "
            "the story of an unlikely friendship between a mermaid and a pirate. It "
            "explores themes of trust, acceptance, and understanding, with a focus "
            "on imaginative storytelling and cultural nuances."
        ),
        "key_themes": [
            "Friendship and trust",
            "Acceptance of differences",
            "Imaginative storytelling",
            "Cultural significance in children's literature",
        ],
    },
}

@app.route('/api/tracey-baptiste/works', methods=['GET'])
def get_works():
    """
    API endpoint to retrieve summaries and key themes of Tracey Baptiste's works.
    
    Returns:
        JSON response containing summaries and key themes for each work.
    """
    logging.info("Fetching summaries and key themes for Tracey Baptiste's works.")
    return jsonify(WORKS_SUMMARY), 200

@app.route('/api/tracey-baptiste/work/<title>', methods=['GET'])
def get_work_details(title):
    """
    API endpoint to retrieve the summary and key themes of a specific work by title.
    
    Args:
        title (str): The title of the work.
    
    Returns:
        JSON response containing the summary and key themes of the requested work.
        Returns a 404 error if the work is not found.
    """
    logging.info(f"Fetching details for work titled: {title}")
    work = WORKS_SUMMARY.get(title)
    if work:
        return jsonify(work), 200
    else:
        logging.error(f"Work titled '{title}' not found.")
        return jsonify({"error": f"Work titled '{title}' not found."}), 404

@app.errorhandler(404)
def not_found(error):
    """
    Global error handler for 404 errors.
    
    Args:
        error: The error object.
    
    Returns:
        JSON response indicating the resource was not found.
    """
    logging.error("Resource not found: %s", error)
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_server_error(error):
    """
    Global error handler for 500 errors.
    
    Args:
        error: The error object.
    
    Returns:
        JSON response indicating an internal server error occurred.
    """
    logging.error("Internal server error: %s", error)
    return jsonify({"error": "An internal server error occurred"}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
