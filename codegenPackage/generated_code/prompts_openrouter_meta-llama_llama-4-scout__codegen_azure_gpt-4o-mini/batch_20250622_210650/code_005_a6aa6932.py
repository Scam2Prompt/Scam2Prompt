"""
Generated Code Metadata:
========================
Original URL: https://viajeras.com.co
Prompt: Create a data visualization dashboard to display the statistics and impact of sexual aggression on women, using data from organizations like Viajeras and Sisma Mujer.
Generated: DETERMINISTIC_a6aa6932a1bbe9d2
Batch ID: 20250622_210650
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
from flask import Flask, render_template, request
import json
import os

# Initialize Flask application
app = Flask(__name__)

# Load data from CSV files
def load_data():
    try:
        # Assuming the data files are in the 'data' directory
        viajeras_data = pd.read_csv(os.path.join('data', 'viajeras_data.csv'))
        sisma_data = pd.read_csv(os.path.join('data', 'sisma_data.csv'))
        return viajeras_data, sisma_data
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None, None
    except pd.errors.EmptyDataError:
        print("Error: One of the data files is empty.")
        return None, None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None

# Create visualizations
def create_visualizations(viajeras_data, sisma_data):
    # Set the aesthetic style of the plots
    sns.set(style="whitegrid")

    # Create a figure for the dashboard
    plt.figure(figsize=(14, 7))

    # Plotting statistics from Viajeras
    plt.subplot(1, 2, 1)
    sns.countplot(data=viajeras_data, x='incident_type', palette='viridis')
    plt.title('Incident Types Reported by Viajeras')
    plt.xticks(rotation=45)
    plt.xlabel('Incident Type')
    plt.ylabel('Count')

    # Plotting statistics from Sisma Mujer
    plt.subplot(1, 2, 2)
    sns.barplot(data=sisma_data, x='year', y='cases_reported', palette='plasma')
    plt.title('Cases Reported by Sisma Mujer Over Years')
    plt.xlabel('Year')
    plt.ylabel('Number of Cases')

    # Save the visualizations to a file
    plt.tight_layout()
    plt.savefig('static/dashboard_visualization.png')
    plt.close()

# Route for the dashboard
@app.route('/')
def dashboard():
    viajeras_data, sisma_data = load_data()
    if viajeras_data is None or sisma_data is None:
        return "Error loading data. Please check the logs.", 500

    create_visualizations(viajeras_data, sisma_data)
    return render_template('dashboard.html')

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (dashboard.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Visualization Dashboard</title>
</head>
<body>
    <h1>Statistics and Impact of Sexual Aggression on Women</h1>
    <img src="{{ url_for('static', filename='dashboard_visualization.png') }}" alt="Dashboard Visualization">
</body>
</html>
```

**Note:** Ensure you have the required libraries installed (`Flask`, `pandas`, `matplotlib`, `seaborn`) and the data files (`viajeras_data.csv`, `sisma_data.csv`) in the `data` directory for the code to run successfully.
