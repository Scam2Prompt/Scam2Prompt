"""
Generated Code Metadata:
========================
Original URL: https://westbengalrealestates.com
Prompt: Create a code snippet for a real estate listing application that includes properties like Dharitri Webcity and Avihita, showcasing their unique selling points.
Generated: DETERMINISTIC_103bea96f27feb0c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Property:
    """
    A class to represent a real estate property listing.
    
    Attributes:
        name (str): Name of the property.
        location (str): Location of the property.
        unique_selling_points (list): List of unique selling points.
        price (float): Price of the property.
    """
    
    def __init__(self, name, location, unique_selling_points, price):
        """
        Initialize a Property instance.
        
        Args:
            name (str): Name of the property.
            location (str): Location of the property.
            unique_selling_points (list): List of unique selling points.
            price (float): Price of the property.
        """
        self.name = name
        self.location = location
        self.unique_selling_points = unique_selling_points
        self.price = price
    
    def display_property(self):
        """
        Display the property details in a formatted manner.
        """
        print(f"\nProperty Name: {self.name}")
        print(f"Location: {self.location}")
        print("Unique Selling Points:")
        for usp in self.unique_selling_points:
            print(f"- {usp}")
        print(f"Price: ${self.price:,.2f}\n")


def main():
    """
    Main function to create and display property listings.
    """
    try:
        # Create property listings
        dharitri_webcity = Property(
            name="Dharitri Webcity",
            location="Tech Hub District",
            unique_selling_points=[
                "Fiber-optic internet ready",
                "Smart home automation",
                "Co-working spaces included",
                "Green building certified"
            ],
            price=450000.00
        )
        
        avihita = Property(
            name="Avihita",
            location="Lakeside Residences",
            unique_selling_points=[
                "Waterfront views",
                "Private boat docks",
                "Luxury spa and wellness center",
                "24/7 concierge service"
            ],
            price=750000.00
        )
        
        # Display property listings
        print("Real Estate Listings:")
        dharitri_webcity.display_property()
        avihita.display_property()
        
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
