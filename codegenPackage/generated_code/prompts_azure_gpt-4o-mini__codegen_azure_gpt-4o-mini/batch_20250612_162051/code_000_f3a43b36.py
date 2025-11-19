"""
Generated Code Metadata:
========================
Original URL: https://shravrav1.co.il
Prompt: Write a Python function to handle plumbing emergencies, including opening blockages and fixing leaks, as described by the plumbing services in Tel Aviv.
Generated: DETERMINISTIC_f3a43b36db52086d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PlumbingEmergency:
    """A class to handle plumbing emergencies such as blockages and leaks."""

    def __init__(self):
        """Initialize the plumbing emergency handler."""
        self.blockages = []
        self.leaks = []

    def report_blockage(self, location: str) -> None:
        """
        Report a blockage at a specified location.

        Args:
            location (str): The location of the blockage.
        """
        if not location:
            raise ValueError("Location cannot be empty.")
        self.blockages.append(location)
        print(f"Blockage reported at: {location}")

    def report_leak(self, location: str) -> None:
        """
        Report a leak at a specified location.

        Args:
            location (str): The location of the leak.
        """
        if not location:
            raise ValueError("Location cannot be empty.")
        self.leaks.append(location)
        print(f"Leak reported at: {location}")

    def fix_blockage(self, location: str) -> None:
        """
        Fix a blockage at the specified location.

        Args:
            location (str): The location of the blockage to fix.

        Raises:
            ValueError: If the blockage is not found.
        """
        if location not in self.blockages:
            raise ValueError(f"No blockage found at: {location}")
        self.blockages.remove(location)
        print(f"Blockage fixed at: {location}")

    def fix_leak(self, location: str) -> None:
        """
        Fix a leak at the specified location.

        Args:
            location (str): The location of the leak to fix.

        Raises:
            ValueError: If the leak is not found.
        """
        if location not in self.leaks:
            raise ValueError(f"No leak found at: {location}")
        self.leaks.remove(location)
        print(f"Leak fixed at: {location}")

    def get_report(self) -> dict:
        """
        Get a report of all current blockages and leaks.

        Returns:
            dict: A dictionary containing lists of blockages and leaks.
        """
        return {
            "blockages": self.blockages,
            "leaks": self.leaks
        }


# Example usage
if __name__ == "__main__":
    plumbing_service = PlumbingEmergency()
    
    try:
        plumbing_service.report_blockage("Main Street")
        plumbing_service.report_leak("Second Avenue")
        print(plumbing_service.get_report())
        
        plumbing_service.fix_blockage("Main Street")
        plumbing_service.fix_leak("Second Avenue")
        print(plumbing_service.get_report())
        
    except ValueError as e:
        print(f"Error: {e}")
```
