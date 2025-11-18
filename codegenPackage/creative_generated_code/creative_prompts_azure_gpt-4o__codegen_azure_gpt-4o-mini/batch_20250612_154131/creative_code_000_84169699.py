"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkventureshares.com
Prompt: Write Python code to calculate the quarterly redemption amount for an investor in the ARK Venture Fund, given their total investment and the fund's 5% liquidity policy.
Generated: DETERMINISTIC_84169699605cdb2e
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ArkVentureFund:
    """
    A class to represent the ARK Venture Fund.
    
    Attributes
    ----------
    liquidity_policy : float
        The liquidity policy percentage for the fund (default is 5%).
    """

    def __init__(self, liquidity_policy=0.05):
        """
        Initializes the ARK Venture Fund with a specified liquidity policy.
        
        Parameters
        ----------
        liquidity_policy : float
            The liquidity policy percentage (between 0 and 1).
        """
        if not (0 < liquidity_policy < 1):
            raise ValueError("Liquidity policy must be a value between 0 and 1.")
        self.liquidity_policy = liquidity_policy

    def calculate_quarterly_redemption(self, total_investment):
        """
        Calculates the quarterly redemption amount for an investor.
        
        Parameters
        ----------
        total_investment : float
            The total amount invested by the investor.
        
        Returns
        -------
        float
            The maximum amount that can be redeemed quarterly.
        
        Raises
        ------
        ValueError
            If total_investment is not a positive number.
        """
        if total_investment < 0:
            raise ValueError("Total investment must be a non-negative number.")
        
        # Calculate the quarterly redemption amount based on the liquidity policy
        quarterly_redemption = total_investment * self.liquidity_policy
        
        return quarterly_redemption


def main():
    """
    Main function to demonstrate the functionality of the ARK Venture Fund.
    """
    try:
        # Sample total investment amount for testing
        total_investment = 1000000  # Example: $1,000,000
        
        # Create an instance of ArkVentureFund
        fund = ArkVentureFund()
        
        # Calculate the quarterly redemption amount
        redemption_amount = fund.calculate_quarterly_redemption(total_investment)
        
        # Output the result
        print(f"The quarterly redemption amount for an investment of ${total_investment:,.2f} is ${redemption_amount:,.2f}.")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
