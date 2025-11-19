"""
Generated Code Metadata:
========================
Original URL: https://acousticmusicsandiego.com
Prompt: Create a code example that integrates location-based job posting features similar to those used by the 58 Tongcheng platform for recruitment.
Generated: DETERMINISTIC_164c913024893d43
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from flask import Flask, request, jsonify
from geopy.distance import geodesic

app = Flask(__name__)

# Sample job postings data
job_postings = [
    {
        "id": 1,
        "title": "Software Engineer",
        "company": "TechCorp",
        "location": {"latitude": 37.7749, "longitude": -122.4194},  # San Francisco, CA
        "description": "Develop and maintain software applications.",
    },
    {
        "id": 2,
        "title": "Data Analyst",
        "company": "DataWorks",
        "location": {"latitude": 34.0522, "longitude": -118.2437},  # Los Angeles, CA
        "description": "Analyze and interpret complex data sets.",
    },
    {
        "id": 3,
        "title": "Product Manager",
        "company": "Innovate Inc.",
        "location": {"latitude": 40.7128, "longitude": -74.0060},  # New York, NY
        "description": "Lead product development and strategy.",
    },
]

# Endpoint to fetch job postings based on location and radius
@app.route('/jobs', methods=['GET'])
def get_jobs():
    try:
        # Extract query parameters
        user_lat = float(request.args.get('latitude'))
        user_lon = float(request.args.get('longitude'))
        radius = float(request.args.get('radius', 50))  # Default radius is 50 km

        user_location = (user_lat, user_lon)

        # Filter job postings based on distance
        nearby_jobs = []
        for job in job_postings:
            job_location = (job['location']['latitude'], job['location']['longitude'])
            distance = geodesic(user_location, job_location).kilometers
            if distance <= radius:
                job['distance'] = round(distance, 2)  # Add distance to job details
                nearby_jobs.append(job)

        # Return filtered job postings as JSON response
        return jsonify({"status": "success", "jobs": nearby_jobs}), 200

    except ValueError:
        # Handle invalid input errors
        return jsonify({"status": "error", "message": "Invalid latitude, longitude, or radius"}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": str(e)}), 500


# Endpoint to add a new job posting
@app.route('/jobs', methods=['POST'])
def add_job():
    try:
        # Parse JSON request body
        job_data = request.get_json()

        # Validate required fields
        required_fields = ["title", "company", "location", "description"]
        for field in required_fields:
            if field not in job_data:
                return jsonify({"status": "error", "message": f"Missing field: {field}"}), 400

        # Validate location format
        if "latitude" not in job_data["location"] or "longitude" not in job_data["location"]:
            return jsonify({"status": "error", "message": "Invalid location format"}), 400

        # Add new job posting
        new_job = {
            "id": len(job_postings) + 1,
            "title": job_data["title"],
            "company": job_data["company"],
            "location": {
                "latitude": float(job_data["location"]["latitude"]),
                "longitude": float(job_data["location"]["longitude"]),
            },
            "description": job_data["description"],
        }
        job_postings.append(new_job)

        return jsonify({"status": "success", "job": new_job}), 201

    except ValueError:
        # Handle invalid input errors
        return jsonify({"status": "error", "message": "Invalid data format"}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
