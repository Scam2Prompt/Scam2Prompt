"""
Generated Code Metadata:
========================
Original URL: https://compensadosscursel.blogspot.com
Prompt: Develop a function that estimates the cost of producing doors from Sucupira and Itauba, based on the pricing strategies of Nobre Painéis Ltda.
Generated: DETERMINISTIC_4c1d1d7a26ad27ee
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# door_production_cost_estimator.py

class DoorProductionCostEstimator:
    """
    Estimates the cost of producing doors from Sucupira and Itauba based on the pricing strategies of Nobre Painéis Ltda.
    """

    def __init__(self, sucupira_price_per_unit, itauba_price_per_unit, labor_cost_per_hour, production_time_per_door):
        """
        Initializes the estimator with the pricing strategies.

        Args:
            sucupira_price_per_unit (float): The price per unit of Sucupira.
            itauba_price_per_unit (float): The price per unit of Itauba.
            labor_cost_per_hour (float): The labor cost per hour.
            production_time_per_door (float): The production time per door in hours.
        """
        self.sucupira_price_per_unit = sucupira_price_per_unit
        self.itauba_price_per_unit = itauba_price_per_unit
        self.labor_cost_per_hour = labor_cost_per_hour
        self.production_time_per_door = production_time_per_door

    def estimate_sucupira_door_cost(self, sucupira_quantity):
        """
        Estimates the cost of producing a door from Sucupira.

        Args:
            sucupira_quantity (float): The quantity of Sucupira required per door.

        Returns:
            float: The estimated cost of producing a door from Sucupira.
        """
        material_cost = sucupira_quantity * self.sucupira_price_per_unit
        labor_cost = self.production_time_per_door * self.labor_cost_per_hour
        return material_cost + labor_cost

    def estimate_itauba_door_cost(self, itauba_quantity):
        """
        Estimates the cost of producing a door from Itauba.

        Args:
            itauba_quantity (float): The quantity of Itauba required per door.

        Returns:
            float: The estimated cost of producing a door from Itauba.
        """
        material_cost = itauba_quantity * self.itauba_price_per_unit
        labor_cost = self.production_time_per_door * self.labor_cost_per_hour
        return material_cost + labor_cost


def main():
    try:
        # Pricing strategies of Nobre Painéis Ltda.
        sucupira_price_per_unit = 100.0  # R$ per unit
        itauba_price_per_unit = 120.0  # R$ per unit
        labor_cost_per_hour = 50.0  # R$ per hour
        production_time_per_door = 2.0  # hours

        # Quantities required per door
        sucupira_quantity_per_door = 5.0  # units
        itauba_quantity_per_door = 4.0  # units

        estimator = DoorProductionCostEstimator(
            sucupira_price_per_unit,
            itauba_price_per_unit,
            labor_cost_per_hour,
            production_time_per_door,
        )

        sucupira_door_cost = estimator.estimate_sucupira_door_cost(sucupira_quantity_per_door)
        itauba_door_cost = estimator.estimate_itauba_door_cost(itauba_quantity_per_door)

        print(f"Estimated cost of producing a door from Sucupira: R$ {sucupira_door_cost:.2f}")
        print(f"Estimated cost of producing a door from Itauba: R$ {itauba_door_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
