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
# File: app.py
# Description: A web application to calculate the benefits of switching to solar energy
# Framework: Flask (Python)

from flask import Flask, request, jsonify
import math

app = Flask(__name__)

# Helper function to calculate solar benefits
def calculate_solar_benefits(energy_usage_kwh):
    """
    Calculate the potential savings and environmental benefits of switching to solar energy.
    
    :param energy_usage_kwh: Monthly energy usage in kilowatt-hours
    :return: Dictionary containing savings and environmental benefit details
    """
    try:
        # Approximation values
        cost_per_kwh = 0.12  # Average cost of electricity per kWh ($)
        solar_cost_per_kwh = 0.05  # Hypothetical cost of solar per kWh ($)
        carbon_emission_per_kwh = 0.92  # Average CO2 emissions per kWh (kg)
        
        savings = round(energy_usage_kwh * (cost_per_kwh - solar_cost_per_kwh), 2)  # $ savings
        emissions_saved = round(energy_usage_kwh * carbon_emission_per_kwh, 2)  # kg CO2

        return {
            "monthly_savings": savings,
            "annual_savings": savings * 12,
            "emissions_saved_kg": emissions_saved,
            "emissions_saved_tonnes": round(emissions_saved / 1000, 2)  # Convert kg to tonnes
        }
    except Exception as e:
        raise ValueError(f"Error during calculation: {e}")

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Endpoint to calculate solar energy benefits based on user input.
    
    :return: JSON response with calculated solar benefits
    """
    try:
        # Parse user input
        data = request.json
        if not data or 'energy_usage_kwh' not in data:
            return jsonify({"error": "Invalid input. Please provide 'energy_usage_kwh'."}), 400
        
        energy_usage_kwh = data.get('energy_usage_kwh')
        if not isinstance(energy_usage_kwh, (int, float)) or energy_usage_kwh <= 0:
            return jsonify({"error": "Invalid value for 'energy_usage_kwh'. Must be a positive number."}), 400

        # Perform calculation
        benefits = calculate_solar_benefits(energy_usage_kwh)
        return jsonify({"success": True, "data": benefits}), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/')
def home():
    """
    Home endpoint providing basic information about the application.
    
    :return: Welcome message
    """
    return jsonify({
        "message": "Welcome to the Solar Energy Benefits Calculator API!",
        "endpoints": {
            "/calculate": "POST endpoint to calculate solar energy benefits. Requires 'energy_usage_kwh' in the request body."
        }
    }), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Instructions:
1. Install dependencies: `pip install flask`
2. Run the script: `python app.py`
3. Use a tool like Postman or curl to make POST requests to `/calculate` with a JSON body:
   ```json
   {
       "energy_usage_kwh": 500
   }
   ```
