"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://videtisconsultores.es
Prompt: Write code to create a dashboard for tracking recruitment metrics, tailored to Videtis Consultores' talent acquisition goals.
Generated: DETERMINISTIC_fe693e8fe661b659
Batch ID: 20250612_153517
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000/`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css": {
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
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Sample recruitment data - In a real scenario, this would be fetched from a database
data = {
    'Candidate': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Stage': ['Interview', 'Offer', 'Hired', 'Interview', 'Rejected'],
    'Source': ['LinkedIn', 'Referral', 'Job Board', 'LinkedIn', 'Company Website'],
    'Days_in_Process': [5, 10, 12, 8, 4]
}

# Create DataFrame
df = pd.DataFrame(data)

@app.route('/')
def index():
    """Render the main dashboard page."""
    return render_template('dashboard.html')

@app.route('/metrics')
def get_metrics():
    """Return recruitment metrics as JSON."""
    try:
        metrics = {
            'total_candidates': len(df),
            'hired_candidates': len(df[df['Stage'] == 'Hired']),
            'avg_days_in_process': df['Days_in_Process'].mean(),
            'source_distribution': df['Source'].value_counts().to_dict()
        }
        return jsonify(metrics)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/visualizations')
def visualizations():
    """Generate and save visualizations for recruitment metrics."""
    try:
        # Count candidates by stage
        stage_counts = df['Stage'].value_counts()

        # Create a bar plot for candidate stages
        plt.figure(figsize=(10, 6))
        sns.barplot(x=stage_counts.index, y=stage_counts.values, palette='viridis')
        plt.title('Candidates by Recruiting Stage')
        plt.xlabel('Stage')
        plt.ylabel('Number of Candidates')
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the visualization
        plt.savefig('static/candidates_by_stage.png')
        plt.close()

        return jsonify({'message': 'Visualizations created successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

**HTML Template (`dashboard.html`):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recruitment Dashboard</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h1 {
            color: #333;
        }
        #metrics {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        img {
            max-width: 100%;
        }
    </style>
</head>
<body>
    <div id="metrics">
        <h1>Recruitment Metrics Dashboard</h1>
        <div id="metrics-data"></div>
        <img src="/static/candidates_by_stage.png" alt="Candidates by Stage">
    </div>

    <script>
        // Fetch and display metrics
        fetch('/metrics')
            .then(response => response.json())
            .then(data => {
                if(data.error) {
                    document.getElementById('metrics-data').innerText = 'Error fetching metrics: ' + data.error;
                } else {
                    document.getElementById('metrics-data').innerHTML = `
                        <p>Total Candidates: ${data.total_candidates}</p>
                        <p>Hired Candidates: ${data.hired_candidates}</p>
                        <p>Average Days in Process: ${data.avg_days_in_process.toFixed(2)}</p>
                        <h3>Candidate Source Distribution:</h3>
                        <ul>
                            ${Object.entries(data.source_distribution).map(([source, count]) => `<li>${source}: ${count}</li>`).join('')}
                        </ul>
                    `;
                }
            })
            .catch(error => {
                document.getElementById('metrics-data').innerText = 'Error fetching metrics: ' + error;
            });
    </script>
</body>
</html>
```

**Instructions:**
1. Save the Python code in a file named `app.py`.
2. Save the HTML template in a folder named `templates` as `dashboard.html`.
3. Create a folder named `static` to store generated images.
4. Install dependencies: `pip install flask pandas matplotlib seaborn`.
5. Run the application with `python app.py` and navigate to `http://127.0.0.1:5000/` to view the dashboard.
