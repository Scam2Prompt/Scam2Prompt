"""
Generated Code Metadata:
========================
Original URL: https://aitrader-site-7y6inq1vk-edrive.vercel.app
Prompt: Create a token distribution plan for a new cryptocurrency project, inspired by AI Trader's tokenomics, including allocations for public goods funding, ecosystem fund, and user airdrops.
Generated: DETERMINISTIC_eb9ecfcabe2fb32f
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenDistributionPlan:
    """
    A class to represent the token distribution plan for a cryptocurrency project.
    """

    def __init__(self, total_supply):
        """
        Initializes the TokenDistributionPlan with a total supply of tokens.

        :param total_supply: Total number of tokens to be distributed.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        self.total_supply = total_supply
        self.allocations = {
            "public_goods_funding": 0,
            "ecosystem_fund": 0,
            "user_airdrops": 0,
            "team": 0,
            "advisors": 0,
            "investors": 0,
            "liquidity": 0,
        }

    def allocate_tokens(self, allocation_name, percentage):
        """
        Allocates a percentage of the total supply to a specific category.

        :param allocation_name: The name of the allocation category.
        :param percentage: The percentage of total supply to allocate.
        :raises ValueError: If the percentage is not valid or exceeds remaining supply.
        """
        if allocation_name not in self.allocations:
            raise ValueError(f"Invalid allocation name: {allocation_name}.")
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100.")

        allocation_amount = (percentage / 100) * self.total_supply
        if allocation_amount + sum(self.allocations.values()) > self.total_supply:
            raise ValueError("Allocation exceeds total supply.")

        self.allocations[allocation_name] += allocation_amount

    def get_distribution_summary(self):
        """
        Returns a summary of the token distribution.

        :return: A dictionary containing the allocation details.
        """
        return {
            "total_supply": self.total_supply,
            "allocations": self.allocations,
            "remaining_supply": self.total_supply - sum(self.allocations.values()),
        }

    def display_distribution(self):
        """
        Displays the token distribution in a readable format.
        """
        summary = self.get_distribution_summary()
        print("Token Distribution Summary:")
        print(f"Total Supply: {summary['total_supply']}")
        for allocation, amount in summary['allocations'].items():
            print(f"{allocation.replace('_', ' ').title()}: {amount}")
        print(f"Remaining Supply: {summary['remaining_supply']}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the token distribution plan with a total supply of 1,000,000 tokens
        distribution_plan = TokenDistributionPlan(total_supply=1_000_000)

        # Allocate tokens according to the distribution plan
        distribution_plan.allocate_tokens("public_goods_funding", 10)  # 10%
        distribution_plan.allocate_tokens("ecosystem_fund", 20)         # 20%
        distribution_plan.allocate_tokens("user_airdrops", 15)          # 15%
        distribution_plan.allocate_tokens("team", 15)                   # 15%
        distribution_plan.allocate_tokens("advisors", 5)                # 5%
        distribution_plan.allocate_tokens("investors", 25)              # 25%
        distribution_plan.allocate_tokens("liquidity", 10)              # 10%

        # Display the distribution summary
        distribution_plan.display_distribution()

    except ValueError as e:
        print(f"Error: {e}")
```
