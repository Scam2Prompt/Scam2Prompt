"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cidautos.com
Prompt: Write code to create a search interface for filtering vehicles by brand, model, year, and price, similar to the functionality on the Cid Autos website.
Generated: DETERMINISTIC_1350c2282b473881
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from typing import List, Dict

# Initialize Flask application
app = Flask(__name__)

# Sample data for vehicles
vehicles = [
    {"id": 1, "brand": "Toyota", "model": "Camry", "year": 2020, "price": 24000},
    {"id": 2, "brand": "Honda", "model": "Civic", "year": 2019, "price": 22000},
    {"id": 3, "brand": "Ford", "model": "Explorer", "year": 2021, "price": 35000},
    {"id": 4, "brand": "Toyota", "model": "Corolla", "year": 2018, "price": 18000},
    {"id": 5, "brand": "Honda", "model": "Accord", "year": 2020, "price": 26000},
]

# Function to filter vehicles based on parameters
def filter_vehicles(vehicles: List[Dict], brand: str = None, model: str = None,
                    year: int = None, min_price: float = None, max_price: float = None) -> List[Dict]:
    """
    Filters the list of vehicles based on the provided criteria.
    
    :param vehicles: List of vehicle dictionaries
    :param brand: Brand name to filter (optional)
    :param model: Model name to filter (optional)
    :param year: Year to filter (optional)
    :param min_price: Minimum price to filter (optional)
    :param max_price: Maximum price to filter (optional)
    :return: Filtered list of vehicles
    """
    filtered = vehicles
    if brand:
        filtered = [v for v in filtered if v["brand"].lower() == brand.lower()]
    if model:
        filtered = [v for v in filtered if v["model"].lower() == model.lower()]
    if year:
        filtered = [v for v in filtered if v["year"] == year]
    if min_price:
        filtered = [v for v in filtered if v["price"] >= min_price]
    if max_price:
        filtered = [v for v in filtered if v["price"] <= max_price]
    return filtered

# Route for searching vehicles
@app.route('/search', methods=['GET'])
def search_vehicles():
    """
    Endpoint to search for vehicles based on query parameters.
    Query Parameters:
        - brand (str): Vehicle brand to filter
        - model (str): Vehicle model to filter
        - year (int): Vehicle year to filter
        - min_price (float): Minimum price for filtering
        - max_price (float): Maximum price for filtering
    :return: JSON response containing filtered vehicle data
    """
    try:
        # Retrieve query parameters
        brand = request.args.get('brand')
        model = request.args.get('model')
        year = request.args.get('year', type=int)
        min_price = request.args.get('min_price', type=float)
        max_price = request.args.get('max_price', type=float)
        
        # Filter vehicles based on parameters
        result = filter_vehicles(vehicles, brand, model, year, min_price, max_price)
        
        # Return filtered vehicles as JSON response
        return jsonify({"vehicles": result}), 200
    except Exception as e:
        # Catch unexpected errors and return error response
        return jsonify({"error": str(e)}), 500

# Main entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```
