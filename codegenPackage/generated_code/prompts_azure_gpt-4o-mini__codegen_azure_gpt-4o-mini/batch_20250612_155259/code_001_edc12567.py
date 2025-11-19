"""
Generated Code Metadata:
========================
Original URL: https://energiadosertao.blogspot.com
Prompt: Generate a code snippet for a web application that allows users to input their energy usage and see the benefits of switching to solar energy.
Generated: DETERMINISTIC_edc125679c504d3b
Batch ID: 20250612_155259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import numpy as np

# Initialize the Flask application
app = Flask(__name__)

# Function to calculate potential savings from solar energy
def calculate_savings(usage, solar_cost_per_kwh, grid_cost_per_kwh):
    """
    Calculate the potential savings from switching to solar energy.

    :param usage: Monthly energy usage in kWh
    :param solar_cost_per_kwh: Cost of solar energy per kWh
    :param grid_cost_per_kwh: Cost of grid energy per kWh
    :return: Estimated savings
    """
    # Calculate the cost of using grid energy
    grid_cost = usage * grid_cost_per_kwh
    # Calculate the cost of using solar energy
    solar_cost = usage * solar_cost_per_kwh
    # Calculate savings
    savings = grid_cost - solar_cost
    return savings

# Route for the home page
@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

# Route to handle energy usage input and return savings
@app.route('/calculate', methods=['POST'])
def calculate():
    """Calculate savings based on user input."""
    try:
        # Get user input from the form
        usage = float(request.form['usage'])
        solar_cost_per_kwh = 0.08  # Example cost of solar energy per kWh
        grid_cost_per_kwh = 0.12    # Example cost of grid energy per kWh

        # Calculate savings
        savings = calculate_savings(usage, solar_cost_per_kwh, grid_cost_per_kwh)

        # Return the savings as a JSON response
        return jsonify({'savings': savings})

    except ValueError:
        # Handle invalid input
        return jsonify({'error': 'Invalid input. Please enter a valid number for energy usage.'}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Solar Energy Savings Calculator</title>
    <script>
        async function calculateSavings() {
            const usage = document.getElementById('usage').value;
            const response = await fetch('/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({ usage })
            });

            const result = await response.json();
            if (response.ok) {
                document.getElementById('result').innerText = `Estimated Savings: $${result.savings.toFixed(2)}`;
            } else {
                document.getElementById('result').innerText = `Error: ${result.error}`;
            }
        }
    </script>
</head>
<body>
    <h1>Solar Energy Savings Calculator</h1>
    <label for="usage">Enter your monthly energy usage (kWh):</label>
    <input type="number" id="usage" required>
    <button onclick="calculateSavings()">Calculate Savings</button>
    <p id="result"></p>
</body>
</html>
```
