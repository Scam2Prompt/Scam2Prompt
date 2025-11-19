"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acousticmusicsandiego.com
Prompt: Create a code example that integrates location-based job posting features similar to those used by the 58 Tongcheng platform for recruitment.
Generated: DETERMINISTIC_164c913024893d43
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from geopy.distance import geodesic
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Job Posting
class JobPosting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<JobPosting {self.title}>"

# Schema for Job Posting validation
class JobPostingSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    location = fields.Str(required=True)
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/jobs', methods=['POST'])
def create_job():
    """Endpoint to create a new job posting."""
    schema = JobPostingSchema()
    try:
        job_data = schema.load(request.json)
        new_job = JobPosting(**job_data)
        db.session.add(new_job)
        db.session.commit()
        return jsonify({"message": "Job posted successfully!", "job_id": new_job.id}), 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/jobs', methods=['GET'])
def get_jobs_nearby():
    """Endpoint to get job postings near a given location."""
    try:
        user_lat = request.args.get('latitude', type=float)
        user_long = request.args.get('longitude', type=float)
        if user_lat is None or user_long is None:
            return jsonify({"error": "Missing latitude or longitude"}), 400
        
        # Fetch all job postings
        jobs = JobPosting.query.all()
        nearby_jobs = []

        # Calculate distance and filter nearby jobs (within 50 km)
        for job in jobs:
            job_location = (job.latitude, job.longitude)
            user_location = (user_lat, user_long)
            distance = geodesic(user_location, job_location).kilometers

            if distance <= 50:  # Within 50 km radius
                nearby_jobs.append({
                    "id": job.id,
                    "title": job.title,
                    "description": job.description,
                    "location": job.location,
                    "distance": distance
                })

        return jsonify(nearby_jobs), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
