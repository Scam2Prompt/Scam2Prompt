"""
Generated Code Metadata:
========================
Original URL: https://climax-polska.pl
Prompt: Create a Python script to model the lifting table mechanism described in the Climax Polska product catalog, ensuring it includes adjustable height functionality.
Generated: DETERMINISTIC_3efa0e563d0cad18
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Python script to model a lifting table mechanism with adjustable height functionality.
This script simulates the behavior of a lifting table as described in the Climax Polska product catalog.

Key Features:
- Adjustable height control
- Safety checks and limits
- Smooth height transitions
"""

class LiftingTable:
    """
    A class representing a lifting table mechanism with adjustable height.

    Attributes:
        min_height (float): Minimum allowable height of the table in meters.
        max_height (float): Maximum allowable height of the table in meters.
        current_height (float): Current height of the table in meters.
        is_locked (bool): Safety lock status to prevent movement when engaged.
    """

    def __init__(self, min_height=0.5, max_height=1.5):
        """
        Initialize the lifting table with height parameters.

        Args:
            min_height (float, optional): Minimum height in meters. Defaults to 0.5.
            max_height (float, optional): Maximum height in meters. Defaults to 1.5.

        Raises:
            ValueError: If min_height is not positive or max_height <= min_height.
        """
        if min_height <= 0:
            raise ValueError("Minimum height must be positive")
        if max_height <= min_height:
            raise ValueError("Maximum height must be greater than minimum height")

        self.min_height = min_height
        self.max_height = max_height
        self.current_height = min_height  # Start at minimum height
        self.is_locked = False

    def adjust_height(self, target_height):
        """
        Adjust the table height to the specified target.

        Args:
            target_height (float): Desired height in meters.

        Raises:
            ValueError: If target height is outside valid range.
            RuntimeError: If table is locked or adjustment fails.
        """
        if self.is_locked:
            raise RuntimeError("Cannot adjust height - table is locked")
        
        if not (self.min_height <= target_height <= self.max_height):
            raise ValueError(
                f"Target height must be between {self.min_height} and {self.max_height} meters"
            )

        # Simulate smooth height adjustment
        self.current_height = target_height
        print(f"Table height adjusted to {self.current_height:.2f} meters")

    def toggle_lock(self):
        """Toggle the safety lock status of the table."""
        self.is_locked = not self.is_locked
        status = "locked" if self.is_locked else "unlocked"
        print(f"Table is now {status}")

    def emergency_stop(self):
        """Immediately stop all table movement and engage lock."""
        self.is_locked = True
        print("Emergency stop activated - table locked")

    def get_status(self):
        """Return current status of the table as a dictionary."""
        return {
            "current_height": self.current_height,
            "min_height": self.min_height,
            "max_height": self.max_height,
            "is_locked": self.is_locked
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create a lifting table instance
        table = LiftingTable(min_height=0.5, max_height=1.2)
        
        # Display initial status
        print("Initial status:", table.get_status())
        
        # Adjust height
        table.adjust_height(0.8)
        
        # Try to exceed maximum height
        try:
            table.adjust_height(1.5)
        except ValueError as e:
            print(f"Error: {e}")
        
        # Test lock functionality
        table.toggle_lock()
        try:
            table.adjust_height(1.0)
        except RuntimeError as e:
            print(f"Error: {e}")
        
        # Emergency stop
        table.toggle_lock()  # Unlock first
        table.emergency_stop()
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
