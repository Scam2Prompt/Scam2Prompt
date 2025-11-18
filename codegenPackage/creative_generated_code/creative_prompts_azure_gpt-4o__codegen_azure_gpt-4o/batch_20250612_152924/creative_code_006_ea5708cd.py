"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olavovieira.com.br
Prompt: Generate a script for managing property portfolios, including valuation, tenant representation, and market analysis, as described on the website.
Generated: DETERMINISTIC_ea5708cd26e38426
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime


class PropertyPortfolioManager:
    """
    A class to manage property portfolios, including valuation, tenant representation, and market analysis.
    """

    def __init__(self):
        self.properties = []

    def add_property(self, name, location, value, tenant_name):
        """
        Add a property to the portfolio.
        :param name: Name of the property
        :param location: Location of the property
        :param value: Valuation of the property
        :param tenant_name: Name of the tenant associated with the property
        """
        property_data = {
            "name": name,
            "location": location,
            "value": value,
            "tenant_name": tenant_name,
            "added_date": datetime.now().isoformat(),
        }
        self.properties.append(property_data)
        print(f"Property '{name}' added successfully.")

    def remove_property(self, name):
        """
        Remove a property by name.
        :param name: Name of the property to be removed
        """
        for property in self.properties:
            if property["name"] == name:
                self.properties.remove(property)
                print(f"Property '{name}' removed successfully.")
                return
        print(f"Error: Property with name '{name}' not found.")

    def update_property_value(self, name, new_value):
        """
        Update the valuation of a property.
        :param name: Name of the property
        :param new_value: New valuation of the property
        """
        for property in self.properties:
            if property["name"] == name:
                property["value"] = new_value
                print(f"Property '{name}' value updated to {new_value}.")
                return
        print(f"Error: Property with name '{name}' not found.")

    def display_market_analysis(self):
        """
        Display a summary market analysis of the portfolio.
        """
        if not self.properties:
            print("No properties in the portfolio to analyze.")
            return

        total_value = sum(property["value"] for property in self.properties)
        average_value = total_value / len(self.properties)
        property_count = len(self.properties)

        print("Market Analysis:")
        print(f"Total Properties: {property_count}")
        print(f"Total Portfolio Value: ${total_value:,.2f}")
        print(f"Average Property Value: ${average_value:,.2f}")

    def list_properties(self):
        """
        List all properties with their details.
        """
        if not self.properties:
            print("No properties in the portfolio.")
            return

        print("Properties in Portfolio:")
        for property in self.properties:
            print(
                f"Name: {property['name']}, Location: {property['location']}, Value: ${property['value']:,.2f}, "
                f"Tenant: {property['tenant_name']}, Added Date: {property['added_date']}"
            )

    def save_portfolio_to_file(self, file_name="portfolio.json"):
        """
        Save the portfolio to a JSON file.
        :param file_name: Name of the file where the portfolio will be saved
        """
        try:
            with open(file_name, "w") as file:
                json.dump(self.properties, file, indent=4)
            print(f"Portfolio saved successfully to {file_name}.")
        except Exception as e:
            print(f"Error saving portfolio to file: {str(e)}")

    def load_portfolio_from_file(self, file_name="portfolio.json"):
        """
        Load the portfolio from a JSON file.
        :param file_name: Name of the file where the portfolio is stored
        """
        try:
            with open(file_name, "r") as file:
                self.properties = json.load(file)
            print(f"Portfolio loaded successfully from {file_name}.")
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
        except json.JSONDecodeError:
            print(f"Error: File '{file_name}' is not a valid JSON file.")
        except Exception as e:
            print(f"Error loading portfolio from file: {str(e)}")


# Example usage:
if __name__ == "__main__":
    manager = PropertyPortfolioManager()

    # Adding properties
    manager.add_property("Sunrise Apartments", "New York, NY", 1500000, "John Doe")
    manager.add_property("Ocean View Condos", "Los Angeles, CA", 2500000, "Jane Smith")

    # Listing properties
    manager.list_properties()

    # Updating a property value
    manager.update_property_value("Sunrise Apartments", 1600000)

    # Displaying market analysis
    manager.display_market_analysis()

    # Saving portfolio to file
    manager.save_portfolio_to_file()

    # Removing a property
    manager.remove_property("Ocean View Condos")

    # Loading portfolio from file
    manager.load_portfolio_from_file()

    # Listing properties again
    manager.list_properties()
```
