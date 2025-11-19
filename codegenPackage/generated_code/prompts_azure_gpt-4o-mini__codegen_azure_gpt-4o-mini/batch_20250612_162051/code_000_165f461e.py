"""
Generated Code Metadata:
========================
Original URL: https://www.jobone.careers
Prompt: How can I implement a job search feature that allows users to find jobs within a specified radius, such as 5 km to 100 km, similar to the functionality on jobONE?
Generated: DETERMINISTIC_165f461ef97d0370
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from geopy.distance import geodesic
from typing import List, Dict

app = Flask(__name__)

# Sample job data (In a real application, this would come from a database)
jobs_data = [
    {"id": 1, "title": "Software Engineer", "location": (40.7128, -74.0060)},  # New York
    {"id": 2, "title": "Data Scientist", "location": (34.0522, -118.2437)},  # Los Angeles
    {"id": 3, "title": "Product Manager", "location": (41.8781, -87.6298)},  # Chicago
    {"id": 4, "title": "Web Developer", "location": (37.7749, -122.4194)},  # San Francisco
]

@app.route('/search_jobs', methods=['GET'])
def search_jobs():
    """
    Search for jobs within a specified radius from a given location.

    Query Parameters:
    - lat: Latitude of the user's location
    - lon: Longitude of the user's location
    - radius: Search radius in kilometers (5 to 100)

    Returns:
    - A JSON response containing the list of jobs within the specified radius.
    """
    try:
        # Get query parameters
        lat = float(request.args.get('lat'))
        lon = float(request.args.get('lon'))
        radius = float(request.args.get('radius'))

        # Validate radius
        if radius < 5 or radius > 100:
            return jsonify({"error": "Radius must be between 5 and 100 km."}), 400

        user_location = (lat, lon)
        matching_jobs = []

        # Find jobs within the specified radius
        for job in jobs_data:
            job_location = job['location']
            distance = geodesic(user_location, job_location).kilometers
            
            if distance <= radius:
                matching_jobs.append(job)

        return jsonify({"jobs": matching_jobs}), 200

    except ValueError:
        return jsonify({"error": "Invalid input. Please provide valid latitude, longitude, and radius."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
