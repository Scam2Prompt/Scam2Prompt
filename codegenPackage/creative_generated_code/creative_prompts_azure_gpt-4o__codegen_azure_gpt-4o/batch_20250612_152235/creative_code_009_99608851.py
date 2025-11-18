"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rrr-9a3.pages.dev
Prompt: Write a function to dynamically update and display the vesting and TGE details of BorpaToken based on the current phase (Whitelist, Overflow, Claim).
Generated: DETERMINISTIC_99608851c77a8de1
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
from datetime import datetime

class BorpaTokenVesting:
    def __init__(self):
        """
        Initialize the BorpaTokenVesting instance with default values.
        """
        self.phases = ["Whitelist", "Overflow", "Claim"]
        self.current_phase = None
        self.vesting_details = {
            "Whitelist": {"vesting_period": "3 months", "TGE_release": "10%"},
            "Overflow": {"vesting_period": "6 months", "TGE_release": "20%"},
            "Claim": {"vesting_period": "immediate", "TGE_release": "100%"}
        }

    def update_phase(self, phase_name):
        """
        Update the current phase and adjust vesting details accordingly.

        Args:
            phase_name (str): The name of the phase to set (Whitelist, Overflow, Claim).

        Raises:
            ValueError: If the phase_name is not a valid phase.
        """
        if phase_name not in self.phases:
            raise ValueError(f"Invalid phase '{phase_name}'. Valid phases are: {', '.join(self.phases)}")
        self.current_phase = phase_name

    def display_vesting_details(self):
        """
        Display the vesting details for the current phase.

        Returns:
            str: A formatted string with vesting period and TGE release details.
        """
        if self.current_phase is None:
            return "Phase not set. Please update the phase first."
        
        details = self.vesting_details[self.current_phase]
        return (f"Current Phase: {self.current_phase}\n"
                f"Vesting Period: {details['vesting_period']}\n"
                f"TGE Release: {details['TGE_release']}")

# Main function to demonstrate the functionality
def main():
    """
    Demonstrates the dynamic update and display of BorpaToken vesting details.
    Handles user input and updates the vesting details based on the current phase.
    """
    token_vesting = BorpaTokenVesting()
    print("Available phases: Whitelist, Overflow, Claim")
    
    while True:
        try:
            # Get user input for the phase
            phase = input("Enter the phase to update (or type 'exit' to quit): ").strip()
            
            if phase.lower() == 'exit':
                print("Exiting the program.")
                break
            
            # Update the phase and display the vesting details
            token_vesting.update_phase(phase)
            print(token_vesting.display_vesting_details())
        
        except ValueError as e:
            # Handle invalid phase input
            print(f"Error: {e}")
        except Exception as e:
            # Handle any unexpected errors
            print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
