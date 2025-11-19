"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: Write code to simulate the construction of tennis courts with security features and top-tier materials, inspired by C&M Pinnacle's Goldfields Tennis Court project.
Generated: DETERMINISTIC_5235d25427f7aba2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TennisCourt:
    """
    A class to represent a tennis court with security features and top-tier materials.
    """

    def __init__(self, surface_type, lighting, fencing, security_system):
        """
        Initializes a new TennisCourt instance.

        :param surface_type: str - Type of surface (e.g., 'hard', 'clay', 'grass')
        :param lighting: bool - Whether the court has lighting
        :param fencing: bool - Whether the court is fenced
        :param security_system: str - Type of security system (e.g., 'CCTV', 'alarm')
        """
        self.surface_type = surface_type
        self.lighting = lighting
        self.fencing = fencing
        self.security_system = security_system

    def display_court_details(self):
        """
        Displays the details of the tennis court.
        """
        print("Tennis Court Details:")
        print(f"Surface Type: {self.surface_type}")
        print(f"Lighting: {'Yes' if self.lighting else 'No'}")
        print(f"Fencing: {'Yes' if self.fencing else 'No'}")
        print(f"Security System: {self.security_system}")

    def upgrade_security(self, new_security_system):
        """
        Upgrades the security system of the tennis court.

        :param new_security_system: str - New type of security system
        """
        if not new_security_system:
            raise ValueError("New security system must be a valid string.")
        self.security_system = new_security_system
        print(f"Security system upgraded to: {self.security_system}")

    def toggle_lighting(self):
        """
        Toggles the lighting of the tennis court.
        """
        self.lighting = not self.lighting
        print(f"Lighting turned {'on' if self.lighting else 'off'}.")

    def is_ready_for_play(self):
        """
        Checks if the court is ready for play based on its features.

        :return: bool - True if the court is ready, False otherwise
        """
        return self.surface_type in ['hard', 'clay', 'grass'] and self.fencing and self.security_system is not None


def main():
    """
    Main function to simulate the construction of a tennis court.
    """
    try:
        # Create a new tennis court instance
        court = TennisCourt(surface_type='hard', lighting=True, fencing=True, security_system='CCTV')

        # Display court details
        court.display_court_details()

        # Upgrade the security system
        court.upgrade_security('Advanced CCTV')

        # Toggle lighting
        court.toggle_lighting()

        # Check if the court is ready for play
        if court.is_ready_for_play():
            print("The tennis court is ready for play!")
        else:
            print("The tennis court is not ready for play.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
