"""
Generated Code Metadata:
========================
Original URL: https://azumi.vercel.app
Prompt: Design a basic roadmap or development plan for an NFT project, inspired by the Azumi roadmap.
Generated: DETERMINISTIC_ffcc2e2393f58159
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class NFTProjectRoadmap:
    """
    A class to represent a basic roadmap for an NFT project inspired by the Azumi roadmap.
    """

    def __init__(self):
        """
        Initializes the roadmap with key phases and milestones.
        """
        self.phases = {
            "Phase 1": {
                "Milestones": [
                    "Market Research",
                    "Concept Development",
                    "Team Formation"
                ]
            },
            "Phase 2": {
                "Milestones": [
                    "Art Creation",
                    "Smart Contract Development",
                    "Website Launch"
                ]
            },
            "Phase 3": {
                "Milestones": [
                    "Community Building",
                    "Marketing Campaign",
                    "Pre-Sale Announcement"
                ]
            },
            "Phase 4": {
                "Milestones": [
                    "Public Sale",
                    "NFT Minting",
                    "Post-Sale Support"
                ]
            },
            "Phase 5": {
                "Milestones": [
                    "Future Utility Development",
                    "Partnerships",
                    "Ongoing Community Engagement"
                ]
            }
        }

    def display_roadmap(self):
        """
        Displays the roadmap in a structured format.
        """
        try:
            print("NFT Project Roadmap:")
            for phase, details in self.phases.items():
                print(f"\n{phase}:")
                for milestone in details["Milestones"]:
                    print(f" - {milestone}")
        except Exception as e:
            print(f"An error occurred while displaying the roadmap: {e}")

    def add_phase(self, phase_name, milestones):
        """
        Adds a new phase to the roadmap.

        Parameters:
        phase_name (str): The name of the new phase.
        milestones (list): A list of milestones for the new phase.
        """
        try:
            if phase_name in self.phases:
                raise ValueError("Phase already exists.")
            self.phases[phase_name] = {"Milestones": milestones}
            print(f"Phase '{phase_name}' added successfully.")
        except Exception as e:
            print(f"An error occurred while adding a phase: {e}")

    def remove_phase(self, phase_name):
        """
        Removes a phase from the roadmap.

        Parameters:
        phase_name (str): The name of the phase to remove.
        """
        try:
            if phase_name not in self.phases:
                raise ValueError("Phase does not exist.")
            del self.phases[phase_name]
            print(f"Phase '{phase_name}' removed successfully.")
        except Exception as e:
            print(f"An error occurred while removing a phase: {e}")


# Example usage
if __name__ == "__main__":
    roadmap = NFTProjectRoadmap()
    roadmap.display_roadmap()
    
    # Adding a new phase
    roadmap.add_phase("Phase 6", ["Expansion to Other Platforms", "Enhanced Features"])
    
    # Displaying the updated roadmap
    roadmap.display_roadmap()
    
    # Removing a phase
    roadmap.remove_phase("Phase 1")
    
    # Displaying the final roadmap
    roadmap.display_roadmap()
```
