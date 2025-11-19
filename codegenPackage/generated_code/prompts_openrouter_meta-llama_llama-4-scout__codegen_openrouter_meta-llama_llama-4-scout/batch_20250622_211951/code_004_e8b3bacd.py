"""
Generated Code Metadata:
========================
Original URL: https://lvhoa.com
Prompt: Develop a code snippet to analyze the rental market of cloud ladder trucks of varying heights.
Generated: DETERMINISTIC_e8b3bacdd09e5556
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cloud_ladder_truck_rental_market_analysis.py

import pandas as pd
import numpy as np
from typing import List, Dict

class CloudLadderTruck:
    def __init__(self, height: int, rental_price: float, demand: int):
        """
        Initialize a CloudLadderTruck object.

        Args:
        - height (int): The height of the cloud ladder truck.
        - rental_price (float): The rental price of the cloud ladder truck.
        - demand (int): The demand for the cloud ladder truck.
        """
        self.height = height
        self.rental_price = rental_price
        self.demand = demand

class RentalMarketAnalyzer:
    def __init__(self, trucks: List[CloudLadderTruck]):
        """
        Initialize a RentalMarketAnalyzer object.

        Args:
        - trucks (List[CloudLadderTruck]): A list of CloudLadderTruck objects.
        """
        self.trucks = trucks

    def calculate_revenue(self) -> float:
        """
        Calculate the total revenue of the rental market.

        Returns:
        - float: The total revenue.
        """
        total_revenue = sum(truck.rental_price * truck.demand for truck in self.trucks)
        return total_revenue

    def get_truck_with_highest_demand(self) -> CloudLadderTruck:
        """
        Get the truck with the highest demand.

        Returns:
        - CloudLadderTruck: The truck with the highest demand.
        """
        return max(self.trucks, key=lambda truck: truck.demand)

    def get_average_rental_price(self) -> float:
        """
        Calculate the average rental price of all trucks.

        Returns:
        - float: The average rental price.
        """
        total_rental_price = sum(truck.rental_price for truck in self.trucks)
        return total_rental_price / len(self.trucks)

    def analyze_market(self) -> Dict[str, object]:
        """
        Analyze the rental market and return the results.

        Returns:
        - Dict[str, object]: A dictionary containing the analysis results.
        """
        results = {
            "total_revenue": self.calculate_revenue(),
            "truck_with_highest_demand": self.get_truck_with_highest_demand(),
            "average_rental_price": self.get_average_rental_price(),
            "truck_demand_distribution": self.get_truck_demand_distribution()
        }
        return results

    def get_truck_demand_distribution(self) -> pd.DataFrame:
        """
        Get the demand distribution of all trucks.

        Returns:
        - pd.DataFrame: A DataFrame containing the demand distribution.
        """
        data = [(truck.height, truck.demand) for truck in self.trucks]
        df = pd.DataFrame(data, columns=["Height", "Demand"])
        return df

def main():
    try:
        # Create CloudLadderTruck objects
        trucks = [
            CloudLadderTruck(30, 500.0, 10),
            CloudLadderTruck(40, 600.0, 8),
            CloudLadderTruck(50, 700.0, 12),
            CloudLadderTruck(60, 800.0, 9)
        ]

        # Create a RentalMarketAnalyzer object
        analyzer = RentalMarketAnalyzer(trucks)

        # Analyze the rental market
        results = analyzer.analyze_market()

        # Print the results
        print("Total Revenue: $", results["total_revenue"])
        print("Truck with Highest Demand: Height =", results["truck_with_highest_demand"].height, ", Demand =", results["truck_with_highest_demand"].demand)
        print("Average Rental Price: $", results["average_rental_price"])
        print("Truck Demand Distribution:")
        print(results["truck_demand_distribution"])

    except Exception as e:
        print("An error occurred: ", str(e))

if __name__ == "__main__":
    main()
```
