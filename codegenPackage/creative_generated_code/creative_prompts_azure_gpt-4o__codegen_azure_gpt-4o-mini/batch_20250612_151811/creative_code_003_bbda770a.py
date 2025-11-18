"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalgatetechnology.com.ng
Prompt: Develop a logistics dashboard for monitoring haulage performance metrics, referencing the sustainable financial performance goals mentioned on Kalgate Technology's website.
Generated: DETERMINISTIC_bbda770afc13cf07
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, jsonify
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Sample data for demonstration, replace with database or API calls
data = {
    'hauler': ['Hauler A', 'Hauler B', 'Hauler C'],
    'distance_km': [120, 80, 150],
    'cost_usd': [300, 200, 450],
    'emissions_kg': [50, 30, 70],
}

# Convert sample data to DataFrame
df = pd.DataFrame(data)

@app.route('/')
def index():
    """
    Render the main dashboard page.
    """
    return render_template('index.html', haulers=df['hauler'].tolist())

@app.route('/metrics', methods=['GET'])
def metrics():
    """
    Calculate haulage performance metrics and return as JSON.
    """
    try:
        # Calculate performance metrics
        df['cost_per_km'] = df['cost_usd'] / df['distance_km']
        df['emissions_per_km'] = df['emissions_kg'] / df['distance_km']

        # Compile results into a dictionary
        metrics_data = df[['hauler', 'cost_per_km', 'emissions_per_km']].to_dict(orient='records')
        return jsonify(metrics_data)
    
    except Exception as e:
        logging.error(f"Error calculating metrics: {e}")
        return jsonify({'error': 'Failed to calculate metrics'}), 500

@app.route('/plot')
def plot():
    """
    Generate a plot of cost and emissions per hauler.
    """
    try:
        # Create a bar plot for cost and emissions
        plt.figure(figsize=(10, 5))
        plt.bar(df['hauler'], df['cost_per_km'], color='blue', label='Cost per km (USD)')
        plt.bar(df['hauler'], df['emissions_per_km'], color='green', alpha=0.6, label='Emissions per km (kg)')
        plt.xlabel('Hauler')
        plt.ylabel('Metrics')
        plt.title('Haulage Performance Metrics')
        plt.legend()
        plt.tight_layout()
        
        # Save the plot to a file
        plt.savefig('static/metrics_plot.png')
        plt.close()
        
        return render_template('plot.html')
    
    except Exception as e:
        logging.error(f"Error generating plot: {e}")
        return jsonify({'error': 'Failed to generate plot'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Template Files

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Logistics Dashboard</title>
</head>
<body>
    <h1>Logistics Dashboard</h1>
    <h2>Available Haulers</h2>
    <ul>
        {% for hauler in haulers %}
            <li>{{ hauler }}</li>
        {% endfor %}
    </ul>
    <button onclick="fetchMetrics()">Load Metrics</button>
    <div id="metrics"></div>
    <img src="/static/metrics_plot.png" alt="Metrics Plot">
    
    <script>
        async function fetchMetrics() {
            const response = await fetch('/metrics');
            const data = await response.json();
            const metricsDiv = document.getElementById('metrics');
            metricsDiv.innerHTML = '<h3>Metrics</h3><pre>' + JSON.stringify(data, null, 2) + '</pre>';
        }
    </script>
</body>
</html>
```

**plot.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Metrics Plot</title>
</head>
<body>
    <h1>Haulage Performance Metrics Plot</h1>
    <img src="/static/metrics_plot.png" alt="Metrics Plot">
    <a href="/">Back to Dashboard</a>
</body>
</html>
```

### Note:
- Install required packages using `pip install Flask pandas matplotlib`.
- Ensure that Flask is set up properly to serve static files in a directory named `static` for the plot images.
- Replace sample data and HTML as needed for real-world integration.
