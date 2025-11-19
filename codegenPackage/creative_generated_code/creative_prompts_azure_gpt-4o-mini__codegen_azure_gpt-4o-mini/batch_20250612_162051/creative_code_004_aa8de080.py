"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://searchhr.com.ar
Prompt: Develop a simple web application that allows users to optimize their job search process, incorporating elements from Search HR's personalized services.
Generated: DETERMINISTIC_aa8de0807d3aa3a4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
import re

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for sessions
db = SQLAlchemy(app)  # Initialize the database

# Define the Job model
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    company = db.Column(db.String(100), nullable=False)

# Create the database tables if they do not exist
with app.app_context():
    db.create_all()

# Route for the homepage
@app.route('/')
def home():
    """Render the homepage with a list of jobs."""
    jobs = Job.query.all()  # Retrieve all jobs from the database
    return render_template('index.html', jobs=jobs)

# Route to add a new job
@app.route('/add_job', methods=['GET', 'POST'])
def add_job():
    """Add a new job to the database."""
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        company = request.form['company']
        
        # Basic validation for inputs
        if not title or not description or not company:
            flash('All fields are required!', 'error')
            return redirect(url_for('add_job'))

        # Create a new job instance and add it to the database
        new_job = Job(title=title, description=description, company=company)
        db.session.add(new_job)
        db.session.commit()
        flash('Job added successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('add_job.html')

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Handle HTTP exceptions."""
    return render_template("error.html", error=e), e.code

# Main block to run the application
if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode for development
```

**HTML Templates:**

1. **index.html**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Job Search Optimization</title>
</head>
<body>
    <h1>Job Listings</h1>
    <ul>
        {% for job in jobs %}
            <li>
                <h2>{{ job.title }}</h2>
                <p>{{ job.description }}</p>
                <p><strong>Company:</strong> {{ job.company }}</p>
            </li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('add_job') }}">Add Job</a>
</body>
</html>
```

2. **add_job.html**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Add Job</title>
</head>
<body>
    <h1>Add a New Job</h1>
    <form method="POST">
        <label for="title">Job Title:</label>
        <input type="text" name="title" required><br>
        
        <label for="description">Job Description:</label>
        <textarea name="description" required></textarea><br>
        
        <label for="company">Company Name:</label>
        <input type="text" name="company" required><br>
        
        <input type="submit" value="Add Job">
    </form>
    <a href="{{ url_for('home') }}">Back to Job List</a>
</body>
</html>
```

3. **error.html**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Error</title>
</head>
<body>
    <h1>Error {{ error.code }}: {{ error.name }}</h1>
    <p>{{ error.description }}</p>
    <a href="{{ url_for('home') }}">Return to Homepage</a>
</body>
</html>
``` 

**Note:** Before running this application, ensure you have Flask and Flask-SQLAlchemy installed. You can do this via pip:
```bash
pip install Flask Flask-SQLAlchemy
```
