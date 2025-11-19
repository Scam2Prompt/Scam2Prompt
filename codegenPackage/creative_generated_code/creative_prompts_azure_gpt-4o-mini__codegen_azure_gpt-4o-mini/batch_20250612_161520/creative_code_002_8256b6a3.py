"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiburonfishingreels.com
Prompt: Generate a Python script that calculates the shipping costs for orders under $200 from Tiburon Fishing Reels to a third-party shipping company.
Generated: DETERMINISTIC_8256b6a3e2d04645
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to log errors and debug information
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class ShippingCostCalculator:
    """
    A class to calculate shipping costs based on the order amount.
    Shipping costs apply only to orders under $200.
    """

    def __init__(self, base_cost=5.00, additional_cost_per_50=2.00):
        """
        Initializes the ShippingCostCalculator with default cost values.
        
        :param base_cost: The base shipping cost for orders under $200.
        :param additional_cost_per_50: Additional cost for every $50 increment over the base cost.
        """
        self.base_cost = base_cost
        self.additional_cost_per_50 = additional_cost_per_50

    def calculate_shipping(self, order_amount):
        """
        Calculate the shipping cost based on the order amount.
        
        :param order_amount: The total amount of the order.
        :return: Shipping cost in dollars.
        :raises ValueError: If order_amount is negative.
        """
        if order_amount < 0:
            logging.error('Order amount cannot be negative.')
            raise ValueError('Order amount cannot be negative.')

        if order_amount >= 200:
            logging.info('Order amount is $200 or more. No shipping cost calculated.')
            return 0.0  # Free shipping for orders $200 or more

        # Calculate additional shipping cost if order is under $200
        additional_cost = self.calculate_additional_cost(order_amount)
        total_cost = self.base_cost + additional_cost
        logging.debug(f'Calculated shipping cost: {total_cost} for order amount: {order_amount}')
        
        return total_cost

    def calculate_additional_cost(self, order_amount):
        """
        Calculate additional shipping cost based on the order amount.
        
        :param order_amount: The total amount of the order.
        :return: Additional shipping cost.
        """
        additional_cost = 0.0
        # Calculate how many $50 increments are there in the order amount
        if order_amount < 50:
            return additional_cost  # No additional cost below $50
        
        # Calculate additional cost for every $50 over $50
        increments = (order_amount - 50) // 50
        additional_cost = increments * self.additional_cost_per_50
        logging.debug(f'Additional shipping cost calculated: {additional_cost} for order amount: {order_amount}')
        
        return additional_cost

def main():
    """
    Main function to execute the shipping cost calculation.
    """
    calculator = ShippingCostCalculator()
    
    # Example order amounts to test
    order_amounts = [75, 150, 199, 200, -10]  # Including a negative value to test error handling

    for order_amount in order_amounts:
        try:
            shipping_cost = calculator.calculate_shipping(order_amount)
            print(f'Shipping cost for order amount ${order_amount}: ${shipping_cost:.2f}')
        except ValueError as e:
            print(f'Error calculating shipping for order amount ${order_amount}: {e}')

if __name__ == '__main__':
    main()
```
