"""
Generated Code Metadata:
========================
Original URL: https://asphaltsc.cl
Prompt: Generate a code snippet for a web application that showcases the environmental benefits of using Asphalt Solutions Chile's products in asphalt maintenance.
Generated: DETERMINISTIC_107fb8629990900a
Batch ID: 20250612_155845
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})

# Define a function to calculate emissions reduction
def calculate_emissions_reduction(asphalt_used, emission_factor):
    """
    Calculate emissions reduction in kg CO2e.

    Args:
        asphalt_used (float): Amount of asphalt used in tons.
        emission_factor (float): Emission factor in kg CO2e/ton.

    Returns:
        float: Emissions reduction in kg CO2e.
    """
    return asphalt_used * emission_factor

# Define routes
@app.route('/')
def index():
    try:
        # Sample data
        asphalt_products = [
            {'name': 'Asphalt Emulsion', 'description': 'A cost-effective solution for asphalt maintenance.', 'emission_reduction': 10},
            {'name': 'Asphalt Sealcoat', 'description': 'A protective layer for asphalt surfaces.', 'emission_reduction': 15},
            {'name': 'Asphalt Overlay', 'description': 'A durable solution for asphalt rehabilitation.', 'emission_reduction': 20}
        ]

        # Render template with sample data
        return render_template('index.html', asphalt_products=asphalt_products)
    except Exception as e:
        # Handle exceptions
        return render_template('error.html', error=str(e)), 500

@app.route('/calculate-emissions-reduction', methods=['POST'])
def calculate_emissions_reduction_route():
    try:
        # Get form data
        asphalt_used = float(request.form['asphalt_used'])
        emission_factor = float(request.form['emission_factor'])

        # Calculate emissions reduction
        emissions_reduction = calculate_emissions_reduction(asphalt_used, emission_factor)

        # Return result as JSON
        return {'emissions_reduction': emissions_reduction}
    except Exception as e:
        # Handle exceptions
        return {'error': str(e)}, 400

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Asphalt Solutions Chile</title>
</head>
<body>
    <h1>Asphalt Solutions Chile</h1>
    <h2>Environmental Benefits</h2>
    <ul>
    {% for product in asphalt_products %}
        <li>
            {{ product.name }}: {{ product.description }} (Emissions reduction: {{ product.emission_reduction }} kg CO2e)
        </li>
    {% endfor %}
    </ul>

    <form id="emissions-reduction-form">
        <label for="asphalt_used">Asphalt used (tons):</label>
        <input type="number" id="asphalt_used" name="asphalt_used"><br><br>
        <label for="emission_factor">Emission factor (kg CO2e/ton):</label>
        <input type="number" id="emission_factor" name="emission_factor"><br><br>
        <button type="submit">Calculate Emissions Reduction</button>
    </form>

    <div id="result"></div>

    <script>
        const form = document.getElementById('emissions-reduction-form');
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(form);
            const response = await fetch('/calculate-emissions-reduction', {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
            if (response.ok) {
                document.getElementById('result').innerHTML = `Emissions reduction: ${result.emissions_reduction} kg CO2e`;
            } else {
                document.getElementById('result').innerHTML = `Error: ${result.error}`;
            }
        });
    </script>
</body>
</html>
```

```html
<!-- templates/error.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <p>{{ error }}</p>
</body>
</html>
```

```bash
# requirements.txt

Flask==2.0.2
Flask-Caching==1.1.1
```

To run the application:

```bash
# Create a new directory for the project
mkdir asphalt-solutions-chile

# Navigate to the project directory
cd asphalt-solutions-chile

# Create a new virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create a new directory for templates
mkdir templates

# Create template files
touch templates/index.html templates/error.html

# Create a new file for the application
touch app.py

# Copy the code into the respective files

# Run the application
python app.py
```
