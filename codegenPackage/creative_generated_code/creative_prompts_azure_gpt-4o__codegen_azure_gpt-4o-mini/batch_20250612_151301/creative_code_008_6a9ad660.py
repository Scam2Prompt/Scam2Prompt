"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantadev.pages.dev
Prompt: Write a program to simulate balance transfer quests on MANTRA Zone and calculate the KARMA earned from completing these quests.
Generated: DETERMINISTIC_6a9ad6607274bb2d
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BalanceTransferQuest:
    """
    A class to represent a balance transfer quest on the MANTRA Zone platform.
    
    Attributes
    ----------
    quest_id : int
        Unique identifier for the quest.
    transfer_amount : float
        The amount of balance to be transferred.
    karma_multiplier : float
        The multiplier for calculating earned KARMA based on transfer amount.
    """

    def __init__(self, quest_id, transfer_amount, karma_multiplier=0.1):
        """
        Initializes the BalanceTransferQuest with an ID, transfer amount, and KARMA multiplier.
        
        Parameters
        ----------
        quest_id : int
            Unique identifier for the quest.
        transfer_amount : float
            The amount of balance to be transferred.
        karma_multiplier : float, optional
            The multiplier for calculating earned KARMA (default is 0.1).
        """
        self.quest_id = quest_id
        self.transfer_amount = transfer_amount
        self.karma_multiplier = karma_multiplier

    def calculate_karma(self):
        """
        Calculates the KARMA earned from completing the balance transfer quest.
        
        Returns
        -------
        float
            The amount of KARMA earned.
        """
        if self.transfer_amount < 0:
            raise ValueError("Transfer amount must be non-negative.")
        karma_earned = self.transfer_amount * self.karma_multiplier
        return karma_earned

def main():
    """
    Main function to simulate balance transfer quests and display KARMA earned.
    """
    quests = [
        BalanceTransferQuest(1, 100.0),
        BalanceTransferQuest(2, 200.0),
        BalanceTransferQuest(3, -50.0)  # This will raise an error
    ]

    for quest in quests:
        try:
            karma = quest.calculate_karma()
            print(f"Quest ID: {quest.quest_id}, Transfer Amount: {quest.transfer_amount}, KARMA Earned: {karma}")
        except ValueError as e:
            print(f"Error processing Quest ID {quest.quest_id}: {e}")

if __name__ == "__main__":
    main()
```
