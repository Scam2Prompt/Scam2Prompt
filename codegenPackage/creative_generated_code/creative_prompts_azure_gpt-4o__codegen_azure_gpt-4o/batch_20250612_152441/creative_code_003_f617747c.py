"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.dexodoor.com
Prompt: Provide a Python function to model sliding and casement door mechanisms, using the types of doors mentioned on the Dexodoor site.
Generated: DETERMINISTIC_f617747ce7768ab4
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This module provides functionality to model sliding and casement door mechanisms.
Dexodoor types of doors are considered for implementation.

Sliding Door: A door that slides horizontally using tracks.
Casement Door: A door that swings open using hinges.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

class DoorMechanismError(Exception):
    """Custom exception for door mechanism errors."""
    pass


class SlidingDoor:
    def __init__(self, position: str = "closed"):
        """
        Initialize a SlidingDoor instance.

        :param position: Initial position of the door, either 'closed' or 'open'.
        """
        if position not in ["closed", "open"]:
            raise ValueError("SlidingDoor position must be 'closed' or 'open'.")
        self.position = position

    def slide(self, action: str):
        """
        Slide the door to open or close.

        :param action: 'open' to slide open, 'close' to slide closed.
        """
        if action not in ["open", "close"]:
            raise ValueError("Action must be 'open' or 'close'.")
        
        if action == "open" and self.position == "open":
            raise DoorMechanismError("SlidingDoor is already open.")
        elif action == "close" and self.position == "closed":
            raise DoorMechanismError("SlidingDoor is already closed.")
        
        self.position = "open" if action == "open" else "closed"
        print(f"SlidingDoor has been slid {action}.")

    def __str__(self):
        return f"SlidingDoor is currently {self.position}."


class CasementDoor:
    def __init__(self, position: str = "closed"):
        """
        Initialize a CasementDoor instance.

        :param position: Initial position of the door, either 'closed' or 'open'.
        """
        if position not in ["closed", "open"]:
            raise ValueError("CasementDoor position must be 'closed' or 'open'.")
        self.position = position

    def swing(self, action: str):
        """
        Swing the door to open or close.

        :param action: 'open' to swing open, 'close' to swing closed.
        """
        if action not in ["open", "close"]:
            raise ValueError("Action must be 'open' or 'close'.")
        
        if action == "open" and self.position == "open":
            raise DoorMechanismError("CasementDoor is already open.")
        elif action == "close" and self.position == "closed":
            raise DoorMechanismError("CasementDoor is already closed.")
        
        self.position = "open" if action == "open" else "closed"
        print(f"CasementDoor has been swung {action}.")

    def __str__(self):
        return f"CasementDoor is currently {self.position}."


# Example usage:
if __name__ == "__main__":
    try:
        sliding_door = SlidingDoor()
        print(sliding_door)
        sliding_door.slide("open")
        print(sliding_door)
        sliding_door.slide("close")
        print(sliding_door)

        casement_door = CasementDoor()
        print(casement_door)
        casement_door.swing("open")
        print(casement_door)
        casement_door.swing("close")
        print(casement_door)
    except (ValueError, DoorMechanismError) as e:
        print(f"Error: {e}")
```
