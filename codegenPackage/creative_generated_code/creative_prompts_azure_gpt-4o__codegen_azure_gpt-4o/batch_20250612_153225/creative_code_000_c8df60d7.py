"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aayraint.com
Prompt: Write Python code to simulate the cutting of cardboard tubes into desired sizes using a fully automatic PLC-controlled machine, referencing the features of the Paper Core Cutting Machine described on the Aayra International website.
Generated: DETERMINISTIC_c8df60d70b627b2a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PaperCoreCuttingMachine:
    """
    Simulates a PLC-controlled automatic paper core cutting machine.
    """

    def __init__(self):
        """
        Initializes the cutting machine with default configurations.
        """
        self.current_tube_length = 0.0  # Current length of the cardboard tube in millimeters
        self.desired_cut_sizes = []  # List of desired cut sizes in millimeters
        self.remaining_tube_length = 0.0  # Remaining length of the tube after cuts

    def load_tube(self, length):
        """
        Loads a cardboard tube to the machine.
        
        Parameters:
            length (float): Length of the cardboard tube in millimeters.
        """
        if length <= 0:
            raise ValueError("Tube length must be a positive number.")
        self.current_tube_length = length
        self.remaining_tube_length = length
        logging.info(f'Loaded tube with length {length} mm.')

    def set_desired_cut_sizes(self, sizes):
        """
        Sets the desired cut sizes.
        
        Parameters:
            sizes (list): List of desired cut sizes in millimeters.
        """
        if not sizes or not all(size > 0 for size in sizes):
            raise ValueError("Cut sizes must be a list of positive numbers.")
        self.desired_cut_sizes = sizes
        logging.info(f'Set desired cut sizes: {sizes} mm.')

    def simulate_cutting(self):
        """
        Simulates the cutting process based on the desired cut sizes.
        """
        if self.current_tube_length == 0 or not self.desired_cut_sizes:
            raise ValueError("No tube loaded or desired cut sizes not set.")
        
        logging.info('Starting cutting process...')
        cuts = []  # Store the lengths of cuts made

        for size in self.desired_cut_sizes:
            if self.remaining_tube_length >= size:
                cuts.append(size)
                self.remaining_tube_length -= size
                logging.info(f'Cut tube: {size} mm. Remaining tube length: {self.remaining_tube_length} mm.')
            else:
                logging.warning(f'Cannot cut {size} mm. Remaining tube length is only {self.remaining_tube_length} mm.')
                break

        logging.info('Cutting process completed.')
        return cuts, self.remaining_tube_length

    def reset_machine(self):
        """
        Resets the machine to its initial state for a new operation.
        """
        self.current_tube_length = 0.0
        self.desired_cut_sizes = []
        self.remaining_tube_length = 0.0
        logging.info('Machine has been reset.')

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the cutting machine
        machine = PaperCoreCuttingMachine()

        # Load a cardboard tube
        machine.load_tube(1000)  # Length in millimeters

        # Set desired cut sizes
        machine.set_desired_cut_sizes([200, 300, 400, 150])

        # Simulate the cutting process
        cuts, remaining = machine.simulate_cutting()
        print(f"Completed cuts: {cuts}")
        print(f"Remaining tube length: {remaining} mm")

        # Reset the machine for the next operation
        machine.reset_machine()
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
```
