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
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sexual_aggression.db'
db = SQLAlchemy(app)

# Define the data model
class SexualAggression(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    organization = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    cases_reported = db.Column(db.Integer, nullable=False)
    impact_description = db.Column(db.Text, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Load data from Viajeras and Sisma Mujer organizations
def load_data():
    try:
        viajeras_data = pd.read_csv('viajeras_data.csv')
        sisma_mujer_data = pd.read_csv('sisma_mujer_data.csv')

        # Convert data to SQLAlchemy objects
        viajeras_data['date'] = pd.to_datetime(viajeras_data['date'])
        sisma_mujer_data['date'] = pd.to_datetime(sisma_mujer_data['date'])

        viajeras_data.to_sql('sexual_aggression', db.engine, if_exists='append', index=False)
        sisma_mujer_data.to_sql('sexual_aggression', db.engine, if_exists='append', index=False)

    except Exception as e:
        print(f"Error loading data: {e}")

# Create a route for the dashboard
@app.route('/')
def dashboard():
    try:
        # Query the database for data
        data = SexualAggression.query.all()

        # Create a Pandas dataframe from the data
        df = pd.DataFrame([d.__dict__ for d in data])

        # Calculate statistics
        total_cases = df['cases_reported'].sum()
        avg_cases_per_month = df['cases_reported'].mean()

        # Create visualizations
        plt.figure(figsize=(10,6))
        sns.lineplot(x='date', y='cases_reported', data=df)
        plt.title('Monthly Cases of Sexual Aggression')
        plt.xlabel('Date')
        plt.ylabel('Cases Reported')
        plt.savefig('static/line_plot.png')

        plt.figure(figsize=(10,6))
        sns.barplot(x='organization', y='cases_reported', data=df)
        plt.title('Cases of Sexual Aggression by Organization')
        plt.xlabel('Organization')
        plt.ylabel('Cases Reported')
        plt.savefig('static/bar_plot.png')

        # Render the dashboard template
        return render_template('dashboard.html', 
            total_cases=total_cases, 
            avg_cases_per_month=avg_cases_per_month)

    except Exception as e:
        print(f"Error rendering dashboard: {e}")
        return "Error rendering dashboard"

# Run the application
if __name__ == '__main__':
    load_data()
    app.run(debug=True)
```

```html
<!-- dashboard.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Sexual Aggression Dashboard</title>
</head>
<body>
    <h1>Sexual Aggression Dashboard</h1>
    <p>Total Cases: {{ total_cases }}</p>
    <p>Average Cases per Month: {{ avg_cases_per_month }}</p>
    <img src="{{ url_for('static', filename='line_plot.png') }}" alt="Line Plot">
    <img src="{{ url_for('static', filename='bar_plot.png') }}" alt="Bar Plot">
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
}

h1 {
    color: #00698f;
}

p {
    font-size: 18px;
}

img {
    width: 800px;
    height: 600px;
    margin: 20px;
}
```

```javascript
// Not used in this example, but could be used for interactive visualizations
// using a library like D3.js
```

```sql
-- schema.sql

CREATE TABLE sexual_aggression (
    id INTEGER PRIMARY KEY,
    organization TEXT NOT NULL,
    date DATETIME NOT NULL,
    cases_reported INTEGER NOT NULL,
    impact_description TEXT NOT NULL
);
```
