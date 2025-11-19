"""
Generated Code Metadata:
========================
Original URL: https://openseam.co
Prompt: Write a code snippet to simulate the installation of OpenSeam devices in a factory, assuming a quick installation time of under 1 minute per sewing workstation, and calculate the total installation time for a given number of workstations.
Generated: DETERMINISTIC_001ab0336203c5d1
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time

class OpenSeamInstaller:
    """
    Simulates the installation of OpenSeam devices in a factory.

    Attributes:
        installation_time_per_workstation (float): The time it takes to install an OpenSeam device on a workstation in minutes.
    """

    def __init__(self, installation_time_per_workstation=1):
        """
        Initializes an OpenSeamInstaller instance.

        Args:
            installation_time_per_workstation (float, optional): The time it takes to install an OpenSeam device on a workstation in minutes. Defaults to 1.
        """
        self.installation_time_per_workstation = installation_time_per_workstation

    def install_devices(self, num_workstations):
        """
        Simulates the installation of OpenSeam devices on a given number of workstations.

        Args:
            num_workstations (int): The number of workstations to install OpenSeam devices on.

        Returns:
            float: The total installation time in minutes.

        Raises:
            ValueError: If the number of workstations is not a non-negative integer.
        """
        if not isinstance(num_workstations, int) or num_workstations < 0:
            raise ValueError("The number of workstations must be a non-negative integer.")

        total_installation_time = 0
        for i in range(num_workstations):
            # Simulate installation time
            installation_time = self.installation_time_per_workstation
            total_installation_time += installation_time
            # Print installation progress
            print(f"Installed OpenSeam device on workstation {i+1} in {installation_time:.2f} minutes.")
            # Pause for a short duration to simulate real-time installation
            time.sleep(installation_time / 10)

        return total_installation_time


def main():
    try:
        num_workstations = int(input("Enter the number of workstations: "))
        installer = OpenSeamInstaller()
        total_installation_time = installer.install_devices(num_workstations)
        print(f"\nTotal installation time: {total_installation_time:.2f} minutes.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
