"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-home-f.blogspot.com
Prompt: Develop a feature for an interior design website that showcases evolving kitchen designs over time, as discussed in the "A Mudança da Cozinha com o Tempo" blog post.
Generated: DETERMINISTIC_2cf912664e59f592
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, render_template, jsonify
import os

# Initialize the Flask application
app = Flask(__name__)

# Mock data representing the evolution of kitchen designs
# Normally, this data would be fetched from a database or external API
kitchen_designs = [
    {
        "year": 1950,
        "design": "Vintage retro style kitchens with pastel colors and chrome finishes.",
        "image_url": "/static/images/kitchen_1950.jpg"
    },
    {
        "year": 1970,
        "design": "Bold, vibrant colors with geometric patterns and modular elements.",
        "image_url": "/static/images/kitchen_1970.jpg"
    },
    {
        "year": 1990,
        "design": "Neutral tones, minimalistic cabinetry, and open layouts.",
        "image_url": "/static/images/kitchen_1990.jpg"
    },
    {
        "year": 2020,
        "design": "Modern, smart kitchens with integrated technology and sustainable materials.",
        "image_url": "/static/images/kitchen_2020.jpg"
    }
]

# Route to render the main page showcasing kitchen designs
@app.route("/")
def home():
    """
    Render the homepage template with kitchen designs data.
    """
    return render_template("index.html", kitchen_designs=kitchen_designs)

# API route to fetch kitchen designs data in JSON format
@app.route("/api/kitchen-designs", methods=["GET"])
def get_kitchen_designs():
    """
    API endpoint to provide kitchen designs data in JSON format.
    """
    try:
        return jsonify({"status": "success", "data": kitchen_designs}), 200
    except Exception as error:
        # Handle potential errors and return error response
        return jsonify({"status": "error", "message": str(error)}), 500

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(error):
    """
    Custom error handler for 404 - Page Not Found.
    """
    return render_template("404.html"), 404

# Run the application
if __name__ == "__main__":
    # Ensure the app runs only when executed directly
    app.run(debug=True)
```

### Notes:
1. Ensure you have the following directory structure:
    ```
    /static/images/kitchen_1950.jpg
    /static/images/kitchen_1970.jpg
    /static/images/kitchen_1990.jpg
    /static/images/kitchen_2020.jpg
    /templates/index.html
    /templates/404.html
    ```
2. The `index.html` template should iterate over `kitchen_designs` to display the designs and their images.
3. The `404.html` template should provide a user-friendly message for invalid routes.
4. Use `Flask` for this application. Install Flask via `pip install flask` if not already installed.
