"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: Suggest a library or framework to create an interactive web interface for comparing fishing reel models, such as "Old School Brass 1 & 2" and "Trout 2," using the data from Emanuelson Reels.
Generated: DETERMINISTIC_cba68c9dde03830b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from flask import Flask, render_template, request
from flask_caching import Cache

# Create a Flask application instance
app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})

# Sample data for Emanuelson Reels (replace with actual data source)
reel_data = {
    "Old School Brass 1 & 2": {
        "Weight": 12.5,
        "Gear Ratio": 5.1,
        "Line Capacity": 200,
        "Price": 99.99
    },
    "Trout 2": {
        "Weight": 10.2,
        "Gear Ratio": 4.5,
        "Line Capacity": 150,
        "Price": 79.99
    }
}

# Convert reel data to a Pandas DataFrame for easier manipulation
df = pd.DataFrame([
    {"Model": "Old School Brass 1 & 2", "Weight": 12.5, "Gear Ratio": 5.1, "Line Capacity": 200, "Price": 99.99},
    {"Model": "Trout 2", "Weight": 10.2, "Gear Ratio": 4.5, "Line Capacity": 150, "Price": 79.99}
])

# Define a route for the index page
@app.route('/', methods=['GET'])
def index():
    try:
        # Render the index template with reel data
        return render_template('index.html', reels=df.to_dict(orient='records'))
    except Exception as e:
        # Handle any exceptions that occur during rendering
        return f"An error occurred: {str(e)}", 500

# Define a route for comparing reels
@app.route('/compare', methods=['POST'])
def compare_reels():
    try:
        # Get the selected reel models from the request
        selected_reels = request.form.getlist('reels')

        # Filter the DataFrame to only include selected reels
        selected_df = df[df['Model'].isin(selected_reels)]

        # Render the comparison template with selected reel data
        return render_template('compare.html', reels=selected_df.to_dict(orient='records'))
    except Exception as e:
        # Handle any exceptions that occur during comparison
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Fishing Reel Comparison</title>
</head>
<body>
    <h1>Fishing Reel Comparison</h1>
    <form action="/compare" method="post">
        {% for reel in reels %}
        <input type="checkbox" name="reels" value="{{ reel.Model }}">{{ reel.Model }}<br>
        {% endfor %}
        <input type="submit" value="Compare Reels">
    </form>
</body>
</html>
```

**templates/compare.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Fishing Reel Comparison</title>
</head>
<body>
    <h1>Fishing Reel Comparison</h1>
    <table border="1">
        <tr>
            <th>Model</th>
            <th>Weight</th>
            <th>Gear Ratio</th>
            <th>Line Capacity</th>
            <th>Price</th>
        </tr>
        {% for reel in reels %}
        <tr>
            <td>{{ reel.Model }}</td>
            <td>{{ reel.Weight }}</td>
            <td>{{ reel.Gear Ratio }}</td>
            <td>{{ reel.Line Capacity }}</td>
            <td>{{ reel.Price }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

**requirements.txt**
```
Flask
Flask-Caching
pandas
```
