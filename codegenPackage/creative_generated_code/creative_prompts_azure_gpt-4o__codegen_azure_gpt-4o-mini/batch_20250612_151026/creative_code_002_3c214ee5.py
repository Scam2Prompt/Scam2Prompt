"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virtual5.com.mx
Prompt: Generate Python code for a dashboard that visualizes metrics such as the number of courses imparted, hours of consultancy, and executives trained, similar to the statistics provided by Virtual5.
Generated: DETERMINISTIC_3c214ee528f27f6f
Batch ID: 20250612_151026
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
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
from flask import Flask, render_template, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample data initialization (In a production environment, this would be retrieved from a database)
data = {
    'Metrics': ['Courses Imparted', 'Hours of Consultancy', 'Executives Trained'],
    'Values': [50, 200, 150]
}

# Convert sample data into a DataFrame
metrics_df = pd.DataFrame(data)

@app.route('/')
def index():
    """Render the main dashboard view."""
    return render_template('dashboard.html', metrics=metrics_df.to_dict(orient='records'))

@app.route('/api/metrics')
def get_metrics():
    """API endpoint to retrieve metrics data as JSON."""
    try:
        return jsonify(metrics_df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def plot_metrics(metrics_df):
    """Generate a bar plot for the metrics data."""
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Metrics', y='Values', data=metrics_df, palette='viridis')
    plt.title('Dashboard Metrics')
    plt.xlabel('Metrics')
    plt.ylabel('Values')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/metrics_plot.png')

if __name__ == '__main__':
    plot_metrics(metrics_df)
    app.run(debug=False, host='0.0.0.0', port=5000)
```

**HTML Template (dashboard.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="my-4">Metrics Dashboard</h1>
        <div class="row">
            <div class="col-md-12">
                <h2>Metrics Summary</h2>
                <table class="table">
                    <thead>
                        <tr>
                            <th>Metric</th>
                            <th>Value</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for metric in metrics %}
                        <tr>
                            <td>{{ metric.Metrics }}</td>
                            <td>{{ metric.Values }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
                <h2>Metrics Visualization</h2>
                <img src="{{ url_for('static', filename='metrics_plot.png') }}" alt="Metrics Plot" class="img-fluid">
            </div>
        </div>
    </div>
</body>
</html>
```

**Note**: Ensure you have Flask, Pandas, Matplotlib, and Seaborn installed in your Python environment. You can install these packages using pip:

```bash
pip install Flask pandas matplotlib seaborn
```
