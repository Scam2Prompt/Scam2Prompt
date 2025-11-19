"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cem-ac.org
Prompt: Suggest a library for building a web interface that highlights the artistic contributions of Mexican cinema and stage arts, focusing on quality and cultural impact.
Generated: DETERMINISTIC_1fa34cb4868a443d
Batch ID: 20250612_161005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code using Flask for building a web interface
# Flask is a lightweight and flexible library for web development.

from flask import Flask, render_template, request, jsonify
import logging

# Initialize the Flask app
app = Flask(__name__)

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO)

# Sample data showcasing Mexican cinema and stage arts
data = [
    {"title": "Roma", "director": "Alfonso Cuarón", "type": "Cinema", "description": "Academy Award-winning film showcasing Mexican heritage."},
    {"title": "Amores Perros", "director": "Alejandro González Iñárritu", "type": "Cinema", "description": "Groundbreaking film exploring human connections."},
    {"title": "Like Water for Chocolate", "director": "Alfonso Arau", "type": "Cinema", "description": "A tale of love, food, and Mexican traditions."},
    {"title": "Zoot Suit", "director": "Luis Valdez", "type": "Stage", "description": "Iconic play exploring Chicano culture and identity."},
    {"title": "The Labyrinth of Solitude", "director": "Octavio Paz", "type": "Stage", "description": "Theatrical adaptation of Octavio Paz's exploration of Mexican identity."}
]

@app.route('/')
def home():
    """
    Renders the homepage with an introduction to the project.
    """
    return render_template('index.html', title="Mexican Cinema & Stage Arts", data=data)

@app.route('/search', methods=['GET'])
def search():
    """
    Endpoint for searching artistic contributions based on title or director.
    """
    try:
        query = request.args.get('query', '').lower()
        results = [item for item in data if query in item['title'].lower() or query in item['director'].lower()]
        return jsonify(results)
    except Exception as e:
        logging.error(f"Error handling search query: {e}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

@app.errorhandler(404)
def page_not_found(e):
    """
    Handles 404 errors gracefully.
    """
    return render_template('404.html', error="Page Not Found"), 404

@app.errorhandler(500)
def server_error(e):
    """
    Handles server errors gracefully.
    """
    return render_template('500.html', error="Internal Server Error"), 500

if __name__ == '__main__':
    # Run the Flask app
    # Ensure debugging is turned off in production
    app.run(debug=False)
```

**Directory Structure**:
- The above code assumes the presence of `templates/index.html`, `templates/404.html`, and `templates/500.html` for rendering web pages.
- Best practices dictate separating templates and static files (like CSS and JS) into their respective directories.
