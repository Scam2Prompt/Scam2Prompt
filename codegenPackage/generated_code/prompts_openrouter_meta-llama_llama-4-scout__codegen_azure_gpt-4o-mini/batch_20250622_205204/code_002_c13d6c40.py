"""
Generated Code Metadata:
========================
Original URL: https://strk.site
Prompt: "Generate a sample contract for a full-cycle renovation service in Kazan, including details on design project, material costs, and timeline."
Generated: DETERMINISTIC_c13d6c4088caabfa
Batch ID: 20250622_205204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class RenovationContract:
    """
    A class to represent a renovation contract for full-cycle renovation services.
    """

    def __init__(self, client_name, project_address, design_project, material_costs, start_date, duration_days):
        """
        Initializes the RenovationContract with client details and project specifications.

        :param client_name: Name of the client
        :param project_address: Address of the renovation project
        :param design_project: Description of the design project
        :param material_costs: Dictionary of material costs
        :param start_date: Start date of the renovation
        :param duration_days: Duration of the renovation in days
        """
        self.client_name = client_name
        self.project_address = project_address
        self.design_project = design_project
        self.material_costs = material_costs
        self.start_date = self.validate_start_date(start_date)
        self.end_date = self.calculate_end_date(duration_days)

    def validate_start_date(self, start_date):
        """
        Validates the start date to ensure it is a future date.

        :param start_date: Proposed start date
        :return: Validated start date
        :raises ValueError: If the start date is in the past
        """
        if start_date < datetime.now():
            raise ValueError("Start date must be in the future.")
        return start_date

    def calculate_end_date(self, duration_days):
        """
        Calculates the end date based on the start date and duration.

        :param duration_days: Duration of the renovation in days
        :return: Calculated end date
        """
        return self.start_date + timedelta(days=duration_days)

    def generate_contract(self):
        """
        Generates a contract summary in JSON format.

        :return: JSON string of the contract details
        """
        contract_details = {
            "client_name": self.client_name,
            "project_address": self.project_address,
            "design_project": self.design_project,
            "material_costs": self.material_costs,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "total_cost": self.calculate_total_cost()
        }
        return json.dumps(contract_details, indent=4)

    def calculate_total_cost(self):
        """
        Calculates the total cost of materials.

        :return: Total cost of materials
        """
        return sum(self.material_costs.values())

# Example usage
if __name__ == "__main__":
    try:
        # Define contract details
        client_name = "Ivan Petrov"
        project_address = "123 Main St, Kazan"
        design_project = "Modern interior design with eco-friendly materials."
        material_costs = {
            "wood": 15000,
            "tiles": 8000,
            "paint": 3000,
            "fixtures": 5000
        }
        start_date = datetime(2023, 11, 1)  # Future date
        duration_days = 30  # Duration in days

        # Create a RenovationContract instance
        contract = RenovationContract(client_name, project_address, design_project, material_costs, start_date, duration_days)

        # Generate and print the contract
        print(contract.generate_contract())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
