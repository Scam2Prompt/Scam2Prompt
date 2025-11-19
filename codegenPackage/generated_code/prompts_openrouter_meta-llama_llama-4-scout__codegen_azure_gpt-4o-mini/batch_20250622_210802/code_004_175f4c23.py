"""
Generated Code Metadata:
========================
Original URL: https://lkinc.co.za
Prompt: Generate a sample financial plan for a business, incorporating Lund & Kieck's financial planning services and expertise in South African financial regulations.
Generated: DETERMINISTIC_175f4c237313a6df
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class FinancialPlan:
    """
    A class to represent a financial plan for a business.
    """

    def __init__(self, business_name: str, services: List[str], regulations: List[str]):
        """
        Initializes the FinancialPlan with business name, services, and regulations.

        :param business_name: Name of the business
        :param services: List of financial services provided
        :param regulations: List of applicable financial regulations
        """
        self.business_name = business_name
        self.services = services
        self.regulations = regulations
        self.plan_details = {
            "business_name": self.business_name,
            "services": self.services,
            "regulations": self.regulations,
            "created_at": datetime.now().isoformat()
        }

    def add_service(self, service: str) -> None:
        """
        Adds a new service to the financial plan.

        :param service: A financial service to add
        """
        if service not in self.services:
            self.services.append(service)
            self.plan_details["services"] = self.services
        else:
            raise ValueError(f"Service '{service}' already exists in the plan.")

    def remove_service(self, service: str) -> None:
        """
        Removes a service from the financial plan.

        :param service: A financial service to remove
        """
        if service in self.services:
            self.services.remove(service)
            self.plan_details["services"] = self.services
        else:
            raise ValueError(f"Service '{service}' does not exist in the plan.")

    def to_json(self) -> str:
        """
        Converts the financial plan to a JSON string.

        :return: JSON representation of the financial plan
        """
        return json.dumps(self.plan_details, indent=4)

def main():
    """
    Main function to create a financial plan and demonstrate its functionality.
    """
    try:
        # Define business name and services
        business_name = "Example Business"
        services = [
            "Tax Planning",
            "Investment Advisory",
            "Retirement Planning"
        ]
        regulations = [
            "Companies Act 71 of 2008",
            "Income Tax Act 58 of 1962",
            "Value-Added Tax Act 89 of 1991"
        ]

        # Create a financial plan instance
        financial_plan = FinancialPlan(business_name, services, regulations)

        # Add a new service
        financial_plan.add_service("Estate Planning")

        # Remove a service
        financial_plan.remove_service("Tax Planning")

        # Print the financial plan in JSON format
        print(financial_plan.to_json())

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
