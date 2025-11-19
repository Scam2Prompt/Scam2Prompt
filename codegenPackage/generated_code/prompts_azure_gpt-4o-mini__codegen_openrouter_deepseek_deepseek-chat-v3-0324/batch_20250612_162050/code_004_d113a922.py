"""
Generated Code Metadata:
========================
Original URL: https://festivincaraquet.ca
Prompt: Design a web application feature that allows users to explore different wine flavors and aromas, akin to the experiences at FestiVin Caraquet.
Generated: DETERMINISTIC_d113a922caa65ee2
Batch ID: 20250612_162050
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///wine_explorer.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Wine model
class Wine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # red, white, rose, etc.
    region = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    flavors = db.Column(db.String(200), nullable=False)  # comma-separated list
    aromas = db.Column(db.String(200), nullable=False)  # comma-separated list
    image_url = db.Column(db.String(200))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'region': self.region,
            'description': self.description,
            'flavors': self.flavors.split(','),
            'aromas': self.aromas.split(','),
            'image_url': self.image_url
        }

# Create database tables
with app.app_context():
    db.create_all()

# Error handler
@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

# Routes
@app.route('/')
def index():
    """Render the main exploration page."""
    return render_template('index.html')

@app.route('/api/wines', methods=['GET'])
def get_wines():
    """Get all wines with optional filtering."""
    try:
        wine_type = request.args.get('type')
        region = request.args.get('region')
        query = Wine.query

        if wine_type:
            query = query.filter_by(type=wine_type.lower())
        if region:
            query = query.filter_by(region=region.lower())

        wines = [wine.to_dict() for wine in query.all()]
        return jsonify(wines)
    except Exception as e:
        return handle_error(e)

@app.route('/api/wines/<int:wine_id>', methods=['GET'])
def get_wine(wine_id):
    """Get details for a specific wine."""
    try:
        wine = Wine.query.get_or_404(wine_id)
        return jsonify(wine.to_dict())
    except Exception as e:
        return handle_error(e)

@app.route('/api/flavors', methods=['GET'])
def get_flavors():
    """Get all unique flavor profiles."""
    try:
        flavors = set()
        for wine in Wine.query.all():
            flavors.update(wine.flavors.split(','))
        return jsonify(sorted(flavors))
    except Exception as e:
        return handle_error(e)

@app.route('/api/aromas', methods=['GET'])
def get_aromas():
    """Get all unique aroma profiles."""
    try:
        aromas = set()
        for wine in Wine.query.all():
            aromas.update(wine.aromas.split(','))
        return jsonify(sorted(aromas))
    except Exception as e:
        return handle_error(e)

@app.route('/api/explore', methods=['GET'])
def explore():
    """Explore wines by flavor or aroma."""
    try:
        flavor = request.args.get('flavor')
        aroma = request.args.get('aroma')

        if not flavor and not aroma:
            return jsonify({'error': 'Must provide flavor or aroma parameter'}), 400

        query = Wine.query
        if flavor:
            query = query.filter(Wine.flavors.contains(flavor))
        if aroma:
            query = query.filter(Wine.aromas.contains(aroma))

        wines = [wine.to_dict() for wine in query.all()]
        return jsonify(wines)
    except Exception as e:
        return handle_error(e)

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
    <title>Wine Flavor & Aroma Explorer</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .wine-card {
            transition: transform 0.3s;
            margin-bottom: 20px;
        }
        .wine-card:hover {
            transform: scale(1.03);
        }
        .tag {
            display: inline-block;
            background-color: #f8f9fa;
            padding: 2px 8px;
            margin: 2px;
            border-radius: 10px;
            font-size: 0.8em;
        }
    </style>
</head>
<body>
    <div class="container py-5">
        <h1 class="text-center mb-5">Wine Flavor & Aroma Explorer</h1>
        
        <div class="row mb-4">
            <div class="col-md-6">
                <h3>Filter Wines</h3>
                <div class="mb-3">
                    <label for="wineType" class="form-label">Wine Type</label>
                    <select id="wineType" class="form-select">
                        <option value="">All Types</option>
                        <option value="red">Red</option>
                        <option value="white">White</option>
                        <option value="rose">Rosé</option>
                        <option value="sparkling">Sparkling</option>
                    </select>
                </div>
                <div class="mb-3">
                    <label for="wineRegion" class="form-label">Region</label>
                    <input type="text" id="wineRegion" class="form-control" placeholder="Enter region">
                </div>
                <button id="filterBtn" class="btn btn-primary">Filter</button>
            </div>
            
            <div class="col-md-6">
                <h3>Explore by Flavor/Aroma</h3>
                <div class="mb-3">
                    <label for="flavorInput" class="form-label">Flavor</label>
                    <input type="text" id="flavorInput" class="form-control" placeholder="e.g., berry, citrus">
                </div>
                <div class="mb-3">
                    <label for="aromaInput" class="form-label">Aroma</label>
                    <input type="text" id="aromaInput" class="form-control" placeholder="e.g., oak, floral">
                </div>
                <button id="exploreBtn" class="btn btn-primary">Explore</button>
            </div>
        </div>
        
        <div id="wineList" class="row">
            <!-- Wine cards will be dynamically inserted here -->
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Load all wines initially
            fetchWines();
            
            // Set up event listeners
            document.getElementById('filterBtn').addEventListener('click', fetchWines);
            document.getElementById('exploreBtn').addEventListener('click', exploreWines);
        });

        function fetchWines() {
            const type = document.getElementById('wineType').value;
            const region = document.getElementById('wineRegion').value;
            
            let url = '/api/wines';
            const params = new URLSearchParams();
            if (type) params.append('type', type);
            if (region) params.append('region', region);
            
            if (params.toString()) url += `?${params.toString()}`;
            
            fetch(url)
                .then(response => response.json())
                .then(displayWines)
                .catch(error => console.error('Error:', error));
        }

        function exploreWines() {
            const flavor = document.getElementById('flavorInput').value;
            const aroma = document.getElementById('aromaInput').value;
            
            if (!flavor && !aroma) {
                alert('Please enter at least one flavor or aroma');
                return;
            }
            
            let url = '/api/explore';
            const params = new URLSearchParams();
            if (flavor) params.append('flavor', flavor);
            if (aroma) params.append('aroma', aroma);
            
            url += `?${params.toString()}`;
            
            fetch(url)
                .then(response => response.json())
                .then(displayWines)
                .catch(error => console.error('Error:', error));
        }

        function displayWines(wines) {
            const wineList = document.getElementById('
