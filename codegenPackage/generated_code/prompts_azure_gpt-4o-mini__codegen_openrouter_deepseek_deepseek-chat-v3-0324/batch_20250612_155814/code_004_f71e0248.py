"""
Generated Code Metadata:
========================
Original URL: https://beenzonsol.net
Prompt: Design a web application that allows users to compare different Las Vegas neighborhoods, using data and insights from AndySellsVegas.com to enhance user experience.
Generated: DETERMINISTIC_f71e024853a1a95f
Batch ID: 20250612_155814
URLs Found: 5
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
  },
  "https://www.andysellsvegas.com/neighborhoods/henderson": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.andysellsvegas.com/neighborhoods": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.andysellsvegas.com/neighborhoods/summerlin": {
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
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from functools import wraps
from werkzeug.exceptions import HTTPException

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['ANDY_SELLS_VEGAS_URL'] = 'https://www.andysellsvegas.com/neighborhoods'

# Cache for storing neighborhood data to reduce API calls
neighborhood_cache = {}

# Error handler for the application
@app.errorhandler(Exception)
def handle_exception(e):
    # Handle HTTP exceptions
    if isinstance(e, HTTPException):
        response = {
            "error": e.name,
            "message": e.description,
            "status_code": e.code
        }
        return jsonify(response), e.code
    
    # Handle non-HTTP exceptions
    response = {
        "error": "Internal Server Error",
        "message": "An unexpected error occurred",
        "status_code": 500
    }
    return jsonify(response), 500

# Decorator to check if data is cached
def cache_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        neighborhood = kwargs.get('neighborhood')
        if neighborhood in neighborhood_cache:
            return neighborhood_cache[neighborhood]
        result = func(*args, **kwargs)
        neighborhood_cache[neighborhood] = result
        return result
    return wrapper

# Function to fetch neighborhood data from AndySellsVegas.com
@cache_data
def get_neighborhood_data(neighborhood):
    try:
        # Construct URL for the specific neighborhood
        url = f"{app.config['ANDY_SELLS_VEGAS_URL']}/{neighborhood.lower().replace(' ', '-')}"
        
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract relevant data (this will vary based on the website's structure)
        # Example: Extracting the neighborhood description
        description = soup.find('div', class_='neighborhood-description').text.strip()
        
        # Example: Extracting key statistics
        stats = {}
        stat_elements = soup.find_all('div', class_='neighborhood-stat')
        for element in stat_elements:
            key = element.find('span', class_='stat-key').text.strip()
            value = element.find('span', class_='stat-value').text.strip()
            stats[key] = value
        
        # Return structured data
        return {
            'name': neighborhood,
            'description': description,
            'stats': stats,
            'source': url
        }
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch data for {neighborhood}: {str(e)}")

# Route to serve the main comparison page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to get neighborhood data
@app.route('/api/neighborhood/<string:neighborhood>', methods=['GET'])
def neighborhood_api(neighborhood):
    try:
        data = get_neighborhood_data(neighborhood=neighborhood)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to compare multiple neighborhoods
@app.route('/api/compare', methods=['POST'])
def compare_neighborhoods():
    try:
        data = request.get_json()
        neighborhoods = data.get('neighborhoods', [])
        
        if not neighborhoods:
            return jsonify({"error": "No neighborhoods provided"}), 400
        
        comparison_data = []
        for neighborhood in neighborhoods:
            neighborhood_data = get_neighborhood_data(neighborhood=neighborhood)
            comparison_data.append(neighborhood_data)
        
        return jsonify({"comparison": comparison_data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Sample data for testing (can be removed in production)
SAMPLE_DATA = {
    "Summerlin": {
        "name": "Summerlin",
        "description": "A premier master-planned community in Las Vegas...",
        "stats": {
            "Median Home Price": "$500,000",
            "Crime Rate": "Low",
            "Schools": "Highly Rated"
        },
        "source": "https://www.andysellsvegas.com/neighborhoods/summerlin"
    },
    "Henderson": {
        "name": "Henderson",
        "description": "A family-friendly city adjacent to Las Vegas...",
        "stats": {
            "Median Home Price": "$450,000",
            "Crime Rate": "Very Low",
            "Schools": "Excellent"
        },
        "source": "https://www.andysellsvegas.com/neighborhoods/henderson"
    }
}

# Populate cache with sample data for testing
neighborhood_cache.update(SAMPLE_DATA)

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
    <title>Las Vegas Neighborhood Comparison</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .neighborhood-card {
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .stat-item {
            padding: 10px;
            border-bottom: 1px solid #eee;
        }
        .comparison-table {
            width: 100%;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center mb-4">Las Vegas Neighborhood Comparison</h1>
        
        <div class="row">
            <div class="col-md-8 offset-md-2">
                <div class="card">
                    <div class="card-header">
                        <h3>Compare Neighborhoods</h3>
                    </div>
                    <div class="card-body">
                        <div class="mb-3">
                            <label for="neighborhoodInput" class="form-label">Enter Neighborhoods (comma separated)</label>
                            <input type="text" class="form-control" id="neighborhoodInput" placeholder="e.g. Summerlin, Henderson, Downtown">
                        </div>
                        <button id="compareBtn" class="btn btn-primary">Compare</button>
                    </div>
                </div>
                
                <div id="resultsContainer" class="mt-4"></div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        document.getElementById('compareBtn').addEventListener('click', function() {
            const input = document.getElementById('neighborhoodInput').value.trim();
            if (!input) {
                alert('Please enter at least one neighborhood');
                return;
            }
            
            const neighborhoods = input.split(',').map(n => n.trim()).filter(n => n);
            
            fetch('/api/compare', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ neighborhoods: neighborhoods }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert('Error: ' + data.error);
                    return;
                }
                
                displayResults(data.comparison);
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while comparing neighborhoods');
            });
        });
        
        function displayResults(neighborhoods) {
            const container = document.getElementById('resultsContainer');
            container.innerHTML = '';
            
            if (neighborhoods.length === 0) {
                container.innerHTML = '<div class="alert alert-warning">No data found for the specified neighborhoods</div>';
                return;
            }
            
            // Create comparison table
            const table = document.createElement('table');
            table.className = 'table comparison-table';
            
            // Create table header
            const thead = document.createElement('thead');
            const headerRow = document.createElement('tr');
            headerRow.innerHTML = '<th>Metric</th>' + 
                neighborhoods.map(n => `<th>${n.name}</th>`).join('');
            thead.appendChild(headerRow);
            table.appendChild(thead);
            
            // Create table body with stats
            const tbody = document.createElement('tbody');
            
            // Get all unique stat keys
            const allStats = new Set();
            neighborhoods.forEach(n => {
                Object.keys(n.stats || {}).forEach(key => allStats.add(key));
            });
            
            // Add rows for each stat
            Array.from(allStats).forEach(stat => {
                const row = document.createElement('tr');
