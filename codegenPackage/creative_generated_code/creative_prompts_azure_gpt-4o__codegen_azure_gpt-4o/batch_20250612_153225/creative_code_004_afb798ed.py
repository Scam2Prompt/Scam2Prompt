"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soltec-solutions.de
Prompt: Develop an API that allows users to input their energy consumption and receive tailored solar panel installation plans, as described in Soltec Solutions' individual planning services.
Generated: DETERMINISTIC_afb798eda5a50287
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import math

app = Flask(__name__)

# Constants for solar panel calculation
AVG_PANEL_EFFICIENCY = 0.18  # Average efficiency of solar panels (18%)
AVG_SUNLIGHT_HOURS = 5  # Average daily sunlight hours
WATTAGE_PER_PANEL = 400  # Wattage of a single solar panel

# Error messages
ERROR_MISSING_DATA = {"error": "Missing required data: Please provide 'daily_energy_consumption_kwh'."}
ERROR_INVALID_DATA = {"error": "Invalid data: 'daily_energy_consumption_kwh' must be a positive number."}

@app.route('/solar-planning', methods=['POST'])
def solar_planning():
    """
    Endpoint to calculate solar panel installation plans based on energy consumption.

    Request Body:
    {
        "daily_energy_consumption_kwh": <float>  # Daily energy consumption in kWh
    }

    Response:
    {
        "required_panels": <int>,  # Number of solar panels required
        "total_output_kw": <float>,  # Total output of the solar system in kW
        "message": <str>  # Explanation of the plan
    }
    """
    try:
        # Parse input JSON
        data = request.json

        # Validate input data
        if not data or 'daily_energy_consumption_kwh' not in data:
            return jsonify(ERROR_MISSING_DATA), 400
        
        daily_energy_consumption = data['daily_energy_consumption_kwh']
        if not isinstance(daily_energy_consumption, (int, float)) or daily_energy_consumption <= 0:
            return jsonify(ERROR_INVALID_DATA), 400

        # Calculate required solar panels
        daily_output_per_panel = WATTAGE_PER_PANEL * AVG_PANEL_EFFICIENCY * AVG_SUNLIGHT_HOURS / 1000  # kWh/day
        required_panels = math.ceil(daily_energy_consumption / daily_output_per_panel)
        total_output_kw = required_panels * WATTAGE_PER_PANEL / 1000  # Total system output in kW

        # Prepare response
        response = {
            "required_panels": required_panels,
            "total_output_kw": round(total_output_kw, 2),
            "message": f"Based on your daily energy consumption of {daily_energy_consumption} kWh, "
                       f"you will need approximately {required_panels} solar panels to meet your needs."
        }
        return jsonify(response), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
