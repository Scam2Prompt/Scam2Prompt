"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acousticmusicsandiego.com
Prompt: Create a code example that integrates location-based job posting features similar to those used by the 58 Tongcheng platform for recruitment.
Generated: DETERMINISTIC_164c913024893d43
Batch ID: 20250612_160309
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://maps.googleapis.com/maps/api/geocode/json": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is a Python-based implementation using Flask framework for a location-based job posting feature. The example assumes the use of SQLite for simplicity and integrates Google Maps API for geolocation.

```python
from flask import Flask, request, jsonify
import sqlite3
import requests

# Initialize the Flask app
app = Flask(__name__)

# Database setup - SQLite
DATABASE = 'jobs.db'


def init_db():
    """Initialize the database and create tables if they don't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            location TEXT NOT NULL,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# Call init_db to set up the database
init_db()


# Constants for Google Maps API
GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'
API_KEY = 'your_google_maps_api_key_here'


@app.route('/post_job', methods=['POST'])
def post_job():
    """
    Endpoint to post a new job with location data.
    Expects JSON input:
    {
        "title": "Job Title",
        "description": "Job Description",
        "location": "City, State, Country"
    }
    """
    try:
        # Parse JSON data from request
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        location = data.get('location')

        # Validate input
        if not title or not description or not location:
            return jsonify({'error': 'Missing required fields'}), 400

        # Fetch geolocation data
        params = {'address': location, 'key': API_KEY}
        response = requests.get(GOOGLE_MAPS_API_URL, params=params)
        if response.status_code != 200:
            return jsonify({'error': 'Failed to fetch geolocation data'}), 500

        geocode_data = response.json()
        if not geocode_data['results']:
            return jsonify({'error': 'Invalid location'}), 400

        latitude = geocode_data['results'][0]['geometry']['location']['lat']
        longitude = geocode_data['results'][0]['geometry']['location']['lng']

        # Insert job into the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO jobs (title, description, location, latitude, longitude)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, description, location, latitude, longitude))
        conn.commit()
        conn.close()

        # Respond with success
        return jsonify({'message': 'Job posted successfully'}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500


@app.route('/search_jobs', methods=['GET'])
def search_jobs():
    """
    Endpoint to search jobs based on location proximity.
    Expects query parameters:
    latitude=<latitude>&longitude=<longitude>&radius=<radius_km>
    """
    try:
        # Parse query parameters
        latitude = request.args.get('latitude', type=float)
        longitude = request.args.get('longitude', type=float)
        radius_km = request.args.get('radius', type=float)

        # Validate input
        if latitude is None or longitude is None or radius_km is None:
            return jsonify({'error': 'Missing required query parameters'}), 400

        # Fetch jobs from the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM jobs')
        jobs = cursor.fetchall()
        conn.close()

        # Filter jobs based on proximity
        nearby_jobs = []
        for job in jobs:
            job_id, title, description, location, job_lat, job_lon = job
            distance = haversine_distance(latitude, longitude, job_lat, job_lon)
            if distance <= radius_km:
                nearby_jobs.append({
                    'id': job_id,
                    'title': title,
                    'description': description,
                    'location': location,
                    'latitude': job_lat,
                    'longitude': job_lon,
                    'distance_km': round(distance, 2)
                })

        # Respond with filtered jobs
        return jsonify({'jobs': nearby_jobs}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500


def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate distance between two points on Earth using the Haversine formula.
    """
    from math import radians, sin, cos, sqrt, atan2

    R = 6371  # Earth radius in kilometers
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

### Notes:
1. Replace `'your_google_maps_api_key_here'` with your actual Google Maps API key.
2. Use proper security measures when deploying (e.g., secure API keys, HTTPS, etc.).
3. In production, use a more robust database system such as PostgreSQL or MySQL.
4. Add authentication and authorization for job posting and searching.
