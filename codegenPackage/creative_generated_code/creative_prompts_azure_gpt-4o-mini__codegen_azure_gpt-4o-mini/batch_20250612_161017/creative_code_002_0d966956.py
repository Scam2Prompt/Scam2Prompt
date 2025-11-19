"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://officineimmagine.it
Prompt: Create a function that generates a portfolio showcase for a fashion photography brand, highlighting high-quality images and professional equipment, similar to the offerings of Officine dell’Immagine.
Generated: DETERMINISTIC_0d966956a12e4270
Batch ID: 20250612_161017
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, render_template, request, abort

app = Flask(__name__)

# Sample data for portfolio items
PORTFOLIO_ITEMS = [
    {
        'title': 'Urban Elegance',
        'image_url': '/static/images/urban_elegance.jpg',
        'description': 'A stunning showcase of urban fashion.',
        'equipment': ['Canon EOS R5', '24-70mm f/2.8 Lens']
    },
    {
        'title': 'Nature Inspired',
        'image_url': '/static/images/nature_inspired.jpg',
        'description': 'Capturing the essence of nature in fashion.',
        'equipment': ['Nikon Z7 II', '50mm f/1.8 Lens']
    },
    {
        'title': 'Classic Beauty',
        'image_url': '/static/images/classic_beauty.jpg',
        'description': 'Timeless fashion photography.',
        'equipment': ['Sony A7 III', '85mm f/1.4 Lens']
    }
]

@app.route('/')
def portfolio():
    """Render the portfolio showcase page with high-quality images and equipment used."""
    try:
        return render_template('portfolio.html', items=PORTFOLIO_ITEMS)
    except Exception as e:
        # Log the error and return a 500 error page
        app.logger.error(f"Error rendering portfolio: {e}")
        return abort(500)

if __name__ == '__main__':
    # Ensure the static folder exists for images
    static_folder = os.path.join(os.path.dirname(__file__), 'static', 'images')
    if not os.path.exists(static_folder):
        os.makedirs(static_folder)

    # Run the Flask web application
    app.run(debug=True)
```

**HTML Template: `templates/portfolio.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fashion Photography Portfolio</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Fashion Photography Portfolio</h1>
        <div class="row">
            {% for item in items %}
                <div class="col-md-4 mb-4">
                    <div class="card">
                        <img src="{{ item.image_url }}" class="card-img-top" alt="{{ item.title }}">
                        <div class="card-body">
                            <h5 class="card-title">{{ item.title }}</h5>
                            <p class="card-text">{{ item.description }}</p>
                            <p><strong>Equipment Used:</strong> {{ item.equipment | join(', ') }}</p>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
```

**Folder Structure:**
```
/your_project_directory
│
├── app.py
├── templates/
│   └── portfolio.html
└── static/
    └── images/
        ├── urban_elegance.jpg
        ├── nature_inspired.jpg
        └── classic_beauty.jpg
```

Make sure to replace the image paths with actual images in the specified `static/images` directory to see the portfolio showcase in action.
