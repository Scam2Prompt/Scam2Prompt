"""
Generated Code Metadata:
========================
Original URL: https://stelllar.org
Prompt: Create a program to optimize freight management across multiple carriers and schedules, inspired by Stelllar Logistics' coordinated shipping approach.
Generated: DETERMINISTIC_7596a2b12187d28a
Batch ID: 20250612_155028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any
from datetime import datetime, timedelta

class Carrier:
    """Class representing a shipping carrier."""
    
    def __init__(self, name: str, rates: Dict[str, float]):
        """
        Initialize a Carrier instance.

        :param name: Name of the carrier
        :param rates: Dictionary of rates per distance
        """
        self.name = name
        self.rates = rates

    def calculate_cost(self, distance: float) -> float:
        """
        Calculate the shipping cost based on distance.

        :param distance: Distance to be shipped
        :return: Calculated shipping cost
        """
        rate = self.rates.get('standard', 0)
        return rate * distance


class Shipment:
    """Class representing a shipment."""
    
    def __init__(self, weight: float, distance: float, delivery_date: str):
        """
        Initialize a Shipment instance.

        :param weight: Weight of the shipment
        :param distance: Distance to be shipped
        :param delivery_date: Desired delivery date in 'YYYY-MM-DD' format
        """
        self.weight = weight
        self.distance = distance
        self.delivery_date = datetime.strptime(delivery_date, '%Y-%m-%d')

    def is_deliverable_by(self, carrier: Carrier) -> bool:
        """
        Check if the shipment can be delivered by the carrier.

        :param carrier: Carrier instance
        :return: True if deliverable, False otherwise
        """
        # Placeholder for actual logic to determine deliverability
        return True


class FreightOptimizer:
    """Class to optimize freight management across multiple carriers."""
    
    def __init__(self, carriers: List[Carrier]):
        """
        Initialize a FreightOptimizer instance.

        :param carriers: List of available carriers
        """
        self.carriers = carriers

    def find_best_option(self, shipment: Shipment) -> Dict[str, Any]:
        """
        Find the best shipping option for a given shipment.

        :param shipment: Shipment instance
        :return: Dictionary with the best carrier and cost
        """
        best_option = None
        lowest_cost = float('inf')

        for carrier in self.carriers:
            if shipment.is_deliverable_by(carrier):
                cost = carrier.calculate_cost(shipment.distance)
                if cost < lowest_cost:
                    lowest_cost = cost
                    best_option = carrier.name

        if best_option is None:
            raise ValueError("No carrier can deliver the shipment.")

        return {
            'carrier': best_option,
            'cost': lowest_cost,
            'delivery_date': shipment.delivery_date.strftime('%Y-%m-%d')
        }


def load_carriers_from_json(file_path: str) -> List[Carrier]:
    """
    Load carriers from a JSON file.

    :param file_path: Path to the JSON file
    :return: List of Carrier instances
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Carrier(name=carrier['name'], rates=carrier['rates']) for carrier in data['carriers']]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Error loading carriers: {e}")


def main():
    """Main function to execute the freight optimization."""
    try:
        # Load carriers from a JSON file
        carriers = load_carriers_from_json('carriers.json')

        # Create a shipment instance
        shipment = Shipment(weight=100, distance=250, delivery_date='2023-10-15')

        # Initialize the freight optimizer
        optimizer = FreightOptimizer(carriers)

        # Find the best shipping option
        best_option = optimizer.find_best_option(shipment)

        # Output the best option
        print(f"Best shipping option: {best_option}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `carriers.json` file exists in the same directory as the script and follows the expected format:

```json
{
    "carriers": [
        {
            "name": "Carrier A",
            "rates": {
                "standard": 0.5
            }
        },
        {
            "name": "Carrier B",
            "rates": {
                "standard": 0.7
            }
        }
    ]
}
```
