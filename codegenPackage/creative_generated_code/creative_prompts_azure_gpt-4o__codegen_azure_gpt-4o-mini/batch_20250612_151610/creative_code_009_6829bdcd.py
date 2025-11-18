"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://secondcitysummers.com
Prompt: Provide a code example for creating a search interface that allows users to find classes or shows on The Second City website based on multiple filters, such as location, age, and time.
Generated: DETERMINISTIC_6829bdcdc3b5ab4b
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Mock data simulating The Second City classes database
CLASSES_DATA = [
    {"id": 1, "name": "Improv 101", "location": "Chicago", "age_group": "18+", "time": "Evening"},
    {"id": 2, "name": "Sketch Writing", "location": "Toronto", "age_group": "All Ages", "time": "Afternoon"},
    {"id": 3, "name": "Stand-up Comedy", "location": "Chicago", "age_group": "21+", "time": "Evening"},
    {"id": 4, "name": "Youth Improv", "location": "Chicago", "age_group": "Under 18", "time": "Morning"},
    # Add more classes as needed
]

@app.route('/', methods=['GET', 'POST'])
def search_classes():
    results = CLASSES_DATA  # Default to all classes
    if request.method == 'POST':
        # Get filter values from the form
        location = request.form.get('location')
        age_group = request.form.get('age_group')
        time = request.form.get('time')

        # Filter classes based on user input
        results = [cls for cls in CLASSES_DATA if
                   (location in cls['location'] if location else True) and
                   (age_group in cls['age_group'] if age_group else True) and
                   (time in cls['time'] if time else True)]

    return render_template('search.html', classes=results)

@app.errorhandler(500)
def internal_error(error):
    """Handles internal server errors."""
    return "Internal Server Error. Please try again later.", 500

@app.errorhandler(404)
def not_found(error):
    """Handles not found errors."""
    return "Page not found. Please check the URL.", 404

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/search.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Class Search</title>
</head>
<body>
    <h1>Search Classes</h1>
    <form method="POST">
        <label for="location">Location:</label>
        <input type="text" id="location" name="location">
        <br>
        <label for="age_group">Age Group:</label>
        <select id="age_group" name="age_group">
            <option value="">Any</option>
            <option value="Under 18">Under 18</option>
            <option value="18+">18+</option>
            <option value="21+">21+</option>
            <option value="All Ages">All Ages</option>
        </select>
        <br>
        <label for="time">Time:</label>
        <select id="time" name="time">
            <option value="">Any</option>
            <option value="Morning">Morning</option>
            <option value="Afternoon">Afternoon</option>
            <option value="Evening">Evening</option>
        </select>
        <br>
        <input type="submit" value="Search">
    </form>
    
    <h2>Search Results:</h2>
    <ul>
        {% for cls in classes %}
        <li>{{ cls.name }} - {{ cls.location }} - {{ cls.age_group }} - {{ cls.time }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```
