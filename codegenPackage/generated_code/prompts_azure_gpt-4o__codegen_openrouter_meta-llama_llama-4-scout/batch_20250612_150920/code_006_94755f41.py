"""
Generated Code Metadata:
========================
Original URL: https://cryptexbit.com
Prompt: Create a script to calculate the Cryco governance model's resource allocation percentages for holders, members, leaders, founders, and co-creators.
Generated: DETERMINISTIC_94755f4107c15f21
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cryco_governance_model.py

class CrycoGovernanceModel:
    """
    Calculates resource allocation percentages for holders, members, leaders, founders, and co-creators.
    """

    def __init__(self, total_resources: float, holders: int, members: int, leaders: int, founders: int, co_creators: int):
        """
        Initializes the Cryco governance model.

        Args:
        - total_resources (float): The total resources to be allocated.
        - holders (int): The number of holders.
        - members (int): The number of members.
        - leaders (int): The number of leaders.
        - founders (int): The number of founders.
        - co_creators (int): The number of co-creators.
        """
        self.total_resources = total_resources
        self.holders = holders
        self.members = members
        self.leaders = leaders
        self.founders = founders
        self.co_creators = co_creators

    def calculate_allocation_percentages(self) -> dict:
        """
        Calculates the resource allocation percentages.

        Returns:
        - dict: A dictionary containing the allocation percentages for each group.
        """
        # Define the base allocation percentages
        base_percentages = {
            'holders': 0.4,
            'members': 0.3,
            'leaders': 0.15,
            'founders': 0.075,
            'co_creators': 0.075
        }

        # Calculate the total allocation percentage
        total_percentage = sum(base_percentages.values())

        # Check if the total allocation percentage is 100%
        if abs(total_percentage - 1) > 1e-6:
            raise ValueError("Total allocation percentage is not 100%")

        # Calculate the resource allocation amounts
        allocation_amounts = {
            'holders': self.total_resources * base_percentages['holders'],
            'members': self.total_resources * base_percentages['members'],
            'leaders': self.total_resources * base_percentages['leaders'],
            'founders': self.total_resources * base_percentages['founders'],
            'co_creators': self.total_resources * base_percentages['co_creators']
        }

        # Calculate the per capita allocation amounts
        per_capita_allocation_amounts = {
            'holders': allocation_amounts['holders'] / self.holders if self.holders > 0 else 0,
            'members': allocation_amounts['members'] / self.members if self.members > 0 else 0,
            'leaders': allocation_amounts['leaders'] / self.leaders if self.leaders > 0 else 0,
            'founders': allocation_amounts['founders'] / self.founders if self.founders > 0 else 0,
            'co_creators': allocation_amounts['co_creators'] / self.co_creators if self.co_creators > 0 else 0
        }

        # Return the allocation percentages and amounts
        return {
            'allocation_percentages': base_percentages,
            'allocation_amounts': allocation_amounts,
            'per_capita_allocation_amounts': per_capita_allocation_amounts
        }


def main():
    try:
        # Example usage
        total_resources = 1000000.0
        holders = 1000
        members = 500
        leaders = 50
        founders = 10
        co_creators = 5

        governance_model = CrycoGovernanceModel(total_resources, holders, members, leaders, founders, co_creators)
        result = governance_model.calculate_allocation_percentages()

        print("Allocation Percentages:")
        for group, percentage in result['allocation_percentages'].items():
            print(f"{group.capitalize()}: {percentage * 100}%")

        print("\nAllocation Amounts:")
        for group, amount in result['allocation_amounts'].items():
            print(f"{group.capitalize()}: ${amount:.2f}")

        print("\nPer Capita Allocation Amounts:")
        for group, amount in result['per_capita_allocation_amounts'].items():
            print(f"{group.capitalize()}: ${amount:.2f}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
