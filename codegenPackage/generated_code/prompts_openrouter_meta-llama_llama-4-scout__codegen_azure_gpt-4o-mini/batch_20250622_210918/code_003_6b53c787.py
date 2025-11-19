"""
Generated Code Metadata:
========================
Original URL: https://mydogclub.pages.dev
Prompt: Design a roadmap for a Game-Fi project on the Bitcoin blockchain, including milestones for NFT debut, game launch, and multi-chain support, inspired by the Bitcoin Dogs Club roadmap.
Generated: DETERMINISTIC_6b53c787f467c134
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GameFiProjectRoadmap:
    """
    A class to represent the roadmap for a Game-Fi project on the Bitcoin blockchain.
    """

    def __init__(self):
        """
        Initializes the roadmap with predefined milestones.
        """
        self.milestones = []

    def add_milestone(self, milestone_name, target_date, description):
        """
        Adds a milestone to the roadmap.

        Parameters:
        milestone_name (str): The name of the milestone.
        target_date (str): The target date for the milestone (format: YYYY-MM-DD).
        description (str): A brief description of the milestone.

        Raises:
        ValueError: If the target_date is not in the correct format.
        """
        if not self.validate_date_format(target_date):
            raise ValueError("Target date must be in YYYY-MM-DD format.")

        milestone = {
            "name": milestone_name,
            "target_date": target_date,
            "description": description
        }
        self.milestones.append(milestone)

    @staticmethod
    def validate_date_format(date_string):
        """
        Validates the date format.

        Parameters:
        date_string (str): The date string to validate.

        Returns:
        bool: True if the date format is valid, False otherwise.
        """
        from datetime import datetime
        try:
            datetime.strptime(date_string, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def display_roadmap(self):
        """
        Displays the roadmap milestones in a formatted manner.
        """
        if not self.milestones:
            print("No milestones have been added to the roadmap.")
            return

        print("Game-Fi Project Roadmap:")
        for milestone in self.milestones:
            print(f"- {milestone['name']} (Target Date: {milestone['target_date']}): {milestone['description']}")

# Example usage
if __name__ == "__main__":
    try:
        roadmap = GameFiProjectRoadmap()
        
        # Adding milestones to the roadmap
        roadmap.add_milestone("NFT Debut", "2024-01-15", "Launch of the first NFT collection.")
        roadmap.add_milestone("Game Launch", "2024-06-01", "Official launch of the Game-Fi platform.")
        roadmap.add_milestone("Multi-Chain Support", "2024-12-01", "Integration with Ethereum and other blockchains.")
        
        # Display the roadmap
        roadmap.display_roadmap()
        
    except ValueError as e:
        print(f"Error: {e}")
```
