"""
Generated Code Metadata:
========================
Original URL: https://viregocx.amecoe.com
Prompt: Generate a concise API documentation for a service that allows florists to create unique gift offerings, highlighting key features and customer testimonials.
Generated: DETERMINISTIC_c5d6dfc0ab1afd7f
Batch ID: 20250612_140436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database for storing gift offerings and testimonials
gift_offerings = []
testimonials = []

# API Documentation
api_documentation = {
    "title": "Florist Gift Offering API",
    "description": "An API service for florists to create unique gift offerings and manage customer testimonials.",
    "endpoints": [
        {
            "path": "/api/gift-offerings",
            "method": "POST",
            "description": "Create a new gift offering.",
            "parameters": {
                "name": "string (required)",
                "description": "string (required)",
                "price": "float (required)"
            },
            "response": {
                "status": 201,
                "body": {
                    "message": "Gift offering created successfully.",
                    "gift_offering": {
                        "id": "integer",
                        "name": "string",
                        "description": "string",
                        "price": "float"
                    }
                }
            }
        },
        {
            "path": "/api/gift-offerings",
            "method": "GET",
            "description": "Retrieve all gift offerings.",
            "response": {
                "status": 200,
                "body": {
                    "gift_offerings": [
                        {
                            "id": "integer",
                            "name": "string",
                            "description": "string",
                            "price": "float"
                        }
                    ]
                }
            }
        },
        {
            "path": "/api/testimonials",
            "method": "POST",
            "description": "Add a customer testimonial.",
            "parameters": {
                "name": "string (required)",
                "testimonial": "string (required)"
            },
            "response": {
                "status": 201,
                "body": {
                    "message": "Testimonial added successfully.",
                    "testimonial": {
                        "id": "integer",
                        "name": "string",
                        "testimonial": "string"
                    }
                }
            }
        },
        {
            "path": "/api/testimonials",
            "method": "GET",
            "description": "Retrieve all customer testimonials.",
            "response": {
                "status": 200,
                "body": {
                    "testimonials": [
                        {
                            "id": "integer",
                            "name": "string",
                            "testimonial": "string"
                        }
                    ]
                }
            }
        }
    ]
}

@app.route('/api/documentation', methods=['GET'])
def get_documentation():
    """
    Endpoint to retrieve API documentation.
    """
    return jsonify(api_documentation), 200

@app.route('/api/gift-offerings', methods=['POST'])
def create_gift_offering():
    """
    Endpoint to create a new gift offering.
    """
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')

        # Validate input
        if not name or not description or not price:
            return jsonify({"error": "Missing required fields"}), 400

        # Create new gift offering
        gift_offering = {
            "id": len(gift_offerings) + 1,
            "name": name,
            "description": description,
            "price": price
        }
        gift_offerings.append(gift_offering)
        return jsonify({"message": "Gift offering created successfully.", "gift_offering": gift_offering}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/gift-offerings', methods=['GET'])
def get_gift_offerings():
    """
    Endpoint to retrieve all gift offerings.
    """
    return jsonify({"gift_offerings": gift_offerings}), 200

@app.route('/api/testimonials', methods=['POST'])
def add_testimonial():
    """
    Endpoint to add a customer testimonial.
    """
    try:
        data = request.get_json()
        name = data.get('name')
        testimonial = data.get('testimonial')

        # Validate input
        if not name or not testimonial:
            return jsonify({"error": "Missing required fields"}), 400

        # Add new testimonial
        new_testimonial = {
            "id": len(testimonials) + 1,
            "name": name,
            "testimonial": testimonial
        }
        testimonials.append(new_testimonial)
        return jsonify({"message": "Testimonial added successfully.", "testimonial": new_testimonial}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/testimonials', methods=['GET'])
def get_testimonials():
    """
    Endpoint to retrieve all customer testimonials.
    """
    return jsonify({"testimonials": testimonials}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
