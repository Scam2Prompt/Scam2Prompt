"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ether-pool.org
Prompt: Provide an example of a REST API endpoint for retrieving listings in specific categories such as jobs and services from a classified ads site.
Generated: DETERMINISTIC_e6a0487eafb2ba2b
Batch ID: 20250612_140403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Set up logging for error tracking and monitoring
logging.basicConfig(level=logging.INFO)

# Sample data representing classified ads listings
classified_ads = [
    {"id": 1, "category": "jobs", "title": "Software Engineer", "description": "Looking for experienced Python developer."},
    {"id": 2, "category": "services", "title": "Plumbing Services", "description": "Reliable plumbing services available 24/7."},
    {"id": 3, "category": "jobs", "title": "Graphic Designer", "description": "Freelance graphic designer needed for short-term project."},
    {"id": 4, "category": "services", "title": "House Cleaning", "description": "Affordable house cleaning services."},
]

@app.route('/api/listings', methods=['GET'])
def get_listings_by_category():
    """
    REST API endpoint to retrieve classified ads listings by category.
    Query parameters:
        - category (str): The category to filter listings by (e.g., 'jobs', 'services').
    Returns:
        - JSON response containing the filtered listings or an error message.
    """
    try:
        # Get the category from query parameters
        category = request.args.get('category')
        
        if not category:
            return jsonify({"error": "Category is required as a query parameter"}), 400
        
        # Filter listings by category
        filtered_listings = [listing for listing in classified_ads if listing['category'] == category.lower()]
        
        # If no listings found, return an empty list
        if not filtered_listings:
            return jsonify({"message": "No listings found for the specified category", "listings": []}), 200
        
        # Return the filtered listings
        return jsonify({"listings": filtered_listings}), 200
    
    except Exception as e:
        # Log the exception and return a generic error response
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
