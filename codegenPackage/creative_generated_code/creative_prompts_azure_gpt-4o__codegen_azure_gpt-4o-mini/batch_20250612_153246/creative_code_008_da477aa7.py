"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis-investment.gr
Prompt: Generate code for a dashboard that monitors and visualizes the environmental impact of integrated waste management systems, inspired by Metis Investment's mission.
Generated: DETERMINISTIC_da477aa791889bff
Batch ID: 20250612_153246
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
import seaborn as sns
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for environmental impact metrics
data = {
    'Year': [2020, 2021, 2022, 2023],
    'Recycling Rate (%)': [25, 30, 35, 40],
    'Landfill Diversion Rate (%)': [20, 25, 30, 35],
    'Carbon Footprint Reduction (metric tons)': [100, 150, 200, 250]
}

# Convert the above data into a DataFrame
df = pd.DataFrame(data)

@app.route('/')
def index():
    """Render the main dashboard page."""
    return render_template('index.html')

@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    """API endpoint to fetch environmental metrics."""
    try:
        return jsonify(df.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def create_visualizations():
    """Create and save visualizations for the environmental impact metrics."""
    plt.figure(figsize=(12, 6))

    # Recycling Rate
    plt.subplot(1, 3, 1)
    sns.barplot(x='Year', y='Recycling Rate (%)', data=df, palette='viridis')
    plt.title('Recycling Rate Over Years')
    plt.xlabel('Year')
    plt.ylabel('Recycling Rate (%)')

    # Landfill Diversion Rate
    plt.subplot(1, 3, 2)
    sns.barplot(x='Year', y='Landfill Diversion Rate (%)', data=df, palette='magma')
    plt.title('Landfill Diversion Rate Over Years')
    plt.xlabel('Year')
    plt.ylabel('Landfill Diversion Rate (%)')

    # Carbon Footprint Reduction
    plt.subplot(1, 3, 3)
    sns.lineplot(x='Year', y='Carbon Footprint Reduction (metric tons)', data=df, marker='o', color='blue')
    plt.title('Carbon Footprint Reduction Over Years')
    plt.xlabel('Year')
    plt.ylabel('Carbon Footprint Reduction (metric tons)')

    plt.tight_layout()
    plt.savefig('static/metrics_visualization.png')
    plt.close()

@app.route('/visualize')
def visualize():
    """Generate visualizations and render them on the dashboard."""
    create_visualizations()
    return render_template('visualization.html')

if __name__ == '__main__':
    create_visualizations()  # Generate visualizations before starting the server
    app.run(debug=True)
```

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Environmental Impact Dashboard</title>
</head>
<body>
    <h1>Integrated Waste Management Systems Dashboard</h1>
    <a href="/visualize">View Metrics Visualization</a>
</body>
</html>
```

**visualization.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Metrics Visualization</title>
</head>
<body>
    <h1>Environmental Metrics Visualization</h1>
    <img src="{{ url_for('static', filename='metrics_visualization.png') }}" alt="Metrics Visualization">
    <br>
    <a href="/">Back to Dashboard</a>
</body>
</html>
```

Make sure to have Flask, Pandas, Matplotlib, and Seaborn installed in your environment to run the application. You can install them using pip:

```bash
pip install Flask pandas matplotlib seaborn
``` 

Run the application with:

```bash
python your_script_name.py
``` 

Replace `your_script_name.py` with the name of the Python file containing the code.
