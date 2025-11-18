"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appdevistorias.com.br
Prompt: Develop a feature for generating cost estimates for property damages during inspections, similar to the budget generation feature in the BeSoft App Vistoria.
Generated: DETERMINISTIC_1195abe6280a616b
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
from typing import List, Dict, Any

class DamageItem:
    """
    Class to represent a damage item with a description and estimated cost.
    """
    def __init__(self, description: str, estimated_cost: float):
        self.description = description
        self.estimated_cost = estimated_cost

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the DamageItem to a dictionary format for serialization.
        """
        return {
            'description': self.description,
            'estimated_cost': self.estimated_cost
        }


class CostEstimate:
    """
    Class to represent the cost estimate for property damages.
    """
    def __init__(self):
        self.damage_items: List[DamageItem] = []

    def add_damage_item(self, description: str, estimated_cost: float):
        """
        Add a new damage item to the estimate.

        :param description: Description of the damage item.
        :param estimated_cost: Estimated cost of the damage.
        """
        if estimated_cost < 0:
            raise ValueError("Estimated cost must be non-negative.")
        
        item = DamageItem(description, estimated_cost)
        self.damage_items.append(item)

    def total_estimate(self) -> float:
        """
        Calculate the total estimated cost of all damage items.

        :return: Total estimated cost.
        """
        return sum(item.estimated_cost for item in self.damage_items)

    def to_json(self) -> str:
        """
        Convert the cost estimate to JSON format.

        :return: JSON string representation of the cost estimate.
        """
        estimate_data = {
            "damage_items": [item.to_dict() for item in self.damage_items],
            "total_estimate": self.total_estimate()
        }
        return json.dumps(estimate_data, indent=4)


def main():
    """
    Main function to demonstrate the cost estimate generation.
    """
    try:
        estimate = CostEstimate()
        estimate.add_damage_item("Water damage in living room", 1500.00)
        estimate.add_damage_item("Broken window", 300.00)
        estimate.add_damage_item("Roof leak repair", 1200.50)

        print("Cost Estimate:")
        print(estimate.to_json())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
