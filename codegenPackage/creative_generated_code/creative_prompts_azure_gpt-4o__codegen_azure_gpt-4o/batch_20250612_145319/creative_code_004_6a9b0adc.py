"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gigzio.com
Prompt: Write code to display job categories (e.g., SEO Specialist, HR, DevOps) dynamically on a job board website, inspired by Gigzio's job browsing functionality.
Generated: DETERMINISTIC_6a9b0adc3005a85f
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Sample data simulating fetched categories from a database or API
job_categories = [
    {"id": 1, "name": "SEO Specialist"},
    {"id": 2, "name": "HR"},
    {"id": 3, "name": "DevOps"},
    {"id": 4, "name": "Software Engineer"},
    {"id": 5, "name": "Data Scientist"},
    {"id": 6, "name": "Project Manager"},
]

@app.route('/')
def home():
    """
    Renders the homepage with job categories dynamically loaded.
    """
    return render_template('index.html')

@app.route('/api/job-categories', methods=['GET'])
def get_job_categories():
    """
    API endpoint to return job categories in JSON format.
    """
    try:
        # Simulating response delay or business logic if required
        response = jsonify(job_categories)
        response.status_code = 200
        return response
    except Exception as e:
        # Return a 500 Internal Server Error in case of unexpected issues
        return jsonify({"error": "An error occurred while fetching job categories.", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

# Static HTML Template (index.html)
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Categories</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; padding: 0; }
        ul { list-style-type: none; padding: 0; }
        li { padding: 10px 0; border-bottom: 1px solid #ccc; }
    </style>
</head>
<body>
    <h1>Job Categories</h1>
    <ul id="job-categories"></ul>
    <script>
        // JavaScript to fetch and display job categories dynamically
        document.addEventListener('DOMContentLoaded', function () {
            const jobCategoriesList = document.getElementById('job-categories');

            // Fetch job categories from the API
            fetch('/api/job-categories')
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    data.forEach(category => {
                        const listItem = document.createElement('li');
                        listItem.textContent = category.name;
                        jobCategoriesList.appendChild(listItem);
                    });
                })
                .catch(error => {
                    console.error('Error fetching job categories:', error);
                    jobCategoriesList.innerHTML = '<li>Error loading job categories. Please try again later.</li>';
                });
        });
    </script>
</body>
</html>
"""
```
