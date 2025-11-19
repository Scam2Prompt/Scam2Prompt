"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gitcoin-qf-manager-bhrfz6odu-bootnode.vercel.app
Prompt: What are the key features of the Gitcoin Round Manager for managing grant funding?
Generated: DETERMINISTIC_f0c9c11dcf9060ce
Batch ID: 20250612_161356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict, Union


class Grant:
    """
    A class representing a grant. Each grant has an ID, name, funded amount, and funding goal.
    """
    def __init__(self, grant_id: int, grant_name: str, funded_amount: float, funding_goal: float):
        self.grant_id = grant_id
        self.grant_name = grant_name
        self.funded_amount = funded_amount
        self.funding_goal = funding_goal


class GitcoinRoundManager:
    """
    A class to manage Gitcoin grant funding rounds.
    """

    def __init__(self):
        # Initialize a list to store grant objects
        self.grants: List[Grant] = []

    def add_grant(self, grant_id: int, grant_name: str, funded_amount: float, funding_goal: float) -> None:
        """
        Adds a new grant to the round manager.

        :param grant_id: Unique identifier for the grant
        :param grant_name: Name of the grant
        :param funded_amount: Amount of money funded so far
        :param funding_goal: Target funding amount
        """
        # Check if a grant with the same ID already exists
        if any(grant.grant_id == grant_id for grant in self.grants):
            raise ValueError(f"Grant with ID {grant_id} already exists.")
        
        # Create a new grant object and add it to the list
        new_grant = Grant(grant_id, grant_name, funded_amount, funding_goal)
        self.grants.append(new_grant)

    def get_all_grants(self) -> List[Dict[str, Union[int, str, float]]]:
        """
        Retrieves all grants in the round manager.

        :return: List of dictionaries containing grant details
        """
        return [
            {
                "grant_id": grant.grant_id,
                "grant_name": grant.grant_name,
                "funded_amount": grant.funded_amount,
                "funding_goal": grant.funding_goal
            }
            for grant in self.grants
        ]

    def update_funded_amount(self, grant_id: int, new_funded_amount: float) -> None:
        """
        Updates the funded amount for a specific grant.

        :param grant_id: Unique identifier for the grant
        :param new_funded_amount: New funded amount to update
        """
        # Locate the grant by ID and update its funded amount
        for grant in self.grants:
            if grant.grant_id == grant_id:
                grant.funded_amount = new_funded_amount
                return

        # Raise an error if the grant ID was not found
        raise ValueError(f"Grant with ID {grant_id} not found.")

    def get_grant_status(self, grant_id: int) -> str:
        """
        Retrieves the funding status of a specific grant.

        :param grant_id: Unique identifier for the grant
        :return: Status of the grant as a string
        """
        # Locate the grant by ID and determine its funding status
        for grant in self.grants:
            if grant.grant_id == grant_id:
                if grant.funded_amount >= grant.funding_goal:
                    return f"Grant '{grant.grant_name}' has been fully funded."
                else:
                    remaining = grant.funding_goal - grant.funded_amount
                    return f"Grant '{grant.grant_name}' needs {remaining:.2f} more to reach its funding goal."

        # Raise an error if the grant ID was not found
        raise ValueError(f"Grant with ID {grant_id} not found.")

    def delete_grant(self, grant_id: int) -> None:
        """
        Deletes a grant from the round manager.

        :param grant_id: Unique identifier for the grant
        """
        # Filter out the grant with the specified ID
        self.grants = [grant for grant in self.grants if grant.grant_id != grant_id]


# Example usage
if __name__ == "__main__":
    try:
        # Create a round manager instance
        round_manager = GitcoinRoundManager()
        
        # Add grants
        round_manager.add_grant(1, "Grant Alpha", 500, 1000)
        round_manager.add_grant(2, "Grant Beta", 1000, 1000)
        
        # Get all grants
        print("All grants:", round_manager.get_all_grants())
        
        # Get grant status
        print(round_manager.get_grant_status(1))  # Should indicate funding needed
        print(round_manager.get_grant_status(2))  # Should indicate fully funded
        
        # Update funded amount
        round_manager.update_funded_amount(1, 1000)
        print(round_manager.get_grant_status(1))  # Should indicate fully funded
        
        # Delete a grant
        round_manager.delete_grant(1)
        print("All grants after deletion:", round_manager.get_all_grants())
    except ValueError as e:
        print("Error:", e)
    except Exception as ex:
        print("An unexpected error occurred:", ex)
```
