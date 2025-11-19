"""
Generated Code Metadata:
========================
Original URL: https://celestia.homes
Prompt: Construct a sample JSON response for a property listing that includes details about a two-bedroom apartment in Celestia Homes, emphasizing its luxury and coastal living aspects.
Generated: DETERMINISTIC_cad3e3187f8c15da
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def generate_property_listing():
    """
    Generate a sample JSON response for a luxury property listing.

    Returns:
        str: A JSON string representing the property listing.
    """

    # Define the property listing details
    property_listing = {
        "listingId": "CLST-001",
        "propertyType": "Apartment",
        "numBedrooms": 2,
        "numBathrooms": 2,
        "squareFootage": 1200,
        "location": {
            "community": "Celestia Homes",
            "city": "Coastal City",
            "state": "CA",
            "zipCode": "90210"
        },
        "amenities": [
            "Private Balcony with Ocean View",
            "Hardwood Flooring",
            "High-End Appliances",
            "Resort-Style Pool",
            "24/7 Security"
        ],
        "features": {
            "view": "Ocean Front",
            "orientation": "West",
            "floor": 10,
            "totalFloors": 20
        },
        "price": {
            "amount": 1250000,
            "currency": "USD"
        },
        "description": "Luxury two-bedroom apartment in Celestia Homes, offering stunning coastal living with top-notch amenities and breathtaking ocean views.",
        "agent": {
            "name": "John Doe",
            "email": "john.doe@realestate.com",
            "phone": "+1 555 123 4567"
        }
    }

    try:
        # Convert the property listing to a JSON string
        json_response = json.dumps(property_listing, indent=4)
        return json_response
    except TypeError as e:
        # Handle any errors during JSON conversion
        print(f"Error generating JSON response: {e}")
        return None

# Example usage
if __name__ == "__main__":
    json_response = generate_property_listing()
    if json_response:
        print(json_response)
```
