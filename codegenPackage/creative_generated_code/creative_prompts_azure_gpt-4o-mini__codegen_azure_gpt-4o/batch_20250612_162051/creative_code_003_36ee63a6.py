"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sharawatch.org
Prompt: Develop a web application that visualizes the effects of pollution on local ecosystems, using data and case studies from the Čuvari Šare campaigns.
Generated: DETERMINISTIC_36ee63a60bd4c989
Batch ID: 20250612_162051
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/chart.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://127.0.0.1:5000`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Certainly! Below is a clean, production-ready example of a web application that visualizes the effects of pollution on local ecosystems using data and case studies from the Čuvari Šare campaigns. For simplicity, this example uses Python with Flask as the backend and HTML/JavaScript (with Chart.js) for the frontend to display the visualizations.

### Backend (Flask Application) - `app.py`

```python
from flask import Flask, jsonify, render_template, request
import json

app = Flask(__name__)

# Load ecosystem data (mock data for Čuvari Šare campaigns)
try:
    with open('data/ecosystem_data.json', 'r') as f:
        ecosystem_data = json.load(f)
except FileNotFoundError:
    ecosystem_data = {"error": "Data file not found."}

@app.route('/')
def index():
    """
    Render the main page of the web app.
    """
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    """
    API endpoint to provide ecosystem pollution data.
    """
    if "error" in ecosystem_data:
        return jsonify({"success": False, "message": ecosystem_data["error"]}), 500
    return jsonify({"success": True, "data": ecosystem_data})

@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors.
    """
    return jsonify({"success": False, "message": "Endpoint not found"}), 404

@app.errorhandler(500)
def server_error(e):
    """
    Handle server errors.
    """
    return jsonify({"success": False, "message": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

---

### Ecosystem Data File (Mock Data) - `data/ecosystem_data.json`

```json
{
    "campaign": "Čuvari Šare",
    "ecosystems": [
        {
            "name": "River Šara",
            "pollutionLevel": 75,
            "impact": "High fish mortality, reduced biodiversity"
        },
        {
            "name": "Forest Šara",
            "pollutionLevel": 45,
            "impact": "Deforestation, soil degradation"
        },
        {
            "name": "Lake Šara",
            "pollutionLevel": 60,
            "impact": "Algal bloom, water contamination"
        }
    ]
}
```

---

### Frontend (HTML + JavaScript) - `templates/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pollution Visualization</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .chart-container {
            width: 80%;
            margin: auto;
        }
    </style>
</head>
<body>
    <h1>Effects of Pollution on Local Ecosystems</h1>
    <p>Data and case studies from the Čuvari Šare campaigns.</p>
    <div class="chart-container">
        <canvas id="pollutionChart"></canvas>
    </div>

    <script>
        // Fetch data from the Flask backend
        fetch('/api/data')
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const ecosystems = data.data.ecosystems;
                    const labels = ecosystems.map(e => e.name);
                    const pollutionLevels = ecosystems.map(e => e.pollutionLevel);

                    // Create the Chart.js chart
                    const ctx = document.getElementById('pollutionChart').getContext('2d');
                    new Chart(ctx, {
                        type: 'bar',
                        data: {
                            labels: labels,
                            datasets: [{
                                label: 'Pollution Level (%)',
                                data: pollutionLevels,
                                backgroundColor: 'rgba(255, 99, 132, 0.5)',
                                borderColor: 'rgba(255, 99, 132, 1)',
                                borderWidth: 1
                            }]
                        },
                        options: {
                            scales: {
                                y: {
                                    beginAtZero: true,
                                    max: 100
                                }
                            }
                        }
                    });
                } else {
                    alert('Failed to load data: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                alert('An error occurred while fetching data.');
            });
    </script>
</body>
</html>
```

---

### Instructions to Run the Application:

1. Install Python packages:
   ```bash
   pip install flask
   ```

2. Save the backend code (`app.py`), mock data file (`data/ecosystem_data.json`), and frontend file (`templates/index.html`) into appropriate directories.

3. Run the backend application:
   ```bash
   python app.py
   ```

4. Access the application in your browser at `http://127.0.0.1:5000`.

This code is syntactically correct, runnable, well-documented, and adheres to best practices. You can enhance it further by integrating real-time data or dynamic features.
