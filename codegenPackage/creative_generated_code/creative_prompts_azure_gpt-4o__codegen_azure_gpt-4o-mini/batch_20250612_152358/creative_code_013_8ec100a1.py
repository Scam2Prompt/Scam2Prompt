"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lite-trades.org
Prompt: Create a Python script to calculate team leader commissions for an affiliate program, referencing Lite Trade's partnership offer requirements.
Generated: DETERMINISTIC_8ec100a1f01fa80d
Batch ID: 20250612_152358
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

class CommissionCalculator:
    def __init__(self, base_rate, bonus_rate, threshold):
        """
        Initialize the commission calculator with given parameters.
        
        :param base_rate: The base commission rate as a percentage (0-100).
        :param bonus_rate: The bonus commission rate as a percentage (0-100).
        :param threshold: The sales threshold to qualify for the bonus (float).
        """
        self.base_rate = base_rate / 100  # Convert percentage to decimal
        self.bonus_rate = bonus_rate / 100  # Convert percentage to decimal
        self.threshold = threshold

    def calculate_commission(self, sales_amount):
        """
        Calculate the commission based on sales amount.
        
        :param sales_amount: The total sales amount (float).
        :return: The total commission earned (float).
        """
        if sales_amount < 0:
            logging.error("Sales amount cannot be negative.")
            raise ValueError("Sales amount cannot be negative.")

        # Calculate base commission
        commission = sales_amount * self.base_rate

        # Check if sales qualify for bonus
        if sales_amount >= self.threshold:
            bonus = sales_amount * self.bonus_rate
            commission += bonus
            logging.info(f"Bonus applied: {bonus:.2f}")

        logging.info(f"Total commission calculated: {commission:.2f}")
        return commission

def main():
    # Example parameters for Lite Trade's partnership offer
    BASE_COMMISSION_RATE = 10  # 10%
    BONUS_COMMISSION_RATE = 5   # 5%
    SALES_THRESHOLD = 1000      # Sales threshold of 1000

    # Create an instance of the CommissionCalculator
    calculator = CommissionCalculator(BASE_COMMISSION_RATE, BONUS_COMMISSION_RATE, SALES_THRESHOLD)

    # Example sales amount
    sales_amount = 1500  # Change this value to test different sales amounts

    try:
        total_commission = calculator.calculate_commission(sales_amount)
        print(f"Total commission for sales amount {sales_amount}: {total_commission:.2f}")
    except ValueError as e:
        print(f"Error calculating commission: {e}")

if __name__ == "__main__":
    main()
```
