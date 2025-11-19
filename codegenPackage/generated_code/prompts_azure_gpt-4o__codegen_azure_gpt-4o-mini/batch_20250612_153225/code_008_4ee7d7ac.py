"""
Generated Code Metadata:
========================
Original URL: https://tibvanboxtel.nl
Prompt: Write a program to simulate the installation process for a solar panel system with micro-inverters, following the guidelines provided by Technische Installatiebedrijf van Boxtel.
Generated: DETERMINISTIC_4ee7d7ace32318d1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random

class SolarPanelSystem:
    def __init__(self, num_panels):
        """
        Initialize the solar panel system with a specified number of panels.
        
        :param num_panels: Number of solar panels in the system
        """
        self.num_panels = num_panels
        self.installed_panels = 0
        self.micro_inverters = []

    def install_panel(self):
        """
        Simulate the installation of a single solar panel with a micro-inverter.
        """
        if self.installed_panels < self.num_panels:
            time.sleep(random.uniform(0.5, 1.5))  # Simulate installation time
            self.micro_inverters.append(self._install_micro_inverter())
            self.installed_panels += 1
            print(f"Installed panel {self.installed_panels} with micro-inverter.")
        else:
            raise Exception("All panels have already been installed.")

    def _install_micro_inverter(self):
        """
        Simulate the installation of a micro-inverter.
        
        :return: A unique identifier for the installed micro-inverter
        """
        inverter_id = f"MI-{self.installed_panels + 1}"
        time.sleep(random.uniform(0.2, 0.5))  # Simulate inverter installation time
        return inverter_id

    def install_system(self):
        """
        Simulate the installation process for the entire solar panel system.
        """
        print("Starting installation of solar panel system...")
        for _ in range(self.num_panels):
            try:
                self.install_panel()
            except Exception as e:
                print(f"Error during installation: {e}")
                break
        print("Installation process completed.")

def main():
    """
    Main function to execute the solar panel installation simulation.
    """
    try:
        num_panels = int(input("Enter the number of solar panels to install: "))
        if num_panels <= 0:
            raise ValueError("Number of panels must be a positive integer.")
        
        solar_system = SolarPanelSystem(num_panels)
        solar_system.install_system()
        
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
