"""
Generated Code Metadata:
========================
Original URL: https://udizine.com
Prompt: Create a script that generates assembly instructions for UDIZINE's modular shelving systems, including Vertik and Palo systems, based on user-selected configurations.
Generated: DETERMINISTIC_4852c9d52f631fed
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# udizine_shelving_generator.py

class ShelvingSystem:
    def __init__(self, system_type, width, height, depth, num_shelves):
        """
        Initialize a shelving system.

        Args:
            system_type (str): Type of shelving system (Vertik or Palo).
            width (int): Width of the shelving system in mm.
            height (int): Height of the shelving system in mm.
            depth (int): Depth of the shelving system in mm.
            num_shelves (int): Number of shelves in the shelving system.
        """
        self.system_type = system_type
        self.width = width
        self.height = height
        self.depth = depth
        self.num_shelves = num_shelves

    def generate_assembly_instructions(self):
        """
        Generate assembly instructions for the shelving system.

        Returns:
            list: List of assembly instructions.
        """
        instructions = []

        if self.system_type == "Vertik":
            instructions.extend(self.generate_vertik_instructions())
        elif self.system_type == "Palo":
            instructions.extend(self.generate_palo_instructions())
        else:
            raise ValueError("Invalid system type. Must be 'Vertik' or 'Palo'.")

        return instructions

    def generate_vertik_instructions(self):
        """
        Generate assembly instructions for a Vertik shelving system.

        Returns:
            list: List of assembly instructions.
        """
        instructions = [
            f"Prepare {self.num_shelves + 2} Vertik uprights (Part A).",
            f"Cut {self.num_shelves} shelves (Part B) to width {self.width}mm and depth {self.depth}mm.",
            f"Assemble shelves to uprights using shelf clips (Part C).",
            f"Secure uprights to floor using floor anchors (Part D).",
            f"Add top and bottom panels (Part E) to complete shelving system."
        ]

        shelf_height = self.height // (self.num_shelves + 1)
        for i in range(self.num_shelves):
            instructions.append(f"Install shelf {i+1} at height {(i+1) * shelf_height}mm.")

        return instructions

    def generate_palo_instructions(self):
        """
        Generate assembly instructions for a Palo shelving system.

        Returns:
            list: List of assembly instructions.
        """
        instructions = [
            f"Prepare {self.num_shelves + 2} Palo uprights (Part F).",
            f"Cut {self.num_shelves} shelves (Part G) to width {self.width}mm and depth {self.depth}mm.",
            f"Assemble shelves to uprights using shelf supports (Part H).",
            f"Secure uprights to wall using wall brackets (Part I).",
            f"Add top and bottom panels (Part J) to complete shelving system."
        ]

        shelf_height = self.height // (self.num_shelves + 1)
        for i in range(self.num_shelves):
            instructions.append(f"Install shelf {i+1} at height {(i+1) * shelf_height}mm.")

        return instructions


def main():
    try:
        system_type = input("Enter shelving system type (Vertik or Palo): ")
        width = int(input("Enter width (mm): "))
        height = int(input("Enter height (mm): "))
        depth = int(input("Enter depth (mm): "))
        num_shelves = int(input("Enter number of shelves: "))

        shelving_system = ShelvingSystem(system_type, width, height, depth, num_shelves)
        instructions = shelving_system.generate_assembly_instructions()

        print("\nAssembly Instructions:")
        for i, instruction in enumerate(instructions, start=1):
            print(f"{i}. {instruction}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
