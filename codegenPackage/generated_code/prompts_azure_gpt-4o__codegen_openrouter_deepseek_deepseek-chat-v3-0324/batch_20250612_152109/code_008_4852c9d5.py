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
#!/usr/bin/env python3
# UDIZINE Assembly Instruction Generator
# Supports Vertik and Palo modular shelving systems

import json
from enum import Enum
from typing import Dict, List, Optional, Tuple


class ShelvingSystem(Enum):
    VERTIK = "Vertik"
    PALO = "Palo"


class ComponentType(Enum):
    PANEL = "Panel"
    SHELF = "Shelf"
    BRACKET = "Bracket"
    SCREW = "Screw"
    ANCHOR = "Anchor"


class AssemblyStep:
    def __init__(self, description: str, components: List[Tuple[ComponentType, int]], tools: List[str]):
        self.description = description
        self.components = components
        self.tools = tools

    def to_dict(self) -> Dict:
        return {
            "description": self.description,
            "components": [(comp.value, qty) for comp, qty in self.components],
            "tools": self.tools
        }


class ShelvingConfig:
    def __init__(self, system: ShelvingSystem, width: int, height: int, depth: int, 
                 shelf_count: int, wall_type: str):
        self.system = system
        self.width = width
        self.height = height
        self.depth = depth
        self.shelf_count = shelf_count
        self.wall_type = wall_type
        self.validate()

    def validate(self):
        if self.width <= 0 or self.height <= 0 or self.depth <= 0:
            raise ValueError("Dimensions must be positive numbers")
        if self.shelf_count <= 0:
            raise ValueError("Shelf count must be at least 1")
        if self.wall_type not in ["drywall", "concrete", "brick"]:
            raise ValueError("Invalid wall type")


class InstructionGenerator:
    def __init__(self):
        self._load_component_data()

    def _load_component_data(self):
        with open('component_data.json') as f:
            self.component_data = json.load(f)

    def generate_instructions(self, config: ShelvingConfig) -> Dict:
        if config.system == ShelvingSystem.VERTIK:
            return self._generate_vertik_instructions(config)
        else:
            return self._generate_palo_instructions(config)

    def _generate_vertik_instructions(self, config: ShelvingConfig) -> Dict:
        steps = []
        
        # Step 1: Wall mounting
        steps.append(AssemblyStep(
            "Mark and drill holes for vertical rails",
            [
                (ComponentType.PANEL, 2),
                (ComponentType.ANCHOR, 4)
            ],
            ["measuring tape", "level", "drill", "hammer"]
        ))

        # Step 2: Install vertical rails
        steps.append(AssemblyStep(
            "Install vertical rails using provided anchors",
            [
                (ComponentType.PANEL, 2),
                (ComponentType.SCREW, 8)
            ],
            ["screwdriver", "level"]
        ))

        # Step 3: Install brackets
        bracket_count = (config.shelf_count + 1) * 2
        steps.append(AssemblyStep(
            "Attach brackets to vertical rails at marked positions",
            [
                (ComponentType.BRACKET, bracket_count),
                (ComponentType.SCREW, bracket_count * 2)
            ],
            ["screwdriver"]
        ))

        # Step 4: Install shelves
        steps.append(AssemblyStep(
            "Place shelves on brackets and secure",
            [
                (ComponentType.SHELF, config.shelf_count),
                (ComponentType.SCREW, config.shelf_count * 4)
            ],
            ["screwdriver"]
        ))

        return self._format_output(config, steps)

    def _generate_palo_instructions(self, config: ShelvingConfig) -> Dict:
        steps = []
        
        # Step 1: Wall mounting
        steps.append(AssemblyStep(
            "Mark and drill holes for wall mounts",
            [
                (ComponentType.PANEL, 1),
                (ComponentType.ANCHOR, 4)
            ],
            ["measuring tape", "level", "drill", "hammer"]
        ))

        # Step 2: Install central column
        steps.append(AssemblyStep(
            "Secure central column to wall",
            [
                (ComponentType.PANEL, 1),
                (ComponentType.SCREW, 6)
            ],
            ["screwdriver", "level"]
        ))

        # Step 3: Install arms
        arm_count = config.shelf_count * 2
        steps.append(AssemblyStep(
            "Attach shelf arms to central column",
            [
                (ComponentType.BRACKET, arm_count),
                (ComponentType.SCREW, arm_count * 2)
            ],
            ["screwdriver"]
        ))

        # Step 4: Install shelves
        steps.append(AssemblyStep(
            "Place shelves on arms and secure",
            [
                (ComponentType.SHELF, config.shelf_count),
                (ComponentType.SCREW, config.shelf_count * 4)
            ],
            ["screwdriver"]
        ))

        return self._format_output(config, steps)

    def _format_output(self, config: ShelvingConfig, steps: List[AssemblyStep]) -> Dict:
        return {
            "system": config.system.value,
            "dimensions": {
                "width": config.width,
                "height": config.height,
                "depth": config.depth
            },
            "shelf_count": config.shelf_count,
            "wall_type": config.wall_type,
            "steps": [step.to_dict() for step in steps],
            "total_components": self._calculate_total_components(steps)
        }

    def _calculate_total_components(self, steps: List[AssemblyStep]) -> Dict:
        totals = {}
        for step in steps:
            for component, quantity in step.components:
                comp_name = component.value
                totals[comp_name] = totals.get(comp_name, 0) + quantity
        return totals


def main():
    print("UDIZINE Assembly Instruction Generator")
    print("-------------------------------------\n")

    try:
        system = input("Enter shelving system (Vertik/Palo): ").strip().capitalize()
        system = ShelvingSystem[system.upper()]
        
        width = int(input("Enter width (cm): "))
        height = int(input("Enter height (cm): "))
        depth = int(input("Enter depth (cm): "))
        shelf_count = int(input("Enter number of shelves: "))
        wall_type = input("Enter wall type (drywall/concrete/brick): ").strip().lower()

        config = ShelvingConfig(system, width, height, depth, shelf_count, wall_type)
        generator = InstructionGenerator()
        instructions = generator.generate_instructions(config)

        output_file = f"{system.value.lower()}_assembly_instructions.json"
        with open(output_file, 'w') as f:
            json.dump(instructions, f, indent=2)

        print(f"\nAssembly instructions generated successfully: {output_file}")

    except ValueError as e:
        print(f"\nError: {str(e)}")
    except KeyError:
        print("\nError: Invalid shelving system. Please choose Vertik or Palo.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
