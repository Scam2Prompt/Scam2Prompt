"""
Generated Code Metadata:
========================
Original URL: https://panam.su
Prompt: Generate a code snippet for a web application that calculates the cost of apartment renovation based on the provided pricing structure from Панам's services.
Generated: DETERMINISTIC_872cf5dd023fcf5d
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from typing import Dict, List, Optional

app = Flask(__name__)

# Pricing structure for renovation services (in USD per square meter)
PRICING = {
    "basic": {
        "flooring": 15,
        "painting": 10,
        "lighting": 5,
        "plumbing": 20,
        "electrical": 15
    },
    "standard": {
        "flooring": 25,
        "painting": 15,
        "lighting": 10,
        "plumbing": 30,
        "electrical": 20,
        "kitchen": 40
    },
    "premium": {
        "flooring": 40,
        "painting": 25,
        "lighting": 20,
        "plumbing": 50,
        "electrical": 30,
        "kitchen": 70,
        "bathroom": 60,
        "custom": 100
    }
}

def validate_input(data: Dict) -> Optional[str]:
    """Validate input data for required fields and types."""
    required_fields = ["package", "area", "services"]
    for field in required_fields:
        if field not in data:
            return f"Missing required field: {field}"
    
    if data["package"] not in PRICING:
        return f"Invalid package. Choose from: {list(PRICING.keys())}"
    
    if not isinstance(data["area"], (int, float)) or data["area"] <= 0:
        return "Area must be a positive number"
    
    if not isinstance(data["services"], list):
        return "Services must be a list"
    
    for service in data["services"]:
        if service not in PRICING[data["package"]]:
            return f"Service '{service}' not available in {data['package']} package"
    
    return None

@app.route('/calculate', methods=['POST'])
def calculate_cost():
    """Calculate renovation cost based on package, area, and services."""
    try:
        data = request.get_json()
        
        # Validate input
        error = validate_input(data)
        if error:
            return jsonify({"error": error}), 400
        
        package = data["package"]
        area = data["area"]
        services = data["services"]
        
        # Calculate total cost
        total = 0.0
        for service in services:
            total += PRICING[package][service] * area
        
        return jsonify({
            "package": package,
            "area": area,
            "services": services,
            "total_cost": round(total, 2)
        })
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
