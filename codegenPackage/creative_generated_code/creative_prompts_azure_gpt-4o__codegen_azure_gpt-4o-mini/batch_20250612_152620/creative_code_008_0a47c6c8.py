"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capinaeletrica.com.br
Prompt: Recommend tools or libraries for creating a demo application that showcases Capina Elétrica's weed removal efficiency across different terrains (urban, agricultural, railway).
Generated: DETERMINISTIC_0a47c6c809daff2a
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Initialize the Flask application
app = Flask(__name__)

# Sample data for demonstration purposes
# You would typically fetch this data from a database or an API
data = {
    "urban": {
        "efficiency": [85, 90, 80, 88, 91],
        "terrains": ["concrete", "asphalt", "grass", "dirt", "mixed"]
    },
    "agricultural": {
        "efficiency": [95, 88, 94, 90, 92],
        "terrains": ["plowed", "unplowed", "mixed", "wet", "dry"]
    },
    "railway": {
        "efficiency": [80, 85, 82, 78, 81],
        "terrains": ["ballast", "gravel", "mixed", "grass", "dirt"]
    }
}

@app.route('/efficiency/<terrain_type>', methods=['GET'])
def get_efficiency(terrain_type):
    """
    API endpoint to get weed removal efficiency data based on terrain type.

    :param terrain_type: The type of terrain (urban, agricultural, railway)
    :return: JSON response containing efficiency data
    """
    try:
        # Validate the terrain_type input
        if terrain_type not in data:
            return jsonify({"error": "Invalid terrain type. Choose from urban, agricultural, railway."}), 400
        
        return jsonify(data[terrain_type]), 200
    except Exception as e:
        # Log the error and return a 500 response
        app.logger.error(f"Error retrieving data: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route('/plot/<terrain_type>', methods=['GET'])
def plot_efficiency(terrain_type):
    """
    API endpoint to plot weed removal efficiency based on terrain type.

    :param terrain_type: The type of terrain (urban, agricultural, railway)
    :return: Response indicating the success of the plot request
    """
    try:
        if terrain_type not in data:
            return jsonify({"error": "Invalid terrain type. Choose from urban, agricultural, railway."}), 400
        
        # Create a plot of the efficiency data
        efficiencies = data[terrain_type]['efficiency']
        terrains = data[terrain_type]['terrains']
        
        # Plotting the data
        plt.figure(figsize=(10, 5))
        plt.bar(terrains, efficiencies, color='skyblue')
        plt.title(f"Weed Removal Efficiency in {terrain_type.capitalize()} Terrain")
        plt.xlabel("Terrain Type")
        plt.ylabel("Efficiency (%)")
        plt.ylim(0, 100)
        plt.grid(axis='y')
        
        # Save the plot to a file
        plot_file = f"{terrain_type}_efficiency_plot.png"
        plt.savefig(plot_file)
        plt.close()  # Close the plot to free memory
        
        return jsonify({"message": "Plot generated successfully", "file": plot_file}), 200
    except Exception as e:
        app.logger.error(f"Error generating plot: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)  # Set debug to False in production
```
