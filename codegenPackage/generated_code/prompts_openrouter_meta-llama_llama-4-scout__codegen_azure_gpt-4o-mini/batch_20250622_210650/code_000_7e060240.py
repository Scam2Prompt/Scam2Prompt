"""
Generated Code Metadata:
========================
Original URL: https://seelenschnell.site
Prompt: Write a Python script to calculate the cost of coffin transfer within Europe based on distance, considering a base price of €1000 and an additional €2.00-€2.50 per kilometer.
Generated: DETERMINISTIC_7e06024070d864e2
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# coffin_transfer.py

class CoffinTransferCalculator:
    """
    A class to calculate the cost of coffin transfer within Europe based on distance.
    """

    BASE_PRICE = 1000.00  # Base price for coffin transfer in euros
    COST_PER_KM_MIN = 2.00  # Minimum cost per kilometer in euros
    COST_PER_KM_MAX = 2.50  # Maximum cost per kilometer in euros

    def __init__(self, distance_km):
        """
        Initializes the CoffinTransferCalculator with the distance for the transfer.

        :param distance_km: Distance in kilometers for the coffin transfer
        """
        if distance_km < 0:
            raise ValueError("Distance cannot be negative.")
        self.distance_km = distance_km

    def calculate_cost(self):
        """
        Calculates the total cost of the coffin transfer based on the distance.

        :return: A tuple containing the minimum and maximum cost of the transfer
        """
        min_cost = self.BASE_PRICE + (self.COST_PER_KM_MIN * self.distance_km)
        max_cost = self.BASE_PRICE + (self.COST_PER_KM_MAX * self.distance_km)
        return min_cost, max_cost

def main():
    """
    Main function to execute the coffin transfer cost calculation.
    """
    try:
        # Input distance from the user
        distance = float(input("Enter the distance for coffin transfer in kilometers: "))
        
        # Create an instance of the calculator
        calculator = CoffinTransferCalculator(distance)
        
        # Calculate the cost
        min_cost, max_cost = calculator.calculate_cost()
        
        # Display the results
        print(f"The estimated cost of coffin transfer for {distance} km is between €{min_cost:.2f} and €{max_cost:.2f}.")
    
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid number for distance.")

if __name__ == "__main__":
    main()
```
