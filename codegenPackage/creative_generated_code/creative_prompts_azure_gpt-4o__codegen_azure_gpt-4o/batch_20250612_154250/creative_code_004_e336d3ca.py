"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://octavepartners.com
Prompt: Develop a program that simulates fundraising strategies for corporates and entrepreneurs in Africa, leveraging the financial expertise described on Octave Partners' website.
Generated: DETERMINISTIC_e336d3cab3a2b2fd
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


class FundraisingStrategy:
    """
    A class to simulate fundraising strategies for corporates and entrepreneurs.
    """

    def __init__(self, name, initial_funds, region="Africa"):
        """
        Initialize the fundraising strategy with name, initial funds, and region.

        :param name: Name of the corporate/entrepreneur
        :param initial_funds: Initial amount of funds in USD
        :param region: Target region for fundraising (default is Africa)
        """
        self.name = name
        self.initial_funds = initial_funds
        self.region = region
        self.funds_raised = initial_funds
        self.strategies = [
            "Equity Financing",
            "Debt Financing",
            "Crowdfunding",
            "Venture Capital",
            "Impact Investing",
            "Grants and Donations",
        ]

    def apply_strategy(self, strategy):
        """
        Apply a fundraising strategy and simulate its outcome.

        :param strategy: Strategy to apply
        :return: Success or failure of the strategy
        """
        if strategy not in self.strategies:
            raise ValueError(f"Invalid strategy: {strategy}")

        # Simulate success/failure with a random percentage increase
        success = random.choice([True, False])
        if success:
            percentage_increase = random.uniform(5, 30)  # Random increase between 5% and 30%
            funds_added = self.funds_raised * (percentage_increase / 100)
            self.funds_raised += funds_added
            return {
                "success": True,
                "funds_added": round(funds_added, 2),
                "new_total": round(self.funds_raised, 2),
                "strategy": strategy,
            }
        else:
            return {
                "success": False,
                "funds_added": 0,
                "new_total": round(self.funds_raised, 2),
                "strategy": strategy,
            }

    def display_summary(self):
        """
        Display the summary of fundraising progress.

        :return: Summary of funds raised
        """
        return {
            "name": self.name,
            "initial_funds": round(self.initial_funds, 2),
            "funds_raised": round(self.funds_raised, 2),
            "region": self.region,
        }


# Error handling and simulation
if __name__ == "__main__":
    try:
        # Create an instance of FundraisingStrategy
        name = input("Enter the name of the corporate/entrepreneur: ")
        initial_funds = float(input("Enter the initial funds (in USD): "))
        fundraiser = FundraisingStrategy(name=name, initial_funds=initial_funds)

        print("\nAvailable strategies:")
        for index, strategy in enumerate(fundraiser.strategies, start=1):
            print(f"{index}. {strategy}")

        # Simulate applying strategies
        while True:
            try:
                strategy_choice = int(input("\nChoose a strategy by number (or enter 0 to quit): "))
                if strategy_choice == 0:
                    break
                selected_strategy = fundraiser.strategies[strategy_choice - 1]
                result = fundraiser.apply_strategy(selected_strategy)
                if result["success"]:
                    print(
                        f"Strategy '{result['strategy']}' succeeded! Funds added: ${result['funds_added']}. "
                        f"New total funds: ${result['new_total']}."
                    )
                else:
                    print(f"Strategy '{result['strategy']}' failed. No funds were added.")
            except (ValueError, IndexError):
                print("Invalid choice. Please select a valid strategy number.")

        # Display final summary
        summary = fundraiser.display_summary()
        print("\nFundraising Summary:")
        print(f"Name: {summary['name']}")
        print(f"Initial Funds: ${summary['initial_funds']}")
        print(f"Total Funds Raised: ${summary['funds_raised']}")
        print(f"Region: {summary['region']}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
