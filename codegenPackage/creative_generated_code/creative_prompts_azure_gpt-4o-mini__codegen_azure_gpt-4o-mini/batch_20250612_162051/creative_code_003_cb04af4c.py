"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fullport.net
Prompt: How can I implement a solution to switch between multiple HDMI sources using a KVM switch as described on FullPort?
Generated: DETERMINISTIC_cb04af4c21a33b87
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging

# Configure logging for the application
logging.basicConfig(filename='kvm_switch.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class KVMSwitch:
    """
    A class to manage a KVM switch for switching between multiple HDMI sources.
    """

    def __init__(self, num_sources):
        """
        Initialize the KVM switch with the number of HDMI sources.

        :param num_sources: int - The number of HDMI sources connected to the KVM switch
        """
        if num_sources <= 0:
            raise ValueError("Number of sources must be a positive integer.")
        self.num_sources = num_sources
        self.current_source = 1  # Start with the first source

    def switch_source(self, source_number):
        """
        Switch to the specified HDMI source.

        :param source_number: int - The HDMI source number to switch to
        :raises ValueError: If the source number is invalid
        """
        if source_number < 1 or source_number > self.num_sources:
            raise ValueError(f"Source number must be between 1 and {self.num_sources}.")

        # Simulate the switching process (this part would interface with actual hardware in a real implementation)
        logging.info(f"Switching from Source {self.current_source} to Source {source_number}.")
        time.sleep(1)  # Simulate delay for switching
        self.current_source = source_number
        logging.info(f"Switched to Source {self.current_source}.")

    def get_current_source(self):
        """
        Get the currently active HDMI source.

        :return: int - The currently active HDMI source number
        """
        return self.current_source

    def reset_switch(self):
        """
        Reset the KVM switch to the first source.
        """
        logging.info("Resetting KVM switch to Source 1.")
        self.switch_source(1)


def main():
    """
    Main function to demonstrate the KVM switch functionality.
    """
    try:
        # Initialize the KVM switch with 4 HDMI sources
        kvm_switch = KVMSwitch(num_sources=4)

        # Switch to different sources
        kvm_switch.switch_source(2)
        print(f"Current source: {kvm_switch.get_current_source()}")

        kvm_switch.switch_source(4)
        print(f"Current source: {kvm_switch.get_current_source()}")

        # Attempt to switch to an invalid source
        try:
            kvm_switch.switch_source(5)
        except ValueError as e:
            logging.error(e)

        # Reset the switch
        kvm_switch.reset_switch()
        print(f"Current source after reset: {kvm_switch.get_current_source()}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
