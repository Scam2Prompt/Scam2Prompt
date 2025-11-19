"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wazfnynow.com
Prompt: Develop a web application that displays job opportunities from the وظفني الان site, allowing users to search by job title and location.
Generated: DETERMINISTIC_53038500ad694eea
Batch ID: 20250612_160507
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.wazafni.com/": {
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
# File: app.py
# Description: Flask web application to display job opportunities from "وظفني الان" website.
# Features: Allows users to search jobs by title and location.

from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Function to fetch job opportunities from the website
def fetch_jobs(job_title='', location=''):
    """
    Fetch job opportunities from 'وظفني الان' website based on job title and location.

    Args:
        job_title (str): Job title to search for.
        location (str): Location to filter jobs.

    Returns:
        list: List of dictionaries containing job details.
    """
    url = "https://www.wazafni.com/"  # Example URL for 'وظفني الان'
    response = requests.get(url)
    jobs = []

    if response.status_code == 200:
        try:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Assuming job postings are contained in <div> tags with class 'job-posting'
            job_posts = soup.find_all('div', class_='job-posting')

            for post in job_posts:
                title = post.find('h2', class_='job-title').text.strip()
                company = post.find('p', class_='company-name').text.strip()
                loc = post.find('p', class_='job-location').text.strip()
                link = post.find('a', class_='apply-link')['href']

                # Apply filters if job title or location is specified
                if job_title.lower() in title.lower() and location.lower() in loc.lower():
                    jobs.append({
                        'title': title,
                        'company': company,
                        'location': loc,
                        'link': link
                    })
        except Exception as e:
            print(f"Error while parsing job postings: {e}")
    else:
        print(f"Failed to fetch jobs. Status code: {response.status_code}")
    
    return jobs

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Home route to display job search interface and results.

    Returns:
        str: Rendered HTML page.
    """
    job_title = request.form.get('job_title', '')
    location = request.form.get('location', '')
    jobs = fetch_jobs(job_title, location)
    return render_template('index.html', jobs=jobs, job_title=job_title, location=location)

if __name__ == "__main__":
    app.run(debug=True)

# File: templates/index.html
# Description: HTML template for job search interface and displaying job results.
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Search</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Search Job Opportunities</h1>
        <form method="POST" class="my-4">
            <div class="mb-3">
                <label for="job_title" class="form-label">Job Title</label>
                <input type="text" id="job_title" name="job_title" class="form-control" value="{{ job_title }}">
            </div>
            <div class="mb-3">
                <label for="location" class="form-label">Location</label>
                <input type="text" id="location" name="location" class="form-control" value="{{ location }}">
            </div>
            <button type="submit" class="btn btn-primary">Search</button>
        </form>

        <h2 class="my-4">Job Results:</h2>
        <ul class="list-group">
            {% for job in jobs %}
                <li class="list-group-item">
                    <h3>{{ job.title }}</h3>
                    <p><strong>Company:</strong> {{ job.company }}</p>
                    <p><strong>Location:</strong> {{ job.location }}</p>
                    <a href="{{ job.link }}" class="btn btn-success" target="_blank">Apply</a>
                </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

# Notes:
# 1. Replace "https://www.wazafni.com/" with the actual URL of "وظفني الان".
# 2. Ensure the HTML structure matches the actual website for scraping.
# 3. Consider implementing additional error handling for production use.
```
