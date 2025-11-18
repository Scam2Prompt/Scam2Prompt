"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haseebbaig.me
Prompt: Write a Python script for enabling data visualization in dashboards for healthcare applications, as described in the Enorness services section.
Generated: DETERMINISTIC_53a788404ba5070f
Batch ID: 20250612_153314
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
from flask import Flask, jsonify, render_template
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the Flask application
app = Flask(__name__)

# Example data path - replace with the actual data source
DATA_PATH = 'healthcare_data.csv'

def load_data(file_path):
    """
    Load healthcare data from a CSV file.
    
    Parameters:
        file_path (str): The path to the CSV file.
        
    Returns:
        DataFrame: A pandas DataFrame containing the healthcare data.
    """
    try:
        data = pd.read_csv(file_path)
        logging.info("Data loaded successfully from %s", file_path)
        return data
    except FileNotFoundError:
        logging.error("File not found: %s", file_path)
        raise
    except pd.errors.EmptyDataError:
        logging.error("No data found in file: %s", file_path)
        raise
    except Exception as e:
        logging.error("Failed to load data: %s", str(e))
        raise

def create_visualization(data):
    """
    Create data visualizations for the healthcare data.
    
    Parameters:
        data (DataFrame): The healthcare data as a pandas DataFrame.
        
    Returns:
        None
    """
    try:
        plt.figure(figsize=(10, 6))
        sns.countplot(x='condition', data=data)  # Example visualization for conditions
        plt.title('Patient Count by Condition')
        plt.xlabel('Condition')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('visualization.png')  # Save the visualization as a PNG
        logging.info("Visualization created successfully.")
    except Exception as e:
        logging.error("Failed to create visualization: %s", str(e))
        raise

@app.route('/')
def index():
    """
    Render the main dashboard page.
    
    Returns:
        str: Rendered HTML template for the dashboard.
    """
    return render_template('dashboard.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    """
    API endpoint to get the healthcare data for visualization.
    
    Returns:
        JSON: A JSON representation of the healthcare data.
    """
    try:
        data = load_data(DATA_PATH)
        return jsonify(data.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Load data and create visualizations upon starting the application
    try:
        healthcare_data = load_data(DATA_PATH)
        create_visualization(healthcare_data)
    except Exception as e:
        logging.critical("Application failed to start: %s", str(e))
        exit(1)
    
    # Run the Flask application
    app.run(debug=True)
```

Make sure to have a `dashboard.html` file in the templates directory to render the dashboard correctly. The `healthcare_data.csv` file should be in the same directory or provide the correct path to the data file. Install the required packages using:

```bash
pip install pandas matplotlib seaborn flask
```
