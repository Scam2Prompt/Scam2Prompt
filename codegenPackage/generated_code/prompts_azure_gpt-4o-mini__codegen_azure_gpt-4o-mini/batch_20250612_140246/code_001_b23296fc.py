"""
Generated Code Metadata:
========================
Original URL: https://dflow.pages.dev
Prompt: What are the steps to earn DFlow XP in the upcoming phases of the DFlow app launch?
Generated: DETERMINISTIC_b23296fcb9edcf55
Batch ID: 20250612_140246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DFlowXP:
    """
    A class to represent the DFlow XP earning process during the app launch phases.
    """

    def __init__(self):
        """
        Initializes the DFlowXP class with an empty list of earned XP.
        """
        self.earned_xp = []

    def earn_xp(self, phase: str, activity: str, xp: int):
        """
        Earn XP for a specific activity in a given phase.

        Parameters:
        phase (str): The phase of the DFlow app launch.
        activity (str): The activity performed to earn XP.
        xp (int): The amount of XP earned.

        Raises:
        ValueError: If xp is not a positive integer.
        """
        if not isinstance(xp, int) or xp <= 0:
            raise ValueError("XP must be a positive integer.")

        self.earned_xp.append({
            'phase': phase,
            'activity': activity,
            'xp': xp
        })

    def get_total_xp(self) -> int:
        """
        Calculate the total XP earned.

        Returns:
        int: The total XP earned.
        """
        return sum(entry['xp'] for entry in self.earned_xp)

    def display_earned_xp(self):
        """
        Display the list of earned XP with details.
        """
        if not self.earned_xp:
            print("No XP earned yet.")
            return

        print("Earned DFlow XP:")
        for entry in self.earned_xp:
            print(f"Phase: {entry['phase']}, Activity: {entry['activity']}, XP: {entry['xp']}")

# Example usage
if __name__ == "__main__":
    dflow_xp = DFlowXP()

    try:
        dflow_xp.earn_xp("Phase 1", "Complete onboarding", 100)
        dflow_xp.earn_xp("Phase 1", "Invite a friend", 50)
        dflow_xp.earn_xp("Phase 2", "Participate in a survey", 30)

        dflow_xp.display_earned_xp()
        print(f"Total XP earned: {dflow_xp.get_total_xp()}")

    except ValueError as e:
        print(f"Error: {e}")
```
