"""
Generated Code Metadata:
========================
Original URL: https://ontariooffers.com
Prompt: Write a Python script to parse user input for measurements and generate a detailed installation guide for Phantom retractable screens, including door, window, and oversized options.
Generated: DETERMINISTIC_2a25b727ed727272
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, asdict
from enum import Enum, auto
from typing import List, Optional, Dict, Any

class ScreenType(Enum):
    DOOR = auto()
    WINDOW = auto()
    OVERSIZED = auto()

@dataclass
class Measurement:
    width: float
    height: float
    unit: str = "inches"

    def validate(self) -> bool:
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Measurements must be positive values")
        if self.unit not in ["inches", "centimeters"]:
            raise ValueError("Unit must be either 'inches' or 'centimeters'")
        return True

@dataclass
class ScreenInstallation:
    screen_type: ScreenType
    measurements: Measurement
    location: str
    additional_notes: Optional[str] = None

    def generate_guide(self) -> Dict[str, Any]:
        guide = {
            "type": self.screen_type.name,
            "measurements": asdict(self.measurements),
            "location": self.location,
            "steps": self._generate_steps(),
            "tools_required": self._get_tools(),
            "estimated_time": self._get_estimated_time()
        }
        if self.additional_notes:
            guide["additional_notes"] = self.additional_notes
        return guide

    def _generate_steps(self) -> List[str]:
        base_steps = [
            "1. Measure and mark the installation area according to specifications.",
            "2. Ensure the mounting surface is clean and level.",
            "3. Pre-drill holes for mounting brackets if necessary."
        ]
        
        if self.screen_type == ScreenType.DOOR:
            base_steps.extend([
                "4. Install the top track above the door frame.",
                "5. Mount the screen assembly to the top track.",
                "6. Install the side guides on the door frame.",
                "7. Test the retraction mechanism."
            ])
        elif self.screen_type == ScreenType.WINDOW:
            base_steps.extend([
                "4. Install the mounting brackets on the window frame.",
                "5. Attach the screen assembly to the brackets.",
                "6. Adjust the tension as needed.",
                "7. Test the retraction mechanism."
            ])
        elif self.screen_type == ScreenType.OVERSIZED:
            base_steps.extend([
                "4. Install reinforced mounting brackets.",
                "5. Use additional support beams if width exceeds standard.",
                "6. Attach the screen assembly with helper support.",
                "7. Test the retraction mechanism multiple times."
            ])
        
        base_steps.append("8. Clean up the work area and dispose of packaging materials.")
        return base_steps

    def _get_tools(self) -> List[str]:
        tools = ["Measuring tape", "Level", "Drill", "Screwdriver", "Pencil"]
        if self.screen_type == ScreenType.OVERSIZED:
            tools.extend(["Helper", "Additional support clamps"])
        return tools

    def _get_estimated_time(self) -> str:
        if self.screen_type == ScreenType.DOOR:
            return "1-2 hours"
        elif self.screen_type == ScreenType.WINDOW:
            return "45-90 minutes"
        else:
            return "2-3 hours"

def get_user_input() -> ScreenInstallation:
    print("Phantom Retractable Screen Installation Guide Generator")
    print("-----------------------------------------------------")
    
    # Get screen type
    while True:
        try:
            print("\nSelect screen type:")
            for i, screen_type in enumerate(ScreenType):
                print(f"{i+1}. {screen_type.name}")
            choice = int(input("Enter choice (1-3): "))
            if 1 <= choice <= len(ScreenType):
                screen_type = list(ScreenType)[choice-1]
                break
            print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    # Get measurements
    while True:
        try:
            print("\nEnter measurements:")
            width = float(input("Width: "))
            height = float(input("Height: "))
            unit = input("Unit (inches/centimeters): ").lower()
            measurements = Measurement(width, height, unit)
            measurements.validate()
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    # Get location
    location = input("\nEnter installation location (e.g., 'Front Door', 'Living Room Window'): ").strip()
    
    # Get additional notes
    notes = input("\nAny additional notes (press Enter to skip): ").strip()
    additional_notes = notes if notes else None

    return ScreenInstallation(
        screen_type=screen_type,
        measurements=measurements,
        location=location,
        additional_notes=additional_notes
    )

def save_guide_to_file(guide: Dict[str, Any], filename: str = "installation_guide.json") -> None:
    with open(filename, 'w') as f:
        json.dump(guide, f, indent=4)
    print(f"\nInstallation guide saved to {filename}")

def display_guide(guide: Dict[str, Any]) -> None:
    print("\n=== Phantom Retractable Screen Installation Guide ===")
    print(f"Type: {guide['type']}")
    print(f"Location: {guide['location']}")
    print(f"Measurements: {guide['measurements']['width']} {guide['measurements']['unit']} x {guide['measurements']['height']} {guide['measurements']['unit']}")
    
    print("\nTools Required:")
    for tool in guide['tools_required']:
        print(f"- {tool}")
    
    print(f"\nEstimated Installation Time: {guide['estimated_time']}")
    
    if 'additional_notes' in guide:
        print(f"\nAdditional Notes: {guide['additional_notes']}")
    
    print("\nInstallation Steps:")
    for step in guide['steps']:
        print(step)

def main():
    try:
        installation = get_user_input()
        guide = installation.generate_guide()
        display_guide(guide)
        save_guide_to_file(guide)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please check your input and try again.")

if __name__ == "__main__":
    main()
```
