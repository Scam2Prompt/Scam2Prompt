"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wazfnynow.com
Prompt: Create a dashboard using Flask to display job postings from "وظفني الان," focusing on academic positions in Bahrain and Oman with salary filters.
Generated: DETERMINISTIC_ceb5dde29346ddc7
Batch ID: 20250612_151811
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.wazfnni.com/jobs": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Base URL for the job postings
BASE_URL = "https://www.wazfnni.com/jobs"  # Adjust this URL as necessary

@app.route('/')
def index():
    """
    Home route that renders the job postings dashboard.
    """
    return render_template('index.html')

@app.route('/jobs', methods=['GET', 'POST'])
def jobs():
    """
    Route to display job postings based on user's filters for academic positions 
    in Bahrain and Oman with salary filters.
    Handles both GET and POST requests.
    """
    if request.method == 'POST':
        # Get filters from the form
        location = request.form.get('location')
        min_salary = request.form.get('min_salary', type=int)
        max_salary = request.form.get('max_salary', type=int)

        # Fetch filtered job postings
        job_postings = fetch_job_postings(location, min_salary, max_salary)
        return render_template('jobs.html', job_postings=job_postings)

    return redirect(url_for('index'))

def fetch_job_postings(location, min_salary, max_salary):
    """
    Fetch job postings from 'وظفني الان' website filtered by location and salary.

    :param location: The location to filter job postings (Bahrain or Oman)
    :param min_salary: Minimum salary filter
    :param max_salary: Maximum salary filter
    :return: List of job postings
    """
    try:
        # Send a request to the job postings site
        response = requests.get(BASE_URL, params={'location': location})

        # Raise an error for bad responses
        response.raise_for_status()

        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract job postings
        postings = []
        for job in soup.find_all(class_='job-listing'):
            title = job.find(class_='job-title').get_text(strip=True)
            salary = int(job.find(class_='job-salary').get_text(strip=True).replace('BD', '').replace(',', ''))

            # Apply salary filters
            if (min_salary is None or salary >= min_salary) and (max_salary is None or salary <= max_salary):
                postings.append({
                    'title': title,
                    'salary': salary,
                    'location': location
                })

        return postings

    except requests.RequestException as e:
        print(f"Error fetching job postings: {e}")
        return []

if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Templates (index.html and jobs.html)**

Make sure to create the necessary HTML templates for the Flask application to work. Below are basic examples you can expand upon.

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Job Dashboard</title>
</head>
<body>
    <h1>Job Dashboard</h1>
    <form method="POST" action="{{ url_for('jobs') }}">
        <label for="location">Location:</label>
        <select name="location" id="location">
            <option value="Bahrain">Bahrain</option>
            <option value="Oman">Oman</option>
        </select>
        <label for="min_salary">Min Salary:</label>
        <input type="number" name="min_salary" id="min_salary">
        <label for="max_salary">Max Salary:</label>
        <input type="number" name="max_salary" id="max_salary">
        <button type="submit">Filter Jobs</button>
    </form>
</body>
</html>
```

**jobs.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Job Postings</title>
</head>
<body>
    <h1>Job Postings</h1>
    <ul>
        {% for job in job_postings %}
            <li>{{ job.title }} - Salary: BD {{ job.salary }} - Location: {{ job.location }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('index') }}">Back</a>
</body>
</html>
```

Make sure you have the necessary packages installed:
```bash
pip install flask requests beautifulsoup4
```

This code and the accompanying HTML templates provide a basic implementation of a job dashboard using Flask. You can extend and customize this application according to your needs.
