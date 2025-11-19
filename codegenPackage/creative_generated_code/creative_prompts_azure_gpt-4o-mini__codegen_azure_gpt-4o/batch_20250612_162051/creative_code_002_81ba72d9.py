"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Create an API endpoint that retrieves a list of approved disinfectant products used for cleaning poultry buildings, including their environmental impact information.
Generated: DETERMINISTIC_81ba72d9c77a5995
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
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock data: List of approved disinfectant products
DISINFECTANT_PRODUCTS = [
    {
        "id": 1,
        "name": "EcoClean Disinfectant",
        "description": "Environmentally friendly disinfectant for poultry buildings.",
        "approved": True,
        "environmentalImpact": {
            "waterImpact": "Low",
            "airImpact": "Moderate",
            "soilImpact": "Low"
        }
    },
    {
        "id": 2,
        "name": "BioSafe Cleaner",
        "description": "Biodegradable cleaner for better poultry hygiene.",
        "approved": True,
        "environmentalImpact": {
            "waterImpact": "Moderate",
            "airImpact": "Low",
            "soilImpact": "Moderate"
        }
    },
    {
        "id": 3,
        "name": "Chemical-X",
        "description": "High-strength disinfectant for industrial use.",
        "approved": False,
        "environmentalImpact": {
            "waterImpact": "High",
            "airImpact": "High",
            "soilImpact": "High"
        }
    }
]

@app.route('/api/disinfectants', methods=['GET'])
def get_approved_disinfectants():
    """
    API Endpoint to retrieve a list of approved disinfectant products and their environmental impact.

    Returns:
        JSON response containing the list of approved disinfectant products.
    """
    try:
        # Filter only approved disinfectants
        approved_disinfectants = [
            product for product in DISINFECTANT_PRODUCTS if product["approved"]
        ]

        # Log the request
        logging.info("Request received: Retrieve approved disinfectants.")

        # Return the filtered list as a JSON response
        return jsonify({
            "status": "success",
            "data": approved_disinfectants
        }), 200
    except Exception as e:
        # Log error and return an error response
        logging.error(f"Error occurred while retrieving disinfectants: {str(e)}")
        return jsonify({
            "status": "error",
            "message": "An error occurred while processing your request."
        }), 500


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
