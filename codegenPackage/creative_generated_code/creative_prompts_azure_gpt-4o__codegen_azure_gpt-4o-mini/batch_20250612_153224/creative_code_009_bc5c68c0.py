"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vidaglobaltrade.com
Prompt: Write Python code to simulate a no-hidden-fee structure for manufacturers, enabling accurate budget planning and margin maintenance, based on VIDA TRADE LLC’s distribution model.
Generated: DETERMINISTIC_bc5c68c07b3859b1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Manufacturer:
    """
    A class to represent a manufacturer in the VIDA TRADE LLC distribution model.
    
    Attributes:
        name (str): The name of the manufacturer.
        cost_price (float): The cost price of the product.
        selling_price (float): The selling price of the product.
    """

    def __init__(self, name: str, cost_price: float, selling_price: float):
        """
        Initializes a Manufacturer instance.
        
        Args:
            name (str): The name of the manufacturer.
            cost_price (float): The cost price of the product.
            selling_price (float): The selling price of the product.
        
        Raises:
            ValueError: If cost_price or selling_price is negative.
        """
        if cost_price < 0 or selling_price < 0:
            logging.error("Cost price and selling price must be non-negative.")
            raise ValueError("Cost price and selling price must be non-negative.")
        
        self.name = name
        self.cost_price = cost_price
        self.selling_price = selling_price

    def calculate_margin(self) -> float:
        """
        Calculates the profit margin based on cost and selling prices.
        
        Returns:
            float: The profit margin in percentage.
        """
        margin = (self.selling_price - self.cost_price) / self.selling_price * 100
        logging.info(f"Calculated margin for {self.name}: {margin:.2f}%")
        return margin


class BudgetPlanner:
    """
    A class to manage budget planning for manufacturers.
    
    Attributes:
        manufacturers (list): A list of Manufacturer instances.
    """

    def __init__(self):
        """Initializes the BudgetPlanner with an empty manufacturer list."""
        self.manufacturers = []

    def add_manufacturer(self, manufacturer: Manufacturer):
        """
        Adds a Manufacturer instance to the budget planner.
        
        Args:
            manufacturer (Manufacturer): A Manufacturer instance to add.
        """
        self.manufacturers.append(manufacturer)
        logging.info(f"Added manufacturer: {manufacturer.name}")

    def calculate_total_margin(self) -> float:
        """
        Calculates the total profit margin across all manufacturers.
        
        Returns:
            float: The average profit margin.
        """
        if not self.manufacturers:
            logging.warning("No manufacturers available to calculate total margin.")
            return 0.0
        
        total_margin = sum(manufacturer.calculate_margin() for manufacturer in self.manufacturers)
        average_margin = total_margin / len(self.manufacturers)
        logging.info(f"Total average margin across manufacturers: {average_margin:.2f}%")
        return average_margin


# Example usage
if __name__ == "__main__":
    # Create a budget planner instance
    budget_planner = BudgetPlanner()

    try:
        # Create manufacturer instances
        manufacturer1 = Manufacturer("Manufacturer A", 50.0, 75.0)
        manufacturer2 = Manufacturer("Manufacturer B", 30.0, 50.0)

        # Add manufacturers to the budget planner
        budget_planner.add_manufacturer(manufacturer1)
        budget_planner.add_manufacturer(manufacturer2)

        # Calculate and print the total average margin
        average_margin = budget_planner.calculate_total_margin()
        print(f"Average Margin: {average_margin:.2f}%")
    
    except ValueError as e:
        logging.error(f"Error occurred: {e}")
```
