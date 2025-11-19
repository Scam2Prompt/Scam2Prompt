"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://officineimmagine.it
Prompt: Create a function that generates a portfolio showcase for a fashion photography brand, highlighting high-quality images and professional equipment, similar to the offerings of Officine dell’Immagine.
Generated: DETERMINISTIC_0d966956a12e4270
Batch ID: 20250612_161017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s the requested production-ready code in Python:

```python
import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Mock data for portfolio showcase
PORTFOLIO_DATA = [
    {
        "title": "Elegant Evening Wear",
        "image_url": "/static/images/evening_wear.jpg",
        "description": "Highlighting the sophistication of evening fashion with professional lighting techniques.",
        "equipment_used": ["Canon EOS R5", "Profoto B10 Plus", "Manfrotto Tripod"]
    },
    {
        "title": "Casual Street Style",
        "image_url": "/static/images/street_style.jpg",
        "description": "Capturing the vibrancy of urban casual clothing with natural light and portable flash.",
        "equipment_used": ["Sony A7 III", "Godox AD200 Pro", "Compact Reflector"]
    },
    {
        "title": "Luxury Accessories",
        "image_url": "/static/images/luxury_accessories.jpg",
        "description": "Showcasing intricate details of luxury handbags and jewelry through macro photography.",
        "equipment_used": ["Nikon Z7 II", "Tamron 90mm Macro Lens", "Continuous LED Light"]
    }
]

@app.route('/')
def portfolio_showcase():
    """
    Render the portfolio showcase page with high-quality images and equipment details.

    Returns:
        A rendered HTML template displaying the portfolio.
    """
    try:
        # Render the portfolio showcase using template
        return render_template('portfolio.html', portfolio_items=PORTFOLIO_DATA)
    except Exception as e:
        # Handle any unexpected errors gracefully
        return f"An error occurred while rendering the portfolio showcase: {str(e)}", 500

@app.route('/api/portfolio')
def portfolio_api():
    """
    Provide the portfolio data via a JSON API endpoint.

    Returns:
        JSON response containing portfolio items details.
    """
    try:
        return jsonify(PORTFOLIO_DATA), 200
    except Exception as e:
        # Handle errors during JSON serialization
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Ensure static folder is properly set for serving images
    if not os.path.exists('static/images'):
        os.makedirs('static/images')

    # Run the Flask application
    app.run(debug=True)
```

You will need to create an HTML template (`templates/portfolio.html`) and add images in the `static/images` directory for the code to work properly. This code follows best practices, includes error handling, and is well-commented/documented.
