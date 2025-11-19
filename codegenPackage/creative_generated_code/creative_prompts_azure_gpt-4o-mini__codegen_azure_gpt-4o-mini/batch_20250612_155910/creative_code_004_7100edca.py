"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colegiohuitakafusa.com
Prompt: Design a web application feature that displays the schedule for "Clases en Línea" for the Colegio Huitaka Fusagasugá programs.
Generated: DETERMINISTIC_7100edca53a5b16f
Batch ID: 20250612_155910
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://127.0.0.1:5000/`": {
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
from flask import Flask, render_template, jsonify, request
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Set up basic logging
logging.basicConfig(level=logging.INFO)

# Sample schedule data
schedule_data = [
    {"course": "Matemáticas", "date": "2023-10-01", "time": "09:00 AM", "duration": "2 hours"},
    {"course": "Ciencias", "date": "2023-10-02", "time": "10:30 AM", "duration": "1.5 hours"},
    {"course": "Historia", "date": "2023-10-03", "time": "01:00 PM", "duration": "2 hours"},
    {"course": "Inglés", "date": "2023-10-04", "time": "03:00 PM", "duration": "1 hour"}
]

@app.route('/')
def index():
    """Render the main schedule page."""
    return render_template('index.html', schedule=schedule_data)

@app.route('/api/schedule', methods=['GET'])
def get_schedule():
    """API endpoint to retrieve the schedule."""
    try:
        return jsonify(schedule_data), 200
    except Exception as e:
        logging.error(f"Error retrieving schedule: {e}")
        return jsonify({"error": "Failed to retrieve schedule"}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Template: `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clases en Línea - Colegio Huitaka Fusagasugá</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1>Schedule for Clases en Línea</h1>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Course</th>
                    <th>Date</th>
                    <th>Time</th>
                    <th>Duration</th>
                </tr>
            </thead>
            <tbody>
                {% for class in schedule %}
                <tr>
                    <td>{{ class.course }}</td>
                    <td>{{ class.date }}</td>
                    <td>{{ class.time }}</td>
                    <td>{{ class.duration }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
```

### Requirements
Make sure to install Flask before running the application:
```bash
pip install Flask
```

### Running the Application
1. Save the Python code in a file named `app.py`.
2. Create a folder named `templates` in the same directory and save the HTML code as `index.html`.
3. Run the application using:
```bash
python app.py
```
4. Navigate to `http://127.0.0.1:5000/` in your web browser to view the schedule.
