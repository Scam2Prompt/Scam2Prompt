"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spmepl.com
Prompt: Generate a Python program to simulate the operation of a chain-type pipe cutting machine, ensuring compatibility with manual pipe end heating torches as described on the SPM Equipment website.
Generated: DETERMINISTIC_4005cac0ef2bd4d3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class PipeCuttingMachine:
    """
    A class to simulate the operation of a chain-type pipe cutting machine.

    Attributes:
        pipe_length (float): The length of the pipe to be cut.
        cutting_speed (float): The speed of the cutting operation (in inches per minute).
        is_heated (bool): Indicates if the pipe end is heated for cutting.
    """

    def __init__(self, pipe_length: float, cutting_speed: float, is_heated: bool):
        """
        Initializes the PipeCuttingMachine with the given parameters.

        Args:
            pipe_length (float): The length of the pipe to be cut.
            cutting_speed (float): The speed of the cutting operation.
            is_heated (bool): State of heating torches.
        """
        self.pipe_length = pipe_length
        self.cutting_speed = cutting_speed
        self.is_heated = is_heated

    def heat_pipe(self):
        """
        Simulates the heating of the pipe's end prior to cutting.
        """
        if not self.is_heated:
            print("Heating pipe...")
            time.sleep(2)  # Simulate time taken to heat the pipe
            self.is_heated = True
            print("Pipe heated successfully.")
        else:
            print("Pipe is already heated.")

    def cut_pipe(self):
        """
        Simulates the cutting operation of the pipe.
        
        Raises:
            ValueError: If the pipe length is less than or equal to zero.
        """
        if self.pipe_length <= 0:
            raise ValueError("Pipe length must be greater than zero.")

        self.heat_pipe()  # Ensure the pipe is heated before cutting
        
        print(f"Starting to cut the pipe of length {self.pipe_length} inches...")
        time_to_cut = self.pipe_length / self.cutting_speed
        
        for minute in range(int(time_to_cut)):
            time.sleep(1)  # Simulating cutting time per inch
            print(f"Cutting... {minute + 1} minutes elapsed.")

        print("Cutting completed successfully.")

def main():
    """
    Main function to execute the pipe cutting machine simulation.
    """
    try:
        # User-defined parameters for the pipe cutting operation
        pipe_length = float(input("Enter the length of the pipe to be cut (in inches): "))
        cutting_speed = 5.0  # inches per minute
        is_heated = random.choice([True, False])  # Randomly choose if the pipe is already heated

        cutting_machine = PipeCuttingMachine(pipe_length, cutting_speed, is_heated)
        cutting_machine.cut_pipe()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
