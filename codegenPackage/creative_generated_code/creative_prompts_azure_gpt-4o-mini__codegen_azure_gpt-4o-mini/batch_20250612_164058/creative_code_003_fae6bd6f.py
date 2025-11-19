"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://naimatabbasind.com
Prompt: Illustrate how to use the Naimat Abbas Industries API to retrieve information about their martial arts gear and display it on a web page.
Generated: DETERMINISTIC_fae6bd6f1a279959
Batch ID: 20250612_164058
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://code.jquery.com/jquery-3.5.1.slim.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.naimatabbasindustries.com/martial_arts_gear": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js": {
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
# Import required libraries
from flask import Flask, jsonify, render_template
import requests

# Initialize Flask application
app = Flask(__name__)

# Constants for the Naimat Abbas Industries API
API_URL = "https://api.naimatabbasindustries.com/martial_arts_gear"

def fetch_gears():
    """
    Fetches martial arts gear from the Naimat Abbas Industries API.

    Returns:
        list: A list of martial arts gear if the request is successful.
        None: If there is an error during the API call.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return JSON data from the response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

@app.route('/')
def index():
    """
    Renders the main page displaying martial arts gear.

    Returns:
        Rendered HTML page with gear information.
    """
    gears = fetch_gears()  # Fetch the gear data
    if gears is None:
        return render_template('error.html', message="Failed to load gear data."), 500

    return render_template('index.html', gears=gears)

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development
```

**HTML Template (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Martial Arts Gear</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Martial Arts Gear</h1>
        <div class="row">
            {% for gear in gears %}
                <div class="col-md-4">
                    <div class="card mb-4">
                        <img src="{{ gear.image_url }}" class="card-img-top" alt="{{ gear.name }}">
                        <div class="card-body">
                            <h5 class="card-title">{{ gear.name }}</h5>
                            <p class="card-text">{{ gear.description }}</p>
                            <p class="card-text"><strong>Price:</strong> ${{ gear.price }}</p>
                            <a href="{{ gear.purchase_link }}" class="btn btn-primary">Buy Now</a>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
```

**Error Template (error.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <div style="text-align:center; margin-top:50px;">
        <h1>An Error Occurred</h1>
        <p>{{ message }}</p>
        <a href="/" style="text-decoration: underline;">Back to Home</a>
    </div>
</body>
</html>
```

**Note**: Make sure to install Flask and Requests via pip if they are not already installed:

```bash
pip install Flask requests
```
