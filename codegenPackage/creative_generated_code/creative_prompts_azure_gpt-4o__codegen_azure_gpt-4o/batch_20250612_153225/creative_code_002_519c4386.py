"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shelterder.com
Prompt: Generate code to integrate a gas fireplace system with both GLP and natural gas options, ensuring safety with a fully glass-enclosed design.
Generated: DETERMINISTIC_519c438613f76c5c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Gas Fireplace System Integration Code
This script controls a gas fireplace system with support for both GLP (Liquefied Petroleum Gas) and natural gas options.
Safety features include proper error handling and a full glass-enclosure design.
"""

import time

class GasFireplaceSystem:
    def __init__(self):
        """
        Initialize the fireplace system with default settings.
        """
        self.gas_type = None  # 'GLP' or 'Natural Gas'
        self.is_running = False  # Fireplace status
        self.glass_enclosure_status = False  # Ensure glass enclosure is secure

    def set_gas_type(self, gas_type):
        """
        Set the type of gas to be used (GLP or Natural Gas).
        :param gas_type: str - 'GLP' or 'Natural Gas'
        """
        if gas_type not in ['GLP', 'Natural Gas']:
            raise ValueError("Invalid gas type. Please choose 'GLP' or 'Natural Gas'.")
        self.gas_type = gas_type
        print(f"Gas type set to: {self.gas_type}")

    def check_glass_enclosure(self):
        """
        Simulate checking if the glass enclosure is properly secured.
        """
        # Simulated hardware check for glass enclosure
        self.glass_enclosure_status = True  # Always returns True for this example
        if not self.glass_enclosure_status:
            raise RuntimeError("Safety error: Glass enclosure is not secured!")
        print("Glass enclosure is properly secured.")

    def ignite_fireplace(self):
        """
        Ignite the fireplace system safely.
        """
        if self.gas_type is None:
            raise RuntimeError("Gas type is not set. Please set the gas type before igniting the fireplace.")
        
        if not self.glass_enclosure_status:
            raise RuntimeError("Safety error: Glass enclosure is not secured!")

        self.is_running = True
        print(f"Fireplace is now running using {self.gas_type}. Enjoy the warmth!")

    def extinguish_fireplace(self):
        """
        Safely extinguish the fireplace.
        """
        if not self.is_running:
            print("Fireplace is already off.")
            return

        self.is_running = False
        print("Fireplace has been safely extinguished.")

    def system_status(self):
        """
        Get the current status of the fireplace system.
        """
        status = {
            "Gas Type": self.gas_type,
            "Is Running": self.is_running,
            "Glass Enclosure Secured": self.glass_enclosure_status
        }
        return status


def main():
    """
    Main function to simulate the operation of the gas fireplace system.
    """
    try:
        fireplace = GasFireplaceSystem()

        # Set the gas type (choose 'GLP' or 'Natural Gas')
        fireplace.set_gas_type('Natural Gas')

        # Check if the glass enclosure is properly secured
        fireplace.check_glass_enclosure()

        # Ignite the fireplace
        fireplace.ignite_fireplace()

        # Simulate the fireplace running for a while
        time.sleep(5)

        # Print the current status
        print("System Status:", fireplace.system_status())

        # Extinguish the fireplace
        fireplace.extinguish_fireplace()

        # Print the status after extinguishing
        print("System Status:", fireplace.system_status())

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
```
