"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.somosfortic.es
Prompt: Illustrate how to use Fortic's technical services in a project management tool, including steps for calculating structures and logistics for material delivery.
Generated: DETERMINISTIC_3724f69c1f7d8b0e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Any

class MaterialDelivery:
    """Class to handle material delivery logistics for a project."""

    def __init__(self, project_name: str):
        self.project_name = project_name
        self.delivery_schedule: List[Dict[str, Any]] = []

    def add_delivery(self, material: str, quantity: int, delivery_date: str) -> None:
        """Add a material delivery to the schedule.

        Args:
            material (str): The name of the material.
            quantity (int): The quantity of the material.
            delivery_date (str): The expected delivery date in 'YYYY-MM-DD' format.

        Raises:
            ValueError: If the delivery date is in the past.
        """
        # Validate the delivery date
        delivery_date_obj = datetime.datetime.strptime(delivery_date, '%Y-%m-%d')
        if delivery_date_obj < datetime.datetime.now():
            raise ValueError("Delivery date cannot be in the past.")

        # Append the delivery information to the schedule
        self.delivery_schedule.append({
            'material': material,
            'quantity': quantity,
            'delivery_date': delivery_date
        })

    def calculate_delivery_costs(self, cost_per_unit: float) -> float:
        """Calculate total delivery costs based on material quantities.

        Args:
            cost_per_unit (float): The cost per unit of material.

        Returns:
            float: Total cost of materials to be delivered.
        """
        total_cost = 0.0
        for delivery in self.delivery_schedule:
            total_cost += delivery['quantity'] * cost_per_unit
        return total_cost

    def get_delivery_schedule(self) -> List[Dict[str, Any]]:
        """Retrieve the current delivery schedule.

        Returns:
            List[Dict[str, Any]]: A list of scheduled deliveries.
        """
        return self.delivery_schedule

def main():
    """Main function to demonstrate the MaterialDelivery class."""
    try:
        # Create a MaterialDelivery instance for a project
        project = MaterialDelivery("Fortic Construction Project")

        # Add some deliveries with error handling for past dates
        project.add_delivery("Cement", 100, "2023-11-01")
        project.add_delivery("Bricks", 200, "2023-11-15")
        
        # This will raise an error if the date is in the past
        # project.add_delivery("Steel", 50, "2022-12-01")  # Uncomment to test error handling

        # Calculate delivery costs
        cost_per_unit = 10.0  # Example cost per unit of material
        total_cost = project.calculate_delivery_costs(cost_per_unit)

        # Print the delivery schedule and total cost
        print(f"Delivery Schedule for {project.project_name}:")
        for delivery in project.get_delivery_schedule():
            print(delivery)
        print(f"Total Delivery Cost: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
