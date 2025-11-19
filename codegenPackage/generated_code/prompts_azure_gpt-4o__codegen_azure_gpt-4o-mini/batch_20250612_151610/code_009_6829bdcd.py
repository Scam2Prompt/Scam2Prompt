"""
Generated Code Metadata:
========================
Original URL: https://secondcitysummers.com
Prompt: Provide a code example for creating a search interface that allows users to find classes or shows on The Second City website based on multiple filters, such as location, age, and time.
Generated: DETERMINISTIC_6829bdcdc3b5ab4b
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for classes/shows (In a real application, this would come from a database)
classes_data = [
    {"id": 1, "name": "Improv 101", "location": "Chicago", "age_group": "18+", "time": "Evening"},
    {"id": 2, "name": "Sketch Writing", "location": "Toronto", "age_group": "All Ages", "time": "Afternoon"},
    {"id": 3, "name": "Stand-Up Comedy", "location": "Chicago", "age_group": "21+", "time": "Night"},
    {"id": 4, "name": "Advanced Improv", "location": "Los Angeles", "age_group": "18+", "time": "Evening"},
    # Add more classes/shows as needed
]

@app.route('/')
def index():
    """Render the main search interface."""
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    """Search for classes/shows based on filters."""
    try:
        # Get filter parameters from the request
        location = request.args.get('location', '').strip()
        age_group = request.args.get('age_group', '').strip()
        time = request.args.get('time', '').strip()

        # Filter classes based on provided parameters
        filtered_classes = [
            cls for cls in classes_data
            if (location.lower() in cls['location'].lower() if location else True) and
               (age_group.lower() in cls['age_group'].lower() if age_group else True) and
               (time.lower() in cls['time'].lower() if time else True)
        ]

        # Return filtered results as JSON
        return jsonify(filtered_classes)

    except Exception as e:
        # Log the error and return a 500 response
        app.logger.error(f"Error occurred during search: {e}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search Classes/Shows</title>
    <script>
        async function searchClasses() {
            const location = document.getElementById('location').value;
            const ageGroup = document.getElementById('age_group').value;
            const time = document.getElementById('time').value;

            const response = await fetch(`/search?location=${location}&age_group=${ageGroup}&time=${time}`);
            const results = await response.json();

            const resultsContainer = document.getElementById('results');
            resultsContainer.innerHTML = '';

            if (results.error) {
                resultsContainer.innerHTML = `<p>${results.error}</p>`;
            } else {
                results.forEach(cls => {
                    const div = document.createElement('div');
                    div.textContent = `${cls.name} - ${cls.location} - ${cls.age_group} - ${cls.time}`;
                    resultsContainer.appendChild(div);
                });
            }
        }
    </script>
</head>
<body>
    <h1>Search for Classes/Shows</h1>
    <label for="location">Location:</label>
    <input type="text" id="location" placeholder="Enter location">
    
    <label for="age_group">Age Group:</label>
    <input type="text" id="age_group" placeholder="Enter age group">
    
    <label for="time">Time:</label>
    <input type="text" id="time" placeholder="Enter time">
    
    <button onclick="searchClasses()">Search</button>
    
    <h2>Results:</h2>
    <div id="results"></div>
</body>
</html>
```
