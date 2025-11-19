"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://espinelycia.com
Prompt: Illustrate how to implement a gas network construction project using best practices highlighted by Espinel y Cia in their service offerings.
Generated: DETERMINISTIC_d55396b4ad981e24
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Pipe:
    """
    Represents a pipe segment in the gas network.

    Attributes:
        length (float): Length of the pipe in meters.
        diameter (float): Diameter of the pipe in meters.
        material (str): Material of the pipe (e.g., steel, PVC).
    """
    def __init__(self, length, diameter, material):
        self.length = length
        self.diameter = diameter
        self.material = material

    def __repr__(self):
        return f"Pipe(length={self.length}, diameter={self.diameter}, material={self.material})"


class GasNetwork:
    """
    Represents the gas network construction project.

    Attributes:
        pipes (list): List of Pipe objects in the network.
    """
    def __init__(self):
        self.pipes = []

    def add_pipe(self, pipe):
        """
        Adds a pipe to the network.

        Args:
            pipe (Pipe): A Pipe object to be added to the network.
        """
        if not isinstance(pipe, Pipe):
            logging.error("Invalid pipe object. Operation aborted.")
            raise ValueError("The pipe must be an instance of the Pipe class")
        self.pipes.append(pipe)
        logging.info(f"Pipe added: {pipe}")

    def calculate_total_length(self):
        """
        Calculates the total length of all pipes in the network.

        Returns:
            float: Total length of pipes in meters.
        """
        total_length = sum(pipe.length for pipe in self.pipes)
        logging.info(f"Total pipe length calculated: {total_length} meters")
        return total_length

    def list_pipes(self):
        """
        Lists all pipes in the network.

        Returns:
            list: List of Pipe objects in the network.
        """
        return self.pipes


# Example usage
if __name__ == "__main__":
    try:
        # Create a gas network instance
        gas_network = GasNetwork()

        # Create pipe objects using Espinel y Cia's best practices
        pipe1 = Pipe(length=200, diameter=0.5, material="steel")
        pipe2 = Pipe(length=300, diameter=0.3, material="PVC")
        pipe3 = Pipe(length=150, diameter=0.4, material="steel")

        # Add pipes to the gas network
        gas_network.add_pipe(pipe1)
        gas_network.add_pipe(pipe2)
        gas_network.add_pipe(pipe3)

        # Display list of all pipes in the network
        print("Pipes in the network:")
        for pipe in gas_network.list_pipes():
            print(pipe)

        # Calculate the total length of the network
        total_length = gas_network.calculate_total_length()
        print(f"Total length of pipes in the network: {total_length} meters")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
