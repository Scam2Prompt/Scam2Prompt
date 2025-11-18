"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shishehbalkon.ir
Prompt: Create a program that generates a detailed invoice for glass installation services, including options for balcony glass, shower cabins, and sliding glass doors, based on the specifications provided on the website.
Generated: DETERMINISTIC_1769e0e5078dbf25
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Invoice:
    """
    A class to represent an invoice for glass installation services.
    """

    def __init__(self, customer_name, customer_address, services):
        """
        Initializes the invoice with customer details and requested services.

        :param customer_name: str - Name of the customer
        :param customer_address: str - Address of the customer
        :param services: list - List of services requested
        """
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.services = services
        self.total_amount = 0

    def calculate_total(self):
        """
        Calculates the total amount for the requested services.
        """
        for service in self.services:
            self.total_amount += service['price']
    
    def generate_invoice(self):
        """
        Generates the invoice as a formatted string.
        
        :return: str - Formatted invoice details
        """
        invoice_details = f"Invoice for {self.customer_name}\n"
        invoice_details += f"Address: {self.customer_address}\n"
        invoice_details += "Services:\n"
        
        for service in self.services:
            invoice_details += f"- {service['description']}: ${service['price']:.2f}\n"
        
        invoice_details += f"Total Amount: ${self.total_amount:.2f}\n"
        return invoice_details


def load_services_from_json(file_path):
    """
    Loads service options from a JSON file.

    :param file_path: str - Path to the JSON file
    :return: list - List of services
    """
    try:
        with open(file_path, 'r') as file:
            services = json.load(file)
            return services
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: The JSON file is not well formatted.")
        return []


def main():
    # Load available services from a JSON file
    services = load_services_from_json('services.json')

    # Example customer details (In production, these would come from user input)
    customer_name = "John Doe"
    customer_address = "123 Main St, Anytown, USA"

    # Filter the services based on user selections
    selected_services = [
        service for service in services
        if service['selected']  # Assuming the JSON has a 'selected' key
    ]

    # Create an invoice object
    invoice = Invoice(customer_name, customer_address, selected_services)
    
    # Calculate total amount for the invoice
    invoice.calculate_total()

    # Generate and print the invoice
    print(invoice.generate_invoice())


if __name__ == "__main__":
    main()
```

### Example JSON Structure (`services.json`):
```json
[
    {
        "description": "Balcony Glass Installation",
        "price": 500,
        "selected": true
    },
    {
        "description": "Shower Cabin Installation",
        "price": 300,
        "selected": false
    },
    {
        "description": "Sliding Glass Door Installation",
        "price": 700,
        "selected": true
    }
]
```

### Note:
Make sure to create a `services.json` file with the provided structure in the same directory as the Python script for it to run successfully.
