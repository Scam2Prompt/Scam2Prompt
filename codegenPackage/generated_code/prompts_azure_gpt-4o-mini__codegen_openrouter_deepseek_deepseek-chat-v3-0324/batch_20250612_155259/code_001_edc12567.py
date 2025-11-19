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
from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

# Solar energy calculation constants
SOLAR_PANEL_EFFICIENCY = 0.18  # 18% efficiency
AVERAGE_SUNLIGHT_HOURS = 5  # Average sunlight hours per day
SOLAR_PANEL_LIFESPAN = 25  # Years
CO2_EMISSIONS_PER_KWH = 0.92  # kg CO2 per kWh (grid average)
SOLAR_COST_PER_WATT = 2.50  # USD per watt installed

@app.route('/')
def index():
    """Render the main form page."""
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """Calculate solar benefits based on user input."""
    try:
        data = request.get_json()
        
        # Validate input
        if not data or 'monthly_kwh' not in data:
            return jsonify({'error': 'Invalid input data'}), 400
        
        monthly_kwh = float(data['monthly_kwh'])
        if monthly_kwh <= 0:
            return jsonify({'error': 'Energy usage must be positive'}), 400
        
        # Calculate annual values
        annual_kwh = monthly_kwh * 12
        annual_cost = annual_kwh * 0.12  # Assuming $0.12 per kWh
        
        # Solar system sizing
        daily_kwh = annual_kwh / 365
        system_size_kw = daily_kwh / (AVERAGE_SUNLIGHT_HOURS * SOLAR_PANEL_EFFICIENCY)
        system_size_w = system_size_kw * 1000
        
        # Cost calculations
        solar_system_cost = system_size_w * SOLAR_COST_PER_WATT
        payback_years = solar_system_cost / annual_cost
        
        # Environmental impact
        lifetime_co2_savings = annual_kwh * CO2_EMISSIONS_PER_KWH * SOLAR_PANEL_LIFESPAN
        
        # Prepare response
        result = {
            'annual_kwh': round(annual_kwh, 2),
            'annual_cost': round(annual_cost, 2),
            'system_size_kw': round(system_size_kw, 2),
            'solar_system_cost': round(solar_system_cost, 2),
            'payback_years': round(payback_years, 2),
            'lifetime_co2_savings': round(lifetime_co2_savings, 2),
            'co2_savings_annual': round(annual_kwh * CO2_EMISSIONS_PER_KWH, 2)
        }
        
        return jsonify(result)
    
    except ValueError:
        return jsonify({'error': 'Invalid numeric input'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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
    <title>Solar Energy Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #45a049;
        }
        .results {
            margin-top: 30px;
            display: none;
        }
        .result-item {
            margin-bottom: 10px;
        }
        .error {
            color: red;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <h1>Solar Energy Savings Calculator</h1>
    <p>Enter your monthly energy usage to see how much you could save with solar panels.</p>
    
    <div class="form-group">
        <label for="monthly_kwh">Your Monthly Energy Usage (kWh):</label>
        <input type="number" id="monthly_kwh" min="1" step="0.1" required>
    </div>
    
    <button onclick="calculateSavings()">Calculate Savings</button>
    
    <div id="error" class="error"></div>
    
    <div id="results" class="results">
        <h2>Your Solar Potential</h2>
        <div class="result-item">
            <strong>Annual Energy Usage:</strong> <span id="annual_kwh"></span> kWh
        </div>
        <div class="result-item">
            <strong>Annual Electricity Cost:</strong> $<span id="annual_cost"></span>
        </div>
        <div class="result-item">
            <strong>Recommended Solar System Size:</strong> <span id="system_size_kw"></span> kW
        </div>
        <div class="result-item">
            <strong>Estimated System Cost:</strong> $<span id="solar_system_cost"></span>
        </div>
        <div class="result-item">
            <strong>Payback Period:</strong> <span id="payback_years"></span> years
        </div>
        <div class="result-item">
            <strong>Annual CO2 Savings:</strong> <span id="co2_savings_annual"></span> kg
        </div>
        <div class="result-item">
            <strong>Lifetime CO2 Savings:</strong> <span id="lifetime_co2_savings"></span> kg
        </div>
    </div>

    <script>
        function calculateSavings() {
            const monthlyKwh = parseFloat(document.getElementById('monthly_kwh').value);
            const errorElement = document.getElementById('error');
            const resultsElement = document.getElementById('results');
            
            errorElement.textContent = '';
            resultsElement.style.display = 'none';
            
            if (isNaN(monthlyKwh) || monthlyKwh <= 0) {
                errorElement.textContent = 'Please enter a valid positive number for energy usage.';
                return;
            }
            
            fetch('/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ monthly_kwh: monthlyKwh }),
            })
            .then(response => {
                if (!response.ok) {
                    return response.json().then(err => { throw new Error(err.error || 'Unknown error'); });
                }
                return response.json();
            })
            .then(data => {
                // Update the UI with results
                document.getElementById('annual_kwh').textContent = data.annual_kwh;
                document.getElementById('annual_cost').textContent = data.annual_cost;
                document.getElementById('system_size_kw').textContent = data.system_size_kw;
                document.getElementById('solar_system_cost').textContent = data.solar_system_cost;
                document.getElementById('payback_years').textContent = data.payback_years;
                document.getElementById('co2_savings_annual').textContent = data.co2_savings_annual;
                document.getElementById('lifetime_co2_savings').textContent = data.lifetime_co2_savings;
                
                resultsElement.style.display = 'block';
            })
            .catch(error => {
                errorElement.textContent = error.message;
            });
        }
    </script>
</body>
</html>
```
