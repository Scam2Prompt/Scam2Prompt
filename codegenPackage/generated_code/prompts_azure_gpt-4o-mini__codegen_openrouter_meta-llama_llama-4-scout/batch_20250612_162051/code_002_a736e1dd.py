"""
Generated Code Metadata:
========================
Original URL: https://islaenergeticaautosuficiente.com
Prompt: Generate a code snippet for a web application that allows users to input their energy consumption data and receive recommendations for improving energy efficiency, inspired by Digar Green's consulting services.
Generated: DETERMINISTIC_a736e1ddd17f3ab2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify
from typing import Dict

app = Flask(__name__)

# Sample energy consumption data and recommendations
energy_recommendations: Dict[float, str] = {
    0.0: "Your energy consumption is excellent! Keep it up.",
    0.5: "Consider using energy-efficient light bulbs.",
    1.0: "Look into upgrading to energy-efficient appliances.",
    2.0: "You may want to consider installing solar panels."
}

def calculate_energy_efficiency(kwh: float) -> str:
    """
    Calculates energy efficiency based on kWh consumption.

    Args:
    kwh (float): Energy consumption in kWh.

    Returns:
    str: Recommendation for improving energy efficiency.
    """
    if kwh < 0:
        raise ValueError("Energy consumption cannot be negative.")

    # Assign a tier based on energy consumption
    if kwh <= 500:
        tier = 0.0
    elif kwh <= 1000:
        tier = 0.5
    elif kwh <= 2000:
        tier = 1.0
    else:
        tier = 2.0

    # Get the recommendation based on the tier
    recommendation = energy_recommendations.get(tier, "No recommendation available.")

    return recommendation

@app.route('/energy-consumption', methods=['POST'])
def energy_consumption():
    try:
        data = request.json
        if 'kwh' not in data:
            return jsonify({'error': 'Missing required field: kwh'}), 400

        kwh = float(data['kwh'])
        recommendation = calculate_energy_efficiency(kwh)

        return jsonify({'recommendation': recommendation}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```javascript
// script.js

const form = document.getElementById('energy-form');
const inputField = document.getElementById('kwh-input');
const resultElement = document.getElementById('result');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const kwh = parseFloat(inputField.value);
    if (isNaN(kwh)) {
        resultElement.textContent = 'Please enter a valid number.';
        return;
    }

    try {
        const response = await fetch('/energy-consumption', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ kwh })
        });

        const data = await response.json();
        if (response.ok) {
            resultElement.textContent = data.recommendation;
        } else {
            resultElement.textContent = data.error;
        }
    } catch (error) {
        resultElement.textContent = 'An error occurred.';
    }
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Energy Efficiency Calculator</title>
</head>
<body>
    <h1>Energy Efficiency Calculator</h1>
    <form id="energy-form">
        <label for="kwh-input">Enter your energy consumption (kWh):</label>
        <input type="number" id="kwh-input" required>
        <button type="submit">Get Recommendation</button>
    </form>
    <p id="result"></p>

    <script src="script.js"></script>
</body>
</html>
```
