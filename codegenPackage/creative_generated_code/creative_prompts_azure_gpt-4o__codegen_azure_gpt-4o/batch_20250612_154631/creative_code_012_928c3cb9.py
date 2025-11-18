"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econopure.com.vn
Prompt: Recommend an API for tracking the performance of Econopure's water filtration systems, including real-time data from UF, NF, and RO modules.
Generated: DETERMINISTIC_928c3cb958e0ebde
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
API for tracking the performance of Econopure's water filtration systems.
This API provides real-time data from UF (Ultrafiltration), NF (Nanofiltration), and RO (Reverse Osmosis) modules.

Features:
1. Fetch real-time module performance metrics
2. Error handling for invalid requests
3. Modular and extensible design
"""

from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Mock data for demonstration purposes. In production, replace this with actual real-time data sources.
performance_data = {
    "UF": {"flow_rate": 12.5, "pressure": 3.2, "temperature": 25.0},
    "NF": {"flow_rate": 15.0, "pressure": 4.5, "temperature": 24.5},
    "RO": {"flow_rate": 10.0, "pressure": 6.5, "temperature": 23.0},
}

@app.route("/api/modules/<module_name>/data", methods=["GET"])
def get_module_data(module_name):
    """
    Endpoint to fetch real-time performance data for a specified module.

    Args:
        module_name (str): The name of the module (UF, NF, RO).

    Returns:
        JSON: Real-time performance data for the requested module or an error message if the module is invalid.
    """
    try:
        # Validate module name
        module_name = module_name.upper()
        if module_name not in performance_data:
            return jsonify({"error": f"Module '{module_name}' not found. Valid modules are: UF, NF, RO."}), 404
        
        # Fetch and return the performance data for the module
        data = performance_data[module_name]
        return jsonify({"module": module_name, "performance_data": data}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

@app.route("/api/modules", methods=["GET"])
def list_modules():
    """
    Endpoint to list all available modules.

    Returns:
        JSON: A list of all available modules.
    """
    try:
        return jsonify({"modules": list(performance_data.keys())}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Error handling for unsupported routes
@app.errorhandler(404)
def page_not_found(error):
    """
    Handle 404 errors for unsupported routes.

    Args:
        error: The error object.

    Returns:
        JSON: Error message for unsupported routes.
    """
    return jsonify({"error": "The requested resource could not be found."}), 404

# Run the Flask application
if __name__ == "__main__":
    # In production, set debug=False and use a production-ready server (e.g., Gunicorn or uWSGI).
    app.run(host="0.0.0.0", port=5000, debug=True)
```
