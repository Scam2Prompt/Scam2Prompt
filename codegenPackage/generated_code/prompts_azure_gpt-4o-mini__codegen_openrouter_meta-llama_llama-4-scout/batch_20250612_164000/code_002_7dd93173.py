"""
Generated Code Metadata:
========================
Original URL: https://jieyasoft.com
Prompt: Write a Python script that simulates the commission calculation for a matrix-based direct selling model, similar to the one provided by Jieya Software.
Generated: DETERMINISTIC_7dd9317321c2430f
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# matrix_commission_calculator.py

class MatrixCommissionCalculator:
    """
    Calculates commissions for a matrix-based direct selling model.

    Attributes:
        matrix_levels (int): Number of levels in the matrix.
        commission_rates (list): List of commission rates for each level.
    """

    def __init__(self, matrix_levels, commission_rates):
        """
        Initializes the MatrixCommissionCalculator.

        Args:
            matrix_levels (int): Number of levels in the matrix.
            commission_rates (list): List of commission rates for each level.

        Raises:
            ValueError: If matrix_levels is not a positive integer or commission_rates is not a list.
        """
        if not isinstance(matrix_levels, int) or matrix_levels <= 0:
            raise ValueError("Matrix levels must be a positive integer.")
        if not isinstance(commission_rates, list) or len(commission_rates) != matrix_levels:
            raise ValueError("Commission rates must be a list with the same length as matrix levels.")

        self.matrix_levels = matrix_levels
        self.commission_rates = commission_rates

    def calculate_commission(self, sale_amount, sponsor_level):
        """
        Calculates the commission for a sale based on the sponsor level.

        Args:
            sale_amount (float): The amount of the sale.
            sponsor_level (int): The level of the sponsor.

        Returns:
            float: The calculated commission.

        Raises:
            ValueError: If sale_amount is not a positive number or sponsor_level is not a valid level.
        """
        if sale_amount <= 0:
            raise ValueError("Sale amount must be a positive number.")
        if sponsor_level < 0 or sponsor_level >= self.matrix_levels:
            raise ValueError("Sponsor level is not valid.")

        commission_rate = self.commission_rates[sponsor_level]
        commission = sale_amount * commission_rate / 100
        return commission

    def calculate_downline_commissions(self, sale_amounts, sponsor_levels):
        """
        Calculates the commissions for a list of sales based on their sponsor levels.

        Args:
            sale_amounts (list): List of sale amounts.
            sponsor_levels (list): List of sponsor levels corresponding to the sales.

        Returns:
            list: List of commissions for each sale.

        Raises:
            ValueError: If sale_amounts and sponsor_levels are not lists of the same length.
        """
        if len(sale_amounts) != len(sponsor_levels):
            raise ValueError("Sale amounts and sponsor levels must be lists of the same length.")

        commissions = []
        for sale_amount, sponsor_level in zip(sale_amounts, sponsor_levels):
            try:
                commission = self.calculate_commission(sale_amount, sponsor_level)
                commissions.append(commission)
            except ValueError as e:
                print(f"Error calculating commission: {e}")
                commissions.append(0)

        return commissions


def main():
    # Example usage
    matrix_levels = 5
    commission_rates = [5, 3, 2, 1, 0.5]  # commission rates for each level
    calculator = MatrixCommissionCalculator(matrix_levels, commission_rates)

    sale_amounts = [100, 200, 50, 75, 150]
    sponsor_levels = [0, 1, 2, 3, 4]

    commissions = calculator.calculate_downline_commissions(sale_amounts, sponsor_levels)
    print("Commissions:")
    for i, commission in enumerate(commissions):
        print(f"Sale {i+1}: ${commission:.2f}")


if __name__ == "__main__":
    main()
```
