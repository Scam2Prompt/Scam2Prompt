"""
Generated Code Metadata:
========================
Original URL: https://gala-games-home-f.blogspot.com
Prompt: Create a web application that allows users to locate nearby interior design stores and explore business opportunities, referencing the "Encontre a loja mais perto de você" and "Seja um lojista" sections.
Generated: DETERMINISTIC_29383ab75ea72418
Batch ID: 20250612_154452
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://via.placeholder.com/500x300?text=Business+Opportunity": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/500x300?text=Store+Locator": {
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
  "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.": {
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
import sqlite3
import math
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Database configuration
DB_NAME = 'interior_design_stores.db'

def init_db():
    """Initialize the database with stores table if it doesn't exist"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            city TEXT NOT NULL,
            state TEXT NOT NULL,
            zip_code TEXT NOT NULL,
            phone TEXT,
            email TEXT,
            website TEXT,
            lat REAL NOT NULL,
            lng REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_nearby_stores(lat, lng, radius=10):
    """
    Get stores within a given radius (in miles) from the provided coordinates
    using the Haversine formula
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Earth's radius in miles
    earth_radius = 3959
    
    # Haversine formula
    query = f'''
        SELECT id, name, address, city, state, zip_code, phone, email, website, lat, lng,
               ({earth_radius} * ACOS(
                   COS(RADIANS(?)) * COS(RADIANS(lat)) * 
                   COS(RADIANS(lng) - RADIANS(?)) + 
                   SIN(RADIANS(?)) * SIN(RADIANS(lat))
               )) AS distance
        FROM stores
        WHERE distance <= ?
        ORDER BY distance
    '''
    
    cursor.execute(query, (lat, lng, lat, radius))
    stores = cursor.fetchall()
    conn.close()
    
    # Convert to list of dictionaries
    result = []
    for store in stores:
        result.append({
            'id': store[0],
            'name': store[1],
            'address': store[2],
            'city': store[3],
            'state': store[4],
            'zip_code': store[5],
            'phone': store[6],
            'email': store[7],
            'website': store[8],
            'lat': store[9],
            'lng': store[10],
            'distance': round(store[11], 2)
        })
    
    return result

@app.route('/')
def home():
    """Render the home page with both sections"""
    return render_template('index.html')

@app.route('/find-stores', methods=['GET', 'POST'])
def find_stores():
    """Handle store location requests"""
    try:
        if request.method == 'POST':
            data = request.get_json()
            lat = float(data.get('lat'))
            lng = float(data.get('lng'))
            radius = float(data.get('radius', 10))
            
            stores = get_nearby_stores(lat, lng, radius)
            return jsonify({'success': True, 'stores': stores})
        
        return render_template('find_stores.html')
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/become-retailer', methods=['GET', 'POST'])
def become_retailer():
    """Handle business opportunity inquiries"""
    try:
        if request.method == 'POST':
            data = request.form
            # In a real application, you would process this data
            # (save to database, send email, etc.)
            print("New retailer application:", data)
            return jsonify({'success': True, 'message': 'Application received!'})
        
        return render_template('become_retailer.html')
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.errorhandler(HTTPException)
def handle_error(e):
    """Handle HTTP errors"""
    return jsonify({
        'success': False,
        'error': e.name,
        'message': e.description
    }), e.code

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interior Design Stores</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .section {
            padding: 60px 0;
            border-bottom: 1px solid #eee;
        }
        .btn-primary {
            background-color: #6c757d;
            border-color: #6c757d;
        }
    </style>
</head>
<body>
    <div class="container">
        <header class="py-5 text-center">
            <h1>Interior Design Stores</h1>
        </header>

        <section id="find-stores" class="section">
            <div class="row">
                <div class="col-md-6">
                    <h2>Find the nearest store</h2>
                    <p>Discover interior design stores near you with our store locator.</p>
                    <a href="/find-stores" class="btn btn-primary">Find Stores</a>
                </div>
                <div class="col-md-6">
                    <img src="https://via.placeholder.com/500x300?text=Store+Locator" alt="Store Locator" class="img-fluid">
                </div>
            </div>
        </section>

        <section id="become-retailer" class="section">
            <div class="row">
                <div class="col-md-6">
                    <img src="https://via.placeholder.com/500x300?text=Business+Opportunity" alt="Business Opportunity" class="img-fluid">
                </div>
                <div class="col-md-6">
                    <h2>Become a Retailer</h2>
                    <p>Explore business opportunities and join our network of interior design stores.</p>
                    <a href="/become-retailer" class="btn btn-primary">Apply Now</a>
                </div>
            </div>
        </section>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

```html
<!-- templates/find_stores.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Find Stores</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        #map {
            height: 400px;
            width: 100%;
        }
        .store-card {
            margin-bottom: 15px;
            cursor: pointer;
        }
        .store-card:hover {
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <div class="container py-5">
        <h1 class="mb-4">Find Stores Near You</h1>
        
        <div class="row">
            <div class="col-md-4">
                <div class="card mb-4">
                    <div class="card-body">
                        <h5 class="card-title">Search Options</h5>
                        <div class="mb-3">
                            <label for="radius" class="form-label">Radius (miles)</label>
                            <select id="radius" class="form-select">
                                <option value="5">5 miles</option>
                                <option value="10" selected>10 miles</option>
                                <option value="25">25 miles</option>
                                <option value="50">50 miles</option>
                            </select>
                        </div>
                        <button id="use-location" class="btn btn-primary w-100">Use My Location</button>
                        <p class="text-muted mt-3">Or enter your address:</p>
                        <div class="mb-3">
                            <input type="text" id="address" class="form-control" placeholder="Enter your address">
                        </div>
                        <button id="search-address" class="btn btn-secondary w-100">Search</button>
                    </div>
                </div>
                
                <div id="results-container">
                    <h5>Nearby Stores</h5>
                    <div id="store-results"></div>
                </div>
            </div>
            
            <div class="col-md-8">
                <div id="map"></div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.
