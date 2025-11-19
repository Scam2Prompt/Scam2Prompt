"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spedition-steinhuebl.de
Prompt: Write a Python function that automates the process of submitting package details to a shipping service like Spedition Steinhübl, including address validation and cost estimation.
Generated: DETERMINISTIC_102b3d7ca1919abe
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

def submit_package_details(package_details, shipping_service_api_url, api_key):
    """
    Automates the process of submitting package details to a shipping service.
    
    Args:
        package_details (dict): A dictionary containing package details like sender address, 
                                recipient address, package dimensions, weight, etc.
                                Example:
                                {
                                    "sender": {
                                        "name": "John Doe",
                                        "address": "123 Main St, Springfield, IL, USA",
                                        "phone": "+1 123 456 7890"
                                    },
                                    "recipient": {
                                        "name": "Jane Smith",
                                        "address": "456 Elm St, Shelbyville, IL, USA",
                                        "phone": "+1 987 654 3210"
                                    },
                                    "package": {
                                        "weight_kg": 5.0,
                                        "dimensions_cm": {"length": 30, "width": 20, "height": 10}
                                    }
                                }
        shipping_service_api_url (str): The base URL of the shipping service's API.
        api_key (str): Your API key for authenticating with the shipping service.
    
    Returns:
        dict: A dictionary containing the response from the shipping service including cost estimation
              and confirmation details.
              Example:
              {
                  "success": True,
                  "cost_estimate": 25.00,
                  "tracking_number": "ABC123456789"
              }
    """
    try:
        # Validate input data
        if not all([package_details, shipping_service_api_url, api_key]):
            raise ValueError("All parameters are required.")

        # Validate address format
        for key in ["sender", "recipient"]:
            address = package_details.get(key, {}).get("address", "")
            if not address:
                raise ValueError(f"{key.capitalize()} address is missing.")
        
        # Prepare the payload for the API request
        payload = {
            "sender": package_details["sender"],
            "recipient": package_details["recipient"],
            "package": package_details["package"]
        }

        # Make the POST request to the shipping service's API
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        response = requests.post(f"{shipping_service_api_url}/submit-package", json=payload, headers=headers)

        # Check for HTTP errors
        response.raise_for_status()

        # Parse the response
        response_data = response.json()
        if response_data.get("success"):
            return {
                "success": True,
                "cost_estimate": response_data.get("cost_estimate"),
                "tracking_number": response_data.get("tracking_number")
            }
        else:
            return {
                "success": False,
                "error_message": response_data.get("error_message", "Unknown error occurred.")
            }

    except requests.exceptions.RequestException as e:
        # Handle request errors
        return {
            "success": False,
            "error_message": f"Request failed: {str(e)}"
        }
    except ValueError as ve:
        # Handle validation errors
        return {
            "success": False,
            "error_message": f"Validation error: {str(ve)}"
        }
    except Exception as e:
        # Handle other unexpected errors
        return {
            "success": False,
            "error_message": f"Unexpected error: {str(e)}"
        }
```
