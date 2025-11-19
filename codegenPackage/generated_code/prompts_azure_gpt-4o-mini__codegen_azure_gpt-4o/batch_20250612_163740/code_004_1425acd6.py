"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Design a web application feature that allows users to learn about destination marketing and tourism services, referencing the topics covered in the International Tourism & Hospitality Management course at Hampton's.
Generated: DETERMINISTIC_1425acd6ab47e12f
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock data representing topics covered in the International Tourism & Hospitality Management course
COURSE_TOPICS = [
    {
        "id": 1,
        "title": "Destination Marketing Strategies",
        "description": "Learn how to effectively market destinations to attract tourists."
    },
    {
        "id": 2,
        "title": "Sustainable Tourism Practices",
        "description": "Explore methods to promote sustainability in tourism."
    },
    {
        "id": 3,
        "title": "Hospitality Management Essentials",
        "description": "Understand the core principles of managing hospitality services."
    },
    {
        "id": 4,
        "title": "Cultural Tourism Development",
        "description": "Discover how to develop tourism around cultural heritage."
    },
    {
        "id": 5,
        "title": "Digital Marketing in Tourism",
        "description": "Learn about leveraging digital platforms for tourism promotion."
    }
]

# Route to display the homepage
@app.route('/')
def home():
    """
    Render the homepage with a brief introduction to the feature.
    """
    return render_template('index.html', title="Tourism & Hospitality Management", topics=COURSE_TOPICS)

# Route to fetch details of a specific topic
@app.route('/topic/<int:topic_id>', methods=['GET'])
def get_topic_details(topic_id):
    """
    Fetch and return details of a specific topic based on its ID.
    """
    try:
        # Find the topic by ID
        topic = next((t for t in COURSE_TOPICS if t['id'] == topic_id), None)
        if topic:
            return jsonify({"success": True, "topic": topic}), 200
        else:
            return jsonify({"success": False, "message": "Topic not found"}), 404
    except Exception as e:
        logging.error(f"Error fetching topic details: {e}")
        return jsonify({"success": False, "message": "An error occurred"}), 500

# Route to search topics by keyword
@app.route('/search', methods=['GET'])
def search_topics():
    """
    Search for topics based on a keyword provided by the user.
    """
    try:
        keyword = request.args.get('keyword', '').lower()
        if not keyword:
            return jsonify({"success": False, "message": "Keyword is required"}), 400

        # Filter topics based on the keyword
        matching_topics = [t for t in COURSE_TOPICS if keyword in t['title'].lower() or keyword in t['description'].lower()]
        return jsonify({"success": True, "topics": matching_topics}), 200
    except Exception as e:
        logging.error(f"Error searching topics: {e}")
        return jsonify({"success": False, "message": "An error occurred"}), 500

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors gracefully.
    """
    return render_template('404.html', title="Page Not Found"), 404

# Error handling for 500 errors
@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors gracefully.
    """
    return render_template('500.html', title="Internal Server Error"), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This code assumes the presence of HTML templates (`index.html`, `404.html`, `500.html`) in a `templates` directory.
- The `index.html` template should display the list of topics and provide links to view details or search topics.
- The application uses Flask, a lightweight Python web framework, and follows best practices for error handling and logging.
