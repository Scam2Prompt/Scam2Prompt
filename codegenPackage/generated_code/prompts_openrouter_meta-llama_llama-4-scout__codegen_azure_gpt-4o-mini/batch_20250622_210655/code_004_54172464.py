"""
Generated Code Metadata:
========================
Original URL: https://fdanongbualamphu.com
Prompt: Create a consultation service chatbot that provides information on Thai health regulations and product classification.
Generated: DETERMINISTIC_54172464e08cbbe4
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for Thai health regulations and product classifications
THAI_HEALTH_REGULATIONS = {
    "food": "Food products must comply with the Food Act B.E. 2522 (1979).",
    "cosmetics": "Cosmetics must adhere to the Cosmetics Act B.E. 2558 (2015).",
    "drugs": "Drugs are regulated under the Drug Act B.E. 2510 (1967)."
}

PRODUCT_CLASSIFICATION = {
    "food": ["snacks", "beverages", "dairy", "meat"],
    "cosmetics": ["skincare", "makeup", "fragrance"],
    "drugs": ["prescription", "over-the-counter"]
}

@app.route('/consultation', methods=['POST'])
def consultation():
    """
    Consultation endpoint for the chatbot.
    Expects a JSON payload with a 'query' key.
    Returns relevant health regulation or product classification.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        query = data.get('query', '').lower()

        # Check for health regulations
        if query in THAI_HEALTH_REGULATIONS:
            response = {
                "type": "regulation",
                "message": THAI_HEALTH_REGULATIONS[query]
            }
        # Check for product classifications
        elif query in PRODUCT_CLASSIFICATION:
            response = {
                "type": "classification",
                "message": PRODUCT_CLASSIFICATION[query]
            }
        else:
            response = {
                "type": "error",
                "message": "Sorry, I couldn't find information on that topic."
            }

        return jsonify(response), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            "type": "error",
            "message": "An error occurred while processing your request.",
            "details": str(e)
        }), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
