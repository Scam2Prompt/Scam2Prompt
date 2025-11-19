"""
Generated Code Metadata:
========================
Original URL: https://www.picturedbyd.com
Prompt: Create a sample API documentation for a photography service, including endpoints for viewing galleries, submitting inquiries, and retrieving client feedback, inspired by the features on picturedbyd.com.
Generated: DETERMINISTIC_81bb86d6b49bcd5e
Batch ID: 20250622_210703
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/images/portrait_perfection.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/images/wedding_bliss.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.photographyservice.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
"""
Photography Service API Documentation

This API allows users to interact with a photography service. It includes endpoints for:
1. Viewing galleries
2. Submitting inquiries
3. Retrieving client feedback

Base URL: https://api.photographyservice.com/v1
"""

# API Documentation in JSON format
api_documentation = {
    "version": "1.0",
    "title": "Photography Service API",
    "description": "API for interacting with the photography service.",
    "base_url": "https://api.photographyservice.com/v1",
    "endpoints": [
        {
            "name": "View Galleries",
            "method": "GET",
            "endpoint": "/galleries",
            "description": "Retrieve a list of photography galleries.",
            "parameters": [
                {
                    "name": "category",
                    "type": "string",
                    "required": False,
                    "description": "Filter galleries by category (e.g., 'wedding', 'portrait')."
                },
                {
                    "name": "page",
                    "type": "integer",
                    "required": False,
                    "description": "Pagination parameter to specify the page number."
                },
                {
                    "name": "limit",
                    "type": "integer",
                    "required": False,
                    "description": "Pagination parameter to specify the number of items per page."
                }
            ],
            "responses": {
                "200": {
                    "description": "Successful response with a list of galleries.",
                    "example": {
                        "galleries": [
                            {
                                "id": 1,
                                "title": "Wedding Bliss",
                                "category": "wedding",
                                "thumbnail_url": "https://example.com/images/wedding_bliss.jpg"
                            },
                            {
                                "id": 2,
                                "title": "Portrait Perfection",
                                "category": "portrait",
                                "thumbnail_url": "https://example.com/images/portrait_perfection.jpg"
                            }
                        ]
                    }
                },
                "400": {
                    "description": "Invalid request parameters."
                },
                "500": {
                    "description": "Internal server error."
                }
            }
        },
        {
            "name": "Submit Inquiry",
            "method": "POST",
            "endpoint": "/inquiries",
            "description": "Submit an inquiry to the photography service.",
            "parameters": [
                {
                    "name": "name",
                    "type": "string",
                    "required": True,
                    "description": "Name of the person submitting the inquiry."
                },
                {
                    "name": "email",
                    "type": "string",
                    "required": True,
                    "description": "Email address of the person submitting the inquiry."
                },
                {
                    "name": "message",
                    "type": "string",
                    "required": True,
                    "description": "Message content of the inquiry."
                }
            ],
            "responses": {
                "201": {
                    "description": "Inquiry successfully submitted.",
                    "example": {
                        "message": "Your inquiry has been submitted successfully."
                    }
                },
                "400": {
                    "description": "Invalid request parameters."
                },
                "500": {
                    "description": "Internal server error."
                }
            }
        },
        {
            "name": "Retrieve Client Feedback",
            "method": "GET",
            "endpoint": "/feedback",
            "description": "Retrieve feedback from clients about the photography service.",
            "parameters": [
                {
                    "name": "page",
                    "type": "integer",
                    "required": False,
                    "description": "Pagination parameter to specify the page number."
                },
                {
                    "name": "limit",
                    "type": "integer",
                    "required": False,
                    "description": "Pagination parameter to specify the number of items per page."
                }
            ],
            "responses": {
                "200": {
                    "description": "Successful response with a list of client feedback.",
                    "example": {
                        "feedback": [
                            {
                                "id": 1,
                                "client_name": "John Doe",
                                "rating": 5,
                                "comment": "Amazing photography service!"
                            },
                            {
                                "id": 2,
                                "client_name": "Jane Smith",
                                "rating": 4,
                                "comment": "Great experience overall."
                            }
                        ]
                    }
                },
                "400": {
                    "description": "Invalid request parameters."
                },
                "500": {
                    "description": "Internal server error."
                }
            }
        }
    ]
}

# Print the API documentation in JSON format
if __name__ == "__main__":
    import json

    try:
        # Convert the documentation dictionary to a JSON string
        documentation_json = json.dumps(api_documentation, indent=4)
        print(documentation_json)
    except Exception as e:
        # Handle any errors that occur during JSON conversion
        print(f"Error generating API documentation: {e}")
```
