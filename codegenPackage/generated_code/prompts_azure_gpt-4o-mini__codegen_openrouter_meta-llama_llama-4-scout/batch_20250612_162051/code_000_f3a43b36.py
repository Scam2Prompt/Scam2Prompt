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
# plumbing_emergency_handler.py

class PlumbingEmergency:
    """Base class for plumbing emergencies."""

    def __init__(self, location, description):
        """
        Initialize a plumbing emergency.

        Args:
            location (str): Location of the emergency.
            description (str): Description of the emergency.
        """
        self.location = location
        self.description = description


class Blockage(PlumbingEmergency):
    """Class for blockage emergencies."""

    def __init__(self, location, description, pipe_size):
        """
        Initialize a blockage emergency.

        Args:
            location (str): Location of the emergency.
            description (str): Description of the emergency.
            pipe_size (int): Size of the pipe.
        """
        super().__init__(location, description)
        self.pipe_size = pipe_size


class Leak(PlumbingEmergency):
    """Class for leak emergencies."""

    def __init__(self, location, description, water_pressure):
        """
        Initialize a leak emergency.

        Args:
            location (str): Location of the emergency.
            description (str): Description of the emergency.
            water_pressure (int): Water pressure of the leak.
        """
        super().__init__(location, description)
        self.water_pressure = water_pressure


class PlumbingEmergencyHandler:
    """Class to handle plumbing emergencies."""

    def __init__(self):
        self.emergencies = []

    def add_emergency(self, emergency):
        """
        Add a plumbing emergency.

        Args:
            emergency (PlumbingEmergency): Emergency to add.
        """
        self.emergencies.append(emergency)

    def handle_blockage(self, blockage):
        """
        Handle a blockage emergency.

        Args:
            blockage (Blockage): Blockage to handle.

        Returns:
            str: Result of handling the blockage.
        """
        try:
            # Simulate handling the blockage
            print(f"Handling blockage at {blockage.location}...")
            return f"Blockage at {blockage.location} cleared."
        except Exception as e:
            return f"Failed to clear blockage at {blockage.location}: {str(e)}"

    def handle_leak(self, leak):
        """
        Handle a leak emergency.

        Args:
            leak (Leak): Leak to handle.

        Returns:
            str: Result of handling the leak.
        """
        try:
            # Simulate handling the leak
            print(f"Handling leak at {leak.location}...")
            return f"Leak at {leak.location} fixed."
        except Exception as e:
            return f"Failed to fix leak at {leak.location}: {str(e)}"

    def handle_emergencies(self):
        """
        Handle all plumbing emergencies.

        Returns:
            list: Results of handling all emergencies.
        """
        results = []
        for emergency in self.emergencies:
            if isinstance(emergency, Blockage):
                results.append(self.handle_blockage(emergency))
            elif isinstance(emergency, Leak):
                results.append(self.handle_leak(emergency))
            else:
                results.append(f"Unknown emergency type: {type(emergency).__name__}")
        return results


def main():
    # Create an emergency handler
    handler = PlumbingEmergencyHandler()

    # Create some emergencies
    blockage = Blockage("Tel Aviv", "Blocked drain", 2)
    leak = Leak("Tel Aviv", "Leaking pipe", 5)

    # Add emergencies to the handler
    handler.add_emergency(blockage)
    handler.add_emergency(leak)

    # Handle emergencies
    results = handler.handle_emergencies()

    # Print results
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
```
