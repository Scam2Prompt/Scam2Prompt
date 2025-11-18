"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprimeapeplanetmint.pages.dev
Prompt: Create a roadmap for an NFT project inspired by Prime Ape Planet, including stages for minting, community building, Metaverse integration, and charitable contributions.
Generated: DETERMINISTIC_dba2cdebc0362e28
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NFTProjectRoadmap:
    """
    A class to represent the roadmap for an NFT project inspired by Prime Ape Planet.
    """

    def __init__(self):
        """
        Initializes the roadmap with predefined stages.
        """
        self.stages = {
            "Stage 1": "Concept Development",
            "Stage 2": "Minting Process",
            "Stage 3": "Community Building",
            "Stage 4": "Metaverse Integration",
            "Stage 5": "Charitable Contributions",
            "Stage 6": "Expansion and Partnerships"
        }
        self.completed_stages = []

    def complete_stage(self, stage_name):
        """
        Marks a stage as completed.

        Args:
            stage_name (str): The name of the stage to complete.

        Raises:
            ValueError: If the stage is not in the roadmap.
        """
        if stage_name not in self.stages:
            raise ValueError(f"Stage '{stage_name}' is not part of the roadmap.")
        
        if stage_name in self.completed_stages:
            print(f"Stage '{stage_name}' is already completed.")
            return
        
        self.completed_stages.append(stage_name)
        print(f"Stage '{stage_name}' has been marked as completed.")

    def get_roadmap(self):
        """
        Returns the current roadmap with completed stages highlighted.

        Returns:
            dict: A dictionary of stages with completion status.
        """
        roadmap_status = {
            stage: (stage in self.completed_stages) for stage in self.stages
        }
        return roadmap_status

    def print_roadmap(self):
        """
        Prints the roadmap to the console.
        """
        print("NFT Project Roadmap:")
        for stage, completed in self.get_roadmap().items():
            status = "✅ Completed" if completed else "❌ Pending"
            print(f"{stage}: {status}")


# Example usage
if __name__ == "__main__":
    try:
        nft_roadmap = NFTProjectRoadmap()
        nft_roadmap.print_roadmap()

        # Simulate completing stages
        nft_roadmap.complete_stage("Concept Development")
        nft_roadmap.complete_stage("Minting Process")
        nft_roadmap.print_roadmap()

        # Attempt to complete a stage that doesn't exist
        nft_roadmap.complete_stage("Non-Existent Stage")
    except ValueError as e:
        print(f"Error: {e}")
```
