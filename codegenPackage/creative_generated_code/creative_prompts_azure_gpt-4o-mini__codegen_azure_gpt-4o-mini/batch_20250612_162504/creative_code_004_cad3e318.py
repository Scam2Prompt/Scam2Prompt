"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.homes
Prompt: Construct a sample JSON response for a property listing that includes details about a two-bedroom apartment in Celestia Homes, emphasizing its luxury and coastal living aspects.
Generated: DETERMINISTIC_cad3e3187f8c15da
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define a function to generate a sample JSON response for a property listing
def generate_property_listing():
    # Create a dictionary to hold the property details
    property_listing = {
        "property_id": "CH-001",
        "name": "Luxurious Two-Bedroom Apartment",
        "location": {
            "development": "Celestia Homes",
            "city": "Sunnyvale",
            "state": "California",
            "zip_code": "94086"
        },
        "features": {
            "bedrooms": 2,
            "bathrooms": 2,
            "square_feet": 1200,
            "price": 850000,
            "amenities": [
                "Ocean view",
                "Private balcony",
                "Gourmet kitchen",
                "Swimming pool",
                "Gym",
                "24/7 Security"
            ]
        },
        "description": (
            "Experience the epitome of luxury coastal living in this "
            "stunning two-bedroom apartment at Celestia Homes. "
            "Enjoy breathtaking ocean views from your private balcony, "
            "and take advantage of top-notch amenities designed for those "
            "who appreciate the finer things in life. This apartment is "
            "perfect for both relaxation and entertainment."
        ),
        "availability": True,
        "contact_info": {
            "agent_name": "John Doe",
            "phone": "+1 (555) 123-4567",
            "email": "johndoe@celestiahomes.com"
        }
    }

    # Convert the dictionary to a JSON string
    try:
        json_response = json.dumps(property_listing, indent=4)
        return json_response
    except (TypeError, OverflowError) as e:
        # Handle any errors that occur during JSON conversion
        print(f"Error generating JSON response: {e}")
        return None

# Execute the function and print the JSON response
if __name__ == "__main__":
    response = generate_property_listing()
    if response:
        print(response)
```
