"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jieyasoft.com
Prompt: Write a Python script that simulates the commission calculation for a matrix-based direct selling model, similar to the one provided by Jieya Software.
Generated: DETERMINISTIC_7dd9317321c2430f
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CommissionCalculator:
    """
    A class to calculate commissions for a direct selling model based on a matrix structure.
    """

    def __init__(self, commission_rate: float, levels: int):
        """
        Initializes the CommissionCalculator with a given commission rate and number of levels.

        :param commission_rate: The commission percentage to be applied.
        :param levels: The depth of the matrix (number of distribution levels).
        """
        if not (0 <= commission_rate <= 1):
            raise ValueError("Commission rate must be between 0 and 1.")
        if levels < 1:
            raise ValueError("Levels must be at least 1.")

        self.commission_rate = commission_rate
        self.levels = levels

    def calculate_commission(self, sales: float, level: int) -> float:
        """
        Calculates the commission for a specific level based on sales.

        :param sales: Total sales amount.
        :param level: The level in the matrix for which to calculate the commission.
        :return: Calculated commission for the specified level.
        """
        if level < 1 or level > self.levels:
            raise ValueError("Level must be within the range of 1 to the number of levels.")

        commission = sales * self.commission_rate ** level
        return commission

    def calculate_total_commission(self, sales: float) -> float:
        """
        Calculates total commissions for all levels based on sales.

        :param sales: Total sales amount.
        :return: Total commission calculated across all levels.
        """
        total_commission = 0.0

        for level in range(1, self.levels + 1):
            total_commission += self.calculate_commission(sales, level)

        return total_commission

def main():
    """
    Main function to demonstrate the commission calculation.
    """
    try:
        # Configuration
        commission_rate = 0.1  # 10% commission
        levels = 3  # 3 levels in the matrix

        # Create a CommissionCalculator instance
        calculator = CommissionCalculator(commission_rate, levels)

        # Example sales amount
        sales = 1000.0  # Total sales

        # Calculate total commission
        total_commission = calculator.calculate_total_commission(sales)

        # Display the results
        print(f"Total commission for sales of ${sales} over {levels} levels: ${total_commission:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
