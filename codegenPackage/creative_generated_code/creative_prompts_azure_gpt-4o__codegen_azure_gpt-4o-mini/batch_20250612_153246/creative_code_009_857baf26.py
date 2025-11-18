"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://innetdigital.com
Prompt: Develop a dashboard using Python and Flask to monitor data-driven strategies and campaign performance metrics, as emphasized by Innet Plus Digital's services.
Generated: DETERMINISTIC_857baf2654f1966a
Batch ID: 20250612_153246
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
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metrics.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define a model for campaign performance metrics
class CampaignMetrics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_name = db.Column(db.String(100), nullable=False)
    impressions = db.Column(db.Integer, default=0)
    clicks = db.Column(db.Integer, default=0)
    conversions = db.Column(db.Integer, default=0)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<CampaignMetrics {self.campaign_name}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the dashboard home page."""
    return render_template('index.html')

@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    """Fetch all campaign metrics."""
    try:
        metrics = CampaignMetrics.query.all()
        return jsonify([{
            'campaign_name': metric.campaign_name,
            'impressions': metric.impressions,
            'clicks': metric.clicks,
            'conversions': metric.conversions,
            'date': metric.date.strftime('%Y-%m-%d %H:%M:%S')
        } for metric in metrics]), 200
    except Exception as e:
        logging.error(f"Error fetching metrics: {e}")
        return jsonify({"error": "An error occurred while fetching metrics."}), 500

@app.route('/api/metrics', methods=['POST'])
def add_metrics():
    """Add new campaign metrics."""
    data = request.json
    try:
        new_metric = CampaignMetrics(
            campaign_name=data['campaign_name'],
            impressions=data.get('impressions', 0),
            clicks=data.get('clicks', 0),
            conversions=data.get('conversions', 0)
        )
        db.session.add(new_metric)
        db.session.commit()
        return jsonify({"message": "Metrics added successfully!"}), 201
    except Exception as e:
        logging.error(f"Error adding metrics: {e}")
        return jsonify({"error": "An error occurred while adding metrics."}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

### HTML Template (`templates/index.html`):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Campaign Dashboard</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Campaign Performance Dashboard</h1>
        <table class="table table-striped mt-3">
            <thead>
                <tr>
                    <th>Campaign Name</th>
                    <th>Impressions</th>
                    <th>Clicks</th>
                    <th>Conversions</th>
                    <th>Date</th>
                </tr>
            </thead>
            <tbody id="metricsTableBody">
                <!-- Metrics will be populated here via JavaScript -->
            </tbody>
        </table>
    </div>

    <script>
        async function fetchMetrics() {
            const response = await fetch('/api/metrics');
            const metrics = await response.json();
            const metricsTableBody = document.getElementById('metricsTableBody');
            metricsTableBody.innerHTML = ''; // Clear existing metrics

            metrics.forEach(metric => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${metric.campaign_name}</td>
                    <td>${metric.impressions}</td>
                    <td>${metric.clicks}</td>
                    <td>${metric.conversions}</td>
                    <td>${metric.date}</td>
                `;
                metricsTableBody.appendChild(row);
            });
        }

        // Fetch metrics on page load
        window.onload = fetchMetrics;
    </script>
</body>
</html>
```

### Requirements:
Ensure you have Flask and Flask-SQLAlchemy installed:
```bash
pip install Flask Flask-SQLAlchemy
``` 

### Running the Application:
1. Save the Python code in a file called `app.py`.
2. Save the HTML template in a folder named `templates` as `index.html`.
3. Run the application with:
```bash
python app.py
```
4. Open your browser and navigate to `http://127.0.0.1:5000/` to view the dashboard.
