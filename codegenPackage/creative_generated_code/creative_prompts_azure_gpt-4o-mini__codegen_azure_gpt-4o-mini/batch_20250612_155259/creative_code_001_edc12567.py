"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://energiadosertao.blogspot.com
Prompt: Generate a code snippet for a web application that allows users to input their energy usage and see the benefits of switching to solar energy.
Generated: DETERMINISTIC_edc125679c504d3b
Batch ID: 20250612_155259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

# Default values for energy usage and solar benefits
DEFAULT_ENERGY_USAGE = 1000  # kWh
SOLAR_COST_PER_WATT = 3.0  # Cost in $ per watt of solar energy
SOLAR_OUTPUT_PER_WATT = 1.5  # kWh produced per watt per year

def calculate_solar_benefits(usage):
    """
    Calculate the potential benefits of switching to solar energy based on user input.

    :param usage: Monthly energy usage in kWh
    :return: A dictionary containing cost savings and environmental benefits
    """
    # Calculate the watts required to meet the energy usage
    watts_needed = usage * 12 / SOLAR_OUTPUT_PER_WATT
    total_cost = watts_needed * SOLAR_COST_PER_WATT
    environmental_impact = watts_needed * 0.0005  # Example value for CO2 reduction in tons

    return {
        "total_cost": round(total_cost, 2),
        "environmental_impact": round(environmental_impact, 2)
    }

@app.route('/')
def index():
    """Render the main page of the web application."""
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Endpoint to calculate the benefits of solar energy based on user input.

    :return: JSON response containing total cost and environmental impact
    """
    try:
        # Get energy usage from the form input
        energy_usage = float(request.form.get('energy_usage', DEFAULT_ENERGY_USAGE))

        # Validate the energy usage input
        if energy_usage < 0:
            raise ValueError("Energy usage must be a non-negative value.")

        # Calculate solar benefits
        benefits = calculate_solar_benefits(energy_usage)

        return jsonify(benefits)

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the application in debug mode for development purposes
    app.run(debug=True)
```

### HTML Template (`templates/index.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Solar Energy Calculator</title>
</head>
<body>
    <h1>Solar Energy Calculator</h1>
    <form id="energy-form">
        <label for="energy_usage">Enter your monthly energy usage (kWh):</label>
        <input type="number" id="energy_usage" name="energy_usage" required>
        <button type="submit">Calculate Benefits</button>
    </form>
    <div id="results"></div>

    <script>
        document.getElementById('energy-form').onsubmit = async function(event) {
            event.preventDefault();
            const formData = new FormData(this);
            const response = await fetch('/calculate', {
                method: 'POST',
                body: formData
            });

            const result = await response.json();
            const resultsDiv = document.getElementById('results');

            if (response.ok) {
                resultsDiv.innerHTML = `
                    <h2>Solar Energy Benefits</h2>
                    <p>Total Installation Cost: $${result.total_cost}</p>
                    <p>CO2 Reduction: ${result.environmental_impact} tons</p>
                `;
            } else {
                resultsDiv.innerHTML = `<p>Error: ${result.error}</p>`;
            }
        };
    </script>
</body>
</html>
```
