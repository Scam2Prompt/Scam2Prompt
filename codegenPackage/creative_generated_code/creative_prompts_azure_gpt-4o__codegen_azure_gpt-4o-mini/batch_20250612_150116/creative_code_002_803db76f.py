"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aspiregaininvest.com
Prompt: Create a Python script to calculate affiliate rewards for a two-level partnership program, as described on AspireGain Invest's website (5% for first-level referrals and 5% for second-level referrals).
Generated: DETERMINISTIC_803db76f779b154b
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AffiliateProgram:
    """
    A class to represent the affiliate rewards calculation for a two-level partnership program.
    
    Attributes:
    ----------
    first_level_rate : float
        The commission rate for first-level referrals.
    second_level_rate : float
        The commission rate for second-level referrals.
    
    Methods:
    -------
    calculate_rewards(first_level_sales, second_level_sales):
        Calculates total affiliate rewards based on sales from first and second-level referrals.
    """

    def __init__(self, first_level_rate: float = 0.05, second_level_rate: float = 0.05):
        """
        Initializes the AffiliateProgram with given commission rates.

        Parameters:
        ----------
        first_level_rate : float
            The commission rate for first-level referrals (default is 0.05).
        second_level_rate : float
            The commission rate for second-level referrals (default is 0.05).
        """
        self.first_level_rate = first_level_rate
        self.second_level_rate = second_level_rate

    def calculate_rewards(self, first_level_sales: float, second_level_sales: float) -> float:
        """
        Calculates total affiliate rewards from sales.

        Parameters:
        ----------
        first_level_sales : float
            The total sales amount from first-level referrals.
        second_level_sales : float
            The total sales amount from second-level referrals.

        Returns:
        -------
        float
            The total rewards earned from the sales.
        
        Raises:
        ------
        ValueError
            If sales values are negative.
        """
        if first_level_sales < 0 or second_level_sales < 0:
            raise ValueError("Sales values cannot be negative.")

        # Calculate rewards for first-level referrals
        first_level_rewards = first_level_sales * self.first_level_rate
        
        # Calculate rewards for second-level referrals
        second_level_rewards = second_level_sales * self.second_level_rate
        
        # Total rewards
        total_rewards = first_level_rewards + second_level_rewards
        return total_rewards


def main():
    """
    Main function to execute the affiliate rewards calculation.
    """
    # Example sales data for testing
    first_level_sales = 1000.0  # Sales generated from first-level referrals
    second_level_sales = 500.0   # Sales generated from second-level referrals

    # Create an instance of AffiliateProgram
    affiliate_program = AffiliateProgram()

    try:
        # Calculate rewards
        rewards = affiliate_program.calculate_rewards(first_level_sales, second_level_sales)
        print(f'Total Affiliate Rewards: ${rewards:.2f}')
    except ValueError as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main()
```
