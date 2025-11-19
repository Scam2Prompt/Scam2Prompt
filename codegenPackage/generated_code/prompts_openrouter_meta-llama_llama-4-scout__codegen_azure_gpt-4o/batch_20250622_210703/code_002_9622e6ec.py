"""
Generated Code Metadata:
========================
Original URL: https://www.ablakvaros.hu
Prompt: "Generate a list of API endpoints for a web application that allows users to request quotes for Aluplast window installations, including parameters for window type, size, and material."
Generated: DETERMINISTIC_9622e6ec86b59ddd
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for demonstration purposes
WINDOW_TYPES = ["casement", "sliding", "tilt_and_turn"]
MATERIALS = ["PVC", "aluminum", "wood"]

# Error response helper function
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Endpoint: Get available window types
@app.route('/api/window-types', methods=['GET'])
def get_window_types():
    """
    Returns a list of available window types.
    """
    return jsonify({"window_types": WINDOW_TYPES})

# Endpoint: Get available materials
@app.route('/api/materials', methods=['GET'])
def get_materials():
    """
    Returns a list of available materials.
    """
    return jsonify({"materials": MATERIALS})

# Endpoint: Request a quote
@app.route('/api/request-quote', methods=['POST'])
def request_quote():
    """
    Allows users to request a quote for Aluplast window installations.
    Expects JSON payload with the following parameters:
    - window_type: str (required, must be one of WINDOW_TYPES)
    - width: float (required, must be positive)
    - height: float (required, must be positive)
    - material: str (required, must be one of MATERIALS)
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data:
            return error_response("Invalid or missing JSON payload.")

        # Validate window_type
        window_type = data.get("window_type")
        if window_type not in WINDOW_TYPES:
            return error_response(f"Invalid window_type. Must be one of {WINDOW_TYPES}.")

        # Validate width
        width = data.get("width")
        if not isinstance(width, (int, float)) or width <= 0:
            return error_response("Invalid width. Must be a positive number.")

        # Validate height
        height = data.get("height")
        if not isinstance(height, (int, float)) or height <= 0:
            return error_response("Invalid height. Must be a positive number.")

        # Validate material
        material = data.get("material")
        if material not in MATERIALS:
            return error_response(f"Invalid material. Must be one of {MATERIALS}.")

        # Generate a mock quote (in a real application, this would involve complex calculations)
        quote_price = round((width * height) * 10, 2)  # Example pricing logic

        # Return the quote
        return jsonify({
            "window_type": window_type,
            "width": width,
            "height": height,
            "material": material,
            "quote_price": quote_price
        })

    except Exception as e:
        # Catch unexpected errors
        return error_response(f"An error occurred: {str(e)}", status_code=500)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
