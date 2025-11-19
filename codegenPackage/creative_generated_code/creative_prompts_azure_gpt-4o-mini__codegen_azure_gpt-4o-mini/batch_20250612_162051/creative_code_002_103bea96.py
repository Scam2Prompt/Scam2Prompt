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
# real_estate_listing.py

class Property:
    """
    A class to represent a real estate property.
    """

    def __init__(self, name, location, price, features):
        """
        Initializes the Property instance.

        :param name: str - The name of the property
        :param location: str - The location of the property
        :param price: float - The price of the property
        :param features: list - A list of unique selling points of the property
        """
        self.name = name
        self.location = location
        self.price = price
        self.features = features

    def display_info(self):
        """
        Displays the information of the property.
        """
        try:
            print(f"Property Name: {self.name}")
            print(f"Location: {self.location}")
            print(f"Price: ${self.price:,.2f}")
            print("Features:")
            for feature in self.features:
                print(f"- {feature}")
        except Exception as e:
            print(f"Error displaying property info: {e}")

def create_properties():
    """
    Creates a list of properties and displays their information.
    """
    properties = [
        Property(
            name="Dharitri Webcity",
            location="Sector 91, Mohali",
            price=7500000,
            features=[
                "Modern architecture",
                "Eco-friendly design",
                "Smart home technology",
                "Close to major IT parks",
                "Amenities like clubhouse and swimming pool"
            ]
        ),
        Property(
            name="Avihita",
            location="Sector 33, Chandigarh",
            price=9000000,
            features=[
                "Luxury living spaces",
                "Stunning views of the city",
                "Nearby schools and hospitals",
                "High-end security systems",
                "Well-connected transport links"
            ]
        )
    ]

    for property in properties:
        property.display_info()
        print("\n" + "="*40 + "\n")  # Separator for readability

if __name__ == "__main__":
    # Entry point of the application
    create_properties()
```
