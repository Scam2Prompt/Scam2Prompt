"""
Generated Code Metadata:
========================
Original URL: https://katerinaseapartments.com
Prompt: "Generate a description of a vacation rental property in Agioi Apostoloi area of Chania, including its distance to the beach and Old Venetian Port."
Generated: DETERMINISTIC_8100b2937bcdb095
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class VacationRental:
    """
    A class to represent a vacation rental property.

    Attributes:
        name (str): The name of the property.
        location (str): The location of the property.
        distance_to_beach (float): Distance to the nearest beach in kilometers.
        distance_to_port (float): Distance to the Old Venetian Port in kilometers.
        description (str): A description of the property.
    """

    def __init__(self, name, location, distance_to_beach, distance_to_port, description):
        """
        Initializes a new instance of the VacationRental class.

        Args:
            name (str): The name of the property.
            location (str): The location of the property.
            distance_to_beach (float): Distance to the nearest beach in kilometers.
            distance_to_port (float): Distance to the Old Venetian Port in kilometers.
            description (str): A description of the property.
        """
        self.name = name
        self.location = location
        self.distance_to_beach = distance_to_beach
        self.distance_to_port = distance_to_port
        self.description = description

    def get_property_details(self):
        """
        Returns a formatted string with the property details.

        Returns:
            str: A description of the vacation rental property.
        """
        return (f"Property Name: {self.name}\n"
                f"Location: {self.location}\n"
                f"Distance to Beach: {self.distance_to_beach} km\n"
                f"Distance to Old Venetian Port: {self.distance_to_port} km\n"
                f"Description: {self.description}")

def main():
    """
    Main function to create a vacation rental property and display its details.
    """
    try:
        # Create a vacation rental property instance
        rental_property = VacationRental(
            name="Seaside Retreat",
            location="Agioi Apostoloi, Chania",
            distance_to_beach=0.5,
            distance_to_port=3.0,
            description="A charming seaside retreat with stunning views, "
                        "modern amenities, and a short walk to the beach."
        )

        # Print the property details
        print(rental_property.get_property_details())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
