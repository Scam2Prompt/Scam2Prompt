"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ivrtuals.io
Prompt: Explain the process of co-owning AI agents with the VIRTUALS Protocol and the significance of Virgen Point pledges.
Generated: DETERMINISTIC_4821c682efeb9643
Batch ID: 20250612_160440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VirtualAgent:
    """
    A class to represent a Virtual AI agent.
    """

    def __init__(self, name: str, owner: str):
        """
        Initializes a new instance of VirtualAgent.

        :param name: The name of the virtual agent.
        :param owner: The owner of the virtual agent.
        """
        self.name = name
        self.owner = owner
        self.co_owners = []
        self.virgen_point = 0  # Initialize Virgen Points

    def add_co_owner(self, co_owner: str):
        """
        Adds a co-owner to the virtual agent.

        :param co_owner: The name of the co-owner to add.
        :raises ValueError: If the co-owner is already an owner.
        """
        if co_owner in self.co_owners or co_owner == self.owner:
            raise ValueError(f"{co_owner} is already an owner or co-owner.")
        self.co_owners.append(co_owner)

    def pledge_virgen_points(self, points: int):
        """
        Pledges Virgen Points to the virtual agent.

        :param points: The number of Virgen Points to pledge.
        :raises ValueError: If points are negative or zero.
        """
        if points <= 0:
            raise ValueError("Pledging must be a positive number.")
        self.virgen_point += points

    def get_details(self):
        """
        Returns the details of the virtual agent, including the owner, co-owners, and Virgen Points.

        :return: A dictionary containing agent details.
        """
        return {
            "name": self.name,
            "owner": self.owner,
            "co_owners": self.co_owners,
            "virgen_points": self.virgen_point
        }

# Example Usage
if __name__ == "__main__":
    try:
        # Create a new virtual agent
        agent = VirtualAgent(name="AI Assistant", owner="Alice")

        # Add co-owners
        agent.add_co_owner("Bob")
        agent.add_co_owner("Charlie")

        # Pledge Virgen Points
        agent.pledge_virgen_points(10)

        # Retrieve and print agent details
        details = agent.get_details()
        print(details)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
