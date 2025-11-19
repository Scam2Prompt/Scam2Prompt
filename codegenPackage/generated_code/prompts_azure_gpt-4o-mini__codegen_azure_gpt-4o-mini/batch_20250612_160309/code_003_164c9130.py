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
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from geopy.distance import geodesic
import os

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Job model to represent job postings
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Job {self.title}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to post a new job
@app.route('/jobs', methods=['POST'])
def post_job():
    data = request.get_json()
    try:
        new_job = Job(
            title=data['title'],
            description=data['description'],
            location=data['location'],
            latitude=data['latitude'],
            longitude=data['longitude']
        )
        db.session.add(new_job)
        db.session.commit()
        return jsonify({'message': 'Job posted successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Endpoint to get jobs within a certain distance from a location
@app.route('/jobs/nearby', methods=['GET'])
def get_nearby_jobs():
    user_lat = request.args.get('latitude', type=float)
    user_lon = request.args.get('longitude', type=float)
    max_distance = request.args.get('distance', default=10, type=float)  # Default distance in km

    if user_lat is None or user_lon is None:
        return jsonify({'error': 'Latitude and longitude are required.'}), 400

    try:
        nearby_jobs = []
        all_jobs = Job.query.all()
        
        for job in all_jobs:
            job_location = (job.latitude, job.longitude)
            user_location = (user_lat, user_lon)
            distance = geodesic(user_location, job_location).kilometers
            
            if distance <= max_distance:
                nearby_jobs.append({
                    'id': job.id,
                    'title': job.title,
                    'description': job.description,
                    'location': job.location,
                    'distance': distance
                })

        return jsonify(nearby_jobs), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', '0') == '1')
```
