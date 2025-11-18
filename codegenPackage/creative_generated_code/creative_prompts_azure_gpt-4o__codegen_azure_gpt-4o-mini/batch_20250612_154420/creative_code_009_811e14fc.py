"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stuff-artgobblers.com
Prompt: Create a dashboard to visualize campaign performance metrics, inspired by ACE Digital Marketing Agency’s focus on measurable results.
Generated: DETERMINISTIC_811e14fc1c89ed15
Batch ID: 20250612_154420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000`": {
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

# Initialize the Flask application
app = Flask(__name__)

# Sample data for campaign performance metrics
data = {
    'Campaign': ['Campaign A', 'Campaign B', 'Campaign C'],
    'Impressions': [15000, 30000, 20000],
    'Clicks': [1200, 2500, 1800],
    'Conversions': [100, 250, 150],
    'Spend': [1500, 3000, 2000]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

@app.route('/')
def index():
    """
    Render the dashboard for campaign performance metrics.
    """
    return render_template('dashboard.html', data=df.to_dict(orient='records'))

@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    """
    API endpoint to fetch campaign performance metrics in JSON format.
    """
    try:
        metrics = df.to_dict(orient='records')
        return jsonify(metrics), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def plot_metrics(df):
    """
    Generate and save visualizations for campaign performance metrics.
    """
    try:
        plt.figure(figsize=(12, 6))
        
        # Plotting Impressions vs Clicks
        sns.barplot(x='Campaign', y='Impressions', data=df, color='blue', label='Impressions')
        sns.barplot(x='Campaign', y='Clicks', data=df, color='orange', label='Clicks', alpha=0.7)
        
        plt.title('Campaign Performance Metrics')
        plt.ylabel('Count')
        plt.xlabel('Campaign')
        plt.legend()
        plt.tight_layout()
        plt.savefig('static/campaign_performance.png')
        plt.close()
    except Exception as e:
        print(f"Error generating plots: {e}")

# Call the plot_metrics function to create visual representations
plot_metrics(df)

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```

```html
<!-- dashboard.html -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Campaign Performance Dashboard</title>
</head>
<body>
    <h1>Campaign Performance Dashboard</h1>
    <img src="{{ url_for('static', filename='campaign_performance.png') }}" alt="Campaign Performance Metrics">
    <table border="1">
        <thead>
            <tr>
                <th>Campaign</th>
                <th>Impressions</th>
                <th>Clicks</th>
                <th>Conversions</th>
                <th>Spend</th>
            </tr>
        </thead>
        <tbody>
            {% for row in data %}
            <tr>
                <td>{{ row.Campaign }}</td>
                <td>{{ row.Impressions }}</td>
                <td>{{ row.Clicks }}</td>
                <td>{{ row.Conversions }}</td>
                <td>{{ row.Spend }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```

Make sure to install the required libraries before running the application:
```bash
pip install Flask pandas matplotlib seaborn
```

Run the Python script and navigate to `http://127.0.0.1:5000` to view the dashboard.
