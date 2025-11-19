"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://energiadosertao.blogspot.com
Prompt: Suggest an API that provides information on solar panel installation costs and potential savings for residential and commercial properties.
Generated: DETERMINISTIC_205571d397b2d99b
Batch ID: 20250612_155259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging for debugging and production readiness
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_installation_cost(area, property_type):
    """
    Calculate solar panel installation cost based on area and property type.

    Args:
        area (float): Area in square feet.
        property_type (str): Type of property ("residential" or "commercial").

    Returns:
        float: Estimated installation cost.
    """
    base_rate = 100  # Base cost per square foot in USD
    if property_type == 'residential':
        return base_rate * area
    elif property_type == 'commercial':
        return base_rate * area * 1.2  # Commercial properties have higher costs
    else:
        raise ValueError("Invalid property type. Must be 'residential' or 'commercial'.")

def calculate_potential_savings(area, property_type):
    """
    Calculate potential savings from solar panel installation.

    Args:
        area (float): Area in square feet.
        property_type (str): Type of property ("residential" or "commercial").

    Returns:
        float: Estimated annual savings.
    """
    savings_rate = 0.2  # Savings rate per square foot in USD
    if property_type == 'residential':
        return savings_rate * area * 365  # Assume 365 days of savings
    elif property_type == 'commercial':
        return savings_rate * area * 365 * 1.5  # Commercial properties save more
    else:
        raise ValueError("Invalid property type. Must be 'residential' or 'commercial'.")

@app.route('/solar-panel-info', methods=['GET'])
def solar_panel_info():
    """
    API endpoint to provide solar panel installation cost and savings.

    Query Parameters:
        area (float): Area in square feet.
        property_type (str): Type of property ("residential" or "commercial").

    Returns:
        JSON response with installation cost and potential savings.
    """
    try:
        # Get query parameters
        area = float(request.args.get('area', 0))
        property_type = request.args.get('property_type', '').lower()

        # Validate input
        if area <= 0:
            return jsonify({'error': 'Area must be greater than 0'}), 400
        if property_type not in ['residential', 'commercial']:
            return jsonify({'error': "Property type must be 'residential' or 'commercial'"}), 400

        # Calculate costs and savings
        installation_cost = calculate_installation_cost(area, property_type)
        potential_savings = calculate_potential_savings(area, property_type)

        # Respond with the calculated data
        return jsonify({
            'installation_cost': round(installation_cost, 2),
            'potential_savings': round(potential_savings, 2)
        })
    except ValueError as e:
        logging.error(f"Value error occurred: {e}")
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

# Start Flask server
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```
