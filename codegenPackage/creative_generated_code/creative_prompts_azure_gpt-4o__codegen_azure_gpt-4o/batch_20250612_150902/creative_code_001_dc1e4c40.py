"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancerfi.airlst-pages.app
Prompt: Create a script that models customer experience design principles discussed in the Balancer.Fi workshop, focusing on understanding customer needs and preferences.
Generated: DETERMINISTIC_dc1e4c400e36c0c7
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class CustomerExperienceModel:
    """
    A class to model customer experience design principles.
    This includes capturing customer needs and preferences.
    """

    def __init__(self):
        # Initialize a dictionary to store customer data
        self.customer_data = {}

    def add_customer(self, customer_id, name, preferences):
        """
        Adds a new customer to the model.

        :param customer_id: Unique identifier for the customer (str)
        :param name: Name of the customer (str)
        :param preferences: Dictionary of customer preferences (dict)
        """
        if not isinstance(preferences, dict):
            raise ValueError("Preferences must be a dictionary.")

        self.customer_data[customer_id] = {
            "name": name,
            "preferences": preferences
        }

    def update_preferences(self, customer_id, new_preferences):
        """
        Updates the preferences for an existing customer.

        :param customer_id: Unique identifier for the customer (str)
        :param new_preferences: Dictionary of new customer preferences (dict)
        """
        if customer_id not in self.customer_data:
            raise KeyError(f"Customer with ID {customer_id} not found.")

        if not isinstance(new_preferences, dict):
            raise ValueError("New preferences must be a dictionary.")

        # Merge the old and new preferences
        self.customer_data[customer_id]["preferences"].update(new_preferences)

    def get_customer_preferences(self, customer_id):
        """
        Retrieves preferences for a specific customer.

        :param customer_id: Unique identifier for the customer (str)
        :return: Dictionary of customer preferences
        """
        if customer_id not in self.customer_data:
            raise KeyError(f"Customer with ID {customer_id} not found.")

        return self.customer_data[customer_id]["preferences"]

    def export_data(self, filename):
        """
        Exports all customer data to a JSON file.

        :param filename: Name of the file to save data (str)
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.customer_data, file, indent=4)
        except IOError as e:
            raise IOError(f"Error writing to file {filename}: {e}")

    def import_data(self, filename):
        """
        Imports customer data from a JSON file.

        :param filename: Name of the file to read data from (str)
        """
        try:
            with open(filename, 'r') as file:
                self.customer_data = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {filename} does not exist.")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON from file {filename}: {e}")


# Example usage
if __name__ == "__main__":
    # Create an instance of the CustomerExperienceModel
    cx_model = CustomerExperienceModel()

    # Add a few customers
    cx_model.add_customer(
        customer_id="001",
        name="Alice",
        preferences={"likes": "low fees", "dislikes": "complex interfaces"}
    )
    cx_model.add_customer(
        customer_id="002",
        name="Bob",
        preferences={"likes": "high APY", "dislikes": "slow transactions"}
    )

    # Update preferences for Alice
    cx_model.update_preferences(
        customer_id="001",
        new_preferences={"likes": "transparent pricing"}
    )

    # Retrieve and print preferences for Bob
    bob_preferences = cx_model.get_customer_preferences("002")
    print("Bob's Preferences:", bob_preferences)

    # Export data to a JSON file
    cx_model.export_data("customer_data.json")

    # Create a new instance to demonstrate importing data
    new_cx_model = CustomerExperienceModel()
    new_cx_model.import_data("customer_data.json")
    print("Imported Data:", new_cx_model.customer_data)
```
