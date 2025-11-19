"""
Generated Code Metadata:
========================
Original URL: https://starshot90.com
Prompt: Create a program that visualizes web analytics data to improve online business performance, as discussed in the "Web Analytics: Understanding and Utilizing Data" section of the Star Shot 90 website.
Generated: DETERMINISTIC_d06e327b226cb4a1
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import json
import os
from flask import Flask, render_template, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Configuration
DATA_FILE = 'web_analytics_data.json'
PLOT_DIR = 'static/plots'
os.makedirs(PLOT_DIR, exist_ok=True)

# Load or initialize analytics data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {
        'visitors': [],
        'page_views': [],
        'conversion_rates': [],
        'bounce_rates': [],
        'traffic_sources': [],
        'timestamps': []
    }

# Save analytics data
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

# Generate visualizations
def generate_visualizations(data):
    # Convert to DataFrame for easier manipulation
    df = pd.DataFrame(data)
    df['timestamps'] = pd.to_datetime(df['timestamps'])
    
    # Set style
    sns.set_style('whitegrid')
    plt.figure(figsize=(12, 8))
    
    # Plot 1: Visitors Over Time
    plt.subplot(2, 2, 1)
    sns.lineplot(x='timestamps', y='visitors', data=df)
    plt.title('Visitors Over Time')
    plt.xlabel('Date')
    plt.ylabel('Visitors')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plot_path1 = os.path.join(PLOT_DIR, 'visitors_over_time.png')
    plt.savefig(plot_path1)
    plt.clf()
    
    # Plot 2: Conversion Rates
    plt.subplot(2, 2, 2)
    sns.barplot(x='timestamps', y='conversion_rates', data=df)
    plt.title('Conversion Rates')
    plt.xlabel('Date')
    plt.ylabel('Conversion Rate (%)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plot_path2 = os.path.join(PLOT_DIR, 'conversion_rates.png')
    plt.savefig(plot_path2)
    plt.clf()
    
    # Plot 3: Traffic Sources
    traffic_data = pd.DataFrame(data['traffic_sources'])
    plt.subplot(2, 2, 3)
    traffic_data.sum().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Traffic Sources Distribution')
    plt.ylabel('')
    plt.tight_layout()
    plot_path3 = os.path.join(PLOT_DIR, 'traffic_sources.png')
    plt.savefig(plot_path3)
    plt.clf()
    
    # Plot 4: Bounce Rate vs Conversion Rate
    plt.subplot(2, 2, 4)
    sns.scatterplot(x='bounce_rates', y='conversion_rates', data=df)
    plt.title('Bounce Rate vs Conversion Rate')
    plt.xlabel('Bounce Rate (%)')
    plt.ylabel('Conversion Rate (%)')
    plt.tight_layout()
    plot_path4 = os.path.join(PLOT_DIR, 'bounce_vs_conversion.png')
    plt.savefig(plot_path4)
    plt.clf()
    
    return {
        'visitors_over_time': plot_path1,
        'conversion_rates': plot_path2,
        'traffic_sources': plot_path3,
        'bounce_vs_conversion': plot_path4
    }

# Web routes
@app.route('/')
def dashboard():
    data = load_data()
    if data['timestamps']:  # Only generate plots if we have data
        plots = generate_visualizations(data)
    else:
        plots = None
    return render_template('dashboard.html', plots=plots)

@app.route('/add_data', methods=['POST'])
def add_data():
    try:
        data = load_data()
        new_data = request.json
        
        # Validate required fields
        required_fields = ['visitors', 'page_views', 'conversion_rates', 'bounce_rates', 'traffic_sources']
        if not all(field in new_data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Add timestamp
        new_data['timestamps'] = datetime.now().isoformat()
        
        # Append new data
        for field in required_fields:
            data[field].append(new_data[field])
        data['timestamps'].append(new_data['timestamps'])
        
        save_data(data)
        return jsonify({'status': 'success'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/data', methods=['GET'])
def get_data():
    data = load_data()
    return jsonify(data)

# HTML Template (dashboard.html should be in templates folder)
"""
<!DOCTYPE html>
<html>
<head>
    <title>Web Analytics Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .plots-container { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        .plot { border: 1px solid #ddd; padding: 10px; border-radius: 5px; }
        .plot img { width: 100%; height: auto; }
        h1 { color: #333; }
    </style>
</head>
<body>
    <h1>Web Analytics Dashboard</h1>
    {% if plots %}
    <div class="plots-container">
        <div class="plot">
            <h2>Visitors Over Time</h2>
            <img src="{{ url_for('static', filename='plots/visitors_over_time.png') }}" alt="Visitors Over Time">
        </div>
        <div class="plot">
            <h2>Conversion Rates</h2>
            <img src="{{ url_for('static', filename='plots/conversion_rates.png') }}" alt="Conversion Rates">
        </div>
        <div class="plot">
            <h2>Traffic Sources</h2>
            <img src="{{ url_for('static', filename='plots/traffic_sources.png') }}" alt="Traffic Sources">
        </div>
        <div class="plot">
            <h2>Bounce Rate vs Conversion Rate</h2>
            <img src="{{ url_for('static', filename='plots/bounce_vs_conversion.png') }}" alt="Bounce vs Conversion">
        </div>
    </div>
    {% else %}
    <p>No analytics data available. Please add data to generate visualizations.</p>
    {% endif %}
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
```
