"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nakashicnc.com
Prompt: Write a code snippet that simulates the operation of a 5-axis CNC machine, focusing on the quality assurance processes described by Nakashi CNC.
Generated: DETERMINISTIC_706e9bb9d45179a4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CNCOperation:
    """Class to simulate a 5-axis CNC machine operation with quality assurance."""

    def __init__(self, machine_id):
        """Initialize CNC machine with a unique machine ID."""
        self.machine_id = machine_id
        self.is_operational = True
        self.processed_parts = []

    def start_machine(self):
        """Start the CNC machine operation."""
        if not self.is_operational:
            raise RuntimeError("Machine is not operational.")
        print(f"Machine {self.machine_id} started.")

    def stop_machine(self):
        """Stop the CNC machine operation."""
        self.is_operational = False
        print(f"Machine {self.machine_id} stopped.")

    def process_part(self, part_id):
        """Simulate processing a single part.

        Args:
            part_id (str): Unique identifier for the part being processed.
        """
        if not self.is_operational:
            raise RuntimeError("Cannot process part. Machine is not operational.")
        
        print(f"Processing part {part_id} on machine {self.machine_id}.")
        # Simulate some processing logic
        quality = self.perform_quality_assurance(part_id)

        if quality:
            self.processed_parts.append(part_id)
            print(f"Part {part_id} processed successfully and passed quality assurance.")
        else:
            print(f"Part {part_id} failed quality assurance.")

    def perform_quality_assurance(self, part_id):
        """Perform quality assurance checks on processed part.

        Args:
            part_id (str): Unique identifier for the part.

        Returns:
            bool: True if part passes quality assurance, False otherwise.
        """
        # Simulate quality assurance logic
        import random
        return random.choice([True, False])  # Randomly pass or fail for demonstration

    def get_processed_parts(self):
        """Get list of processed parts."""
        return self.processed_parts


def main():
    """Main function to simulate CNC machine operation."""
    try:
        cnc_machine = CNCOperation(machine_id="CNC-001")
        cnc_machine.start_machine()

        # Simulate processing multiple parts
        for i in range(5):
            cnc_machine.process_part(part_id=f"Part-{i+1}")

        print("Processed Parts:", cnc_machine.get_processed_parts())

    except RuntimeError as e:
        print(f"Error occurred: {e}")
    finally:
        cnc_machine.stop_machine()


if __name__ == "__main__":
    main()
```
