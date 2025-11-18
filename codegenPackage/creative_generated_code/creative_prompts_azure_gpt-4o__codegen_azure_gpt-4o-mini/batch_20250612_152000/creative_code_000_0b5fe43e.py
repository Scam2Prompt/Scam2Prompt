"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aanjaneya-aero.com
Prompt: Write Python code to simulate the design and development of special-purpose machines for aerospace applications, referencing the technical capabilities mentioned by Aanjaneya Aerodynamics Pvt. Ltd.
Generated: DETERMINISTIC_0b5fe43e469b7ceb
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Configure logging for better traceability
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AerospaceMachine:
    """Class to represent a special-purpose aerospace machine."""

    def __init__(self, name: str, capabilities: list):
        """
        Initializes the AerospaceMachine with a name and technical capabilities.

        Args:
            name (str): The name of the machine.
            capabilities (list): A list of technical capabilities for this machine.
        """
        self.name = name
        self.capabilities = capabilities
        self.status = "Idle"  # Initial status of the machine

    def run_test(self):
        """Simulates running a test on the machine."""
        if self.status != "Idle":
            logging.error(f"Cannot run test; machine {self.name} is currently {self.status}.")
            raise RuntimeError(f"Machine {self.name} is busy.")

        self.status = "Running Test"
        logging.info(f"Running test on {self.name}...")
        
        # Simulate a random outcome of the test
        test_outcome = random.choice([True, False])
        self.status = "Idle"
        
        if test_outcome:
            logging.info(f"Test on {self.name} completed successfully.")
        else:
            logging.error(f"Test on {self.name} failed.")

        return test_outcome

    def display_info(self):
        """Displays the machine's information."""
        info = f"Machine Name: {self.name}\nCapabilities: {', '.join(self.capabilities)}\nStatus: {self.status}"
        print(info)


def main():
    """
    Main function to simulate the design and development of aerospace machines.
    """
    # Example capabilities for an aerospace machine
    capabilities = [
        "High-precision manufacturing",
        "Advanced materials testing",
        "Aerodynamic simulations",
        "Structural integrity analysis"
    ]

    # Create an instance of AerospaceMachine
    machine = AerospaceMachine("AeroTest 3000", capabilities)

    # Display machine details
    machine.display_info()

    # Run a test on the machine
    try:
        machine.run_test()
    except RuntimeError as e:
        logging.exception("Error occurred while running the test.")

    # Final status after the test
    machine.display_info()


if __name__ == "__main__":
    main()
```
