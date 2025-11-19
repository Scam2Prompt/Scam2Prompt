"""
Generated Code Metadata:
========================
Original URL: https://bankless.pages.dev
Prompt: Explain the differences between the three redemption phases for $BASED tokens and how the token allocation varies depending on the phase.
Generated: DETERMINISTIC_ce65deada9478b40
Batch ID: 20250622_211350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import Tuple

class BasedTokenRedemption:
    """
    A class to represent the redemption phases for $BASED tokens.
    This class explains the differences between the three redemption phases
    and calculates token allocation based on the phase.
    """

    def __init__(self):
        """
        Initialize the redemption phases and their respective allocation percentages.
        """
        self.redemption_phases = {
            "Phase 1": 0.50,  # 50% allocation
            "Phase 2": 0.30,  # 30% allocation
            "Phase 3": 0.20   # 20% allocation
        }

    def get_phase_details(self, phase: str) -> str:
        """
        Get details about a specific redemption phase.

        Args:
            phase (str): The redemption phase ("Phase 1", "Phase 2", or "Phase 3").

        Returns:
            str: A description of the phase and its allocation percentage.
        """
        if phase not in self.redemption_phases:
            raise ValueError(f"Invalid phase: {phase}. Valid phases are: {', '.join(self.redemption_phases.keys())}")
        
        allocation_percentage = self.redemption_phases[phase] * 100
        return f"{phase} allows for {allocation_percentage}% of the total token allocation to be redeemed."

    def calculate_token_allocation(self, total_tokens: int, phase: str) -> Tuple[str, int]:
        """
        Calculate the number of tokens allocated for a specific redemption phase.

        Args:
            total_tokens (int): The total number of $BASED tokens available for redemption.
            phase (str): The redemption phase ("Phase 1", "Phase 2", or "Phase 3").

        Returns:
            Tuple[str, int]: A tuple containing the phase name and the number of tokens allocated.
        """
        if total_tokens <= 0:
            raise ValueError("Total tokens must be greater than zero.")
        
        if phase not in self.redemption_phases:
            raise ValueError(f"Invalid phase: {phase}. Valid phases are: {', '.join(self.redemption_phases.keys())}")
        
        allocation_percentage = self.redemption_phases[phase]
        allocated_tokens = int(total_tokens * allocation_percentage)
        return phase, allocated_tokens


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the redemption system
        redemption_system = BasedTokenRedemption()

        # Define the total number of tokens available
        total_tokens = 10000

        # Get details for each phase
        for phase in redemption_system.redemption_phases.keys():
            print(redemption_system.get_phase_details(phase))
            phase_name, allocated_tokens = redemption_system.calculate_token_allocation(total_tokens, phase)
            print(f"{phase_name}: {allocated_tokens} tokens allocated.\n")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
