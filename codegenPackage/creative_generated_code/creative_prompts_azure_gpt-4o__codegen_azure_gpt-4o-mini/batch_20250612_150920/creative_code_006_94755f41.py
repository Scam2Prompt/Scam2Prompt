"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptexbit.com
Prompt: Create a script to calculate the Cryco governance model's resource allocation percentages for holders, members, leaders, founders, and co-creators.
Generated: DETERMINISTIC_94755f4107c15f21
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ResourceAllocation:
    """
    A class to calculate resource allocation percentages for a governance model.
    """

    def __init__(self, total_resources):
        """
        Initializes the ResourceAllocation instance with the total resources.

        :param total_resources: Total resources available for allocation.
        """
        if total_resources < 0:
            raise ValueError("Total resources must be a non-negative value.")
        self.total_resources = total_resources
        self.allocations = {
            'holders': 0.0,
            'members': 0.0,
            'leaders': 0.0,
            'founders': 0.0,
            'co_creators': 0.0
        }

    def set_allocation_percentages(self, holders_pct, members_pct, leaders_pct, founders_pct, co_creators_pct):
        """
        Sets the allocation percentages for each group.

        :param holders_pct: Percentage for holders.
        :param members_pct: Percentage for members.
        :param leaders_pct: Percentage for leaders.
        :param founders_pct: Percentage for founders.
        :param co_creators_pct: Percentage for co-creators.
        """
        total_pct = sum([holders_pct, members_pct, leaders_pct, founders_pct, co_creators_pct])
        if total_pct != 100:
            raise ValueError("Total allocation percentages must sum to 100.")

        self.allocations['holders'] = holders_pct
        self.allocations['members'] = members_pct
        self.allocations['leaders'] = leaders_pct
        self.allocations['founders'] = founders_pct
        self.allocations['co_creators'] = co_creators_pct

    def calculate_allocations(self):
        """
        Calculates the absolute allocation for each group based on the set percentages.

        :return: A dictionary containing the resource allocation for each group.
        """
        return {group: (self.total_resources * (pct / 100)) for group, pct in self.allocations.items()}

    def display_allocations(self):
        """
        Displays the calculated allocations in a readable format.
        """
        allocations = self.calculate_allocations()
        for group, amount in allocations.items():
            print(f"{group.capitalize()}: {amount:.2f} resources")

def main():
    try:
        # Example total resources
        total_resources = 10000
        
        # Create ResourceAllocation instance
        resource_allocation = ResourceAllocation(total_resources)

        # Set allocation percentages for the governance model
        resource_allocation.set_allocation_percentages(
            holders_pct=40,
            members_pct=25,
            leaders_pct=20,
            founders_pct=10,
            co_creators_pct=5
        )

        # Display the calculated resource allocations
        resource_allocation.display_allocations()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
