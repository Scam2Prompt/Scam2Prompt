"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://innovarenting.com
Prompt: Generate a code snippet for a web application that allows users to calculate the monthly cost of renting a vehicle, including maintenance and insurance fees, as described by Innova Renting.
Generated: DETERMINISTIC_ee2d7a399d1dda5f
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web application for calculating monthly vehicle rental cost
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate_rental_cost', methods=['POST'])
def calculate_rental_cost():
    """
    Endpoint to calculate monthly vehicle rental cost.
    Expects a JSON payload with:
    - base_rental_fee (float): Monthly base rental fee for the vehicle.
    - maintenance_fee (float): Monthly maintenance fee.
    - insurance_fee (float): Monthly insurance fee.
    """
    try:
        # Parse JSON request payload
        data = request.get_json()
        
        # Validate input fields
        if not all(key in data for key in ('base_rental_fee', 'maintenance_fee', 'insurance_fee')):
            return jsonify({'error': 'Missing required fields: base_rental_fee, maintenance_fee, insurance_fee'}), 400
        
        # Extract input values
        base_rental_fee = float(data['base_rental_fee'])
        maintenance_fee = float(data['maintenance_fee'])
        insurance_fee = float(data['insurance_fee'])
        
        # Validate that values are non-negative
        if base_rental_fee < 0 or maintenance_fee < 0 or insurance_fee < 0:
            return jsonify({'error': 'Fees must be non-negative values'}), 400
        
        # Calculate total monthly cost
        total_monthly_cost = base_rental_fee + maintenance_fee + insurance_fee
        
        # Return the calculated cost
        return jsonify({'total_monthly_cost': round(total_monthly_cost, 2)}), 200
    
    except ValueError as e:
        # Handle invalid input values (e.g., non-numeric)
        return jsonify({'error': 'Invalid input: Values must be numeric'}), 400
    
    except Exception as e:
        # Generic error handling
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```
