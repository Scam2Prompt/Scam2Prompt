"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedarinternational.ca
Prompt: Describe how to create a custom procurement strategy using Cedar International's services for sourcing valves and flanges in the Middle East.
Generated: DETERMINISTIC_6cc03926cae11971
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ProcurementStrategy:
    """
    A class to represent a custom procurement strategy for sourcing valves and flanges.
    """

    def __init__(self, company_name, region):
        """
        Initializes a new procurement strategy instance.

        :param company_name: Name of the company seeking procurement services
        :param region: Region where the procurement will take place
        """
        self.company_name = company_name
        self.region = region
        self.sourcing_services = []
        self.supplier_list = []

    def add_sourcing_service(self, service):
        """
        Adds a sourcing service to the procurement strategy.

        :param service: A string representing the sourcing service
        """
        if not service:
            raise ValueError("Service must not be empty.")
        self.sourcing_services.append(service)

    def add_supplier(self, supplier):
        """
        Adds a supplier to the supplier list.

        :param supplier: A string representing the supplier's name
        """
        if not supplier:
            raise ValueError("Supplier must not be empty.")
        self.supplier_list.append(supplier)

    def create_strategy(self):
        """
        Compiles the procurement strategy details.

        :return: A dictionary containing the procurement strategy details
        """
        if not self.sourcing_services:
            raise RuntimeError("No sourcing services have been added.")
        
        if not self.supplier_list:
            raise RuntimeError("No suppliers have been added.")
        
        return {
            "company_name": self.company_name,
            "region": self.region,
            "sourcing_services": self.sourcing_services,
            "suppliers": self.supplier_list
        }

def main():
    """
    Main function to demonstrate the usage of ProcurementStrategy class.
    """
    try:
        # Create a procurement strategy for Cedar International
        procurement = ProcurementStrategy(company_name="Cedar International", region="Middle East")

        # Add sourcing services
        procurement.add_sourcing_service("Supplier Negotiation")
        procurement.add_sourcing_service("Market Analysis")

        # Add suppliers
        procurement.add_supplier("Supplier A")
        procurement.add_supplier("Supplier B")

        # Create and print the procurement strategy
        strategy = procurement.create_strategy()
        print("Custom Procurement Strategy Created:")
        print(strategy)

    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
