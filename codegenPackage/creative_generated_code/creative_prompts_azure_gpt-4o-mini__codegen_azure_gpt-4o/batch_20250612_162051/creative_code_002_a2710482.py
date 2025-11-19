"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.fravitur.com
Prompt: Create an example of a RESTful API request to fetch travel packages for South American countries like Peru and Argentina, based on the content from Fravitur.
Generated: DETERMINISTIC_a2710482a8525b86
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Mock function to simulate fetching data from Fravitur API
def fetch_travel_packages(country):
    """
    Fetch travel packages from Fravitur for a given country.
    This is a mock implementation. Replace with actual API calls if available.

    Args:
        country (str): Name of the country to fetch travel packages for.

    Returns:
        list: List of travel packages for the country.
    """
    # Mock travel packages data
    travel_packages = {
        "Peru": [
            {"package_id": 1, "name": "Machu Picchu Adventure", "price": 1200, "duration": "5 days"},
            {"package_id": 2, "name": "Amazon Rainforest Expedition", "price": 1500, "duration": "7 days"},
        ],
        "Argentina": [
            {"package_id": 3, "name": "Patagonia Explorer", "price": 1800, "duration": "8 days"},
            {"package_id": 4, "name": "Buenos Aires City Tour", "price": 500, "duration": "3 days"},
        ]
    }
    return travel_packages.get(country, [])

@app.route('/api/travel-packages', methods=['GET'])
def get_travel_packages():
    """
    API endpoint to fetch travel packages for a specified South American country.

    Query Parameters:
        country (str): Name of the country (e.g., 'Peru', 'Argentina').

    Returns:
        JSON response with travel packages or an error message.
    """
    # Get 'country' parameter from the query string
    country = request.args.get('country')

    # Validate input
    if not country:
        return jsonify({"error": "Query parameter 'country' is required."}), 400
    
    # Fetch travel packages
    try:
        packages = fetch_travel_packages(country)
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while fetching travel packages.", "details": str(e)}), 500

    # If no packages are found, return an informative message
    if not packages:
        return jsonify({"message": f"No travel packages found for country: {country}"}), 404

    # Return travel packages as a JSON response
    return jsonify({"country": country, "packages": packages})

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Install Flask via `pip install flask` before running this code.
- Replace the `fetch_travel_packages` function with actual API calls to Fravitur's API if available.
- This is a mock implementation and suitable for testing purposes only.
