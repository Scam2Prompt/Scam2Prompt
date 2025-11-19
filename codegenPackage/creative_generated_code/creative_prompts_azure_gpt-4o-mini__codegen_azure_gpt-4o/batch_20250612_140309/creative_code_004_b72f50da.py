"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reg-monprotocol.pages.dev
Prompt: Explain the process of participating in the MON Protocol presale and the significance of the TGE for claiming allocations.
Generated: DETERMINISTIC_b72f50da12cad5db
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script explains the process of participating in the MON Protocol presale and 
the significance of the Token Generation Event (TGE) for claiming allocations.

It contains code to simulate user participation, allocation tracking, 
and TGE-based token claiming functionality.
"""

class MONProtocolPresale:
    def __init__(self):
        """
        Initializes the MONProtocolPresale instance.

        Attributes:
            presale_participants (dict): Stores user IDs and their respective allocation amounts.
            tge_occurred (bool): Indicates whether the Token Generation Event (TGE) has occurred.
        """
        self.presale_participants = {}  # Key: User ID, Value: Allocation
        self.tge_occurred = False  # Tracks the status of the TGE

    def participate_in_presale(self, user_id, allocation_amount):
        """
        Allows a user to participate in the presale and allocate tokens.

        Args:
            user_id (str): Unique identifier for the user.
            allocation_amount (float): Amount of tokens allocated to the user.

        Returns:
            str: Success message confirming the user's participation.
        """
        if user_id in self.presale_participants:
            return f"User {user_id} is already participating in the presale."
        if allocation_amount <= 0:
            return "Allocation amount must be greater than 0."

        # Register the user's allocation in the presale
        self.presale_participants[user_id] = allocation_amount
        return f"User {user_id} successfully participated with an allocation of {allocation_amount} tokens."

    def initiate_tge(self):
        """
        Marks the Token Generation Event (TGE) as occurred.

        Returns:
            str: Success message confirming the initiation of the TGE.
        """
        self.tge_occurred = True
        return "Token Generation Event (TGE) has occurred. Allocations can now be claimed."

    def claim_allocation(self, user_id):
        """
        Allows a user to claim their allocated tokens after the TGE.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            str: Success message confirming the user's claim or an error message if conditions are not met.
        """
        if not self.tge_occurred:
            return "TGE has not occurred yet. Allocations cannot be claimed."

        if user_id not in self.presale_participants:
            return f"User {user_id} is not registered for the presale."

        allocation = self.presale_participants[user_id]
        del self.presale_participants[user_id]  # Remove the user after claiming their allocation
        return f"User {user_id} successfully claimed their allocation of {allocation} tokens."

    def get_presale_status(self):
        """
        Provides the current status of the presale and TGE.

        Returns:
            dict: Summary of presale participants and TGE status.
        """
        return {
            "presale_participants": self.presale_participants,
            "tge_occurred": self.tge_occurred
        }


# Example usage
if __name__ == "__main__":
    # Create an instance of the MONProtocolPresale class
    presale = MONProtocolPresale()

    # Users participate in the presale
    print(presale.participate_in_presale("user1", 100))
    print(presale.participate_in_presale("user2", 200))

    # Check presale status
    print("Presale Status:", presale.get_presale_status())

    # Initiate the TGE
    print(presale.initiate_tge())

    # Users claim their allocation
    print(presale.claim_allocation("user1"))
    print(presale.claim_allocation("user2"))

    # Check presale status after claims
    print("Presale Status After Claims:", presale.get_presale_status())
```
