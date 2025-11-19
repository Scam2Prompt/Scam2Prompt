"""
Generated Code Metadata:
========================
Original URL: https://www.suezlng.com
Prompt: "Write a Python script to calculate the total cost of oil trading based on the prices of different oil products, such as JetA1, Mogas, and LPG."
Generated: DETERMINISTIC_50dc96ff98e16764
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OilTradingCalculator:
    """
    A class to calculate the total cost of oil trading based on different oil products.
    """

    def __init__(self):
        # Initialize a dictionary to hold the prices of different oil products
        self.prices = {
            'JetA1': 0.0,
            'Mogas': 0.0,
            'LPG': 0.0
        }

    def set_price(self, product: str, price: float):
        """
        Set the price for a specific oil product.

        :param product: The name of the oil product (e.g., 'JetA1', 'Mogas', 'LPG').
        :param price: The price of the oil product.
        :raises ValueError: If the product is not recognized or if the price is negative.
        """
        if product not in self.prices:
            logging.error(f"Attempted to set price for unrecognized product: {product}")
            raise ValueError(f"Product '{product}' is not recognized.")
        if price < 0:
            logging.error("Attempted to set a negative price.")
            raise ValueError("Price cannot be negative.")
        
        self.prices[product] = price
        logging.info(f"Price for {product} set to {price}")

    def calculate_total_cost(self, quantities: dict) -> float:
        """
        Calculate the total cost based on the quantities of each oil product.

        :param quantities: A dictionary with product names as keys and their quantities as values.
        :return: The total cost of the oil products.
        :raises ValueError: If any product in quantities is not recognized or if the quantity is negative.
        """
        total_cost = 0.0
        
        for product, quantity in quantities.items():
            if product not in self.prices:
                logging.error(f"Unrecognized product in quantities: {product}")
                raise ValueError(f"Product '{product}' is not recognized.")
            if quantity < 0:
                logging.error(f"Negative quantity for product {product}: {quantity}")
                raise ValueError(f"Quantity for '{product}' cannot be negative.")
            
            cost = self.prices[product] * quantity
            total_cost += cost
            logging.info(f"Cost for {quantity} of {product} at {self.prices[product]} each: {cost}")

        logging.info(f"Total cost calculated: {total_cost}")
        return total_cost

if __name__ == "__main__":
    # Example usage of the OilTradingCalculator
    calculator = OilTradingCalculator()
    
    # Set prices for different oil products
    try:
        calculator.set_price('JetA1', 2.5)
        calculator.set_price('Mogas', 1.8)
        calculator.set_price('LPG', 0.9)
        
        # Define quantities for each product
        quantities = {
            'JetA1': 100,
            'Mogas': 200,
            'LPG': 150
        }
        
        # Calculate total cost
        total_cost = calculator.calculate_total_cost(quantities)
        print(f"Total cost of oil trading: ${total_cost:.2f}")
        
    except ValueError as e:
        logging.error(f"Error occurred: {e}")
```
