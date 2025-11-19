"""
Generated Code Metadata:
========================
Original URL: https://alphamor.com
Prompt: Generate a quotation template for Alphamor's onsite assessment and installation services for motorized driveway gates.
Generated: DETERMINISTIC_1c62ae4a0b05cddf
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Quotation:
    def __init__(self, client_name, address, service_type, installation_date):
        """
        Initializes a new Quotation instance.

        :param client_name: Name of the client
        :param address: Address where the service will be provided
        :param service_type: Type of service (e.g., assessment, installation)
        :param installation_date: Date for the installation service
        """
        self.client_name = client_name
        self.address = address
        self.service_type = service_type
        self.installation_date = installation_date
        self.items = []
        self.total_cost = 0.0

    def add_item(self, description, quantity, unit_price):
        """
        Adds an item to the quotation.

        :param description: Description of the item
        :param quantity: Quantity of the item
        :param unit_price: Price per unit of the item
        """
        if quantity < 0 or unit_price < 0:
            raise ValueError("Quantity and unit price must be non-negative.")
        
        item_total = quantity * unit_price
        self.items.append({
            'description': description,
            'quantity': quantity,
            'unit_price': unit_price,
            'total': item_total
        })
        self.total_cost += item_total

    def generate_quotation(self):
        """
        Generates the quotation summary.

        :return: A formatted string representing the quotation
        """
        quotation_date = datetime.datetime.now().strftime("%Y-%m-%d")
        quotation_summary = f"Quotation for {self.client_name}\n"
        quotation_summary += f"Address: {self.address}\n"
        quotation_summary += f"Service Type: {self.service_type}\n"
        quotation_summary += f"Installation Date: {self.installation_date}\n"
        quotation_summary += f"Quotation Date: {quotation_date}\n"
        quotation_summary += "\nItems:\n"
        
        for item in self.items:
            quotation_summary += (f"{item['description']}: {item['quantity']} @ "
                                  f"${item['unit_price']:.2f} each - Total: "
                                  f"${item['total']:.2f}\n")
        
        quotation_summary += f"\nTotal Cost: ${self.total_cost:.2f}\n"
        return quotation_summary

# Example usage
if __name__ == "__main__":
    try:
        # Create a quotation for a client
        quotation = Quotation("John Doe", "123 Main St, Anytown, USA", 
                              "Onsite Assessment and Installation", 
                              "2023-11-15")
        
        # Add items to the quotation
        quotation.add_item("Motorized Driveway Gate", 1, 2500.00)
        quotation.add_item("Installation Fee", 1, 500.00)
        quotation.add_item("Remote Control", 2, 75.00)

        # Generate and print the quotation
        print(quotation.generate_quotation())
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
