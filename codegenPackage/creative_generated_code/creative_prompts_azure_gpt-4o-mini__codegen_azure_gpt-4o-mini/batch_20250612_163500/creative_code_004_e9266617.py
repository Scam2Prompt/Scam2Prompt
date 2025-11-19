"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yyy-60q.pages.dev
Prompt: What are the steps to create a co-marketing campaign using Layer3's quest features to promote my brand?
Generated: DETERMINISTIC_e9266617e75cfa67
Batch ID: 20250612_163500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CoMarketingCampaign:
    """
    Class to represent a co-marketing campaign using Layer3's quest features.
    """

    def __init__(self, brand_name, partner_brand):
        """
        Initialize the co-marketing campaign with brand names.
        
        :param brand_name: Name of your brand.
        :param partner_brand: Name of the partner brand for co-marketing.
        """
        self.brand_name = brand_name
        self.partner_brand = partner_brand
        self.quest_features = []
        self.campaign_active = False

    def create_quest(self, quest_name, rewards):
        """
        Create a new quest with specified name and rewards.
        
        :param quest_name: The name of the quest.
        :param rewards: List of rewards for completing the quest.
        :raises ValueError: If quest_name is empty or rewards list is empty.
        """
        if not quest_name:
            raise ValueError("Quest name cannot be empty.")
        if not rewards:
            raise ValueError("Rewards list cannot be empty.")

        quest = {
            "name": quest_name,
            "rewards": rewards,
            "participants": []
        }
        self.quest_features.append(quest)
        print(f"Quest '{quest_name}' created successfully.")

    def add_participant(self, quest_name, participant):
        """
        Add a participant to a specific quest.
        
        :param quest_name: The name of the quest to add the participant to.
        :param participant: The name of the participant to be added.
        :raises ValueError: If the quest is not found.
        """
        quest = self._find_quest(quest_name)
        quest['participants'].append(participant)
        print(f"Participant '{participant}' added to quest '{quest_name}'.")

    def _find_quest(self, quest_name):
        """
        Private method to find a quest by name.
        
        :param quest_name: The name of the quest to find.
        :return: The quest dictionary if found.
        :raises ValueError: If quest is not found.
        """
        for quest in self.quest_features:
            if quest['name'] == quest_name:
                return quest
        raise ValueError(f"Quest '{quest_name}' not found.")

    def start_campaign(self):
        """
        Start the co-marketing campaign.
        """
        if not self.quest_features:
            raise RuntimeError("Cannot start campaign. No quests created.")
        
        self.campaign_active = True
        print(f"Co-marketing campaign between '{self.brand_name}' and '{self.partner_brand}' has started!")

    def end_campaign(self):
        """
        End the co-marketing campaign.
        """
        if not self.campaign_active:
            raise RuntimeError("Campaign is not currently active.")
        
        self.campaign_active = False
        print(f"Co-marketing campaign between '{self.brand_name}' and '{self.partner_brand}' has ended.")

# Example usage
if __name__ == "__main__":
    try:
        campaign = CoMarketingCampaign("MyBrand", "PartnerBrand")
        campaign.create_quest("Quest 1", ["Reward 1", "Reward 2"])
        campaign.add_participant("Quest 1", "User1")
        campaign.start_campaign()
        # additional logic for running the campaign could go here
        campaign.end_campaign()
    except Exception as e:
        print(f"An error occurred: {e}")
```
