"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://compensadosscursel.blogspot.com
Prompt: Develop a function that estimates the cost of producing doors from Sucupira and Itauba, based on the pricing strategies of Nobre Painéis Ltda.
Generated: DETERMINISTIC_4c1d1d7a26ad27ee
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DoorProductionCostEstimator:
    """
    A class to estimate the production cost of doors made from Sucupira and Itauba wood.
    """

    def __init__(self, sucupira_price_per_square_meter, itauba_price_per_square_meter):
        """
        Initializes the cost estimator with the prices of Sucupira and Itauba wood.

        Parameters:
            sucupira_price_per_square_meter (float): Price of Sucupira wood per square meter.
            itauba_price_per_square_meter (float): Price of Itauba wood per square meter.
        """
        self.sucupira_price_per_square_meter = sucupira_price_per_square_meter
        self.itauba_price_per_square_meter = itauba_price_per_square_meter

    def estimate_cost(self, wood_type, door_area):
        """
        Estimates the cost of producing a door based on the type of wood and the door area.

        Parameters:
            wood_type (str): The type of wood used ('Sucupira' or 'Itauba').
            door_area (float): The area of the door in square meters.

        Returns:
            float: Estimated cost of producing the door.

        Raises:
            ValueError: If an invalid wood type is provided or if the area is negative.
        """
        if door_area < 0:
            raise ValueError("Door area cannot be negative.")

        if wood_type == 'Sucupira':
            cost = self.sucupira_price_per_square_meter * door_area
        elif wood_type == 'Itauba':
            cost = self.itauba_price_per_square_meter * door_area
        else:
            raise ValueError("Invalid wood type. Choose 'Sucupira' or 'Itauba'.")

        return cost


# Example usage:
if __name__ == "__main__":
    try:
        # Prices in R$ (Brazilian Real) per square meter
        sucupira_price = 150.00  # Example price for Sucupira
        itauba_price = 120.00    # Example price for Itauba

        estimator = DoorProductionCostEstimator(sucupira_price, itauba_price)

        # Estimate cost for a Sucupira door with an area of 2.0 square meters
        cost_sucupira = estimator.estimate_cost('Sucupira', 2.0)
        print(f"Cost of Sucupira door: R$ {cost_sucupira:.2f}")

        # Estimate cost for an Itauba door with an area of 2.0 square meters
        cost_itauba = estimator.estimate_cost('Itauba', 2.0)
        print(f"Cost of Itauba door: R$ {cost_itauba:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
