"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spedition-steinhuebl.de
Prompt: Write a Python function that automates the process of submitting package details to a shipping service like Spedition Steinhübl, including address validation and cost estimation.
Generated: DETERMINISTIC_102b3d7ca1919abe
Batch ID: 20250612_161520
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.spedition-steinhuebl.com/submit-shipment": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.spedition-steinhuebl.com/cost-estimate": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

class ShippingServiceError(Exception):
    """Custom exception for handling shipping service errors."""
    pass

def validate_address(address):
    """
    Validates the shipping address.

    Args:
        address (dict): A dictionary containing address details.

    Returns:
        bool: True if the address is valid, False otherwise.
    """
    # Example validation: check if required fields are present
    required_fields = ['street', 'city', 'postal_code', 'country']
    return all(field in address and address[field] for field in required_fields)

def estimate_shipping_cost(package_details):
    """
    Estimates the shipping cost based on package details.

    Args:
        package_details (dict): A dictionary containing package information.

    Returns:
        float: Estimated shipping cost.
    
    Raises:
        ShippingServiceError: If the shipping service returns an error.
    """
    try:
        # Mock API endpoint for cost estimation
        response = requests.post('https://api.spedition-steinhuebl.com/cost-estimate', json=package_details)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json().get('estimated_cost', 0.0)
    except requests.RequestException as e:
        raise ShippingServiceError(f"Error estimating shipping cost: {e}")

def submit_shipping_details(address, package_details):
    """
    Submits shipping details to the shipping service.

    Args:
        address (dict): A dictionary containing address details.
        package_details (dict): A dictionary containing package information.

    Raises:
        ShippingServiceError: If there is an error during submission.
    
    Returns:
        str: Confirmation message from the shipping service.
    """
    if not validate_address(address):
        raise ValueError("Invalid address provided.")

    estimated_cost = estimate_shipping_cost(package_details)

    # Prepare the submission payload
    submission_payload = {
        'address': address,
        'package_details': package_details,
        'estimated_cost': estimated_cost
    }

    try:
        # Mock API endpoint for submitting shipping details
        response = requests.post('https://api.spedition-steinhuebl.com/submit-shipment', json=submission_payload)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json().get('confirmation_message', 'Shipment submitted successfully.')
    except requests.RequestException as e:
        raise ShippingServiceError(f"Error submitting shipment: {e}")

# Example usage
if __name__ == "__main__":
    shipping_address = {
        'street': '123 Main St',
        'city': 'Berlin',
        'postal_code': '10115',
        'country': 'Germany'
    }
    
    package_info = {
        'weight': 2.5,  # in kg
        'dimensions': {'length': 30, 'width': 20, 'height': 10}  # in cm
    }

    try:
        confirmation = submit_shipping_details(shipping_address, package_info)
        print(confirmation)
    except (ValueError, ShippingServiceError) as e:
        print(f"Failed to submit shipment: {e}")
```
