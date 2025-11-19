"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://natureexcursionsafaris.com
Prompt: Develop a RESTful API endpoint that retrieves information about different safari experiences in Tanzania, including mid-range and luxury options, and formats the data for a mobile app.
Generated: DETERMINISTIC_ca102ea597463df8
Batch ID: 20250612_164122
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

# Initialize Flask app
app = Flask(__name__)

# Logging configuration
logging.basicConfig(level=logging.INFO)

# Sample data for safari experiences
safari_experiences = [
    {
        "id": 1,
        "name": "Serengeti Luxury Safari",
        "type": "Luxury",
        "description": "Immerse yourself in the wildlife of Serengeti in a premium lodge.",
        "price_per_person": 3500,
        "duration_days": 7
    },
    {
        "id": 2,
        "name": "Ngorongoro Mid-Range Safari",
        "type": "Mid-Range",
        "description": "Explore the Ngorongoro Crater with affordable yet comfortable options.",
        "price_per_person": 1500,
        "duration_days": 5
    },
    {
        "id": 3,
        "name": "Tarangire Luxury Safari",
        "type": "Luxury",
        "description": "Discover the unique flora and fauna of Tarangire with a high-end experience.",
        "price_per_person": 3200,
        "duration_days": 6
    },
    {
        "id": 4,
        "name": "Lake Manyara Budget Safari",
        "type": "Budget",
        "description": "Experience Lake Manyara's beauty on a budget-friendly safari.",
        "price_per_person": 800,
        "duration_days": 3
    }
]

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Route to retrieve safari experiences
@app.route('/api/safaris', methods=['GET'])
def get_safari_experiences():
    """
    Endpoint to retrieve safari experiences.
    Supports optional filtering by type (Luxury, Mid-Range, Budget).
    """
    try:
        # Optional filter: type
        safari_type = request.args.get('type', None)
        if safari_type:
            # Filter safari experiences by type
            filtered_experiences = [
                safari for safari in safari_experiences if safari['type'].lower() == safari_type.lower()
            ]
            return jsonify(filtered_experiences), 200
        
        # Return all safari experiences if no filter applied
        return jsonify(safari_experiences), 200

    except Exception as e:
        # Log any unexpected errors
        logging.error(f"Error retrieving safari experiences: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
