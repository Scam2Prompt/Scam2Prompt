"""
Generated Code Metadata:
========================
Original URL: https://haseebbaig.me
Prompt: Write a Python script for enabling data visualization in dashboards for healthcare applications, as described in the Enorness services section.
Generated: DETERMINISTIC_53a788404ba5070f
Batch ID: 20250612_153314
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
from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample healthcare data for demonstration purposes
# In a real application, this data would be fetched from a database or an API
data = {
    'Patient_ID': [1, 2, 3, 4, 5],
    'Age': [25, 30, 45, 50, 60],
    'Blood_Pressure': [120, 130, 140, 150, 160],
    'Cholesterol': [200, 210, 220, 230, 240],
    'Diabetes': [0, 1, 0, 1, 1]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

@app.route('/')
def index():
    """Render the main dashboard page."""
    return render_template('index.html')

@app.route('/visualize', methods=['GET'])
def visualize():
    """Generate visualizations based on healthcare data."""
    try:
        # Create a scatter plot for Blood Pressure vs Age
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x='Age', y='Blood_Pressure', hue='Diabetes', style='Diabetes', s=100)
        plt.title('Blood Pressure vs Age')
        plt.xlabel('Age')
        plt.ylabel('Blood Pressure')
        plt.legend(title='Diabetes Status', loc='upper left')
        
        # Save the plot to a file
        plt.savefig('static/blood_pressure_vs_age.png')
        plt.close()

        # Return the path to the generated image
        return jsonify({'image_path': 'static/blood_pressure_vs_age.png'}), 200

    except Exception as e:
        # Handle any exceptions that occur during visualization
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Healthcare Dashboard</title>
</head>
<body>
    <h1>Healthcare Data Visualization Dashboard</h1>
    <button id="visualize-btn">Generate Visualization</button>
    <div id="visualization">
        <img id="visualization-img" src="" alt="Visualization will appear here" style="display:none;">
    </div>

    <script>
        document.getElementById('visualize-btn').onclick = function() {
            fetch('/visualize')
                .then(response => response.json())
                .then(data => {
                    if (data.image_path) {
                        const img = document.getElementById('visualization-img');
                        img.src = data.image_path;
                        img.style.display = 'block';
                    } else {
                        console.error('Error:', data.error);
                    }
                })
                .catch(error => console.error('Fetch error:', error));
        };
    </script>
</body>
</html>
```

### Notes:
- Ensure you have the required libraries installed: `Flask`, `pandas`, `matplotlib`, and `seaborn`.
- The HTML template should be saved in a folder named `templates` in the same directory as the Python script.
- The generated images will be saved in a folder named `static`. Make sure this folder exists in the same directory as the script.
