"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://square-bear.co.uk
Prompt: Develop a simple web application that showcases a discography of a dance music producer, incorporating elements similar to those found on Square Bear's site.
Generated: DETERMINISTIC_2d0ec8dec1b22b09
Batch ID: 20250612_163218
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/js/bootstrap.bundle.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://127.0.0.1:5000/`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/css/bootstrap.min.css": {
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
# Import necessary libraries
from flask import Flask, render_template, jsonify

# Initialize Flask application
app = Flask(__name__)

# Sample data for the discography
discography = [
    {
        'title': 'Echoes of the Night',
        'release_year': 2021,
        'genre': 'Deep House',
        'tracks': [
            {'track_number': 1, 'name': 'Midnight Dreams'},
            {'track_number': 2, 'name': 'Rhythm of Life'},
            {'track_number': 3, 'name': 'Lost in Time'}
        ]
    },
    {
        'title': 'Waves of Sound',
        'release_year': 2020,
        'genre': 'Tech House',
        'tracks': [
            {'track_number': 1, 'name': 'Tidal Wave'},
            {'track_number': 2, 'name': 'Soundscapes'},
            {'track_number': 3, 'name': 'Deep Dive'}
        ]
    }
]

# Root route to render the homepage
@app.route('/')
def home():
    """Render the homepage to showcase the discography."""
    return render_template('index.html', discography=discography)

# API route to get the discography data
@app.route('/api/discography', methods=['GET'])
def get_discography():
    """API endpoint to retrieve the discography data as JSON."""
    try:
        return jsonify(discography), 200
    except Exception as e:
        # Log the error and return a 500 status code
        print(f"Error retrieving discography: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Discography - Dance Music Producer</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Discography</h1>
        <div class="row">
            {% for album in discography %}
                <div class="col-md-6">
                    <div class="card mb-4">
                        <div class="card-body">
                            <h5 class="card-title">{{ album.title }} ({{ album.release_year }})</h5>
                            <p class="card-text"><strong>Genre:</strong> {{ album.genre }}</p>
                            <h6>Tracks:</h6>
                            <ul>
                                {% for track in album.tracks %}
                                    <li>{{ track.track_number }}. {{ track.name }}</li>
                                {% endfor %}
                            </ul>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

### Instructions:
1. Make sure to install Flask using `pip install Flask`.
2. Save the Python code in a file named `app.py`.
3. Save the HTML code in a folder named `templates` as `index.html`.
4. Run the application using `python app.py` and visit `http://127.0.0.1:5000/` to see the discography.
