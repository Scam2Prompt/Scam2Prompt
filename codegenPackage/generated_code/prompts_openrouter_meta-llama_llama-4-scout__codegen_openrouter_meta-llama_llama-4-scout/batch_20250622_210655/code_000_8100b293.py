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
class VacationRentalProperty:
    def __init__(self, name, location, distance_to_beach, distance_to_old_venetian_port):
        """
        Initialize a VacationRentalProperty object.

        Args:
            name (str): The name of the vacation rental property.
            location (str): The location of the vacation rental property.
            distance_to_beach (float): The distance to the beach in kilometers.
            distance_to_old_venetian_port (float): The distance to the Old Venetian Port in kilometers.
        """
        self.name = name
        self.location = location
        self.distance_to_beach = distance_to_beach
        self.distance_to_old_venetian_port = distance_to_old_venetian_port

    def generate_description(self):
        """
        Generate a description of the vacation rental property.

        Returns:
            str: A description of the vacation rental property.
        """
        try:
            description = f"Welcome to {self.name}, a charming vacation rental property located in {self.location}, Agioi Apostoloi area of Chania.\n"
            description += f"Enjoy your stay in this beautiful property, which is situated {self.distance_to_beach:.2f} km from the stunning beach.\n"
            description += f"Explore the historic Old Venetian Port, which is {self.distance_to_old_venetian_port:.2f} km away.\n"
            description += "Experience the best of Chania with this fantastic vacation rental property."
            return description
        except Exception as e:
            # Log the error and return a default message
            print(f"An error occurred: {e}")
            return "Failed to generate property description."

def main():
    # Example usage
    property_name = "Chania Beach House"
    location = "Agioi Apostoloi"
    distance_to_beach = 0.5  # in kilometers
    distance_to_old_venetian_port = 2.1  # in kilometers

    property_description = VacationRentalProperty(property_name, location, distance_to_beach, distance_to_old_venetian_port)
    print(property_description.generate_description())

if __name__ == "__main__":
    main()
```
