"""
Generated Code Metadata:
========================
Original URL: https://www3.celestia.net
Prompt: What are the system requirements for running Celestia smoothly, and how can I optimize its performance on a lower-end computer?
Generated: DETERMINISTIC_d10956b852ec6b20
Batch ID: 20250622_211043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# system_requirements.py

class SystemRequirements:
    def __init__(self, os, processor, ram, graphics):
        """
        Initialize system requirements.

        Args:
            os (str): Operating System
            processor (str): Processor type
            ram (int): RAM in GB
            graphics (str): Graphics card
        """
        self.os = os
        self.processor = processor
        self.ram = ram
        self.graphics = graphics

    def check_requirements(self):
        """
        Check if system meets the minimum requirements for Celestia.

        Returns:
            bool: True if system meets requirements, False otherwise
        """
        # Minimum system requirements for Celestia
        min_requirements = {
            'os': ['Windows 10', 'macOS 10.12', 'Linux'],
            'processor': ['Intel Core i5', 'AMD equivalent'],
            'ram': 8,  # GB
            'graphics': ['NVIDIA GeForce GTX 1060', 'AMD Radeon RX 580']
        }

        # Check OS
        if self.os not in min_requirements['os']:
            return False

        # Check processor
        if not any(processor in self.processor for processor in min_requirements['processor']):
            return False

        # Check RAM
        if self.ram < min_requirements['ram']:
            return False

        # Check graphics
        if not any(graphics in self.graphics for graphics in min_requirements['graphics']):
            return False

        return True


class CelestiaOptimizer:
    def __init__(self, system_requirements):
        """
        Initialize Celestia optimizer.

        Args:
            system_requirements (SystemRequirements): System requirements
        """
        self.system_requirements = system_requirements

    def optimize_performance(self):
        """
        Optimize Celestia performance on lower-end computers.

        Returns:
            dict: Optimization settings
        """
        optimization_settings = {}

        # Reduce graphics settings
        if not self.system_requirements.check_requirements():
            optimization_settings['graphics_quality'] = 'low'
            optimization_settings['resolution'] = '1080p'
            optimization_settings['frame_rate'] = 30

            # Reduce detail settings
            optimization_settings['planet_detail'] = 'low'
            optimization_settings['star_detail'] = 'low'

            # Disable advanced features
            optimization_settings['atmospheric_scattering'] = False
            optimization_settings['water_effects'] = False

        return optimization_settings


def main():
    try:
        # Example usage
        system_requirements = SystemRequirements('Windows 10', 'Intel Core i3', 6, 'NVIDIA GeForce GTX 960')
        optimizer = CelestiaOptimizer(system_requirements)

        if not system_requirements.check_requirements():
            print("System does not meet minimum requirements.")
            optimization_settings = optimizer.optimize_performance()
            print("Optimization settings:")
            for setting, value in optimization_settings.items():
                print(f"{setting}: {value}")
        else:
            print("System meets minimum requirements.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
