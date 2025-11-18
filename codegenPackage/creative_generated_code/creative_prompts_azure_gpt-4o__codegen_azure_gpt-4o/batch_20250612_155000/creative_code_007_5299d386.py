"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linktre.me
Prompt: Write a function to generate analytics for links, including tracking the number of clicks each link receives, as described on "Bio.links."
Generated: DETERMINISTIC_5299d386f9684857
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from collections import defaultdict

app = Flask(__name__)

# Dictionary to store link analytics
# Structure: {"link_url": {"clicks": int}}
link_analytics = defaultdict(lambda: {"clicks": 0})


@app.route('/track/<path:link_url>', methods=['POST'])
def track_link_click(link_url):
    """
    Endpoint to track a click for a given link.
    - Increments the click count for the specified link URL.
    """
    try:
        # Increment click count for the link
        link_analytics[link_url]["clicks"] += 1
        return jsonify({"message": "Click tracked successfully", "link_url": link_url}), 200
    except Exception as e:
        # Error handling
        return jsonify({"error": "Failed to track click", "details": str(e)}), 500


@app.route('/analytics', methods=['GET'])
def get_analytics():
    """
    Endpoint to retrieve analytics for all links.
    - Returns the number of clicks for each link.
    """
    try:
        return jsonify(link_analytics), 200
    except Exception as e:
        # Error handling
        return jsonify({"error": "Failed to retrieve analytics", "details": str(e)}), 500


@app.route('/analytics/<path:link_url>', methods=['GET'])
def get_link_analytics(link_url):
    """
    Endpoint to retrieve analytics for a specific link.
    - Returns the number of clicks for the specified link URL.
    """
    try:
        if link_url not in link_analytics:
            return jsonify({"error": "Link not found"}), 404
        return jsonify({link_url: link_analytics[link_url]}), 200
    except Exception as e:
        # Error handling
        return jsonify({"error": "Failed to retrieve analytics for the link", "details": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
