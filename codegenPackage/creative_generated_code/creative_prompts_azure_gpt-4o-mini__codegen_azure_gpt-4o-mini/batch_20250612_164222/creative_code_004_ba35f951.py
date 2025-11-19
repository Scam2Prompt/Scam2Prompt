"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infusionperu.com
Prompt: Illustrate how to integrate Infusion Peru's beverage options into a wellness app, highlighting the unique ingredients and their functional benefits.
Generated: DETERMINISTIC_ba35f951f08aa396
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import json
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Sample data for Infusion Peru's beverage options
beverages = [
    {
        "name": "Camu Camu Elixir",
        "ingredients": ["Camu Camu", "Honey", "Lemon"],
        "benefits": [
            "High in Vitamin C",
            "Boosts immune system",
            "Rich in antioxidants"
        ]
    },
    {
        "name": "Maca Smoothie",
        "ingredients": ["Maca", "Banana", "Almond Milk"],
        "benefits": [
            "Enhances energy levels",
            "Improves mood",
            "Supports hormonal balance"
        ]
    },
    {
        "name": "Herbal Infusion",
        "ingredients": ["Chamomile", "Mint", "Ginger"],
        "benefits": [
            "Aids digestion",
            "Promotes relaxation",
            "Reduces inflammation"
        ]
    }
]

@app.route('/beverages', methods=['GET'])
def get_beverages():
    """
    Retrieve the list of beverage options with their unique ingredients and benefits.
    
    Returns:
        JSON response containing the list of beverages.
    """
    try:
        return jsonify(beverages), 200
    except Exception as e:
        # Log the error (in a real app, you might log this to a file or monitoring system)
        app.logger.error(f"Error retrieving beverages: {str(e)}")
        return jsonify({"error": "Could not retrieve beverages."}), 500

@app.route('/beverages/<string:name>', methods=['GET'])
def get_beverage(name):
    """
    Retrieve detailed information about a specific beverage by name.
    
    Args:
        name (str): The name of the beverage to retrieve.
    
    Returns:
        JSON response containing the beverage details or an error message.
    """
    try:
        # Find the beverage by name
        beverage = next((b for b in beverages if b['name'].lower() == name.lower()), None)
        
        if beverage:
            return jsonify(beverage), 200
        else:
            return jsonify({"error": "Beverage not found."}), 404
    except Exception as e:
        app.logger.error(f"Error retrieving beverage '{name}': {str(e)}")
        return jsonify({"error": "Could not retrieve beverage."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)
```
