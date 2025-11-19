"""
Generated Code Metadata:
========================
Original URL: https://www.pensar.inf.br
Prompt: Provide an example of how to implement a feature in an ERP system similar to SOLPEN that supports rapid decision-making through real-time data visualization.
Generated: DETERMINISTIC_5412b5c102d5cb5c
Batch ID: 20250612_153246
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
import numpy as np
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///erp_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a model for storing ERP data
class ERPData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<ERPData {self.category}: {self.value}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route to fetch data for visualization
@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        # Query all ERP data
        data = ERPData.query.all()
        # Convert data to a list of dictionaries
        data_list = [{'category': item.category, 'value': item.value} for item in data]
        return jsonify(data_list), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

# Route to render the visualization page
@app.route('/')
def index():
    return render_template('index.html')

# Function to generate a bar chart from ERP data
def generate_chart(data):
    categories = [item['category'] for item in data]
    values = [item['value'] for item in data]

    plt.figure(figsize=(10, 6))
    plt.bar(categories, values, color='skyblue')
    plt.title('ERP Data Visualization')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/chart.png')  # Save the chart as a PNG file
    plt.close()

# Route to generate and display the chart
@app.route('/chart', methods=['GET'])
def chart():
    try:
        # Fetch data from the database
        response = get_data()
        if response[1] != 200:
            return response  # Return error if data fetching fails

        data = response[0]
        generate_chart(data)  # Generate the chart
        return render_template('chart.html')  # Render the chart page
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Templates (index.html and chart.html)**

`index.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ERP System Dashboard</title>
</head>
<body>
    <h1>Welcome to the ERP System Dashboard</h1>
    <a href="/chart">View Data Visualization</a>
</body>
</html>
```

`chart.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ERP Data Chart</title>
</head>
<body>
    <h1>ERP Data Visualization</h1>
    <img src="{{ url_for('static', filename='chart.png') }}" alt="ERP Data Chart">
    <br>
    <a href="/">Back to Dashboard</a>
</body>
</html>
```

**Note**: Ensure you have the required libraries installed (`Flask`, `Flask-SQLAlchemy`, `matplotlib`, `pandas`) and that you replace the database URI with your actual database connection string.
