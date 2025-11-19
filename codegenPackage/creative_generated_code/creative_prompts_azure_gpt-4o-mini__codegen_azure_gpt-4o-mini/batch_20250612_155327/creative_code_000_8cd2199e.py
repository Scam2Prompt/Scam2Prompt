"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shahkarco.com
Prompt: Generate a code snippet for an e-commerce website that displays a list of coat racks with pricing and special offers, similar to those found on Shahkar Industry's product page.
Generated: DETERMINISTIC_8cd2199e94bb7f14
Batch ID: 20250612_155327
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
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data for coat racks
coat_racks = [
    {
        "id": 1,
        "name": "Modern Wooden Coat Rack",
        "price": 79.99,
        "special_offer": "10% off for first-time buyers!"
    },
    {
        "id": 2,
        "name": "Industrial Iron Coat Rack",
        "price": 129.99,
        "special_offer": "Free shipping on orders over $100"
    },
    {
        "id": 3,
        "name": "Vintage Style Coat Rack",
        "price": 89.99,
        "special_offer": "Buy 2, get 1 free!"
    }
]

@app.route('/')
def home():
    """Render the home page displaying coat racks."""
    return render_template('index.html', coat_racks=coat_racks)

@app.route('/api/coat_racks', methods=['GET'])
def get_coat_racks():
    """API endpoint to get the list of coat racks."""
    try:
        return jsonify(coat_racks), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error starting the server: {e}")
```

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coat Racks</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Coat Racks</h1>
        <div class="row">
            {% for rack in coat_racks %}
                <div class="col-md-4 mb-4">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">{{ rack.name }}</h5>
                            <p class="card-text">Price: ${{ rack.price }}</p>
                            <p class="card-text text-success">{{ rack.special_offer }}</p>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
```

### Requirements
- Ensure Flask is installed (`pip install Flask`) to run this application.
- Place `index.html` in a `templates` folder in the same directory as the Python script.
- Adjust the configurations according to your production environment before deployment.
