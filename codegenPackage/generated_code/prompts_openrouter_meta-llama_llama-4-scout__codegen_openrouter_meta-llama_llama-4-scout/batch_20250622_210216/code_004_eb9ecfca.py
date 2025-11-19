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
# token_distribution_plan.py

class TokenDistributionPlan:
    """
    A class representing a token distribution plan for a cryptocurrency project.

    Attributes:
        total_supply (int): The total supply of tokens.
        public_goods_funding_allocation (float): The percentage of tokens allocated to public goods funding.
        ecosystem_fund_allocation (float): The percentage of tokens allocated to the ecosystem fund.
        user_airdrops_allocation (float): The percentage of tokens allocated to user airdrops.
    """

    def __init__(self, total_supply, public_goods_funding_allocation=0.2, ecosystem_fund_allocation=0.3, user_airdrops_allocation=0.1):
        """
        Initializes a TokenDistributionPlan instance.

        Args:
            total_supply (int): The total supply of tokens.
            public_goods_funding_allocation (float, optional): The percentage of tokens allocated to public goods funding. Defaults to 0.2.
            ecosystem_fund_allocation (float, optional): The percentage of tokens allocated to the ecosystem fund. Defaults to 0.3.
            user_airdrops_allocation (float, optional): The percentage of tokens allocated to user airdrops. Defaults to 0.1.

        Raises:
            ValueError: If the total supply is not a positive integer or if the allocations do not add up to 1.
        """
        if not isinstance(total_supply, int) or total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")

        if public_goods_funding_allocation + ecosystem_fund_allocation + user_airdrops_allocation != 1:
            raise ValueError("Allocations must add up to 1.")

        self.total_supply = total_supply
        self.public_goods_funding_allocation = public_goods_funding_allocation
        self.ecosystem_fund_allocation = ecosystem_fund_allocation
        self.user_airdrops_allocation = user_airdrops_allocation

    def calculate_allocations(self):
        """
        Calculates the number of tokens allocated to each category.

        Returns:
            dict: A dictionary containing the allocations for public goods funding, ecosystem fund, and user airdrops.
        """
        public_goods_funding_tokens = int(self.total_supply * self.public_goods_funding_allocation)
        ecosystem_fund_tokens = int(self.total_supply * self.ecosystem_fund_allocation)
        user_airdrops_tokens = int(self.total_supply * self.user_airdrops_allocation)

        return {
            "public_goods_funding": public_goods_funding_tokens,
            "ecosystem_fund": ecosystem_fund_tokens,
            "user_airdrops": user_airdrops_tokens,
        }

    def __str__(self):
        """
        Returns a string representation of the token distribution plan.

        Returns:
            str: A string containing the total supply and allocations for each category.
        """
        allocations = self.calculate_allocations()

        return (
            f"Token Distribution Plan:\n"
            f"Total Supply: {self.total_supply}\n"
            f"Public Goods Funding: {allocations['public_goods_funding']} tokens ({self.public_goods_funding_allocation*100}%)\n"
            f"Ecosystem Fund: {allocations['ecosystem_fund']} tokens ({self.ecosystem_fund_allocation*100}%)\n"
            f"User Airdrops: {allocations['user_airdrops']} tokens ({self.user_airdrops_allocation*100}%)"
        )


def main():
    try:
        total_supply = 1000000  # example total supply
        plan = TokenDistributionPlan(total_supply)
        print(plan)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
