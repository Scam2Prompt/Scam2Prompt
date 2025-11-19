"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-topgs.com
Prompt: Write a code snippet for a web application that showcases open positions at Hanil Furniture Gallery, including filters for job type and department.
Generated: DETERMINISTIC_83ed06853f5d46a8
Batch ID: 20250612_163432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Job model representing the job listings
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    job_type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Job {self.title} ({self.department})>'

# Route for displaying job listings
@app.route('/jobs', methods=['GET'])
def job_listings():
    job_type_filter = request.args.get('job_type')
    department_filter = request.args.get('department')
    
    # Query the database for jobs with optional filters
    query = Job.query

    if job_type_filter:
        query = query.filter_by(job_type=job_type_filter)
    if department_filter:
        query = query.filter_by(department=department_filter)

    jobs = query.all()  # Fetch results

    return render_template('jobs.html', jobs=jobs)

# Error handling for database connection issues
@app.errorhandler(500)
def internal_error(error):
    return "500 error: Internal server error occurred", 500

# Main function to run the application
if __name__ == '__main__':
    # Create the database and tables if they do not exist
    with app.app_context():
        db.create_all()
    # Start the Flask web server
    app.run(debug=True)
```

```html
<!-- jobs.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Listings - Hanil Furniture Gallery</title>
</head>
<body>
    <h1>Open Positions at Hanil Furniture Gallery</h1>
    
    <form method="GET" action="/jobs">
        <label for="job_type">Job Type:</label>
        <select name="job_type" id="job_type">
            <option value="">All</option>
            <option value="Full-time">Full-time</option>
            <option value="Part-time">Part-time</option>
            <option value="Internship">Internship</option>
        </select>

        <label for="department">Department:</label>
        <select name="department" id="department">
            <option value="">All</option>
            <option value="Sales">Sales</option>
            <option value="Design">Design</option>
            <option value="Manufacturing">Manufacturing</option>
        </select>

        <button type="submit">Filter</button>
    </form>

    <ul>
        {% for job in jobs %}
            <li>{{ job.title }} - {{ job.department }} ({{ job.job_type }})</li>
        {% else %}
            <li>No job listings available.</li>
        {% endfor %}
    </ul>
</body>
</html>
``` 

Make sure to create an SQLite database named `jobs.db` and populate it with relevant job listings that match the `Job` model structure for the application to work.
