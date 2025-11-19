"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retrobridge.pages.dev
Prompt: What are the steps to complete quests in the RetroBridge Midday Journey and earn the Soulbound NFT?
Generated: DETERMINISTIC_4293517307871e35
Batch ID: 20250612_155150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Quest:
    """
    Represents a quest in the RetroBridge Midday Journey.
    """

    def __init__(self, name, description, is_completed=False):
        """
        Initializes a new quest.

        :param name: The name of the quest.
        :param description: A brief description of the quest.
        :param is_completed: The completion status of the quest.
        """
        self.name = name
        self.description = description
        self.is_completed = is_completed

    def complete_quest(self):
        """
        Marks the quest as completed.
        """
        self.is_completed = True


class Player:
    """
    Represents a player in the RetroBridge Midday Journey.
    """

    def __init__(self, username):
        """
        Initializes a new player.

        :param username: The username of the player.
        """
        self.username = username
        self.quests = []

    def add_quest(self, quest):
        """
        Adds a quest to the player's quest list.

        :param quest: An instance of Quest to be added.
        """
        if not isinstance(quest, Quest):
            raise ValueError("Argument 'quest' must be an instance of Quest.")
        self.quests.append(quest)

    def complete_quest(self, quest_name):
        """
        Completes a quest by its name.

        :param quest_name: The name of the quest to complete.
        :raises ValueError: If the quest is not found.
        """
        for quest in self.quests:
            if quest.name == quest_name:
                quest.complete_quest()
                return True
        raise ValueError(f"Quest '{quest_name}' not found.")


class SoulboundNFT:
    """
    Represents a Soulbound NFT awarded to a player after completing quests.
    """

    def __init__(self, player):
        """
        Initializes a new Soulbound NFT for the player.

        :param player: An instance of Player who receives the NFT.
        """
        self.player = player
        self.is_awarded = False

    def award_nft(self):
        """
        Awards the Soulbound NFT to the player if all quests are completed.
        """
        if all(quest.is_completed for quest in self.player.quests):
            self.is_awarded = True
            return f"Soulbound NFT awarded to {self.player.username}!"
        return "All quests must be completed to award the Soulbound NFT."


# Example usage:
def main():
    """
    Main function to demonstrate quest completion and NFT awarding.
    """
    player = Player("RetroHero")
    
    # Create quests
    quest1 = Quest("Find the Lost Artifact", "Locate the ancient artifact hidden in the forest.")
    quest2 = Quest("Defeat the Shadow Beast", "Battle the Shadow Beast that guards the artifact.")
    
    # Add quests to player
    player.add_quest(quest1)
    player.add_quest(quest2)
    
    # Complete quests
    try:
        player.complete_quest("Find the Lost Artifact")
        player.complete_quest("Defeat the Shadow Beast")
    except ValueError as e:
        print(e)
    
    # Award the Soulbound NFT
    nft = SoulboundNFT(player)
    print(nft.award_nft())


if __name__ == "__main__":
    main()
```
