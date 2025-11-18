"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidxxnu2mmv3h3e3o4pjboi7c2ou6bluyjywr5cbxb53ltxd2gp244.ipfs.dweb.link
Prompt: Write code to calculate pledge percentages for a cryptocurrency investment firm, referencing DWF Labs' "$DWF Pledge Now" feature.
Generated: DETERMINISTIC_a1dba0c478d1126d
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to handle errors and debug information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PledgeCalculator:
    def __init__(self):
        self.total_investment = 0.0
        self.total_pledged = 0.0

    def add_investment(self, amount: float):
        """
        Adds an investment amount to the total investment.
        
        Parameters:
        amount (float): The amount to be added as an investment.
        
        Raises:
        ValueError: If the amount is negative.
        """
        if amount < 0:
            logging.error("Attempted to add a negative investment amount.")
            raise ValueError("Investment amount cannot be negative.")
        
        self.total_investment += amount
        logging.info(f"Added investment: {amount}. Total investment: {self.total_investment}")

    def add_pledged(self, amount: float):
        """
        Adds a pledged amount to the total pledged.
        
        Parameters:
        amount (float): The amount to be added as a pledge.
        
        Raises:
        ValueError: If the amount is negative or exceeds total investment.
        """
        if amount < 0:
            logging.error("Attempted to add a negative pledge amount.")
            raise ValueError("Pledge amount cannot be negative.")
        if amount > self.total_investment:
            logging.error("Pledge amount exceeds total investment.")
            raise ValueError("Pledge amount cannot exceed total investment.")
        
        self.total_pledged += amount
        logging.info(f"Added pledge: {amount}. Total pledged: {self.total_pledged}")

    def calculate_pledge_percentage(self) -> float:
        """
        Calculates the pledge percentage based on total pledged and total investment.
        
        Returns:
        float: The pledge percentage.
        
        Raises:
        ZeroDivisionError: If total investment is zero.
        """
        if self.total_investment == 0:
            logging.error("Total investment is zero, cannot calculate pledge percentage.")
            raise ZeroDivisionError("Total investment cannot be zero when calculating pledge percentage.")
        
        pledge_percentage = (self.total_pledged / self.total_investment) * 100
        logging.info(f"Pledge percentage calculated: {pledge_percentage:.2f}%")
        return pledge_percentage

def main():
    """
    Main function to demonstrate the PledgeCalculator's functionality.
    """
    try:
        calculator = PledgeCalculator()
        
        # Example investments
        calculator.add_investment(1000.0)
        calculator.add_investment(500.0)
        
        # Example pledges
        calculator.add_pledged(300.0)

        # Calculate and display pledge percentage
        percentage = calculator.calculate_pledge_percentage()
        print(f"Pledge Percentage: {percentage:.2f}%")

    except (ValueError, ZeroDivisionError) as e:
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
