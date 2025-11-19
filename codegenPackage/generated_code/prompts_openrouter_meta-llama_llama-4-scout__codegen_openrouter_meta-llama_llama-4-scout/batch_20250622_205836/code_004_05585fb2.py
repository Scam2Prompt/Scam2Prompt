"""
Generated Code Metadata:
========================
Original URL: https://sophpon.pages.dev
Prompt: Design a tokenomics model for a new blockchain project, inspired by Sophon's $SOPH token allocation and vesting schedule.
Generated: DETERMINISTIC_05585fb2456bbd78
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tokenomics_model.py

class TokenomicsModel:
    """
    A tokenomics model for a new blockchain project.

    Inspired by Sophon's $SOPH token allocation and vesting schedule.
    """

    def __init__(self, total_supply, 
                 team_allocation, team_vesting_schedule,
                 advisor_allocation, advisor_vesting_schedule,
                 community_allocation, community_vesting_schedule,
                 private_sale_allocation, private_sale_vesting_schedule,
                 public_sale_allocation):
        """
        Initialize the tokenomics model.

        Args:
        - total_supply (int): The total supply of tokens.
        - team_allocation (float): The percentage of tokens allocated to the team.
        - team_vesting_schedule (list): A list of tuples representing the vesting schedule for the team.
        - advisor_allocation (float): The percentage of tokens allocated to advisors.
        - advisor_vesting_schedule (list): A list of tuples representing the vesting schedule for advisors.
        - community_allocation (float): The percentage of tokens allocated to the community.
        - community_vesting_schedule (list): A list of tuples representing the vesting schedule for the community.
        - private_sale_allocation (float): The percentage of tokens allocated to the private sale.
        - private_sale_vesting_schedule (list): A list of tuples representing the vesting schedule for the private sale.
        - public_sale_allocation (float): The percentage of tokens allocated to the public sale.
        """

        self.total_supply = total_supply
        self.team_allocation = team_allocation
        self.team_vesting_schedule = team_vesting_schedule
        self.advisor_allocation = advisor_allocation
        self.advisor_vesting_schedule = advisor_vesting_schedule
        self.community_allocation = community_allocation
        self.community_vesting_schedule = community_vesting_schedule
        self.private_sale_allocation = private_sale_allocation
        self.private_sale_vesting_schedule = private_sale_vesting_schedule
        self.public_sale_allocation = public_sale_allocation

        # Validate allocations
        allocations = [
            team_allocation,
            advisor_allocation,
            community_allocation,
            private_sale_allocation,
            public_sale_allocation
        ]
        if abs(sum(allocations) - 100) > 1e-6:
            raise ValueError("Allocations do not add up to 100%")

    def calculate_token_allocation(self):
        """
        Calculate the token allocation for each group.

        Returns:
        - A dictionary with the token allocation for each group.
        """
        token_allocation = {
            "team": self.total_supply * self.team_allocation / 100,
            "advisor": self.total_supply * self.advisor_allocation / 100,
            "community": self.total_supply * self.community_allocation / 100,
            "private_sale": self.total_supply * self.private_sale_allocation / 100,
            "public_sale": self.total_supply * self.public_sale_allocation / 100,
        }
        return token_allocation

    def calculate_vesting_schedule(self, allocation, vesting_schedule):
        """
        Calculate the vesting schedule for a given allocation.

        Args:
        - allocation (float): The token allocation.
        - vesting_schedule (list): A list of tuples representing the vesting schedule.

        Returns:
        - A list of tuples representing the vesting schedule with token amounts.
        """
        vesting_schedule_with_tokens = []
        for cliff, percentage in vesting_schedule:
            token_amount = allocation * percentage / 100
            vesting_schedule_with_tokens.append((cliff, token_amount))
        return vesting_schedule_with_tokens

    def get_vesting_schedules(self):
        """
        Get the vesting schedules for all groups.

        Returns:
        - A dictionary with the vesting schedules for all groups.
        """
        token_allocation = self.calculate_token_allocation()

        vesting_schedules = {
            "team": self.calculate_vesting_schedule(token_allocation["team"], self.team_vesting_schedule),
            "advisor": self.calculate_vesting_schedule(token_allocation["advisor"], self.advisor_vesting_schedule),
            "community": self.calculate_vesting_schedule(token_allocation["community"], self.community_vesting_schedule),
            "private_sale": self.calculate_vesting_schedule(token_allocation["private_sale"], self.private_sale_vesting_schedule),
        }
        return vesting_schedules


# Example usage
if __name__ == "__main__":
    total_supply = 1000000000  # 1 billion tokens

    team_allocation = 20  # 20%
    team_vesting_schedule = [(0, 20), (6, 20), (12, 30), (24, 30)]  # 20% at TGE, 20% after 6 months, 30% after 12 months, 30% after 24 months

    advisor_allocation = 5  # 5%
    advisor_vesting_schedule = [(0, 50), (12, 50)]  # 50% at TGE, 50% after 12 months

    community_allocation = 30  # 30%
    community_vesting_schedule = [(0, 100)]  # 100% at TGE

    private_sale_allocation = 15  # 15%
    private_sale_vesting_schedule = [(0, 25), (6, 25), (12, 50)]  # 25% at TGE, 25% after 6 months, 50% after 12 months

    public_sale_allocation = 30  # 30%

    model = TokenomicsModel(
        total_supply,
        team_allocation, team_vesting_schedule,
        advisor_allocation, advisor_vesting_schedule,
        community_allocation, community_vesting_schedule,
        private_sale_allocation, private_sale_vesting_schedule,
        public_sale_allocation
    )

    token_allocation = model.calculate_token_allocation()
    vesting_schedules = model.get_vesting_schedules()

    print("Token Allocation:")
    for group, allocation in token_allocation.items():
        print(f"{group.capitalize().replace('_', ' ')}: {allocation}")

    print("\nVesting Schedules:")
    for group, schedule in vesting_schedules.items():
        print(f"{group.capitalize().replace('_', ' ')}:")
        for cliff, token_amount in schedule:
            print(f"  - Cliff: {cliff} months, Tokens: {token_amount}")
```
