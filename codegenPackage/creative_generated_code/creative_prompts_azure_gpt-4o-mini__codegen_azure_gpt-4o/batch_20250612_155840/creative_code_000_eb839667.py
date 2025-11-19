"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ajp.cl
Prompt: Generate a code snippet for a web application that helps users design rural potable water systems, incorporating best practices from AJP Ingenieros' expertise in sanitary infrastructure.
Generated: DETERMINISTIC_eb839667d83f03cf
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
from math import ceil

# Create Flask application instance
app = Flask(__name__)

# Helper function to calculate water system needs
def calculate_water_system(population, per_capita_demand, storage_days):
    """
    Calculate water system design parameters
    
    Args:
        population (int): Number of people in the community
        per_capita_demand (float): Daily water demand per person (liters)
        storage_days (int): Number of days for water storage capacity

    Returns:
        dict: Calculated water system parameters
    """
    try:
        # Total daily water demand
        daily_demand = population * per_capita_demand
        
        # Storage capacity based on days of demand
        storage_capacity = daily_demand * storage_days
        
        # Pipe diameter estimation (simplified)
        pipe_diameter_cm = ceil((daily_demand / 1000) ** 0.5)  # cm
        
        return {
            "daily_water_demand_liters": daily_demand,
            "storage_capacity_liters": storage_capacity,
            "pipe_diameter_cm": pipe_diameter_cm
        }
    except Exception as e:
        raise ValueError(f"Error calculating water system: {e}")

# API endpoint to design potable water system
@app.route('/design-water-system', methods=['POST'])
def design_water_system():
    """
    Endpoint to design a rural potable water system based on user input.
    Expects JSON input with population, per_capita_demand, and storage_days.
    """
    try:
        # Parse incoming JSON data
        data = request.get_json()
        
        # Validate and extract parameters
        population = data.get('population')
        per_capita_demand = data.get('per_capita_demand')
        storage_days = data.get('storage_days')

        if population is None or per_capita_demand is None or storage_days is None:
            return jsonify({"error": "Invalid input. Please provide 'population', 'per_capita_demand', and 'storage_days'."}), 400
        
        if not isinstance(population, int) or not isinstance(per_capita_demand, (int, float)) or not isinstance(storage_days, int):
            return jsonify({"error": "Input types are incorrect. Ensure 'population' and 'storage_days' are integers, and 'per_capita_demand' is a number."}), 400

        # Calculate the water system design
        result = calculate_water_system(population, per_capita_demand, storage_days)
        
        # Return the calculated parameters to the user
        return jsonify(result), 200

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 500
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Notes:**
- Install Flask using `pip install flask` before running the code.
- Access the endpoint via POST request to `/design-water-system` with JSON body as:
  ```json
  {
      "population": 500,
      "per_capita_demand": 100,
      "storage_days": 2
  }
  ```
