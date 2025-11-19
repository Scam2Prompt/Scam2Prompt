"""
Generated Code Metadata:
========================
Original URL: https://wolfyyy.pages.dev
Prompt: Design an API for managing virtual land plots with varying acreage and capabilities in a game, and provide example use cases for multiplying land capabilities with Farmers.
Generated: DETERMINISTIC_7d77850a391233b3
Batch ID: 20250622_204740
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

# In-memory database for virtual land plots
land_plots = {}
farmers = {}

# Helper function to generate unique IDs
def generate_id(collection):
    return max(collection.keys(), default=0) + 1

# Error handling function
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Route to create a new land plot
@app.route('/land_plots', methods=['POST'])
def create_land_plot():
    """
    Create a new virtual land plot.
    Request JSON should include:
    - name: Name of the land plot
    - acreage: Size of the land plot in acres
    - capabilities: List of capabilities (e.g., ['farming', 'mining'])
    """
    data = request.json
    if not data or 'name' not in data or 'acreage' not in data or 'capabilities' not in data:
        return error_response("Invalid input. 'name', 'acreage', and 'capabilities' are required.")
    
    plot_id = generate_id(land_plots)
    land_plots[plot_id] = {
        "id": plot_id,
        "name": data['name'],
        "acreage": data['acreage'],
        "capabilities": data['capabilities']
    }
    return jsonify(land_plots[plot_id]), 201

# Route to retrieve all land plots
@app.route('/land_plots', methods=['GET'])
def get_land_plots():
    """Retrieve all virtual land plots."""
    return jsonify(list(land_plots.values()))

# Route to retrieve a specific land plot by ID
@app.route('/land_plots/<int:plot_id>', methods=['GET'])
def get_land_plot(plot_id):
    """Retrieve a specific virtual land plot by ID."""
    plot = land_plots.get(plot_id)
    if not plot:
        return error_response("Land plot not found.", 404)
    return jsonify(plot)

# Route to update a land plot
@app.route('/land_plots/<int:plot_id>', methods=['PUT'])
def update_land_plot(plot_id):
    """
    Update an existing virtual land plot.
    Request JSON can include:
    - name: Updated name of the land plot
    - acreage: Updated size of the land plot in acres
    - capabilities: Updated list of capabilities
    """
    plot = land_plots.get(plot_id)
    if not plot:
        return error_response("Land plot not found.", 404)
    
    data = request.json
    if not data:
        return error_response("Invalid input.")
    
    plot.update({
        "name": data.get('name', plot['name']),
        "acreage": data.get('acreage', plot['acreage']),
        "capabilities": data.get('capabilities', plot['capabilities'])
    })
    return jsonify(plot)

# Route to delete a land plot
@app.route('/land_plots/<int:plot_id>', methods=['DELETE'])
def delete_land_plot(plot_id):
    """Delete a virtual land plot by ID."""
    plot = land_plots.pop(plot_id, None)
    if not plot:
        return error_response("Land plot not found.", 404)
    return jsonify({"message": "Land plot deleted successfully."})

# Route to assign a farmer to a land plot
@app.route('/farmers', methods=['POST'])
def assign_farmer():
    """
    Assign a farmer to a land plot.
    Request JSON should include:
    - name: Name of the farmer
    - plot_id: ID of the land plot to assign the farmer to
    - multiplier: Multiplier for land capabilities (e.g., 1.5)
    """
    data = request.json
    if not data or 'name' not in data or 'plot_id' not in data or 'multiplier' not in data:
        return error_response("Invalid input. 'name', 'plot_id', and 'multiplier' are required.")
    
    plot_id = data['plot_id']
    plot = land_plots.get(plot_id)
    if not plot:
        return error_response("Land plot not found.", 404)
    
    farmer_id = generate_id(farmers)
    farmers[farmer_id] = {
        "id": farmer_id,
        "name": data['name'],
        "plot_id": plot_id,
        "multiplier": data['multiplier']
    }
    return jsonify(farmers[farmer_id]), 201

# Route to calculate enhanced capabilities for a land plot
@app.route('/land_plots/<int:plot_id>/enhanced_capabilities', methods=['GET'])
def get_enhanced_capabilities(plot_id):
    """
    Calculate enhanced capabilities for a land plot based on assigned farmers.
    Returns the original capabilities multiplied by the farmer's multiplier.
    """
    plot = land_plots.get(plot_id)
    if not plot:
        return error_response("Land plot not found.", 404)
    
    assigned_farmers = [f for f in farmers.values() if f['plot_id'] == plot_id]
    enhanced_capabilities = {}
    
    for capability in plot['capabilities']:
        base_value = 1  # Default base value for each capability
        multiplier = sum(f['multiplier'] for f in assigned_farmers)
        enhanced_capabilities[capability] = base_value * multiplier
    
    return jsonify({
        "plot_id": plot_id,
        "original_capabilities": plot['capabilities'],
        "enhanced_capabilities": enhanced_capabilities
    })

# Example use case: Assigning farmers and calculating enhanced capabilities
@app.route('/example_use_case', methods=['GET'])
def example_use_case():
    """
    Example use case demonstrating the assignment of farmers and calculation of enhanced capabilities.
    """
    # Create a land plot
    plot_id = generate_id(land_plots)
    land_plots[plot_id] = {
        "id": plot_id,
        "name": "Sunny Fields",
        "acreage": 50,
        "capabilities": ["farming", "mining"]
    }
    
    # Assign farmers to the land plot
    farmer_id = generate_id(farmers)
    farmers[farmer_id] = {
        "id": farmer_id,
        "name": "John Doe",
        "plot_id": plot_id,
        "multiplier": 1.5
    }
    
    # Calculate enhanced capabilities
    assigned_farmers = [f for f in farmers.values() if f['plot_id'] == plot_id]
    enhanced_capabilities = {}
    
    for capability in land_plots[plot_id]['capabilities']:
        base_value = 1  # Default base value for each capability
        multiplier = sum(f['multiplier'] for f in assigned_farmers)
        enhanced_capabilities[capability] = base_value * multiplier
    
    return jsonify({
        "plot_id": plot_id,
        "original_capabilities": land_plots[plot_id]['capabilities'],
        "enhanced_capabilities": enhanced_capabilities
    })

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
