"""
Generated Code Metadata:
========================
Original URL: https://zealy.gg
Prompt: "Generate documentation for a community platform API, including endpoints for creating, reading, updating, and deleting community information."
Generated: DETERMINISTIC_0abdf17817c6c846
Batch ID: 20250622_211330
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Community Platform API Documentation Generator

This script generates documentation for a community platform API, including endpoints for
creating, reading, updating, and deleting community information.

Endpoints:
1. POST /api/communities - Create a new community
2. GET /api/communities/{id} - Retrieve community information by ID
3. PUT /api/communities/{id} - Update community information by ID
4. DELETE /api/communities/{id} - Delete a community by ID
"""

import json

def generate_api_documentation():
    """
    Generates API documentation for the community platform.

    Returns:
        str: JSON-formatted API documentation.
    """
    try:
        # Define the API documentation structure
        api_documentation = {
            "title": "Community Platform API",
            "version": "1.0",
            "description": "API for managing community information.",
            "endpoints": [
                {
                    "method": "POST",
                    "endpoint": "/api/communities",
                    "description": "Create a new community.",
                    "parameters": [
                        {"name": "name", "type": "string", "required": True, "description": "Name of the community."},
                        {"name": "description", "type": "string", "required": False, "description": "Description of the community."}
                    ],
                    "responses": {
                        "201": "Community created successfully.",
                        "400": "Invalid input data."
                    }
                },
                {
                    "method": "GET",
                    "endpoint": "/api/communities/{id}",
                    "description": "Retrieve community information by ID.",
                    "parameters": [
                        {"name": "id", "type": "string", "required": True, "description": "Unique identifier of the community."}
                    ],
                    "responses": {
                        "200": "Community information retrieved successfully.",
                        "404": "Community not found."
                    }
                },
                {
                    "method": "PUT",
                    "endpoint": "/api/communities/{id}",
                    "description": "Update community information by ID.",
                    "parameters": [
                        {"name": "id", "type": "string", "required": True, "description": "Unique identifier of the community."},
                        {"name": "name", "type": "string", "required": False, "description": "Updated name of the community."},
                        {"name": "description", "type": "string", "required": False, "description": "Updated description of the community."}
                    ],
                    "responses": {
                        "200": "Community updated successfully.",
                        "400": "Invalid input data.",
                        "404": "Community not found."
                    }
                },
                {
                    "method": "DELETE",
                    "endpoint": "/api/communities/{id}",
                    "description": "Delete a community by ID.",
                    "parameters": [
                        {"name": "id", "type": "string", "required": True, "description": "Unique identifier of the community."}
                    ],
                    "responses": {
                        "200": "Community deleted successfully.",
                        "404": "Community not found."
                    }
                }
            ]
        }

        # Convert the documentation to JSON format
        return json.dumps(api_documentation, indent=4)

    except Exception as e:
        # Handle unexpected errors
        return json.dumps({"error": f"Failed to generate API documentation: {str(e)}"})

# Generate and print the API documentation
if __name__ == "__main__":
    documentation = generate_api_documentation()
    print(documentation)
```
