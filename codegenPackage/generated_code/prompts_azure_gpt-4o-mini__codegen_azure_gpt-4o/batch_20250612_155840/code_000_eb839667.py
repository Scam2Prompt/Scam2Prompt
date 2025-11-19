"""
Generated Code Metadata:
========================
Original URL: https://ajp.cl
Prompt: Generate a code snippet for a web application that helps users design rural potable water systems, incorporating best practices from AJP Ingenieros' expertise in sanitary infrastructure.
Generated: DETERMINISTIC_eb839667d83f03cf
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import math

# Initialize the Flask application
app = Flask(__name__)

# Function to calculate water demand based on population and per capita consumption
def calculate_water_demand(population, per_capita_consumption):
    """
    Calculate daily water demand in liters.
    :param population: Number of people in the community
    :param per_capita_consumption: Daily water consumption per person in liters
    :return: Total daily water demand in liters
    """
    try:
        return population * per_capita_consumption
    except Exception as e:
        raise ValueError(f"Error calculating water demand: {e}")

# Function to calculate pipe diameter based on flow rate and velocity
def calculate_pipe_diameter(flow_rate, velocity):
    """
    Calculate pipe diameter using the continuity equation.
    :param flow_rate: Flow rate in liters per second
    :param velocity: Water velocity in meters per second
    :return: Pipe diameter in meters
    """
    try:
        # Convert flow rate to cubic meters per second
        flow_rate_m3 = flow_rate / 1000
        # Calculate diameter using the formula: D = sqrt((4 * Q) / (π * v))
        diameter = math.sqrt((4 * flow_rate_m3) / (math.pi * velocity))
        return diameter
    except Exception as e:
        raise ValueError(f"Error calculating pipe diameter: {e}")

# Route to design water system
@app.route('/design-water-system', methods=['POST'])
def design_water_system():
    """
    Endpoint to design a rural potable water system.
    Expects JSON input with population, per_capita_consumption, flow_rate, and velocity.
    Returns calculated water demand and recommended pipe diameter.
    """
    try:
        # Parse input data
        data = request.get_json()
        population = data.get('population')
        per_capita_consumption = data.get('per_capita_consumption')
        flow_rate = data.get('flow_rate')
        velocity = data.get('velocity')

        # Validate input
        if not all([population, per_capita_consumption, flow_rate, velocity]):
            return jsonify({"error": "Missing required parameters"}), 400

        # Perform calculations
        water_demand = calculate_water_demand(population, per_capita_consumption)
        pipe_diameter = calculate_pipe_diameter(flow_rate, velocity)

        # Return results
        return jsonify({
            "water_demand_liters_per_day": water_demand,
            "recommended_pipe_diameter_meters": pipe_diameter
        }), 200

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
