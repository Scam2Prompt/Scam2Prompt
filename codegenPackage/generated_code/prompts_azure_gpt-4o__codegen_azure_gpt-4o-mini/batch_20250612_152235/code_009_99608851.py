"""
Generated Code Metadata:
========================
Original URL: https://rrr-9a3.pages.dev
Prompt: Write a function to dynamically update and display the vesting and TGE details of BorpaToken based on the current phase (Whitelist, Overflow, Claim).
Generated: DETERMINISTIC_99608851c77a8de1
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BorpaToken:
    def __init__(self):
        # Initialize the vesting and TGE details
        self.phases = {
            "Whitelist": {"vesting_period": "30 days", "TGE": "10%"},
            "Overflow": {"vesting_period": "60 days", "TGE": "20%"},
            "Claim": {"vesting_period": "90 days", "TGE": "30%"},
        }
        self.current_phase = "Whitelist"

    def update_phase(self, new_phase):
        """
        Update the current phase of the BorpaToken.

        :param new_phase: str - The new phase to update to.
        :raises ValueError: If the new phase is not valid.
        """
        if new_phase not in self.phases:
            raise ValueError(f"Invalid phase: {new_phase}. Valid phases are: {list(self.phases.keys())}")
        
        self.current_phase = new_phase
        self.display_details()

    def display_details(self):
        """
        Display the vesting and TGE details for the current phase.
        """
        details = self.phases[self.current_phase]
        print(f"Current Phase: {self.current_phase}")
        print(f"Vesting Period: {details['vesting_period']}")
        print(f"TGE: {details['TGE']}")

# Example usage
if __name__ == "__main__":
    try:
        borpa_token = BorpaToken()
        borpa_token.display_details()  # Display initial details
        
        # Update to a new phase
        borpa_token.update_phase("Overflow")
        
        # Update to another phase
        borpa_token.update_phase("Claim")
        
        # Attempt to update to an invalid phase
        borpa_token.update_phase("InvalidPhase")  # This will raise an error
    except ValueError as e:
        print(f"Error: {e}")
```
