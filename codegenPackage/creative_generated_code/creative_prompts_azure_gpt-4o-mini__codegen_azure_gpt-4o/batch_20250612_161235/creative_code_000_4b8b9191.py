"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.swellnetwork.tv
Prompt: Generate a code snippet for a digital experience platform that integrates branding and storytelling elements as described by Swell Creative Management.
Generated: DETERMINISTIC_4b8b91911eb2d3eb
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation for a digital experience platform that integrates branding and storytelling elements. This solution uses Flask for the web application framework, allowing modularity and scalability.

```python
from flask import Flask, render_template, request, jsonify
import logging

# Initialize Flask app
app = Flask(__name__)

# Setup logging for error monitoring and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Branding information (static for simplicity; typically fetch from a database)
BRANDING_DATA = {
    "brand_color": "#3498db",
    "logo_url": "/static/logo.png",
    "tagline": "Empowering Stories, Transforming Brands",
    "footer_text": "© 2023 Swell Creative Management"
}

# Storytelling Content (static for simplicity; typically fetch from a CMS)
STORIES = [
    {
        "id": 1,
        "title": "The Journey of Innovation",
        "content": "Discover how embracing change drives growth and creativity.",
        "image_url": "/static/story1.jpg"
    },
    {
        "id": 2,
        "title": "Empathy in Branding",
        "content": "Learn how connecting deeply with your audience builds lasting relationships.",
        "image_url": "/static/story2.jpg"
    },
    {
        "id": 3,
        "title": "Visionary Leadership",
        "content": "Explore the traits that define leaders who shape the future.",
        "image_url": "/static/story3.jpg"
    }
]

@app.route("/")
def home():
    """
    Render the main page with branding and storytelling elements.
    """
    try:
        # Pass branding and storytelling data to the template
        return render_template("index.html", branding=BRANDING_DATA, stories=STORIES)
    except Exception as e:
        logging.error(f"Error rendering home page: {e}")
        return "An error occurred while loading the page.", 500

@app.route("/story/<int:story_id>")
def get_story(story_id):
    """
    Render a detailed view of the selected story.
    """
    try:
        # Find the story by ID
        story = next((s for s in STORIES if s["id"] == story_id), None)
        if not story:
            logging.warning(f"Story ID {story_id} not found.")
            return "Story not found.", 404
        return render_template("story.html", story=story, branding=BRANDING_DATA)
    except Exception as e:
        logging.error(f"Error rendering story page: {e}")
        return "An error occurred while loading the story.", 500

@app.route("/api/stories", methods=["GET"])
def api_stories():
    """
    API endpoint to fetch all stories for integration with other platforms.
    """
    try:
        return jsonify({"stories": STORIES}), 200
    except Exception as e:
        logging.error(f"Error fetching stories API: {e}")
        return jsonify({"error": "An error occurred fetching stories."}), 500

# Error handling routes
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors gracefully.
    """
    return render_template("404.html", branding=BRANDING_DATA), 404

@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors gracefully.
    """
    return render_template("500.html", branding=BRANDING_DATA), 500

# Run the Flask app
if __name__ == "__main__":
    # Enable debug mode only in development
    app.run(debug=True)
```

### Recommendations:
1. Ensure the templates (`index.html`, `story.html`, `404.html`, `500.html`) are created in a `templates` directory.
2. Place the static assets like logos and images in a `static` directory for proper linking.
3. Replace the hardcoded data with dynamic integrations (e.g., database, CMS) in production for scalability.
