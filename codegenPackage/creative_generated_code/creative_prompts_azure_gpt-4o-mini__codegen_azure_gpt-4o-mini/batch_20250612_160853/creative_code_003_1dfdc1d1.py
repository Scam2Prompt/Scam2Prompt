"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://novaforma.hr
Prompt: What are the best practices for using CNC technology in creating marketing materials, as described by Nova Forma?
Generated: DETERMINISTIC_1dfdc1d123b06ba3
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# cnc_marketing_materials.py

class CNCMachine:
    """A class representing a CNC machine used for creating marketing materials."""

    def __init__(self, machine_id):
        """
        Initializes the CNC machine with a unique identifier.
        
        Args:
            machine_id (str): The unique identifier for the CNC machine.
        """
        self.machine_id = machine_id
        self.is_operational = True

    def check_operational_status(self):
        """Checks if the CNC machine is operational."""
        if not self.is_operational:
            raise RuntimeError("CNC machine is not operational.")
        return True

    def create_material(self, material_type, design):
        """
        Creates marketing material using the CNC machine.
        
        Args:
            material_type (str): The type of marketing material to be created.
            design (str): The design file for the marketing material.

        Raises:
            ValueError: If the material type or design is not valid.
            RuntimeError: If the machine is not operational.
        """
        # Check if the machine is operational
        self.check_operational_status()

        # Validate input
        if not material_type or not design:
            raise ValueError("Material type and design cannot be empty.")
        
        # Simulate the creation process
        print(f"Creating {material_type} with design: {design} using CNC machine {self.machine_id}...")

        # Simulating some processing time
        import time
        time.sleep(2)  # Simulates time taken to create the material

        print(f"{material_type} creation completed successfully.")

    def shut_down(self):
        """Shuts down the CNC machine."""
        self.is_operational = False
        print(f"CNC machine {self.machine_id} has been shut down.")


def main():
    """Main function to demonstrate CNC machine usage for marketing materials."""
    try:
        # Create an instance of CNCMachine
        cnc_machine = CNCMachine(machine_id="CNC-001")

        # Create marketing material
        cnc_machine.create_material("Brochure", "brochure_design.svg")
        cnc_machine.create_material("Signage", "signage_design.svg")

    except ValueError as ve:
        print(f"Value error: {ve}")
    except RuntimeError as re:
        print(f"Runtime error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Ensure the machine is shut down
        cnc_machine.shut_down()


if __name__ == "__main__":
    main()
```
