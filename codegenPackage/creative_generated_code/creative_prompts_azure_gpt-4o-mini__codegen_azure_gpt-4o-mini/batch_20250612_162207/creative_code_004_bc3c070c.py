"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cokiessnew.pages.dev
Prompt: Explain how to participate in quests within the Cookie Bakery and the benefits of completing them for earning $COOKIE tokens.
Generated: DETERMINISTIC_bc3c070c2094b446
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CookieBakery:
    def __init__(self):
        """
        Initializes the CookieBakery instance with an empty list of quests
        and a balance of COOKIE tokens.
        """
        self.quests = []
        self.balance = 0

    def add_quest(self, quest_name, reward):
        """
        Adds a new quest to the bakery.

        Parameters:
            quest_name (str): The name of the quest to be added.
            reward (int): The reward in COOKIE tokens for completing the quest.
        """
        if not isinstance(quest_name, str) or not isinstance(reward, int):
            raise ValueError("Quest name must be a string and reward must be an integer.")
        
        self.quests.append({'name': quest_name, 'reward': reward})

    def participate_in_quest(self, quest_name):
        """
        Allows a user to participate in a quest and earn COOKIE tokens.

        Parameters:
            quest_name (str): The name of the quest to participate in.

        Returns:
            str: A message indicating the result of the participation.
        """
        # Check if the quest exists
        for quest in self.quests:
            if quest['name'] == quest_name:
                self.balance += quest['reward']
                return f"Successfully completed the quest '{quest_name}'. You earned {quest['reward']} COOKIE tokens!"
        
        return f"Quest '{quest_name}' not found."

    def get_balance(self):
        """
        Returns the current balance of COOKIE tokens.

        Returns:
            int: The current balance of COOKIE tokens.
        """
        return self.balance

    def list_quests(self):
        """
        Returns a list of available quests in the bakery.

        Returns:
            list: A list of dictionaries containing quest names and rewards.
        """
        return self.quests


# Example usage
if __name__ == "__main__":
    # Create an instance of CookieBakery
    bakery = CookieBakery()

    # Add quests to the bakery
    bakery.add_quest("Bake a Chocolate Chip Cookie", 10)
    bakery.add_quest("Decorate a Cake", 15)

    # List available quests
    print("Available Quests:")
    for quest in bakery.list_quests():
        print(f"Quest: {quest['name']}, Reward: {quest['reward']} COOKIE tokens")

    # Participate in a quest
    result = bakery.participate_in_quest("Bake a Chocolate Chip Cookie")
    print(result)

    # Check balance after completing a quest
    print(f"Current COOKIE balance: {bakery.get_balance()} tokens")
```
