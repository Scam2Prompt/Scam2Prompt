"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freelistingaustralia.com
Prompt: Create a REST API in Flask that allows users to submit business listings to FreeListingAustralia and retrieve featured listings by category.
Generated: DETERMINISTIC_165433d19266f8df
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory datastore
business_listings = []
featured_listings = {
    "restaurants": [],
    "retail": [],
    "services": [],
    "others": []
}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "description": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "description": str(e)
    }), 500

# Submit a business listing
@app.route('/api/business-listings', methods=['POST'])
def submit_business_listing():
    data = request.json
    if not data:
        return jsonify({"error": "Invalid request", "description": "Request body is required"}), 400
    
    # Validate required fields
    required_fields = ["name", "category", "description"]
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({
            "error": "Invalid request",
            "description": f"Missing fields: {', '.join(missing_fields)}"
        }), 400

    # Add the business listing
    new_listing = {
        "name": data["name"],
        "category": data["category"],
        "description": data["description"]
    }
    business_listings.append(new_listing)
    return jsonify({"message": "Business listing submitted successfully", "listing": new_listing}), 201

# Retrieve featured listings by category
@app.route('/api/featured-listings/<category>', methods=['GET'])
def get_featured_listings(category):
    if category not in featured_listings:
        return jsonify({
            "error": "Invalid category",
            "description": f"Category '{category}' not found"
        }), 404
    
    return jsonify({
        "category": category,
        "featured_listings": featured_listings[category]
    }), 200

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK"}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
