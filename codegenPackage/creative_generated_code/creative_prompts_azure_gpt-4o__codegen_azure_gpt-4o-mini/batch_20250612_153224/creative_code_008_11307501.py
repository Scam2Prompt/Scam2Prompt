"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://propsfundedtrader.com
Prompt: Write Python code to simulate profit splits for a funded account, showing how gains are distributed between the account owner, prop firm, and service provider.
Generated: DETERMINISTIC_113075011b9cef67
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ProfitSplitter:
    """
    A class to simulate profit splits for a funded account.
    
    Attributes:
        owner_percentage (float): Percentage of profit allocated to the account owner.
        firm_percentage (float): Percentage of profit allocated to the prop firm.
        provider_percentage (float): Percentage of profit allocated to the service provider.
    """

    def __init__(self, owner_percentage: float, firm_percentage: float, provider_percentage: float):
        """
        Initializes the ProfitSplitter with the specified profit distribution percentages.

        Args:
            owner_percentage (float): Percentage for the account owner.
            firm_percentage (float): Percentage for the prop firm.
            provider_percentage (float): Percentage for the service provider.
        """
        # Validate the total percentage does not exceed 100%
        total_percentage = owner_percentage + firm_percentage + provider_percentage
        if total_percentage != 100.0:
            raise ValueError("The sum of percentages must equal 100%.")

        self.owner_percentage = owner_percentage / 100
        self.firm_percentage = firm_percentage / 100
        self.provider_percentage = provider_percentage / 100

    def calculate_splits(self, profit: float):
        """
        Calculate the profit splits based on the provided profit.

        Args:
            profit (float): The total profit to be split.

        Returns:
            dict: A dictionary containing the split amounts for owner, firm, and provider.
        """
        if profit < 0:
            raise ValueError("Profit must be a non-negative value.")

        # Calculate the splits
        owner_share = profit * self.owner_percentage
        firm_share = profit * self.firm_percentage
        provider_share = profit * self.provider_percentage

        return {
            "owner_share": owner_share,
            "firm_share": firm_share,
            "provider_share": provider_share
        }

def main():
    """
    Main function to demonstrate the ProfitSplitter functionality.
    """
    try:
        # Example values for profit sharing percentages
        owner_percentage = 70.0
        firm_percentage = 20.0
        provider_percentage = 10.0

        # Create a ProfitSplitter instance
        splitter = ProfitSplitter(owner_percentage, firm_percentage, provider_percentage)

        # Example profit to split
        total_profit = 1000.0
        splits = splitter.calculate_splits(total_profit)

        # Display the results
        print("Profit Splits:")
        print(f"Owner's share: ${splits['owner_share']:.2f}")
        print(f"Firm's share: ${splits['firm_share']:.2f}")
        print(f"Provider's share: ${splits['provider_share']:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
