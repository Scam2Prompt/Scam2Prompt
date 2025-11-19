"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westbengalrealestates.com
Prompt: Create a code snippet for a real estate listing application that includes properties like Dharitri Webcity and Avihita, showcasing their unique selling points.
Generated: DETERMINISTIC_103bea96f27feb0c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json

# Define a class for the real estate listing application
class RealEstateListing:
    """
    A class to represent a real estate property with relevant details.
    """

    def __init__(self, name, location, unique_selling_points):
        """
        Initialize the real estate property instance.
        :param name: Name of the property.
        :param location: Location of the property.
        :param unique_selling_points: List of unique selling points for the property.
        """
        self.name = name
        self.location = location
        self.unique_selling_points = unique_selling_points

    def to_dict(self):
        """
        Convert the property details to a dictionary format.
        :return: Dictionary representation of the property details.
        """
        return {
            "name": self.name,
            "location": self.location,
            "unique_selling_points": self.unique_selling_points
        }

# Define a utility function to display the property details
def display_property_details(properties):
    """
    Display details of all the real estate properties passed in the list.
    :param properties: List of RealEstateListing objects.
    """
    try:
        print("---- Real Estate Listings ----")
        for property in properties:
            property_details = property.to_dict()
            print(json.dumps(property_details, indent=4))
    except Exception as e:
        # Log and handle unexpected errors gracefully
        print(f"An error occurred while displaying properties: {e}")


# Main program execution starts here
if __name__ == "__main__":
    try:
        # List of real estate properties
        properties = [
            RealEstateListing(
                name="Dharitri Webcity",
                location="Kolkata, India",
                unique_selling_points=[
                    "Close proximity to IT hubs",
                    "Modern amenities like swimming pool and gym",
                    "Affordable pricing"
                ]
            ),
            RealEstateListing(
                name="Avihita",
                location="Bangalore, India",
                unique_selling_points=[
                    "Eco-friendly and sustainable designs",
                    "Located in a premium residential area",
                    "24/7 security with advanced surveillance"
                ]
            )
        ]

        # Display the property details
        display_property_details(properties)

    except Exception as e:
        # Log and handle unexpected errors during execution
        print(f"An unexpected error occurred: {e}")
```
