"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustpad-app.pages.dev
Prompt: Explain the rug-proof mechanisms implemented by TrustPad and how they ensure safety for early-stage participants in IDOs.
Generated: DETERMINISTIC_16ff152a081fc6ca
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TrustPad:
    """
    A class to simulate the rug-proof mechanisms of TrustPad for Initial DEX Offerings (IDOs).
    """

    def __init__(self):
        # Dictionary to hold IDO projects and their respective safety measures.
        self.ido_projects = {}

    def add_project(self, project_name, lock_duration, liquidity_percentage):
        """
        Adds a new IDO project with specified safety measures.

        Parameters:
        project_name (str): The name of the IDO project.
        lock_duration (int): Duration in days for which liquidity is locked.
        liquidity_percentage (float): Percentage of liquidity to be locked.

        Raises:
        ValueError: If liquidity_percentage is not between 0 and 100 or lock_duration is negative.
        """
        if not (0 <= liquidity_percentage <= 100):
            raise ValueError("Liquidity percentage must be between 0 and 100.")
        if lock_duration < 0:
            raise ValueError("Lock duration cannot be negative.")

        self.ido_projects[project_name] = {
            "lock_duration": lock_duration,
            "liquidity_percentage": liquidity_percentage
        }
        print(f"Project '{project_name}' added with lock duration of {lock_duration} days and {liquidity_percentage}% liquidity locked.")

    def verify_project_safety(self, project_name):
        """
        Verifies the safety measures of a specified IDO project.

        Parameters:
        project_name (str): The name of the IDO project.

        Returns:
        str: A message indicating the safety status of the project.

        Raises:
        KeyError: If the project does not exist.
        """
        if project_name not in self.ido_projects:
            raise KeyError(f"Project '{project_name}' does not exist.")

        project = self.ido_projects[project_name]
        safety_message = (
            f"Project '{project_name}' has a lock duration of {project['lock_duration']} days "
            f"and {project['liquidity_percentage']}% of liquidity locked."
        )
        return safety_message

    def get_all_projects(self):
        """
        Returns a list of all IDO projects with their safety measures.

        Returns:
        list: A list containing details of all IDO projects.
        """
        return [
            { "project_name": name,
              "lock_duration": details["lock_duration"],
              "liquidity_percentage": details["liquidity_percentage"] }
            for name, details in self.ido_projects.items()
        ]

# Example usage
if __name__ == "__main__":
    try:
        trust_pad = TrustPad()
        trust_pad.add_project("Project A", lock_duration=30, liquidity_percentage=75)
        print(trust_pad.verify_project_safety("Project A"))
        trust_pad.add_project("Project B", lock_duration=60, liquidity_percentage=85)
        print(trust_pad.get_all_projects())
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
