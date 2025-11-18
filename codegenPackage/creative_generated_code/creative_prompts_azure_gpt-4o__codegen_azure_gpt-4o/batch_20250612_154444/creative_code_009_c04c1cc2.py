"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beboldproperties.com
Prompt: Develop a system to track and optimize property management costs, focusing on ethical and cost-effective service delivery, as Bebold Properties emphasizes.
Generated: DETERMINISTIC_c04c1cc2618363f9
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class PropertyManagementSystem:
    """
    A system to track and optimize property management costs,
    focusing on ethical and cost-effective service delivery.
    """

    def __init__(self):
        # Initialize an empty list to store property data
        self.properties = []

    def add_property(self, property_id, name, address, management_cost):
        """
        Adds a new property to the system.

        :param property_id: Unique identifier for the property
        :param name: Name of the property
        :param address: Address of the property
        :param management_cost: Monthly management cost of the property
        """
        try:
            new_property = {
                "property_id": property_id,
                "name": name,
                "address": address,
                "management_cost": management_cost,
            }
            self.properties.append(new_property)
            print(f"Property '{name}' added successfully!")
        except Exception as e:
            print(f"Error adding property: {e}")

    def update_management_cost(self, property_id, new_cost):
        """
        Updates the management cost for a specific property.

        :param property_id: Unique identifier for the property
        :param new_cost: Updated monthly management cost
        """
        try:
            for property in self.properties:
                if property["property_id"] == property_id:
                    property["management_cost"] = new_cost
                    print(f"Management cost updated for property '{property_id}'.")
                    return
            print(f"Property with ID '{property_id}' not found.")
        except Exception as e:
            print(f"Error updating management cost: {e}")

    def calculate_total_cost(self):
        """
        Calculates the total monthly management cost for all properties.

        :return: Total monthly cost
        """
        try:
            total_cost = sum(property["management_cost"] for property in self.properties)
            return total_cost
        except Exception as e:
            print(f"Error calculating total cost: {e}")
            return 0

    def save_to_file(self, filename):
        """
        Saves the property data to a file in JSON format.

        :param filename: Name of the file to save the data
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.properties, file, indent=4)
            print(f"Data saved to file '{filename}' successfully.")
        except Exception as e:
            print(f"Error saving data to file: {e}")

    def load_from_file(self, filename):
        """
        Loads property data from a file in JSON format.

        :param filename: Name of the file to load the data from
        """
        try:
            with open(filename, "r") as file:
                self.properties = json.load(file)
            print(f"Data loaded from file '{filename}' successfully.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file '{filename}'.")
        except Exception as e:
            print(f"Error loading data from file: {e}")


# Example usage:
if __name__ == "__main__":
    # Initialize the property management system
    system = PropertyManagementSystem()

    # Add some properties
    system.add_property(1, "Green Acres", "123 Elm Street", 1500)
    system.add_property(2, "Sunny Lodge", "456 Oak Street", 1200)

    # Update the cost of a property
    system.update_management_cost(1, 1600)

    # Calculate total monthly costs
    total_cost = system.calculate_total_cost()
    print(f"Total monthly management cost: ${total_cost}")

    # Save the data to a file
    system.save_to_file("properties.json")

    # Load data from a file
    system.load_from_file("properties.json")
```
